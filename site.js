/* Real links work without JS. Enhance language changes without losing reading position. */
(() => {
  let controller;
  let currentUrl = location.href;
  let currentKey = history.state?.paneluneKey || crypto.randomUUID();
  const positions = new Map();
  history.replaceState({ ...history.state, paneluneKey: currentKey }, '', currentUrl);
  const position = () => {
    const sections = [...document.querySelectorAll('main > [id]')];
    const section = sections.find(el => el.getBoundingClientRect().bottom > 0);
    return { id: section?.id, offset: section?.getBoundingClientRect().top || 0, y: scrollY };
  };
  const restore = pos => {
    const section = pos?.id && document.getElementById(pos.id);
    const y = section ? scrollY + section.getBoundingClientRect().top - pos.offset : (pos?.y || 0);
    window.scrollTo({ top: y, behavior: 'instant' });
  };
  async function navigate(url, push, savedPosition) {
    controller?.abort();
    controller = new AbortController();
    const active = controller;
    const pos = savedPosition || position();
    try {
      const response = await fetch(url, { signal: active.signal });
      if (!response.ok) throw new Error('Language page unavailable');
      const next = new DOMParser().parseFromString(await response.text(), 'text/html');
      if (!next.querySelector('.language-nav') || !next.querySelector('#main')) throw new Error('Invalid language page');
      if (active.signal.aborted) return;
      if (push) {
        positions.set(currentKey, pos);
        history.replaceState({ paneluneKey: currentKey, position: pos }, '', currentUrl);
        currentKey = crypto.randomUUID();
        history.pushState({ paneluneKey: currentKey, position: pos }, '', url);
        currentUrl = url;
      }
      document.documentElement.lang = next.documentElement.lang;
      document.title = next.title;
      const metadata = 'meta, link[rel="canonical"], link[rel="alternate"], script[type="application/ld+json"]';
      document.head.querySelectorAll(metadata).forEach(el => el.remove());
      next.head.querySelectorAll(metadata).forEach(el => document.head.append(document.importNode(el, true)));
      // Existing stylesheet/icons use absolute URLs so history changes cannot break them.
      document.body.replaceChildren(...[...next.body.childNodes].map(el => document.importNode(el, true)));
      restore(pos);
      const current = document.querySelector('.language-nav [aria-current="page"]');
      current?.focus({ preventScroll: true });
    } catch (error) {
      if (error.name !== 'AbortError') location.assign(url);
    }
  }
  document.head.querySelectorAll('link[href], script[src]').forEach(el => {
    const attr = el.hasAttribute('href') ? 'href' : 'src';
    el.setAttribute(attr, new URL(el.getAttribute(attr), location.href).href);
  });
  document.addEventListener('click', event => {
    const link = event.target.closest('a[data-language]');
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    if (link.getAttribute('aria-current') === 'page') return;
    const url = new URL(link.href);
    url.hash = location.hash;
    navigate(url.href, true);
  });
  window.addEventListener('popstate', event => {
    const url = location.href;
    // Native fragment navigation already restores the correct anchor/scroll position.
    if (new URL(currentUrl).pathname === location.pathname) {
      currentUrl = url;
      return;
    }
    positions.set(currentKey, position());
    currentKey = event.state?.paneluneKey || crypto.randomUUID();
    currentUrl = url;
    navigate(url, false, positions.get(currentKey) || event.state?.position);
  });
  window.addEventListener('hashchange', () => { currentUrl = location.href; });
})();
