(() => {
  const profiles = Object.assign(
    {},
    window.ordenacoesProfessorProfiles || {},
    window.ordenacoesProfessorDemoProfiles || {}
  );
  const slots = [...document.querySelectorAll('.professor-fallback[data-professor-course]')];
  let active = null;
  let nextId = 0;

  function textNode(tag, className, text) {
    const node = document.createElement(tag);
    node.className = className;
    node.textContent = text;
    return node;
  }

  function courseHref(root, course) {
    if (course.href && course.href.startsWith('#')) return course.href;
    return root + (course.href || `courses/${course.slug}/index.html`);
  }

  function makeCard(profile, course, root, button) {
    const card = document.createElement('section');
    card.className = 'professor-card';
    card.id = `professor-card-${++nextId}`;
    card.setAttribute('role', 'region');
    card.setAttribute('aria-labelledby', `${card.id}-name`);
    card.hidden = true;
    const heading = textNode('div', 'professor-card-name', profile.name);
    heading.setAttribute('role', 'heading');
    heading.setAttribute('aria-level', '2');
    heading.id = `${card.id}-name`;
    card.append(heading);
    card.append(textNode('p', 'professor-card-title', profile.title));
    card.append(textNode('p', 'professor-card-bio', profile.bio));

    const otherCourses = (profile.courses || []).filter(item => item.slug !== course);
    if (otherCourses.length) {
      const line = textNode('p', 'professor-card-courses', 'Também: ');
      otherCourses.forEach((item, index) => {
        if (index) line.append(document.createTextNode(' · '));
        const link = document.createElement('a');
        link.href = courseHref(root, item);
        link.textContent = item.title;
        line.append(link);
      });
      card.append(line);
    }
    button.setAttribute('aria-controls', card.id);
    return card;
  }

  function alignCard(anchor, card) {
    const rect = anchor.getBoundingClientRect();
    const heading = anchor.closest('header.hero, .front-title')?.querySelector('h1');
    if (heading) {
      const titleBottom = heading.getBoundingClientRect().bottom;
      card.style.top = `${Math.max(9, titleBottom - rect.top + 8)}px`;
    } else {
      card.style.top = '';
    }
    const width = card.getBoundingClientRect().width;
    const left = Math.max(16, Math.min(rect.left, window.innerWidth - width - 16));
    card.style.left = `${left - rect.left}px`;
    card.style.right = 'auto';
  }

  function close(anchor, returnFocus = false) {
    if (!anchor) return;
    const button = anchor.querySelector('.professor-name');
    const card = anchor.querySelector('.professor-card');
    if (anchor._hideTimer) window.clearTimeout(anchor._hideTimer);
    button?.setAttribute('aria-expanded', 'false');
    card?.classList.remove('is-open');
    anchor._hideTimer = window.setTimeout(() => {
      if (card && button?.getAttribute('aria-expanded') !== 'true') card.hidden = true;
    }, 170);
    if (active === anchor) active = null;
    if (returnFocus) button?.focus({ preventScroll: true });
  }

  function open(anchor) {
    if (active && active !== anchor) close(active, false);
    const button = anchor.querySelector('.professor-name');
    const card = anchor.querySelector('.professor-card');
    if (!button || !card) return;
    if (anchor._hideTimer) window.clearTimeout(anchor._hideTimer);
    active = anchor;
    button.setAttribute('aria-expanded', 'true');
    card.hidden = false;
    alignCard(anchor, card);
    requestAnimationFrame(() => card.classList.add('is-open'));
  }

  slots.forEach(slot => {
    const course = slot.dataset.professorCourse;
    const profile = profiles[course];
    if (!profile) return; // No record: keep the name as ordinary text.
    const root = slot.dataset.professorRoot || '';
    const shouldOpen = slot.dataset.professorOpen === 'true';
    const anchor = document.createElement('span');
    anchor.className = 'professor-anchor';
    anchor.dataset.professorCourse = course;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'professor-name';
    button.textContent = slot.textContent.trim() || profile.name;
    button.setAttribute('aria-label', `${profile.name}, abre perfil`);
    button.setAttribute('aria-expanded', 'false');
    const card = makeCard(profile, course, root, button);
    anchor.append(button, card);
    slot.replaceWith(anchor);
    button.addEventListener('click', () => {
      if (active === anchor && button.getAttribute('aria-expanded') === 'true') close(anchor, true);
      else open(anchor);
    });
    if (shouldOpen) open(anchor);
  });

  document.addEventListener('click', event => {
    if (active && !active.contains(event.target)) close(active, true);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && active) {
      event.preventDefault();
      close(active, true);
    }
  });
  window.addEventListener('resize', () => {
    if (active) alignCard(active, active.querySelector('.professor-card'));
  });
})();
