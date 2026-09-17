(function () {
  'use strict';
  var key = 'eecs245-font';
  var root = document.documentElement;
  function apply(value) {
    var palatino = value === 'palatino';
    root.classList.toggle('font-palatino', palatino);
    document.querySelectorAll('.font-preference-input').forEach(function (input) {
      input.checked = palatino;
    });
  }
  // Apply before the page renders; storage may be unavailable in private browsing.
  try { apply(localStorage.getItem(key)); } catch (error) { apply('default'); }
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.font-preference').forEach(function (control) {
      control.hidden = false;
    });
    apply(root.classList.contains('font-palatino') ? 'palatino' : 'default');
    document.querySelectorAll('.font-preference-input').forEach(function (input) {
      input.addEventListener('change', function () {
        var value = input.checked ? 'palatino' : 'default';
        apply(value);
        try { localStorage.setItem(key, value); } catch (error) { /* Keep the current-page choice. */ }
      });
    });
  });
  window.addEventListener('storage', function (event) {
    if (event.key === key || event.key === null) apply(event.newValue);
  });
}());
