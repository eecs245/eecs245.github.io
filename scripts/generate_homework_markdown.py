#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


MATHJAX_SNIPPET = """<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>"""

SECTION_SEPARATOR = "---"

HOMEWORK_STYLE_SNIPPET = """<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
</style>"""


@dataclass
class Metadata:
    assignment: str
    due_date: str
    submission_instructions_latex: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert an EECS 245 homework LaTeX file into a website markdown page, "
            "copy referenced local assets, and optionally update a week module link."
        )
    )
    parser.add_argument("source_tex", help="Path to the homework .tex file.")
    parser.add_argument("output_md", help="Path to the generated markdown file.")
    parser.add_argument(
        "--week-file",
        help="Optional week module to update, e.g. website/_modules/week-16.md.",
    )
    parser.add_argument(
        "--event-title",
        help='Homework event title to update in the week file, e.g. "Homework 11".',
    )
    parser.add_argument(
        "--problems-link",
        help=(
            "Problems link to write into the week file. "
            "Defaults to the generated homework directory, relative to the week file."
        ),
    )
    parser.add_argument(
        "--include-solutions",
        action="store_true",
        help="Embed LaTeX solution environments inline in the generated Markdown as collapsible dropdowns.",
    )
    parser.add_argument(
        "--solutions-link",
        help=(
            "Deprecated. Solutions releases set the week-file release state to solutions: true; "
            "the solutions PDF link is generated in assignment Markdown."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    source_tex = resolve_source_tex(repo_root, Path(args.source_tex))
    output_md = resolve_repo_path(repo_root, Path(args.output_md))

    if (args.week_file is None) ^ (args.event_title is None):
        raise SystemExit("--week-file and --event-title must be provided together.")

    source_text = source_tex.read_text()
    metadata = extract_metadata(source_text)
    expanded_tex = expand_inputs_from_text(strip_latex_comments(source_text), source_tex.parent)
    if not args.include_solutions:
        assert_solutions_disabled(expanded_tex, source_tex)
    transformed_tex = transform_assignment_tex(
        expanded_tex, include_solutions=args.include_solutions
    )
    pdf_link = compute_pdf_link(repo_root, output_md)
    solutions_pdf_link = (
        compute_solutions_pdf_link(repo_root, output_md)
        if args.include_solutions
        else None
    )

    output_md.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        body_tex = tmp_dir / "body.tex"
        body_md = tmp_dir / "body.md"
        body_tex.write_text(transformed_tex)

        run_pandoc(body_tex, body_md)

        body_markdown = body_md.read_text().strip()
        submission_instructions = latex_fragment_to_markdown(
            metadata.submission_instructions_latex
        ).strip()
        final_markdown = build_homework_page(
            metadata=metadata,
            submission_instructions=submission_instructions,
            body_markdown=body_markdown,
            pdf_link=pdf_link,
            solutions_pdf_link=solutions_pdf_link,
            output_md=output_md,
        )
        validate_visible_items_match_source(
            assignment=metadata.assignment,
            source_tex=expanded_tex,
            generated_markdown=final_markdown,
            source_path=source_tex,
        )
        validate_generated_markdown_structure(final_markdown, output_md)

        final_markdown = "\n".join(line.rstrip() for line in final_markdown.splitlines()) + "\n"
        output_md.write_text(final_markdown)

    copy_referenced_assets(output_md, source_tex.parent, repo_root / "website")

    if args.week_file:
        if args.solutions_link and not args.include_solutions:
            raise SystemExit("--solutions-link requires --include-solutions.")
        week_file = resolve_repo_path(repo_root, Path(args.week_file))
        problems_link = args.problems_link or compute_default_problems_link(
            week_file=week_file,
            output_md=output_md,
        )
        update_week_file(
            week_file=week_file,
            event_title=args.event_title,
            problems_link=problems_link,
            solutions_link=("true" if args.include_solutions else None),
        )

    return 0


def resolve_repo_path(repo_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else repo_root / path


def resolve_source_tex(repo_root: Path, requested_path: Path) -> Path:
    candidate = resolve_repo_path(repo_root, requested_path)
    if candidate.exists():
        return candidate

    pdf_fallback = candidate.parent / "pdf" / candidate.name
    if pdf_fallback.exists():
        return pdf_fallback

    raise FileNotFoundError(
        f"Could not find source TeX file at {candidate} or fallback {pdf_fallback}."
    )


def extract_metadata(text: str) -> Metadata:
    assignment = extract_newcommand(text, "assignment")
    due_date = extract_newcommand(text, "duedate")
    submission_instructions = extract_newcommand(text, "submissioninstructions")
    return Metadata(
        assignment=assignment,
        due_date=format_metadata_inline_latex(due_date),
        submission_instructions_latex=submission_instructions.strip(),
    )


def extract_newcommand(text: str, name: str) -> str:
    marker = f"\\newcommand{{\\{name}}}"
    start = text.find(marker)
    if start == -1:
        raise ValueError(f"Could not find {marker}.")

    brace_start = start + len(marker)
    if brace_start >= len(text) or text[brace_start] != "{":
        raise ValueError(f"Malformed {marker}.")

    body, _ = extract_braced(text, brace_start)
    return body


def extract_braced(text: str, brace_start: int) -> tuple[str, int]:
    depth = 0
    chars: list[str] = []
    i = brace_start
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
            if depth > 1:
                chars.append(ch)
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars), i + 1
            chars.append(ch)
        else:
            chars.append(ch)
        i += 1

    raise ValueError("Unbalanced braces while parsing metadata.")


def format_metadata_inline_latex(text: str) -> str:
    """Convert simple inline LaTeX metadata fragments used in titles/dates."""

    def replace_html_textcolor(match: re.Match[str]) -> str:
        color = f"#{match.group('color')}"
        body = match.group("body")
        return f'<span style="color: {color};">{body}</span>'

    def replace_named_textcolor(match: re.Match[str]) -> str:
        color = match.group("color")
        body = match.group("body")
        return f'<span style="color: {color};">{body}</span>'

    text = re.sub(
        r"\\textcolor\[HTML\]\{(?P<color>[0-9A-Fa-f]{6})\}\{(?P<body>[^{}]*)\}",
        replace_html_textcolor,
        text,
    )
    text = re.sub(
        r"\\textcolor\{(?P<color>[^{}]+)\}\{(?P<body>[^{}]*)\}",
        replace_named_textcolor,
        text,
    )
    text = text.replace(r"\#", "#")
    return collapse_whitespace(text)


def expand_inputs(path: Path) -> str:
    return expand_inputs_from_text(strip_latex_comments(path.read_text()), path.parent)


def expand_inputs_from_text(text: str, base_dir: Path) -> str:
    pattern = re.compile(r"\\input\{([^}]+)\}")

    def replace(match: re.Match[str]) -> str:
        relative_path = match.group(1)
        if not relative_path.endswith(".tex"):
            relative_path += ".tex"
        included_path = (base_dir / relative_path).resolve()
        if not included_path.exists():
            raise FileNotFoundError(f"Could not resolve input file {included_path}.")
        return expand_inputs(included_path)

    return pattern.sub(replace, text)


def strip_latex_comments(text: str) -> str:
    """Remove TeX comments while preserving escaped percent signs like \%."""
    stripped_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        body = line[:-1] if line.endswith("\n") else line
        newline = "\n" if line.endswith("\n") else ""
        comment_start = find_unescaped_percent(body)
        if comment_start is not None:
            body = body[:comment_start].rstrip()
        stripped_lines.append(body + newline)
    return "".join(stripped_lines)


def find_unescaped_percent(line: str) -> int | None:
    for index, char in enumerate(line):
        if char != "%":
            continue
        backslash_count = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslash_count += 1
            cursor -= 1
        if backslash_count % 2 == 0:
            return index
    return None


def transform_assignment_tex(text: str, include_solutions: bool = False) -> str:
    text = strip_document_wrapper(text)
    text = strip_false_blocks(text)
    text = strip_latex_comments(text)
    text = strip_layout_commands(text)
    text = replace_youtube_embed_markers(text)
    text = expand_labcodelinks(text)
    text = replace_fbox_markers(text)
    text = add_solution_choice_summaries(text) if include_solutions else text
    text = replace_choice_markers(text, include_solutions=include_solutions)
    text = wrap_bare_alignment_environments(text)
    text = replace_prob_markers(text)
    text = replace_activity_markers(text)
    text = replace_subitem_markers(text)
    text = replace_labeled_items(text)
    text = replace_solution_markers(text, include_solutions=include_solutions)
    text = re.sub(r"\\emptybox\{[^}]*\}", "", text)
    text = text.replace("\\newpage", "")
    text = text.replace("\\makemytitle", "% stripped makemytitle")
    return text


def strip_false_blocks(text: str) -> str:
    return re.sub(r"(?s)\\iffalse\b.*?\\fi\b", "", text)


def strip_showsolutions_blocks(text: str) -> str:
    return re.sub(r"(?s)\\ifshowsolutions\b.*?\\fi\b", "", text)


def strip_latex_comment_lines(text: str) -> str:
    return re.sub(r"(?m)^[ \t]*%.*(?:\n|$)", "", text)


def strip_layout_commands(text: str) -> str:
    text = re.sub(r"\\noindent\s*\\rule\{\\textwidth\}\{[^{}]*\}", "", text)
    text = re.sub(
        r"\\noindent\s*\\makebox\[[^\]]+\]\{\\rule\{\\textwidth\}\{[^{}]*\}\}",
        "",
        text,
    )
    text = re.sub(r"\\begin\{minipage\}(?:\[[^\]]*\])?\{[^{}]*\}", "", text)
    text = text.replace(r"\end{minipage}", "")
    text = re.sub(r"(?m)^[ \t]*\\(?:hfill|centering)\b[ \t]*$", "", text)
    return text


def assert_solutions_disabled(text: str, source_tex: Path) -> None:
    if re.search(r"(?m)^[ \t]*\\enablesolutions\b", text):
        raise SystemExit(
            f"{source_tex} has \\enablesolutions enabled. "
            "Do not generate a student-facing release until it is commented out, "
            "unless this is an explicit solutions release with --include-solutions."
        )


def replace_fbox_markers(text: str) -> str:
    # Pandoc drops \fbox in prose. \ensuremath preserves the placeholder there,
    # and cleanup strips the wrapper again inside display math.
    return re.sub(r"\\fbox\{([^{}]*)\}", r"\\ensuremath{\\boxed{\1}}", text)


def replace_choice_markers(text: str, include_solutions: bool = False) -> str:
    def replace_circle(match: re.Match[str]) -> str:
        command = match.group(1)
        content = match.group(2).strip()
        if command == "solutioncorrectbubble":
            return rf"$\eecsfilledcircle$ {content} \quad "
        return rf"$\bigcirc$ {content} \quad "

    def replace_square(match: re.Match[str]) -> str:
        command = match.group(1)
        content = match.group(2).strip()
        if command == "solutioncorrectsquarebubble":
            return rf"$\eecsfilledsquare$ {content} \quad "
        return rf"$\square$ {content} \quad "

    text = re.sub(
        r"\\((?:correct|filled)?bubble|solution(?:correct)?bubble)\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
        replace_circle,
        text,
    )
    return re.sub(
        r"\\((?:correct|filled)?squarebubble|solution(?:correct)?squarebubble)\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
        replace_square,
        text,
    )


CHOICE_COMMAND_PATTERN = re.compile(
    r"\\(?P<command>(?:correct|filled)?(?:square)?bubble)\{",
)


@dataclass
class ChoiceOption:
    command: str
    content: str

    @property
    def is_square(self) -> bool:
        return "squarebubble" in self.command

    @property
    def is_correct(self) -> bool:
        return self.command.startswith(("correct", "filled"))


def add_solution_choice_summaries(text: str) -> str:
    solution_env_pattern = re.compile(
        r"(?ms)^[ \t]*\\begin\{solution\}[ \t]*\n?(.*?)[ \t]*^[ \t]*\\end\{solution\}[ \t]*"
    )
    parts: list[str] = []
    cursor = 0

    for match in solution_env_pattern.finditer(text):
        before_solution = text[cursor : match.start()]
        parts.append(before_solution)
        options = extract_last_choice_group(before_solution)
        solution_body = match.group(1)
        if options:
            summary = render_solution_choice_summary(options)
            solution_body = f"\n{summary}\n\n{solution_body.lstrip()}"
        parts.append(f"\\begin{{solution}}\n{solution_body.rstrip()}\n\\end{{solution}}\n")
        cursor = match.end()

    parts.append(text[cursor:])
    return "".join(parts)


def extract_last_choice_group(text: str) -> list[ChoiceOption]:
    boundary_markers = [
        "\\begin{prob}",
        "\\begin{subprob}",
        "\\begin{activity}",
        "\\begin{subactivity}",
        "\\end{solution}",
    ]
    boundary = max(text.rfind(marker) for marker in boundary_markers)
    search_region = text[boundary + 1 :] if boundary >= 0 else text
    options = parse_choice_options(search_region)
    if not options:
        return []

    last_option_start = search_region.rfind("\\" + options[-1].command + "{")
    group_start = max(
        search_region.rfind("\n\n", 0, last_option_start),
        search_region.rfind("\\\\", 0, last_option_start),
        search_region.rfind("\\item", 0, last_option_start),
    )
    group_region = search_region[group_start + 1 :] if group_start >= 0 else search_region
    return parse_choice_options(group_region)


def parse_choice_options(text: str) -> list[ChoiceOption]:
    options: list[ChoiceOption] = []
    cursor = 0
    while True:
        match = CHOICE_COMMAND_PATTERN.search(text, cursor)
        if not match:
            break
        content, end = extract_braced(text, match.end() - 1)
        options.append(ChoiceOption(match.group("command"), content.strip()))
        cursor = end
    return options


def render_solution_choice_summary(options: list[ChoiceOption]) -> str:
    rendered_options = []
    for option in options:
        if option.is_square:
            command = "solutioncorrectsquarebubble" if option.is_correct else "solutionsquarebubble"
        else:
            command = "solutioncorrectbubble" if option.is_correct else "solutionbubble"
        rendered_options.append(f"\\{command}{{{option.content}}}")
    return "\n".join(rendered_options)


def clean_align_content(content: str) -> str:
    """Clean up align environment content for markdown rendering."""
    lines = content.split('\n')
    cleaned = []
    for line in lines:
        line = re.sub(r'%.*$', '', line)
        line = line.strip()
        if line:
            cleaned.append(line)
    return '\n'.join(cleaned)


def wrap_bare_alignment_environments(text: str) -> str:
    pattern = re.compile(r"(\\begin\{(align\*?|aligned)\})(.*?)(\\end\{\2\})", re.S)

    def replace(match: re.Match[str]) -> str:
        start = match.start()
        end = match.end()
        before = text[max(0, start - 50):start]
        after = text[end:end + 50]
        begin_tag = match.group(1)
        env_name = match.group(2)
        content = match.group(3)
        end_tag = match.group(4)
        cleaned_content = clean_align_content(content)
        result = f"{begin_tag}\n{cleaned_content}\n{end_tag}"
        if "$$" in before.split('\n')[-1] or "$$" in after.split('\n')[0]:
            return result
        return f"\n$$\n{result}\n$$\n"

    return pattern.sub(replace, text)


def strip_document_wrapper(text: str) -> str:
    text = re.sub(r"(?s)^.*?\\begin\{document\}", "", text)
    text = re.sub(r"(?s)\\end\{document\}.*$", "", text)
    text = re.sub(r"\\makemytitle\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}", "", text, count=1, flags=re.S)
    return text


def replace_prob_markers(text: str) -> str:
    problem_number = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal problem_number
        problem_number += 1
        optional_title = match.group(1)

        header = f"\\section*{{Problem {problem_number}"
        points_badge = ""
        if optional_title:
            title = optional_title.strip()
            points_match = re.search(r"\((\d+)\s*pts?\)\s*$", title)
            if points_match:
                points = points_match.group(1)
                title = title[: points_match.start()].rstrip()
                points_badge = f"<!-- POINTS_BADGE:{points} -->"
            if title:
                header += f": {title}"
        header += "}\n"
        return "\n% ITEM_BOUNDARY\n" + header + points_badge + "\n"

    text = re.sub(r"(?m)^[ \t]*\\begin\{prob\}(?:\[(.*?)\])?", replace, text)
    return text.replace("\\end{prob}", "")


def replace_activity_markers(text: str) -> str:
    activity_number = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal activity_number
        activity_number += 1
        optional_title = match.group(1)

        header = f"\\section*{{Activity {activity_number}"
        if optional_title:
            title = optional_title.strip()
            if title:
                header += f": {title}"
        header += "}\n"
        return "\n% ITEM_BOUNDARY\n" + header + "\n"

    text = re.sub(r"(?m)^[ \t]*\\begin\{activity\}(?:\[(.*?)\])?", replace, text)
    return text.replace("\\end{activity}", "")


def replace_subitem_markers(text: str) -> str:
    chunks = text.split("% ITEM_BOUNDARY")
    processed_chunks = [chunks[0]]

    for chunk in chunks[1:]:
        part_index = 0

        def replace(match: re.Match[str]) -> str:
            nonlocal part_index
            part_index += 1
            letter = chr(ord("a") + part_index - 1)
            points = match.group(1) if match.lastindex else None
            points_badge = f"<!-- POINTS_BADGE:{points} -->" if points else ""
            return f"\n\\subsection*{{Part {letter})}}\n{points_badge}\n"

        processed_chunk = re.sub(
            r"(?m)^[ \t]*\\begin\{subprob\}(?:\(\s*(\d+)\s*pts?\s*\))?",
            replace,
            chunk,
        )
        processed_chunk = re.sub(
            r"(?m)^[ \t]*\\begin\{subactivity\}", replace, processed_chunk
        )
        processed_chunks.append(processed_chunk)

    text = "".join(processed_chunks)
    text = text.replace("\\end{subprob}", "")
    return text.replace("\\end{subactivity}", "")


def replace_labeled_items(text: str) -> str:
    r"""Convert LaTeX \item[X:] to labeled HTML spans for answer choice lists."""
    pattern = re.compile(r"\\item\[([A-Z]):\]")

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        return f"\\item \\textbf{{{label}:}}"

    return pattern.sub(replace, text)


def replace_solution_markers(text: str, include_solutions: bool = False) -> str:
    solution_env_pattern = r"(?ms)^[ \t]*\\begin\{solution\}[ \t]*\n?(.*?)[ \t]*^[ \t]*\\end\{solution\}[ \t]*"

    if not include_solutions:
        return re.sub(solution_env_pattern, "", text)

    def replace(match: re.Match[str]) -> str:
        solution_body = match.group(1).strip()
        return (
            "\n<details markdown=\"1\"><summary>Solution</summary>\n\n"
            f"{solution_body}\n\n"
            "</details>\n"
        )

    return re.sub(solution_env_pattern, replace, text)


def expand_labcodelinks(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        lab = match.group(1)
        stem = match.group(2)
        datahub_url = (
            "https://datahub.eecs245.org/hub/user-redirect/git-pull?"
            "repo=https\\%3A\\%2F\\%2Fgithub.com\\%2Feecs245\\%2Fsp26-code"
            f"\\&urlpath=tree\\%2Fsp26-code\\%2Flabs\\%2F{lab}\\%2F{stem}.ipynb"
            "\\&branch=main"
        )
        github_url = f"https://github.com/eecs245/sp26-code/tree/main/labs/{lab}/{stem}.ipynb"
        return rf"""
There are two ways to access the supplemental Jupyter Notebook:
\begin{{itemize}}
  \item \textbf{{Option 1 (preferred)}}: Set up a Jupyter Notebook environment locally, use \texttt{{git}} to clone our \href{{{github_url}}}{{course repository}}, and open \texttt{{labs/{lab}/{stem}.ipynb}}. For instructions on how to do this, see the \href{{https://eecs245.org/env-setup}}{{Environment Setup}} page of the course website.
  \item \textbf{{Option 2}}: Click \href{{{datahub_url}}}{{here}} to open \texttt{{{stem}.ipynb}} on DataHub. Before doing so, read the instructions on the \href{{https://eecs245.org/env-setup/\#option-2-using-the-eecs-245-datahub}}{{Environment Setup}} page on how to use the DataHub.
\end{{itemize}}
"""

    return re.sub(r"\\labcodelinks\{([^}]+)\}\{([^}]+)\}", replace, text)


def run_pandoc(input_path: Path, output_path: Path) -> None:
    command = [
        "pandoc",
        str(input_path),
        "--from=latex",
        "--to=markdown+raw_html-simple_tables-multiline_tables-grid_tables",
        "--shift-heading-level-by=1",
        "--wrap=none",
        "-o",
        str(output_path),
    ]
    subprocess.run(command, check=True)


def latex_fragment_to_markdown(fragment: str) -> str:
    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        input_path = tmp_dir / "fragment.tex"
        output_path = tmp_dir / "fragment.md"
        input_path.write_text(fragment)
        run_pandoc(input_path, output_path)
        return cleanup_markdown(output_path.read_text())


def build_homework_page(
    metadata: Metadata,
    submission_instructions: str,
    body_markdown: str,
    pdf_link: str | None,
    solutions_pdf_link: str | None,
    output_md: Path,
) -> str:
    cleaned_body = cleanup_markdown(
        body_markdown,
        use_point_badges=not metadata.assignment.startswith("Homework "),
    )
    toc = generate_toc(cleaned_body, toc_title=toc_title_for(metadata.assignment))
    pdf_button = (
        f'<a class="btn btn-info assignment-pdf-button" href="{pdf_link}" target="_blank">View as PDF ✏️</a>'
        if pdf_link
        else ""
    )
    solutions_button = (
        f'<a class="btn btn-info assignment-pdf-button" href="{solutions_pdf_link}" target="_blank">Solutions PDF ✅</a>'
        if solutions_pdf_link
        else ""
    )
    action_buttons = "\n".join(button for button in (pdf_button, solutions_button) if button)
    actions = f'<div class="assignment-actions">\n{action_buttons}\n</div>' if action_buttons else ""
    preamble = (
        '{: .yellow }\n'
        '<div markdown="1">\n'
        f"{submission_instructions}\n"
        "</div>"
    )

    parts = [
        "---",
        "layout: page",
        f'title: "{escape_frontmatter(metadata.assignment)}"',
        f'description: "{escape_frontmatter(metadata.assignment)} {description_noun_for(metadata.assignment)}."',
        "nav_exclude: true",
        "hide_footer_hr: true",
        "---",
        "",
        "{% raw %}",
        "",
        MATHJAX_SNIPPET,
        "",
        HOMEWORK_STYLE_SNIPPET,
        "",
        f"# {metadata.assignment}",
        "",
        f"**due** {metadata.due_date}",
        "",
    ]
    if actions:
        parts.extend([actions, ""])
    parts.extend(
        [
            preamble,
            "",
            SECTION_SEPARATOR,
            "",
            toc,
            "",
            SECTION_SEPARATOR,
            "",
            cleaned_body,
            "",
            "{% endraw %}",
            "",
        ]
    )
    return "\n".join(parts)


def toc_title_for(assignment: str) -> str:
    return "Activities" if assignment.startswith("Lab ") else "Problems"


def description_noun_for(assignment: str) -> str:
    return "activities" if assignment.startswith("Lab ") else "problems"


def generate_toc(body_markdown: str, toc_title: str) -> str:
    toc_lines = [f"## {toc_title}", ""]
    problem_pattern = re.compile(
        r"^## ((?:Problem|Activity) \d+(?::\s*(.+?))?)(?:\s+(?:<span class=\"badge\"[^<]*</span>|\(\d+\s+pts?\)))?$",
        re.M,
    )

    for match in problem_pattern.finditer(body_markdown):
        full_title = format_heading_for_toc(match.group(1))
        full_heading = re.sub(r"^##\s+", "", match.group(0))
        anchor_text = re.sub(r"<[^>]+>", "", full_heading)
        anchor = re.sub(r"[^\w\s-]", "", anchor_text.lower())
        anchor = re.sub(r"\s+", "-", anchor.strip())

        toc_lines.append(f"- [{full_title}](#{anchor})")

    if len(toc_lines) <= 2:
        return ""

    return "\n".join(toc_lines)


def format_heading_for_toc(heading: str) -> str:
    heading = replace_inline_math_spans_with_dollars(heading)
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = html.unescape(heading)
    return heading.replace("\\\\", "\\")


def cleanup_markdown(text: str, use_point_badges: bool = True) -> str:
    text = text.replace("\\\u2019", "'")
    text = re.sub(r"(?<!\\)\\&", "&", text)
    text = text.replace('\\"', '"')
    text = text.replace("\\<", "<")
    text = text.replace("\\>", ">")
    text = re.sub(
        r"^(#{2,6}\s+.+?)\s+\{#.*?\.unnumbered\}$",
        r"\1",
        text,
        flags=re.M,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = fix_latex_for_mathjax(text)
    text = convert_pandoc_attribute_spans(text)
    text = fix_image_syntax(text)
    text = remove_blank_table_headers(text)
    text = escape_blank_rules(text)
    text = replace_recap_markers(text)
    text = add_item_separators(text)
    text = promote_interstitial_callouts(text)
    text = promote_extra_practice_callouts(text)
    text = add_separator_after_recap(text)
    text = indent_ordered_list_display_math(text)
    text = unindent_accidental_list_code_blocks(text)
    text = convert_points_badges(text, use_badges=use_point_badges)
    text = convert_part_headings_to_lists(text)
    text = fix_leading_italics(text)
    text = normalize_markdown_inside_emphasis(text)
    text = format_multiple_choice_rows(text)
    text = add_total_points_separator(text)
    text = collapse_repeated_section_separators(text)
    text = fix_accidental_indented_prose(text)
    text = fence_indented_code_blocks(text)
    text = flatten_solution_ordered_lists(text)
    text = keep_ordered_list_display_math_items(text)
    text = remove_pandoc_layout_fences(text)
    text = render_youtube_embeds(text)
    text = re.sub(r"(</div>)\n---", r"\1\n\n---", text)
    text = collapse_repeated_section_separators(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = remove_trailing_section_separator(text)
    return text.strip()


def replace_youtube_embed_markers(text: str) -> str:
    return re.sub(
        r"\\youtubeembed\{([A-Za-z0-9_-]+)\}",
        r"\n\nYOUTUBE_EMBED:\1\n\n",
        text,
    )


def youtube_embed_html(video_id: str) -> str:
    return (
        '<center><iframe width="560" height="315" '
        f'src="https://www.youtube.com/embed/{video_id}" '
        'title="YouTube video player" frameborder="0" '
        'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        'gyroscope; picture-in-picture; web-share" '
        'referrerpolicy="strict-origin-when-cross-origin" '
        "allowfullscreen></iframe></center>"
    )


def render_youtube_embeds(text: str) -> str:
    return re.sub(
        r"(?m)^YOUTUBE_EMBED:([A-Za-z0-9_-]+)$",
        lambda match: youtube_embed_html(match.group(1)),
        text,
    )


def remove_pandoc_layout_fences(text: str) -> str:
    lines = text.splitlines()
    cleaned: list[str] = []
    suppress_next_closing = 0

    for line in lines:
        if re.fullmatch(r"[ \t]*:::[ \t]*(?:center|minipage)[ \t]*", line):
            suppress_next_closing += 1
            continue
        if suppress_next_closing and re.fullmatch(r"[ \t]*:::[ \t]*", line):
            suppress_next_closing -= 1
            continue
        cleaned.append(line)

    return "\n".join(cleaned)


def convert_pandoc_attribute_spans(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group("label")
        color = match.group("color").strip()
        if re.fullmatch(r"[0-9A-Fa-f]{6}", color):
            color = f"#{color}"
        return f'<span style="color: {color}">{label}</span>'

    return re.sub(
        r'\[(?P<label>[^\]]+)\]\{style="color:\s*(?P<color>[^"]+)"\}',
        replace,
        text,
    )


def add_item_separators(text: str) -> str:
    pattern = re.compile(r"^(## (?:Problem|Activity) \d+)", re.M)
    first_match = True

    def replace(match: re.Match[str]) -> str:
        nonlocal first_match
        if first_match:
            first_match = False
            prior_content = text[: match.start()].strip()
            if prior_content and not prior_content.endswith(SECTION_SEPARATOR):
                return f"{SECTION_SEPARATOR}\n\n{match.group(1)}"
            return match.group(1)
        return f"{SECTION_SEPARATOR}\n\n{match.group(1)}"

    return pattern.sub(replace, text)


def remove_trailing_section_separator(text: str) -> str:
    return re.sub(rf"\s*{re.escape(SECTION_SEPARATOR)}\s*$", "", text)


def collapse_repeated_section_separators(text: str) -> str:
    """Collapse adjacent horizontal rules into one rendered divider."""
    return re.sub(
        rf"(?m)(?:^{re.escape(SECTION_SEPARATOR)}$[ \t]*\n\s*){{2,}}",
        f"{SECTION_SEPARATOR}\n\n",
        text,
    )


def promote_interstitial_callouts(text: str) -> str:
    """Move standalone prose before the next item boundary into that item block."""
    pattern = re.compile(
        rf"\n\n(?P<message>(?:\*\*|<strong>)(?:(?!\n\n).)+?(?:\*\*|</strong>))[ \t]*"
        rf"\n\n{re.escape(SECTION_SEPARATOR)}\n\n(?P<heading>## (?:Problem|Activity) \d+)",
        flags=re.S,
    )

    def replace(match: re.Match[str]) -> str:
        message = match.group("message").strip()
        heading = match.group("heading")
        return (
            f"\n\n{SECTION_SEPARATOR}\n\n"
            "{: .yellow }\n"
            f"> {message}\n\n"
            f"{heading}"
        )

    return pattern.sub(replace, text)


def promote_extra_practice_callouts(text: str) -> str:
    pattern = re.compile(
        r"(?m)^(?P<message>\*\*(?:(?:The rest of this worksheet is)|(?:The following are)) extra practice\.[^\n]*\*\*)$"
    )

    return pattern.sub(lambda match: "{: .yellow }\n> " + match.group("message"), text)


def add_separator_after_recap(text: str) -> str:
    recap_match = re.search(r"(?m)^## Recap:", text)
    if not recap_match:
        return text

    next_item_match = re.search(
        r"(?m)^## (?:Problem|Activity) \d+",
        text[recap_match.end() :],
    )
    if not next_item_match:
        return text

    next_item_start = recap_match.end() + next_item_match.start()
    before_recap = text[: recap_match.start()]
    recap_block = text[recap_match.start() : next_item_start]
    after_recap = text[next_item_start:]
    recap_block = re.sub(
        rf"\s*(?:{re.escape(SECTION_SEPARATOR)}\s*)+$",
        "",
        recap_block.rstrip(),
    )
    return f"{before_recap}{recap_block}\n\n{SECTION_SEPARATOR}\n\n{after_recap}"


def indent_ordered_list_display_math(text: str) -> str:
    # Older output indented raw HTML math blocks after ordered lists, which
    # Kramdown rendered as literal code. Raw math-display blocks render cleanly
    # when left unindented.
    lines = text.splitlines()
    fixed: list[str] = []
    index = 0
    while index < len(lines):
        if lines[index].startswith('    <div class="math-display">'):
            while index < len(lines):
                fixed.append(lines[index][4:] if lines[index].startswith("    ") else lines[index])
                if lines[index].strip() == "</div>":
                    index += 1
                    break
                index += 1
            continue
        fixed.append(lines[index])
        index += 1
    return "\n".join(fixed)


def keep_ordered_list_display_math_items(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        marker = match.group("marker")
        math = match.group("math").strip()
        return f"{marker}  $$\n{math}\n$$"

    return re.sub(
        r'(?ms)^(?P<marker>\d+\.)[ \t]*\n\n<div class="math-display">\n\$\$\n(?P<math>.*?)\n\$\$\n</div>',
        replace,
        text,
    )


def convert_points_badges(text: str, use_badges: bool = True) -> str:
    def replace_point_label(match: re.Match[str]) -> str:
        points = match.group(1)
        unit = "pt" if points == "1" else "pts"
        if not use_badges:
            return f"({points} {unit})"
        return f'<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">{points} {unit}</span>'

    text = re.sub(r"<!-- POINTS_BADGE:(\d+) -->", replace_point_label, text)
    point_label_pattern = r"(<span class=\"badge\"[^<]*</span>|\(\d+\s+pts?\))"

    def add_point_label_standalone(match: re.Match[str]) -> str:
        heading = match.group(1)
        point_label = match.group(2)
        return f"{heading} {point_label}\n\n"

    text = re.sub(
        rf"^(##+ [^\n]+)\n\n{point_label_pattern}[ \t]*\n+",
        add_point_label_standalone,
        text,
        flags=re.M,
    )

    def add_point_label_inline(match: re.Match[str]) -> str:
        heading = match.group(1)
        point_label = match.group(2)
        rest = match.group(3)
        return f"{heading} {point_label}\n\n{rest}"

    text = re.sub(
        rf"^(##+ [^\n]+)\n\n{point_label_pattern} +([^\n])",
        add_point_label_inline,
        text,
        flags=re.M,
    )

    return text


def convert_part_headings_to_lists(text: str) -> str:
    lines = text.splitlines()
    converted: list[str] = []
    index = 0
    part_heading = re.compile(r"^### Part ([a-z])\)(.*)$")
    block_boundary = re.compile(rf"^(?:## (?:Problem|Activity) \d+|{re.escape(SECTION_SEPARATOR)}$)")

    while index < len(lines):
        match = part_heading.match(lines[index])
        if not match:
            converted.append(lines[index])
            index += 1
            continue

        converted.append('<div class="assignment-parts" markdown="1">')
        while index < len(lines):
            match = part_heading.match(lines[index])
            if not match:
                break

            letter = match.group(1)
            label_suffix = match.group(2).strip()
            index += 1

            while index < len(lines) and lines[index].strip() == "":
                index += 1

            body_lines: list[str] = []
            while index < len(lines):
                if part_heading.match(lines[index]) or block_boundary.match(lines[index]):
                    break
                body_lines.append(lines[index])
                index += 1

            first_content = ""
            while body_lines and body_lines[0].strip() == "":
                body_lines.pop(0)
            if body_lines and can_join_part_first_line(body_lines[0]):
                first_content = body_lines.pop(0).strip()

            label = label_suffix
            if first_content:
                label += f" {first_content}" if label else first_content

            converted.append('<div class="assignment-part" markdown="1">')
            converted.append(f'<div class="assignment-part-label">{letter})</div>')
            converted.append('<div class="assignment-part-content" markdown="1">')
            if label:
                converted.append(label)
            for body_line in body_lines:
                converted.append(body_line)
            converted.append("</div>")
            converted.append("</div>")
            converted.append("")

        converted.append("</div>")
        continue

    return "\n".join(converted)


def can_join_part_first_line(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith(
        ("$$", "-", "1.", ">", "|", "!", "<", "  ")
    )


def fix_leading_italics(text: str) -> str:
    """Fix italics at line start being interpreted as bullet points.
    
    When a line starts with *text* (italics), markdown may interpret the leading
    asterisk as a bullet point. We fix this by converting such lines to use
    HTML <em> tags instead. Handles both single-line and multi-line italics.
    """
    def convert_to_em(match: re.Match[str]) -> str:
        content = match.group(1)
        return f"<em>{content}</em>"
    
    text = re.sub(r"^\*([^*\n]+)\*$", convert_to_em, text, flags=re.M)
    text = re.sub(r"\*(Hint:[^\n]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"(?m)^\*(Hint:[^\n]+)$", r"<em>\1</em>", text)
    text = re.sub(r"(?m)^(<em>Hint:[^\n]*?)\*</em>$", r"\1</em>", text)
    text = re.sub(r"(?m)^\*\s*$\n?", "", text)
    
    def convert_multiline_to_em(match: re.Match[str]) -> str:
        first_line = match.group(1)
        rest = match.group(2)
        return f"<em>{first_line}</em>{rest}"
    
    text = re.sub(
        r"^\*([A-Z][a-z]+:[^\n]+)\n(.*?)^\*\s*$",
        convert_multiline_to_em,
        text,
        flags=re.M | re.S,
    )
    return text


def normalize_markdown_inside_emphasis(text: str) -> str:
    def replace_em(match: re.Match[str]) -> str:
        content = match.group(1)
        content = re.sub(r"\*\*([^*\n]+?)\*\*", r"<strong>\1</strong>", content)
        content = re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", r'<a href="\2">\1</a>', content)
        return f"<em>{content}</em>"

    return re.sub(r"<em>(.*?)</em>", replace_em, text, flags=re.S)


def replace_recap_markers(text: str) -> str:
    lines = text.splitlines()
    converted: list[str] = []
    for line in lines:
        stripped = line.strip()
        recap_match = re.match(r"^\*\*Recap:\s*(.+?)\*\*(?:\s*\\\\)?$", stripped)
        if recap_match:
            converted.append(f"## Recap: {recap_match.group(1)}")
            converted.append("")
            continue

        recap_match = re.match(r"^<strong>Recap:\s*(.+?)</strong>(?:\s*\\\\)?$", stripped)
        if recap_match:
            converted.append(f"## Recap: {recap_match.group(1)}")
            converted.append("")
            continue

        converted.append(line)

    return "\n".join(converted)


def mc_bubble_html(correct: bool = False) -> str:
    classes = "mc-bubble mc-correct" if correct else "mc-bubble"
    return f'<span class="{classes}" aria-hidden="true"></span>'


def mc_square_html(correct: bool = False) -> str:
    classes = "mc-square mc-correct" if correct else "mc-square"
    return f'<span class="{classes}" aria-hidden="true"></span>'


def escape_inline_math_content(content: str) -> str:
    content = html.unescape(content)
    content = normalize_xcolor_for_mathjax(content)
    content = strip_inline_math_spacing_commands(content)
    content = protect_markdown_sensitive_math(content)
    content = content.replace(r"\{", r"\lbrace")
    content = content.replace(r"\}", r"\rbrace")
    content = html.escape(content, quote=False)
    return content.replace("_", "&#95;")


def protect_markdown_sensitive_math(content: str) -> str:
    return content.replace("^{*}", r"^{\ast}").replace("^*", r"^{\ast}")


def normalize_xcolor_for_mathjax(content: str) -> str:
    def strip_textcolor(match: re.Match[str]) -> str:
        return match.group("body")

    content = re.sub(
        r"\\textcolor\[HTML\]\{[0-9A-Fa-f]{6}\}\{(?P<body>[^{}]*)\}",
        strip_textcolor,
        content,
    )
    content = re.sub(
        r"\\textcolor\{[^{}]+\}\{(?P<body>[^{}]*)\}",
        strip_textcolor,
        content,
    )
    return re.sub(
        r"\\color(?:\[HTML\])?\{(?:[0-9A-Fa-f]{6}|[^{}]+)\}\s*",
        "",
        content,
    )


def strip_inline_math_spacing_commands(content: str) -> str:
    return re.sub(r"\\[!,;:]", "", content)


def unindent_accidental_list_code_blocks(text: str) -> str:
    return re.sub(r"(?m)^ {4}(-\s+)", r"\1", text)


def fence_indented_code_blocks(text: str) -> str:
    """Convert real Pandoc-indented code blocks to fenced blocks for Kramdown.

    Assignment pages put Markdown inside raw HTML wrappers. Kramdown handles
    fenced code there more reliably than four-space-indented code, while the
    prose cleanup above has already removed accidental indentation.
    """

    lines = text.splitlines()
    converted: list[str] = []
    i = 0

    while i < len(lines):
        indent_width = code_block_indent_width(lines[i])
        if indent_width is None:
            converted.append(lines[i])
            i += 1
            continue

        block_start = i
        block: list[str] = []
        while i < len(lines):
            line_indent_width = code_block_indent_width(lines[i])
            if lines[i].strip() == "":
                block.append("")
                i += 1
                continue
            if line_indent_width is None or line_indent_width < indent_width:
                break
            block.append(lines[i][indent_width:])
            i += 1

        if any(looks_like_code_line(line) for line in block):
            while block and block[-1] == "":
                block.pop()
            converted.append("```python")
            converted.extend(block)
            converted.append("```")
        else:
            converted.extend(lines[block_start:i])

    return "\n".join(converted)


def code_block_indent_width(line: str) -> int | None:
    match = re.match(r"^( {3,})(?=\S)", line)
    return len(match.group(1)) if match else None


def looks_like_code_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith((">>>", "...", "import ", "from ", "array(", "np.", "#")):
        return True
    if stripped.startswith(("[", "]")) and re.search(r"[\[\],]", stripped):
        return True
    return bool(re.match(r"[A-Za-z_][\w.]*\s*(?:=|\(|@)", stripped))


def format_multiple_choice_rows(text: str) -> str:
    lines = text.splitlines()
    converted: list[str] = []
    choice_marker_pattern = re.compile(
        r'(<span class="(?:mc-bubble|mc-square)(?: mc-correct)?" aria-hidden="true"></span>)'
    )

    for line in lines:
        if not choice_marker_pattern.search(line):
            converted.append(line)
            continue
        if line.lstrip().startswith("|"):
            converted.append(line)
            continue

        pieces = choice_marker_pattern.split(line)
        markers = pieces[1::2]
        if len(markers) < 2:
            converted.append(line)
            continue
        prompt = pieces[0].strip()

        rendered_options = []
        for marker_html, option_html in zip(markers, pieces[2::2]):
            option_html = normalize_mc_option_html(option_html.strip())
            if not option_html:
                continue
            rendered_options.append(f'<span class="mc-option">{marker_html} {option_html}</span>')
        if prompt:
            converted.append(prompt)
        converted.append(f'<div class="mc-options">{"".join(rendered_options)}</div>')

    return "\n".join(converted)


def normalize_mc_option_html(option_html: str) -> str:
    if '<span class="math-inline">' in option_html:
        return option_html

    def inline_math_to_span(match: re.Match[str]) -> str:
        return f'<span class="math-inline">\\\\({escape_inline_math_content(match.group(1))}\\\\)</span>'

    # Math has usually already been protected by fix_latex_for_mathjax before
    # we group multiple-choice rows. Re-wrapping those spans creates nested
    # inline-math HTML, so only protect raw \( ... \) fragments here.
    option_html = re.sub(r"\\\\\((.*?)\\\\\)", inline_math_to_span, option_html)
    option_html = re.sub(r"\\\((.*?)\\\)", inline_math_to_span, option_html)
    return option_html


def replace_inline_math_spans_with_dollars(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        content = html.unescape(match.group(1)).replace("\\\\", "\\")
        return f"${content}$"

    return re.sub(r'<span class="math-inline">\\\\\((.*?)\\\\\)</span>', replace, text)


def add_total_points_separator(text: str) -> str:
    """Add horizontal rule after Total Points line."""
    return re.sub(
        r"^(Total Points:[^\n]+)$",
        r"\1\n\n---",
        text,
        flags=re.M,
    )


def fix_accidental_indented_prose(text: str) -> str:
    """Convert unintended 4-space-indented prose lines into normal paragraphs.

    Markdown treats lines beginning with 4 spaces as code blocks. In our assignment
    sources, this occasionally appears for normal English instructions. We only
    unindent lines that look like prose to avoid changing real code blocks.
    """

    lines = text.splitlines()
    fixed: list[str] = []
    in_list_item = False
    list_base_indent = 0

    for line in lines:
        list_item_match = re.match(r"^(\s*)(?:\d+\.\s+|[-*]\s+)", line)
        if list_item_match:
            in_list_item = True
            list_base_indent = len(list_item_match.group(1))
        elif line.strip() == "":
            pass
        elif re.match(r"^\s*---\s*$", line):
            in_list_item = False
            list_base_indent = 0

        if line.startswith("    "):
            candidate = line[4:]
            if looks_like_accidental_indented_prose(candidate):
                if in_list_item:
                    # Within list items, 4-space indentation often triggers code blocks.
                    # Keep it as a continuation paragraph by using 3 spaces.
                    fixed.append(" " * max(0, list_base_indent + 3) + candidate.lstrip())
                else:
                    fixed.append(candidate)
                continue

        fixed.append(line)
    return "\n".join(fixed)


def looks_like_accidental_indented_prose(content: str) -> bool:
    stripped = content.strip()
    if not stripped:
        return False
    if looks_like_code_line(stripped):
        return False
    if stripped.startswith(("-", "*", "1.", "2.", "3.", "`", "|", "$$")):
        return False
    if stripped.startswith("<") and not stripped.startswith('<span class="math-inline">'):
        return False
    if '<span class="math-inline">' in stripped and re.search(r"[A-Za-z]", stripped):
        return True
    normalized = re.sub(r'<span class="math-inline">.*?</span>', "MATH", stripped)
    if re.search(r"[{};=<>]|\\begin\{|\\end\{", normalized):
        return False
    return bool(
        re.search(r"[A-Za-z].*[.?!:)]$", normalized)
        or re.fullmatch(r"[A-Z][A-Za-z0-9 ,.'\"()/-]+", normalized)
        or normalized in {"then"}
    )


def flatten_solution_ordered_lists(text: str) -> str:
    """Keep solution dropdown lists from rendering as reset lists/code blocks.

    Pandoc emits LaTeX enumerate environments as Markdown ordered lists. Inside
    `<details markdown="1">`, Kramdown can split those lists around raw HTML
    math blocks and treat indented continuation prose as literal code. Explicit
    labels preserve the intended part structure without relying on nested
    Markdown-list continuation rules.
    """

    solution_pattern = re.compile(
        r'(?ms)(<details markdown="1"><summary>Solution</summary>\n\n)(.*?)(\n</details>)'
    )

    def replace_solution(match: re.Match[str]) -> str:
        return (
            match.group(1)
            + flatten_top_level_ordered_list(match.group(2))
            + match.group(3)
        )

    return solution_pattern.sub(replace_solution, text)


def flatten_top_level_ordered_list(text: str) -> str:
    lines = text.splitlines()
    flattened: list[str] = []
    saw_top_level_ordered_item = False
    in_fenced_code = False
    item_pattern = re.compile(r"^(\d+)\.\s+(.*)$")

    for line in lines:
        if line.startswith("```"):
            in_fenced_code = not in_fenced_code
            flattened.append(line)
            continue
        if in_fenced_code:
            flattened.append(line)
            continue

        item_match = item_pattern.match(line)
        if item_match:
            saw_top_level_ordered_item = True
            number = int(item_match.group(1))
            flattened.append(
                f"**({to_lower_roman(number)})** {item_match.group(2).strip()}"
            )
            continue

        if saw_top_level_ordered_item and line.startswith(("    ", "   ")):
            flattened.append(re.sub(r"^ {1,4}", "", line))
            continue

        flattened.append(line)

    return "\n".join(flattened)


def to_lower_roman(number: int) -> str:
    if number <= 0:
        return str(number)

    values = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    ]
    parts: list[str] = []
    remaining = number
    for value, symbol in values:
        count, remaining = divmod(remaining, value)
        if count:
            parts.append(symbol * count)
    return "".join(parts)


def fix_latex_for_mathjax(text: str) -> str:
    display_block_pattern = re.compile(
        r'(<div class="math-display">\n\$\$.*?\$\$\n</div>)',
        flags=re.S,
    )

    def cleanup_display_content(content: str) -> str:
        content = normalize_xcolor_for_mathjax(content)
        content = re.sub(r"\\ensuremath\{\\boxed\{([^{}]*)\}\}", r"\\boxed{\1}", content)

        def clean_text_command(match: re.Match[str]) -> str:
            inner = match.group(1).replace("$", "")
            return rf"\text{{{inner}}}"

        return re.sub(r"\\text\{([^{}]*)\}", clean_text_command, content)

    def fix_backslashes_in_math(content: str) -> str:
        return content.replace("\\\\", "\\\\\\\\")

    def protect_inline_math(content: str) -> str:
        if content.strip() == r"\bigcirc":
            return mc_bubble_html()
        if content.strip() == r"\eecsfilledcircle":
            return mc_bubble_html(correct=True)
        if content.strip() == r"\square":
            return mc_square_html()
        if content.strip() == r"\eecsfilledsquare":
            return mc_square_html(correct=True)
        content = escape_inline_math_content(content)
        return f'<span class="math-inline">\\\\({content}\\\\)</span>'

    def protect_display_math(content: str) -> str:
        content = cleanup_display_content(content.strip())
        content = fix_backslashes_in_math(content)
        return f'\n\n<div class="math-display">\n$$\n{content}\n$$\n</div>\n\n'

    def process_latex_display_math(match: re.Match[str]) -> str:
        return protect_display_math(match.group(2))

    def process_display_math(match: re.Match[str]) -> str:
        return protect_display_math(match.group(1))

    text = re.sub(
        r"(?P<slash>\\{1,2})\[(.*?)(?P=slash)\]",
        process_latex_display_math,
        text,
        flags=re.S,
    )
    text = re.sub(r"\$\$(.*?)\$\$", process_display_math, text, flags=re.S)

    def protect_inline_math_outside_display(segment: str) -> str:
        def convert_multiline_inline_math(match: re.Match[str]) -> str:
            content = match.group(1)
            if "\n\n" in content:
                return match.group(0)
            content = re.sub(r"[ \t]*\n[ \t]*", " ", content).strip()
            content = fix_backslashes_in_math(content)
            return protect_inline_math(content)

        segment = re.sub(
            r"(?<![\\$])\$([^$]*\\begin\{(?:[bpvV]?matrix|array|aligned|cases)\}[^$]*\n[^$]*?)\$(?!\$)",
            convert_multiline_inline_math,
            segment,
            flags=re.S,
        )

        def process_latex_inline_math(match: re.Match[str]) -> str:
            content = match.group(2)
            return protect_inline_math(content)

        segment = re.sub(
            r"(?P<slash>\\{1,2})\((.*?)(?P=slash)\)",
            process_latex_inline_math,
            segment,
        )

        def convert_inline_math(match: re.Match[str]) -> str:
            content = match.group(1)
            if "\n\n" in content or content.startswith("$"):
                return match.group(0)
            content = fix_backslashes_in_math(content)
            return protect_inline_math(content)

        segment = re.sub(
            r"(?<![\\$])\$([^\$\n]+?)\$(?!\$)",
            convert_inline_math,
            segment,
        )
        segment = re.sub(
            r'<span class="math-inline"><span class="math-inline">(.*?)</span></span>',
            r'<span class="math-inline">\1</span>',
            segment,
            flags=re.S,
        )
        return segment.replace(r"\$", "&#36;")

    parts = display_block_pattern.split(text)
    for index in range(0, len(parts), 2):
        parts[index] = protect_inline_math_outside_display(parts[index])
    text = "".join(parts)

    text = convert_linebreaks_outside_display_math(text)

    return text


def convert_linebreaks_outside_display_math(text: str) -> str:
    parts = re.split(r"(\$\$.*?\$\$)", text, flags=re.S)
    for index in range(0, len(parts), 2):
        parts[index] = re.sub(r"\\\\[ \t]*(?=\n|$)", "\n", parts[index])
        parts[index] = re.sub(r"(?<!\\)\\[ \t]*(?=\n|$)", "\n", parts[index])
    return "".join(parts)


def escape_blank_rules(text: str) -> str:
    lines = text.splitlines()
    escaped: list[str] = []

    for index, line in enumerate(lines):
        stripped = line.strip()
        previous_blank = index == 0 or not lines[index - 1].strip()
        next_blank = index == len(lines) - 1 or not lines[index + 1].strip()
        if previous_blank and next_blank and re.fullmatch(r"[-_]{5,}", stripped):
            escaped.append('<span class="answer-blank"></span>')
        else:
            escaped.append(re.sub(r"(?<!\\)_{3,}", escape_underscores, line))

    return "\n".join(escaped)


def escape_underscores(match: re.Match[str]) -> str:
    return "\\_" * len(match.group(0))


@dataclass
class AssignmentItem:
    number: int
    title: str
    body: str


def validate_visible_items_match_source(
    assignment: str,
    source_tex: str,
    generated_markdown: str,
    source_path: Path,
) -> None:
    item_kind = "Activity" if assignment.startswith("Lab ") else "Problem"
    source_items = extract_source_items(source_tex)
    generated_items = extract_generated_items(generated_markdown, item_kind)
    source_labels = [format_item_label(item_kind, item.number, item.title) for item in source_items]
    generated_labels = [format_item_label(item_kind, item.number, item.title) for item in generated_items]

    if source_labels != generated_labels:
        raise SystemExit(
            "Generated Markdown visible items do not match the TeX/PDF source of truth.\n"
            f"Source: {source_path}\n"
            f"TeX/PDF visible {item_kind.lower()}s: {source_labels}\n"
            f"Markdown {item_kind.lower()}s: {generated_labels}"
        )

    if item_kind == "Problem":
        report_programming_problem_positions(source_items, generated_items)


def validate_generated_markdown_structure(markdown: str, output_md: Path) -> None:
    if re.search(r"(?m)^[ \t]*:::[ \t]*(?:[A-Za-z].*)?$", markdown):
        raise SystemExit(
            f"{output_md}: Pandoc fenced div marker leaked into generated Markdown."
        )
    bad_solution_line = find_accidental_solution_code_block(markdown)
    if bad_solution_line:
        raise SystemExit(
            f"{output_md}: solution prose would render as a code block: "
            f"{bad_solution_line!r}"
        )


def find_accidental_solution_code_block(markdown: str) -> str | None:
    solution_pattern = re.compile(
        r'(?ms)<details markdown="1"><summary>Solution</summary>\n\n(.*?)\n</details>'
    )
    for match in solution_pattern.finditer(markdown):
        for line in match.group(1).splitlines():
            if line.startswith("    ") and looks_like_accidental_indented_prose(line[4:]):
                return line.strip()
    return None


def extract_source_items(source_tex: str) -> list[AssignmentItem]:
    source_tex = strip_false_blocks(source_tex)
    source_tex = strip_showsolutions_blocks(source_tex)
    items: list[AssignmentItem] = []
    pattern = re.compile(r"\\begin\{(?:prob|activity)\}(?:\[(.*?)\])?")
    matches = list(pattern.finditer(source_tex))
    for index, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(source_tex)
        title = normalize_item_title(match.group(1) or "")
        items.append(AssignmentItem(index + 1, title, source_tex[body_start:body_end]))
    return items


def extract_generated_items(markdown: str, item_kind: str) -> list[AssignmentItem]:
    items: list[AssignmentItem] = []
    pattern = re.compile(
        rf"^## {item_kind} (\d+)(?::\s*(.*?))?(?:\s+(?:<span class=\"badge\"[^<]*</span>|\(\d+\s+pts?\)))?$",
        re.M,
    )
    matches = list(pattern.finditer(markdown))
    for index, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        items.append(
            AssignmentItem(
                int(match.group(1)),
                normalize_item_title(match.group(2) or ""),
                markdown[body_start:body_end],
            )
        )
    return items


def normalize_item_title(title: str) -> str:
    title = collapse_whitespace(re.sub(r"<[^>]*>", "", title))
    title = title.replace(r"\\(", "$").replace(r"\\)", "$")
    title = title.replace("\\\\", "\\")
    title = title.replace("–", "--")
    return re.sub(r"\s*\(\d+\s+pts?\)\s*$", "", title)


def format_item_label(item_kind: str, number: int, title: str) -> str:
    return f"{item_kind} {number}: {title}" if title else f"{item_kind} {number}"


def report_programming_problem_positions(
    source_items: list[AssignmentItem],
    generated_items: list[AssignmentItem],
) -> None:
    for source_item in source_items:
        if not is_programming_problem(source_item):
            continue
        generated_match = next(
            (item for item in generated_items if item.title == source_item.title),
            None,
        )
        if generated_match and generated_match.number != source_item.number:
            print(
                "WARNING: Programming problem numbering mismatch: "
                f'"{source_item.title}" is Problem {source_item.number} in TeX/PDF '
                f"but Problem {generated_match.number} in generated Markdown.",
                file=sys.stderr,
            )
        else:
            print(
                f'Programming problem check: "{source_item.title}" is Problem {source_item.number}.',
                file=sys.stderr,
            )


def is_programming_problem(item: AssignmentItem) -> bool:
    text = f"{item.title}\n{item.body}".lower()
    return any(
        keyword in text
        for keyword in (
            "programming",
            "jupyter notebook",
            "gradescope autograder",
            "autograder",
        )
    )


def compute_pdf_link(repo_root: Path, output_md: Path) -> str | None:
    pdf_path = output_md.parent / f"{output_md.parent.name}.pdf"
    if not pdf_path.exists():
        return None

    website_root = repo_root / "website"
    try:
        web_path = pdf_path.relative_to(website_root)
    except ValueError:
        return None
    return "/" + web_path.as_posix()


def compute_solutions_pdf_link(repo_root: Path, output_md: Path) -> str | None:
    solutions_pdf_path = output_md.parent / f"{output_md.parent.name}-solutions.pdf"
    if not solutions_pdf_path.exists():
        return None

    website_root = repo_root / "website"
    try:
        web_path = solutions_pdf_path.relative_to(website_root)
    except ValueError:
        return None
    return "/" + web_path.as_posix()


def fix_image_syntax(text: str) -> str:
    def replace_image(match: re.Match[str]) -> str:
        alt = match.group("alt")
        src = match.group("src")
        attrs = match.group("attrs")
        width_match = re.search(r'width="([^"]+)"', attrs)
        if not width_match:
            return f"![{alt}]({src})"

        width = normalize_image_width(width_match.group(1))
        escaped_src = html.escape(src, quote=True)
        escaped_alt = html.escape(alt, quote=True)
        return (
            f'<img src="{escaped_src}" alt="{escaped_alt}" '
            f'style="width: {width}; max-width: 100%;">'
        )

    text = re.sub(
        r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)\{(?P<attrs>[^}]*)\}",
        replace_image,
        text,
    )
    text = re.sub(
        r'(?ms)^:::\s*center\s*\n\s*(<img\b[^>]*>)\s*\n:::\s*$',
        r'<div style="text-align: center;">\n\1\n</div>\n',
        text,
    )
    text = re.sub(r"^:::\s*center\s*$", "", text, flags=re.M)
    text = re.sub(r"^:::\s*$", "", text, flags=re.M)
    return text


def normalize_image_width(width: str) -> str:
    width = html.unescape(width).strip()
    width = width.replace("\\\\", "\\")
    if width in {r"\textwidth", r"\linewidth"}:
        return "100%"

    relative_match = re.fullmatch(r"([0-9]*\.?[0-9]+)\\(?:textwidth|linewidth)", width)
    if relative_match:
        percent = float(relative_match.group(1)) * 100
        return f"{percent:g}%"

    return html.escape(width, quote=True)


def remove_blank_table_headers(text: str) -> str:
    lines = text.splitlines()
    cleaned: list[str] = []
    index = 0

    while index < len(lines):
        if (
            index + 2 < len(lines)
            and is_blank_table_row(lines[index])
            and is_table_separator(lines[index + 1])
            and is_table_row(lines[index + 2])
        ):
            cleaned.append(lines[index + 2])
            cleaned.append(lines[index + 1])
            index += 3
            continue

        cleaned.append(lines[index])
        index += 1

    return "\n".join(cleaned)


def is_table_row(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def table_cells(line: str) -> list[str]:
    return line.strip().strip("|").split("|")


def is_blank_table_row(line: str) -> bool:
    return is_table_row(line) and all(not cell.strip() for cell in table_cells(line))


def is_table_separator(line: str) -> bool:
    if not is_table_row(line):
        return False
    return all(
        bool(re.fullmatch(r":?-{3,}:?", cell.strip()))
        for cell in table_cells(line)
    )


def collapse_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def escape_frontmatter(text: str) -> str:
    return text.replace('"', '\\"')


def compute_default_problems_link(week_file: Path, output_md: Path) -> str:
    relative_target = output_md.parent.relative_to(week_file.parent.parent)
    return f"../{relative_target.as_posix()}/"


def update_week_file(
    week_file: Path,
    event_title: str,
    problems_link: str,
    solutions_link: str | None = None,
) -> None:
    lines = week_file.read_text().splitlines()
    updated = False

    for index, line in enumerate(lines):
        if event_line_matches(line, event_title):
            event_indent = len(line) - len(line.lstrip())
            field_indent = event_indent + 2 if line.lstrip().startswith("- name:") else event_indent
            if line.strip().startswith("title:"):
                value = line.strip().removeprefix("title:").strip()
                lines[index] = " " * event_indent + f"title: {plain_title_value(value)}"
            j = index + 1
            while j < len(lines):
                stripped = lines[j].strip()
                current_indent = len(lines[j]) - len(lines[j].lstrip())

                if stripped.startswith("- name:") and current_indent <= event_indent:
                    break
                if stripped.startswith("title:") and current_indent <= event_indent and j != index:
                    break
                if stripped.startswith("title:") and current_indent >= event_indent:
                    lines[j] = " " * current_indent + f"title: {plain_title_value(stripped.removeprefix('title:').strip())}"
                if stripped.startswith("problems:") and current_indent >= event_indent:
                    lines[j] = " " * current_indent + f"problems: {problems_link}"
                    updated = True
                if stripped.startswith("# problems:") and current_indent >= event_indent:
                    lines[j] = " " * current_indent + f"problems: {problems_link}"
                    updated = True
                if stripped.startswith("solutions:") and current_indent >= event_indent:
                    if solutions_link:
                        lines[j] = " " * current_indent + f"solutions: {solutions_link}"
                    else:
                        del lines[j]
                        continue
                j += 1

            if not updated:
                insert_at = index + 1
                while insert_at < len(lines):
                    stripped = lines[insert_at].strip()
                    current_indent = len(lines[insert_at]) - len(lines[insert_at].lstrip())
                    if stripped.startswith("- name:") and current_indent <= event_indent:
                        break
                    if current_indent <= event_indent and stripped:
                        break
                    insert_at += 1

                lines.insert(index + 1, " " * field_indent + f"problems: {problems_link}")
                if solutions_link:
                    lines.insert(
                        index + 2,
                        " " * field_indent + f"solutions: {solutions_link}",
                    )
                updated = True
            elif solutions_link:
                has_solutions = False
                j = index + 1
                while j < len(lines):
                    stripped = lines[j].strip()
                    current_indent = len(lines[j]) - len(lines[j].lstrip())
                    if stripped.startswith("- name:") and current_indent <= event_indent:
                        break
                    if stripped.startswith("title:") and current_indent <= event_indent and j != index:
                        break
                    if stripped.startswith("solutions:") and current_indent >= event_indent:
                        has_solutions = True
                        break
                    j += 1
                if not has_solutions:
                    lines.insert(index + 2, " " * field_indent + f"solutions: {solutions_link}")
            break

    if not updated:
        raise ValueError(
            f'Could not find event with title "{event_title}" in {week_file}.'
        )

    week_file.write_text("\n".join(lines) + "\n")


def event_line_matches(line: str, event_title: str) -> bool:
    stripped = line.strip()
    return stripped in {
        f"name: {event_title}",
        f"- name: {event_title}",
        f"title: {event_title}",
        f'title: "{event_title}"',
    } or (
        stripped.startswith("title:")
        and plain_title_value(stripped.removeprefix("title:").strip()).strip('"') == event_title
    )


def plain_title_value(value: str) -> str:
    quote = ""
    stripped = value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in {"'", '"'}:
        quote = stripped[0]
        stripped = stripped[1:-1]
    stripped = re.sub(r"</?b>", "", stripped)
    stripped = re.sub(r"</?strong>", "", stripped)
    stripped = re.sub(r"^\*\*(.*?)\*\*$", r"\1", stripped)
    return f"{quote}{stripped}{quote}" if quote else stripped


def copy_referenced_assets(output_md: Path, source_base_dir: Path, website_root: Path) -> None:
    markdown = output_md.read_text()
    relative_paths = find_relative_paths(markdown)
    path_updates: dict[str, str] = {}

    for relative_path in relative_paths:
        source_path = (source_base_dir / relative_path).resolve()
        if not source_path.exists() or not source_path.is_file():
            continue

        dest_filename = source_path.name
        dest_relative, destination_path = asset_destination(
            output_md=output_md,
            website_root=website_root,
            dest_filename=dest_filename,
        )

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)

        new_path = markdown_asset_path(output_md, website_root, dest_relative)
        if str(relative_path) != new_path:
            path_updates[str(relative_path)] = new_path

    if path_updates:
        updated_markdown = markdown
        for old_path, new_path in path_updates.items():
            updated_markdown = updated_markdown.replace(f"]({old_path})", f"]({new_path})")
            updated_markdown = updated_markdown.replace(f'src="{old_path}"', f'src="{new_path}"')
        output_md.write_text(updated_markdown)


def asset_destination(
    output_md: Path,
    website_root: Path,
    dest_filename: str,
) -> tuple[Path, Path]:
    dest_relative = Path("imgs") / dest_filename
    return dest_relative, output_md.parent / dest_relative


def markdown_asset_path(output_md: Path, website_root: Path, dest_relative: Path) -> str:
    return dest_relative.as_posix()


def find_relative_paths(markdown: str) -> set[Path]:
    matches = set()
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)")
    for match in pattern.finditer(markdown):
        candidate = match.group(1) or match.group(2)
        if not candidate:
            continue
        candidate = candidate.strip()
        if candidate.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if candidate.startswith("<") and candidate.endswith(">"):
            candidate = candidate[1:-1]
        if " " in candidate and not candidate.startswith("imgs/"):
            continue
        matches.add(Path(candidate))
    image_pattern = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
    for match in image_pattern.finditer(markdown):
        candidate = match.group(1).strip()
        if candidate.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if " " in candidate and not candidate.startswith("imgs/"):
            continue
        matches.add(Path(candidate))
    return matches


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        raise
