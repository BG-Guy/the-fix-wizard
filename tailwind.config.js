/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './partials/**/*.html',
    './index.html',
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#091236',
          900: '#0d1b4b',
          800: '#152468',
          700: '#1e3480',
        },
        orange: {
          DEFAULT: '#FF6B35',
          light:   '#FF8C42',
          dark:    '#e55a22',
        },
      },
      fontFamily: {
        sans:   ['Inter', 'sans-serif'],
        cinzel: ['Cinzel', 'serif'],
      },
      borderRadius: {
        card: '22px',
        xl2:  '36px',
        md2:  '14px',
      },
      screens: {
        xs:  '480px',
        tab: '900px',
        // sm: 640 | md: 768 | lg: 1024 | xl: 1280  (Tailwind defaults kept)
      },
      maxWidth: {
        site: '1200px',
      },
      boxShadow: {
        orange: '0 8px 28px rgba(255,107,53,.4)',
        card:   '0 8px 40px rgba(13,27,75,.16)',
        'card-xl': '0 20px 60px rgba(13,27,75,.22)',
      },
      transitionDuration: {
        400: '400ms',
        550: '550ms',
      },
    },
  },
}
