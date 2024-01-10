// /** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: [],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
//   purge: [
//     './projects/templates/**/*.html',
//     './templates/*.html',
//     './static/**/*.js',
//   ],
// }


// module.exports = {
//   // other settings...

//   purge: [
//     './projects/templates/**/*.html',
//     './templates/*.html',
//     './static/**/*.js',
//   ],

//   // other settings...
// }

module.exports = {
  content: [
      './templates/*.html',
      './templates/**/*.html',
      './static/**/*.js',
      './projects/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}