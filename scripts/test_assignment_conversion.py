"""Regression tests through Pandoc and the site's actual Kramdown renderer.

Run from any directory: python3 website/scripts/test_assignment_conversion.py
Requires the website's installed Bundler gems and Pandoc.
"""
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import generate_homework_markdown as converter
from check_assignment_html import check_list_and_choice_structure


class AssignmentConversionTests(unittest.TestCase):
    def convert(self, source, solutions=False):
        transformed = converter.transform_assignment_tex(source, solutions)
        transformed, tables = converter.replace_tabulars_with_html_placeholders(transformed)
        with tempfile.TemporaryDirectory() as directory:
            source_path = Path(directory) / 'input.tex'
            result_path = Path(directory) / 'output.md'
            source_path.write_text(transformed)
            converter.run_pandoc(source_path, result_path)
            markdown = converter.cleanup_markdown(result_path.read_text())
        markdown = converter.restore_tabular_html(markdown, tables)
        self.assertEqual(check_list_and_choice_structure(markdown), [])
        rendered = subprocess.run(
            ['bundle', 'exec', 'ruby', '-e',
             'require "kramdown"; require "kramdown-parser-gfm"; '
             'puts Kramdown::Document.new(STDIN.read, input: "GFM").to_html'],
            cwd=Path(converter.__file__).resolve().parents[1],
            input=markdown, text=True, capture_output=True, check=True,
        ).stdout
        self.assertEqual(check_list_and_choice_structure(rendered), [])
        for code in re.findall(r'(?s)<pre\b.*?</pre>', rendered):
            self.assertNotRegex(code, r'math-display|\\frac|<li')
        return markdown, rendered

    def test_equations_stay_inside_three_numbered_items(self):
        _, rendered = self.convert(r'''
\begin{enumerate}
\item \textbf{Choose a model.} \[h(x)=w\]
\item \textbf{Choose a loss function.} \[L(y,w)=(y-w)^2\]
\item Minimize average loss.
\begin{itemize}
\item Squared loss: \[R(w)=\frac{1}{n}\sum_i(y_i-w)^2\]
\item Absolute loss: \[R(w)=\frac{1}{n}\sum_i|y_i-w|\]
\end{itemize}
\end{enumerate}
''')
        self.assertEqual(len(re.findall(r'<ol\b', rendered)), 1)
        self.assertEqual(re.findall(r'<li value="(\d+)"', rendered), ['1', '2', '3'])
        self.assertRegex(rendered, r'(?s)<li value="1">.*?Choose a model.*?math-display.*?</li>')
        self.assertRegex(rendered, r'(?s)<li value="3">.*?<ul.*?</ul>\s*</li>')

    def test_solution_lists_keep_math_code_and_nested_items(self):
        _, rendered = self.convert(r'''
\begin{solution}
\begin{enumerate}
\item First step. \[x=\frac{1}{2}\]
Continuation after the equation.
\begin{enumerate}
\item Nested first.
\item Nested second.
\end{enumerate}
\item Second step.
\begin{verbatim}
1. literal code
print("not a list")
\end{verbatim}
\end{enumerate}
\end{solution}
\begin{enumerate}
\item A separate list starts again.
\end{enumerate}
''', solutions=True)
        self.assertEqual(len(re.findall(r'<ol\b', rendered)), 3)
        self.assertIn('Continuation after the equation.', rendered)
        self.assertIn('1. literal code', re.sub(r'<[^>]+>', '', rendered))
        self.assertRegex(rendered, r'(?s)</details>.*?<ol[^>]*start="1"')

    def test_numbering_start_and_style_survive(self):
        node = [{'t': 'OrderedList', 'c': [[4, {'t': 'UpperRoman'}, {'t': 'Period'}],
                [[{'t': 'Para', 'c': [{'t': 'Str', 'c': 'Fourth'}]}],
                 [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'Fifth'}]}]]]}]
        preserved = converter.preserve_pandoc_lists(node)
        html = '\n'.join(x['c'][1] for x in preserved if x['t'] == 'RawBlock')
        self.assertIn('start="4"', html)
        self.assertIn('list-style-type: upper-roman', html)
        self.assertIn('value="5"', html)
        self.assertEqual(check_list_and_choice_structure(html), [])

    def test_explicit_item_labels_are_not_dropped(self):
        _, rendered = self.convert(r'\begin{itemize}\item[(i)] First.\item[(ii)] Second.\end{itemize}')
        self.assertIn('<strong>(i)</strong>', rendered)
        self.assertIn('<strong>(ii)</strong>', rendered)

    def test_legacy_leading_answers_fill_exact_choices(self):
        for answer in ['30', '7', '11', '15']:
            with self.subTest(answer=answer):
                _, rendered = self.convert(
                    r'\bubble{1} \bubble{5} \bubble{6} \bubble{7} \bubble{11} \bubble{15} \bubble{30}'
                    '\n\\begin{solution}\n\\textbf{$' + answer + '$.} Explanation.\n\\end{solution}',
                    solutions=True,
                )
                before, solution = rendered.split('<details', 1)
                self.assertNotIn('mc-correct', before)
                self.assertEqual(solution.count('mc-correct'), 1)
                self.assertRegex(solution, rf'mc-correct[^>]*></span> {answer}</span>')

    def test_explicit_multiple_checkbox_answers(self):
        _, rendered = self.convert(r'''
\correctsquarebubble{A} \squarebubble{B} \correctsquarebubble{C}
\begin{solution}
Both A and C work.
\end{solution}
''', solutions=True)
        before, solution = rendered.split('<details', 1)
        self.assertNotIn('mc-correct', before)
        self.assertEqual(solution.count('mc-square mc-correct'), 2)

    def test_unmarked_answers_are_not_guessed_from_prose(self):
        _, rendered = self.convert(r'''
\bubble{1} \bubble{11}
\begin{solution}
Consider 11, then compare it to 1.
\end{solution}
''', solutions=True)
        self.assertNotIn('mc-options', rendered.split('<details', 1)[1])

    def test_student_page_has_no_answer_markers(self):
        _, rendered = self.convert(r'''
\bubble{No} \correctbubble{Yes}
\begin{solution}
Yes is correct.
\end{solution}
''')
        self.assertNotIn('mc-correct', rendered)
        self.assertNotIn('<details', rendered)

    def test_table_bubbles_do_not_create_an_empty_solution_row(self):
        _, rendered = self.convert(r'''
\begin{tabular}{cc}
\bubble{} & \correctbubble{} \\
\end{tabular}
\begin{solution}
The second column is correct.
\end{solution}
''', solutions=True)
        self.assertNotIn('mc-options', rendered.split('<details', 1)[1])

    def test_checks_reject_reset_numbering_and_empty_answer_rows(self):
        self.assertTrue(check_list_and_choice_structure(
            '<ol class="assignment-list" start="1" data-item-count="2">'
            '<li value="1">A</li><li value="1">B</li></ol>'))
        self.assertTrue(check_list_and_choice_structure(
            '<ol class="assignment-list" start="1" data-item-count="2">'
            '<li value="1">A</li></ol>'))
        self.assertTrue(check_list_and_choice_structure(
            '<details><summary>Solution</summary><div class="mc-options">'
            '<span class="mc-bubble"></span> A</div></details>'))


if __name__ == '__main__':
    unittest.main()
