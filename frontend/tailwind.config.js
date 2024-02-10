/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        textColor: '#F4F4F4',
        headerColor: "#021027",
        primary: "#02183C",
        secondary: "#CC5F00",
        sidebar: '#3d68ff',
        active_nav_link : '#1947ee'
      }
    },
  },
  plugins: [],
}

