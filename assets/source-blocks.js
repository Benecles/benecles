(() => {
  const wordCount = (node) => (node.textContent.match(/\S+/g) || []).length;

  document.querySelectorAll('.source-block').forEach((block, index) => {
    const original = block.querySelector('blockquote');
    if (!original) return;

    const actions = block.querySelector('.source-block__actions');
    if (!actions) return;

    const translation = block.querySelector('.source-block__translation');
    if (wordCount(original) >= 300 || (translation && wordCount(translation) >= 300)) {
      block.dataset.collapsible = 'true';
      const expand = document.createElement('button');
      expand.className = 'source-block__button';
      expand.type = 'button';
      const initiallyExpanded = block.dataset.expanded === 'true';
      expand.textContent = initiallyExpanded ? 'recolher' : 'continuar lendo';
      expand.setAttribute('aria-expanded', String(initiallyExpanded));
      expand.addEventListener('click', () => {
        const expanded = block.dataset.expanded !== 'true';
        block.dataset.expanded = String(expanded);
        expand.setAttribute('aria-expanded', String(expanded));
        expand.textContent = expanded ? 'recolher' : 'continuar lendo';
      });
      actions.append(expand);
    }

    const translate = block.querySelector('[data-source-translate]');
    if (translation && translate) {
      translation.id ||= `source-translation-${index + 1}`;
      translate.setAttribute('aria-controls', translation.id);
      const demoTranslated = block.dataset.demoTranslation === 'true';
      if (demoTranslated) {
        translation.hidden = false;
        original.hidden = true;
        translate.textContent = 'ver original';
      }
      translate.setAttribute('aria-expanded', String(demoTranslated));
      translate.addEventListener('click', () => {
        const showingTranslation = translation.hidden;
        translation.hidden = !showingTranslation;
        original.hidden = showingTranslation;
        translate.setAttribute('aria-expanded', String(showingTranslation));
        translate.textContent = showingTranslation ? 'ver original' : 'traduzir';
      });
    }
  });
})();
