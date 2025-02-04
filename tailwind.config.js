/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Templates inside apps
    // './tasks/**/*.html',
    './tasks/*.py',
    './**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

