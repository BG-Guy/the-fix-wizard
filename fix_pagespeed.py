#!/usr/bin/env python3
"""
PageSpeed fixes:
  1. Replace render-blocking Google Fonts + Font Awesome <link> tags with
     async rel="preload" + onload pattern across all 203 HTML files.
  2. Add missing width/height to images in partials.
  3. Update COMMON_HEAD in generate_areas.py.
"""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# ─── Async font pattern ────────────────────────────────────────────────────────

GFONTS_URL = "https://fonts.googleapis.com/css2?family=Cinzel:wght@600;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap"
FA_URL     = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"

# Every variant of the blocking tags seen across different files
BLOCKING_VARIANTS = [
    # partials/head.html + service pages
    (
        f'<link href="{GFONTS_URL}" rel="stylesheet">\n'
        f'    <link rel="stylesheet" href="{FA_URL}">',
        f'<link rel="preload" href="{GFONTS_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
        f'    <noscript><link rel="stylesheet" href="{GFONTS_URL}"></noscript>\n'
        f'    <link rel="preload" href="{FA_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
        f'    <noscript><link rel="stylesheet" href="{FA_URL}"></noscript>'
    ),
    # generate_areas.py COMMON_HEAD (different indentation)
    (
        f'    <link href="{GFONTS_URL}" rel="stylesheet">\n'
        f'    <link rel="stylesheet" href="{FA_URL}">',
        f'    <link rel="preload" href="{GFONTS_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
        f'    <noscript><link rel="stylesheet" href="{GFONTS_URL}"></noscript>\n'
        f'    <link rel="preload" href="{FA_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
        f'    <noscript><link rel="stylesheet" href="{FA_URL}"></noscript>'
    ),
]

def patch_async_fonts(content):
    for old, new in BLOCKING_VARIANTS:
        if old in content:
            content = content.replace(old, new)
            return content, True
    # Already patched
    return content, False


# ─── Patch all HTML files ──────────────────────────────────────────────────────

def patch_all_html():
    patched = 0
    skipped = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip node_modules
        dirnames[:] = [d for d in dirnames if d != "node_modules"]
        for fname in filenames:
            if fname != "index.html":
                continue
            fpath = os.path.join(dirpath, fname)
            with open(fpath) as f:
                content = f.read()
            new_content, changed = patch_async_fonts(content)
            if changed:
                with open(fpath, "w") as f:
                    f.write(new_content)
                patched += 1
            else:
                skipped += 1
    print(f"  ✓  {patched} HTML files patched (async fonts), {skipped} already done")


# ─── Patch partials/head.html ──────────────────────────────────────────────────

def patch_head_partial():
    path = os.path.join(ROOT, "partials", "head.html")
    with open(path) as f:
        content = f.read()
    new_content, changed = patch_async_fonts(content)
    if changed:
        with open(path, "w") as f:
            f.write(new_content)
        print("  ✓  partials/head.html patched")
    else:
        print("  –  partials/head.html already patched")


# ─── Fix image width/height in partials ───────────────────────────────────────

def patch_images():
    changes = 0

    # services.html — all 8 service card images (displayed at h-[210px], fluid width)
    path = os.path.join(ROOT, "partials", "services.html")
    with open(path) as f:
        content = f.read()
    # Add width="800" height="210" to card images missing it
    new = re.sub(
        r'(<img src="assets/images/[^"]+\.webp" alt="[^"]+" class="w-full h-\[210px\][^"]*")',
        r'\1 width="800" height="210"',
        content
    )
    if new != content:
        with open(path, "w") as f:
            f.write(new)
        changes += content.count('class="w-full h-[210px]') - new.count('class="w-full h-[210px]') + \
                   new.count('width="800" height="210"')
        print("  ✓  partials/services.html — service card images got width/height")

    # footer.html — footer logo
    path = os.path.join(ROOT, "partials", "footer.html")
    with open(path) as f:
        content = f.read()
    new = content.replace(
        'class="h-[64px] w-auto object-contain rounded-lg">',
        'class="h-[64px] w-auto object-contain rounded-lg" width="199" height="64" loading="lazy">'
    )
    if new != content:
        with open(path, "w") as f:
            f.write(new)
        print("  ✓  partials/footer.html — footer logo got width/height")

    # loader.html — loader logo
    path = os.path.join(ROOT, "partials", "loader.html")
    with open(path) as f:
        content = f.read()
    new = content.replace(
        'class="loader-logo-img">',
        'class="loader-logo-img" width="199" height="110">'
    )
    if new != content:
        with open(path, "w") as f:
            f.write(new)
        print("  ✓  partials/loader.html — loader logo got width/height")


# ─── Patch generate_areas.py COMMON_HEAD ──────────────────────────────────────

def patch_generator():
    path = os.path.join(ROOT, "generate_areas.py")
    with open(path) as f:
        content = f.read()

    old = (
        f'    <link href="{GFONTS_URL}" rel="stylesheet">\\n'
        f'    <link rel="stylesheet" href="{FA_URL}">"""'
    )
    new = (
        f'    <link rel="preload" href="{GFONTS_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\\n'
        f'    <noscript><link rel="stylesheet" href="{GFONTS_URL}"></noscript>\\n'
        f'    <link rel="preload" href="{FA_URL}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\\n'
        f'    <noscript><link rel="stylesheet" href="{FA_URL}"></noscript>"""'
    )
    if old in content:
        with open(path, "w") as f:
            f.write(content.replace(old, new))
        print("  ✓  generate_areas.py COMMON_HEAD updated")
    else:
        print("  –  generate_areas.py already updated")


# ─── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Patching async font loading in all HTML files...")
    patch_all_html()
    patch_head_partial()

    print("Fixing image width/height attributes...")
    patch_images()

    print("Updating generator script...")
    patch_generator()

    print("\nDone. Next: node build.js && ./node_modules/.bin/tailwind -i css/input.css -o css/tw.css --minify")
