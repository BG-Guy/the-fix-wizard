'use strict';
// build.js — master build script for the whole site.
// Run with: node build.js
// Wipes docs/ and regenerates it from source: assembles the homepage from
// sections/*/*.html, bundles the section JS/CSS, then hands off to the
// page generators for every service & location detail page. GitHub Pages
// serves docs/ directly — never edit files inside docs/ by hand.
const fs   = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { generate: generateLocations }        = require('./generate-locations');
const { generate: generateServicePages }     = require('./generate-service-pages');
const { generate: generateGenericPages }     = require('./generate-generic-service-pages');
const { generate: generateSitemap }          = require('./generate-sitemap');

const ROOT     = __dirname;
const DOCS     = path.join(ROOT, 'docs');
const SECTIONS = path.join(ROOT, 'sections');

// ---- Small file-copy helpers ----

// Copies an entire directory tree as-is (used for images, etc).
function copyDir(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

// Copies only *.js files from a directory tree, keeping the same relative
// folder structure. Used for sections/, shared/, generated-pages/ so the
// browser's ES module imports (which use relative paths like
// "../sections/navbar/navbar.js") resolve the same way in docs/ as they do
// in source — without also publishing the .html/.css source files, which
// are already consumed at build time below.
function copyJsOnly(src, dest) {
  if (!fs.existsSync(src)) return;
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyJsOnly(s, d);
    } else if (entry.name.endsWith('.js')) {
      fs.mkdirSync(path.dirname(d), { recursive: true });
      fs.copyFileSync(s, d);
    }
  }
}

function copyFile(src, dest) {
  if (fs.existsSync(src)) fs.copyFileSync(src, dest);
}

console.log('Rebuilding...');
fs.mkdirSync(DOCS, { recursive: true });
fs.mkdirSync(path.join(DOCS, 'css'), { recursive: true });

// Static assets
copyDir(path.join(ROOT, 'assets'),   path.join(DOCS, 'assets'));
copyDir(path.join(ROOT, 'services'), path.join(DOCS, 'services'));

// Section/shared/generated-page JS, mirrored into docs/ at the same
// relative paths their import statements expect.
copyJsOnly(path.join(ROOT, 'sections'),        path.join(DOCS, 'sections'));
copyJsOnly(path.join(ROOT, 'shared'),          path.join(DOCS, 'shared'));
copyJsOnly(path.join(ROOT, 'generated-pages'), path.join(DOCS, 'generated-pages'));

const staticFiles = [
  'CNAME', 'robots.txt', 'llms.txt',
  'favicon.ico', 'favicon.png', 'favicon.webp',
  'favicon-32.png', 'apple-touch-icon.png',
];
for (const f of staticFiles) copyFile(path.join(ROOT, f), path.join(DOCS, f));

// ---- Homepage: assemble sections/*/*.html in page order ----
const order = [
  'head', 'loader', 'navbar', 'hero', 'why-us',
  'services', 'gallery', 'how-it-works', 'faq', 'cta-banner', 'contact', 'footer', 'sticky-cta',
];
const parts = order.map(n => fs.readFileSync(path.join(SECTIONS, n, `${n}.html`), 'utf8'));
const html  = `<!DOCTYPE html>\n<html lang="en">\n${parts[0]}\n<body>\n\n${parts.slice(1).join('\n')}\n</body>\n</html>\n`;
fs.writeFileSync(path.join(DOCS, 'index.html'), html, 'utf8');
console.log(`✓ docs/index.html assembled (${order.length} sections)`);

// ---- CSS: concatenate each section's stylesheet into one docs/css/custom.css ----
// Every page links a single "/css/custom.css" — bundling here means adding
// a new section's CSS is just adding its file to this list, no HTML changes.
const cssFiles = [
  'shared/global.css',
  'sections/loader/loader.css',
  'sections/navbar/navbar.css',
  'sections/hero/hero.css',
  'sections/why-us/why-us.css',
  'sections/gallery/gallery.css',
  'sections/faq/faq.css',
  'sections/sticky-cta/sticky-cta.css',
  'generated-pages/service-page.css',
];
const bundledCss = cssFiles
  .map(f => fs.readFileSync(path.join(ROOT, f), 'utf8'))
  .join('\n');
fs.writeFileSync(path.join(DOCS, 'css', 'custom.css'), bundledCss, 'utf8');
console.log(`✓ docs/css/custom.css bundled (${cssFiles.length} files)`);

// ---- Generated pages → docs/ ----
generateLocations(DOCS);
generateServicePages(DOCS);
generateGenericPages(DOCS);
generateSitemap(DOCS);

// ---- Tailwind → docs/css/tw.css ----
try {
  execSync(`./node_modules/.bin/tailwind -i css/input.css -o docs/css/tw.css`, { stdio: 'inherit' });
  console.log('✓ docs/css/tw.css compiled');
} catch (e) {
  process.exit(1);
}
