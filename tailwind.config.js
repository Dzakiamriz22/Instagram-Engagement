module.exports = {
  content: [
    './app/templates/**/*.{html,js}',
    './app/static/**/*.{html,js}',  
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#34105b',
        'primary-variant': '#e1c7fd',
        'primary-variant2': '#46157a',
        'secondary' : '#fdd100',
        'secondary-variant' : '#ffe994',
        'text': '#212529',
        'textun': '#6c7592',
        'surface': '#f8f9fa',
        'background': '#ffffff',
      },
    },
  },
  plugins: [],
};
