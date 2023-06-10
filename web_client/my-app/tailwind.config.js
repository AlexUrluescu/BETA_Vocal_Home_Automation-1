/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      screens: {
        'sm': '740px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        'custom': '1440px', // Media querie personalizat
      },
    },
  },
  plugins: [],
}