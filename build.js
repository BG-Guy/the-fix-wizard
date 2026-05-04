const fs = require('fs');
const path = require('path');

const PARTIALS_DIR = path.join(__dirname, 'partials');
const OUTPUT = path.join(__dirname, 'index.html');

const order = [
    'head',
    'loader',
    'navbar',
    'hero',
    'why-us',
    'services',
    'faq',
    'cta-banner',
    'contact',
    'footer',
    'sticky-cta',
];

const parts = order.map(name => {
    const file = path.join(PARTIALS_DIR, `${name}.html`);
    return fs.readFileSync(file, 'utf8');
});

const html = `<!DOCTYPE html>
<html lang="en">
${parts[0]}
<body>

${parts.slice(1).join('\n')}
</body>
</html>
`;

fs.writeFileSync(OUTPUT, html, 'utf8');
console.log(`Built index.html from ${order.length} partials`);
