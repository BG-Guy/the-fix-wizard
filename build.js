const fs   = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { generate: generateLocations } = require('./generate-locations');

const PARTIALS = path.join(__dirname, 'partials');
const OUTPUT   = path.join(__dirname, 'index.html');

const order = [
  'head', 'loader', 'navbar', 'hero', 'why-us',
  'services', 'how-it-works', 'faq', 'cta-banner', 'contact', 'footer', 'sticky-cta',
];

// 1. Assemble index.html from partials
const parts = order.map(n => fs.readFileSync(path.join(PARTIALS, `${n}.html`), 'utf8'));
const html  = `<!DOCTYPE html>\n<html lang="en">\n${parts[0]}\n<body>\n\n${parts.slice(1).join('\n')}\n</body>\n</html>\n`;
fs.writeFileSync(OUTPUT, html, 'utf8');
console.log(`✓ index.html assembled (${order.length} partials)`);

// 2. Generate location pages
generateLocations();

// 3. Compile Tailwind
try {
  execSync('./node_modules/.bin/tailwind -i css/input.css -o css/tw.css', { stdio: 'inherit' });
  console.log('✓ css/tw.css compiled');
} catch (e) {
  process.exit(1);
}
