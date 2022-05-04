module.exports = {
   purge: {
     content: [
       "./hello_api/_templates/*.{html,js}",
       "./hello_api/_templates/**/*.{html,js}",
       "./hello_api/_app/templates/**/*.{html,md}"
     ],
     //options: {
     //  keyframes: true,
     //},
   },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
