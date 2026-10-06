/* CASA-1: translation toggle for source blocks (.fonte). Original stays the default; the translation sits under it. */
document.querySelectorAll('.fonte [data-tr]').forEach(function (b) {
  b.addEventListener('click', function () {
    var s = b.closest('.fonte'), t = s.querySelector('.tr'), show = t.hidden;
    t.hidden = !show;
    b.setAttribute('aria-expanded', String(show));
    b.textContent = show ? 'ocultar tradução' : 'ver tradução';
  });
});
