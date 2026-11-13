(() => {
  const root = document.documentElement;
  const fontKey = 'eecs245-font';
  const appearanceKey = 'eecs245-appearance';
  const alternateFonts = ['palatino', 'atkinson'];
  const schemes = { light: 'default', paper: 'paper', dark: 'dark' };
  const cookieLifetime = 60 * 60 * 24 * 365;

  function savePreference(key, value) {
    const secure = location.protocol === 'https:' ? '; Secure' : '';
    try {
      document.cookie = `${key}=${value}; Max-Age=${cookieLifetime}; Path=/; SameSite=Lax${secure}`;
    } catch {
      // Keep the selection for the current page if cookies are disabled.
    }
  }

  function readPreference(key, validValues) {
    const prefix = `${key}=`;
    const entry = document.cookie.split(';').map((cookie) => cookie.trim())
      .find((cookie) => cookie.startsWith(prefix));
    const value = entry?.slice(prefix.length);
    return validValues.includes(value) ? value : null;
  }

  function loadPreference(key, validValues) {
    const value = readPreference(key, validValues);
    if (value) return value;
    // Migrate the preference saved by the old sidebar switch or local preview.
    try {
      const previous = localStorage.getItem(key);
      if (validValues.includes(previous)) {
        savePreference(key, previous);
        if (readPreference(key, validValues)) localStorage.removeItem(key);
        return previous;
      }
    } catch {
      // Use the site defaults when browser storage is unavailable.
    }
    return null;
  }

  function applyFont(value) {
    const font = alternateFonts.includes(value) ? value : 'default';
    for (const option of alternateFonts) {
      root.classList.toggle(`font-${option}`, option === font);
    }
    return font;
  }

  function applyAppearance(value) {
    const appearance = Object.hasOwn(schemes, value) ? value : 'light';
    root.dataset.readingAppearance = appearance;
    if (window.jtd.getTheme() !== schemes[appearance]) {
      window.jtd.setTheme(schemes[appearance]);
    }
    return appearance;
  }

  const fontValues = ['default', ...alternateFonts];
  const appearanceValues = Object.keys(schemes);
  let font = applyFont(loadPreference(fontKey, fontValues));
  let appearance = applyAppearance(loadPreference(appearanceKey, appearanceValues));

  document.addEventListener('DOMContentLoaded', () => {
    const dialog = document.getElementById('reading-settings');
    const button = document.querySelector('.reading-settings-button');
    const fontChoices = dialog?.querySelectorAll('input[name="font"]');
    const colorChoices = dialog?.querySelectorAll('input[name="appearance"]');

    function syncChoices() {
      fontChoices?.forEach((choice) => { choice.checked = choice.value === font; });
      colorChoices?.forEach((choice) => { choice.checked = choice.value === appearance; });
    }

    if (!button || typeof dialog?.showModal !== 'function') return;
    syncChoices();
    button.hidden = false;

    const mobile = window.matchMedia('(max-width: 639px)');
    const toolbarMobile = window.matchMedia('(max-width: 799px)');
    const toolbar = document.getElementById('main-header');
    const menu = document.getElementById('menu-button');

    function placeButton() {
      if (toolbarMobile.matches && menu) menu.after(button);
      else toolbar?.append(button);
      positionDialog();
    }

    function positionDialog() {
      if (!dialog.open || mobile.matches) return;
      const rect = button.getBoundingClientRect();
      const width = dialog.offsetWidth;
      const viewportWidth = document.documentElement.clientWidth;
      const left = Math.max(12, Math.min(rect.right - width, viewportWidth - width - 12));
      const top = Math.max(12, rect.bottom + 8);
      dialog.style.setProperty('--reading-left', `${left}px`);
      dialog.style.setProperty('--reading-top', `${top}px`);
    }

    function openDialog() {
      if (mobile.matches) {
        dialog.showModal();
        root.classList.add('reading-settings-modal-open');
      } else {
        dialog.show();
        positionDialog();
      }
      button.setAttribute('aria-expanded', 'true');
    }

    button.addEventListener('click', () => {
      if (dialog.open) dialog.close();
      else openDialog();
    });

    dialog.querySelectorAll('button').forEach((action) => {
      action.addEventListener('click', () => dialog.close());
    });

    dialog.addEventListener('close', () => {
      root.classList.remove('reading-settings-modal-open');
      button.setAttribute('aria-expanded', 'false');
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && dialog.open && !mobile.matches) {
        event.preventDefault();
        dialog.close();
        button.focus({ preventScroll: true });
      }
    });

    document.addEventListener('pointerdown', (event) => {
      if (dialog.open && !mobile.matches && !dialog.contains(event.target) && !button.contains(event.target)) {
        dialog.close();
      }
    });

    dialog.addEventListener('click', (event) => {
      if (event.target !== dialog || !mobile.matches) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientY < rect.top) dialog.close();
    });

    mobile.addEventListener('change', () => { if (dialog.open) dialog.close(); });
    toolbarMobile.addEventListener('change', placeButton);
    placeButton();
    window.addEventListener('resize', positionDialog);
    window.addEventListener('scroll', positionDialog, { passive: true });

    dialog.addEventListener('change', (event) => {
      const { name, value } = event.target;
      if (name === 'font') {
        font = applyFont(value);
        savePreference(fontKey, font);
      } else if (name === 'appearance') {
        appearance = applyAppearance(value);
        savePreference(appearanceKey, appearance);
      }
    });

    window.addEventListener('focus', () => {
      const savedFont = readPreference(fontKey, fontValues);
      const savedAppearance = readPreference(appearanceKey, appearanceValues);
      if (savedFont) font = applyFont(savedFont);
      if (savedAppearance) appearance = applyAppearance(savedAppearance);
      syncChoices();
    });
  });
})();
