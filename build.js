'use strict';
const fs   = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { generate: generateLocations }    = require('./generate-locations');
const { generate: generateServicePages } = require('./generate-service-pages');

const ROOT    = __dirname;
const DOCS    = path.join(ROOT, 'docs');
const PARTIALS = path.join(ROOT, 'partials');

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

function copyFile(src, dest) {
  if (fs.existsSync(src)) fs.copyFileSync(src, dest);
}

console.log('Rebuilding...');
fs.mkdirSync(DOCS, { recursive: true });

// Static assets
copyDir(path.join(ROOT, 'assets'),   path.join(DOCS, 'assets'));
copyDir(path.join(ROOT, 'js'),       path.join(DOCS, 'js'));
copyDir(path.join(ROOT, 'css'),      path.join(DOCS, 'css'));
copyDir(path.join(ROOT, 'services'), path.join(DOCS, 'services'));

const staticFiles = [
  'CNAME', 'robots.txt', 'sitemap.xml', 'llms.txt',
  'favicon.ico', 'favicon.png', 'favicon.webp',
  'favicon-32.png', 'apple-touch-icon.png',
];
for (const f of staticFiles) copyFile(path.join(ROOT, f), path.join(DOCS, f));

// Homepage
const order = [
  'head', 'loader', 'navbar', 'hero', 'why-us',
  'services', 'how-it-works', 'faq', 'cta-banner', 'contact', 'footer', 'sticky-cta',
];
const parts = order.map(n => fs.readFileSync(path.join(PARTIALS, `${n}.html`), 'utf8'));
const html  = `<!DOCTYPE html>\n<html lang="en">\n${parts[0]}\n<body>\n\n${parts.slice(1).join('\n')}\n</body>\n</html>\n`;
fs.writeFileSync(path.join(DOCS, 'index.html'), html, 'utf8');
console.log(`✓ docs/index.html assembled (${order.length} partials)`);

// Generated pages → docs/
generateLocations(DOCS);
generateServicePages(DOCS);

// Tailwind → docs/css/tw.css
try {
  execSync(`./node_modules/.bin/tailwind -i css/input.css -o docs/css/tw.css`, { stdio: 'inherit' });
  console.log('✓ docs/css/tw.css compiled');
} catch (e) {
  process.exit(1);
}
