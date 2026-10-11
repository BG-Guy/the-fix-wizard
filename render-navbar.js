'use strict';
// render-navbar.js — the single source for the site navbar. Every page gets
// its navbar from here (homepage via build.js, generated pages via the
// generate-*.js scripts, hand-written pages via the <!-- @navbar --> marker),
// so the navbar can never drift between pages. Markup lives in
// sections/navbar/navbar.html.
const fs   = require('fs');
const path = require('path');

const SOURCE = path.join(__dirname, 'sections', 'navbar', 'navbar.html');

// contactHref: where Contact / Free Quote point. Service pages pass e.g.
// "/?service=Chimney+%26+Masonry#contact" to pre-select the quote form.
function renderNavbar(contactHref = '/#contact') {
  return fs.readFileSync(SOURCE, 'utf8').replaceAll('{{CONTACT_HREF}}', contactHref);
}

// For hand-written pages: replaces `<!-- @navbar -->` (or
// `<!-- @navbar /?service=...#contact -->`) with the rendered navbar.
function injectNavbar(html) {
  return html.replace(/<!-- @navbar(?: (\S+))? -->/g, (_, href) => renderNavbar(href));
}

module.exports = { renderNavbar, injectNavbar };
