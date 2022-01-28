module.exports = {
  content: ["../templates/**/*.html", "../templates/*.html"],
  theme: {
    extend: {
      colors: {
        "red": {
          "blood": "#660708",
          "ruby": "#a4161a",
          "carnelian": "#ba181b",
          "imperial": "#e5383b"
        },
        "black": {
          "rich": "#0b090a",
          "eerie": "#161a1d",
        },
        "silverchalice": "#b1a7a6",
        "lightgray": "#d3d3d3",
        "cultured": "#f5f3f4",
        "royal-blue-dark": "#001177",
        "link-blue": "#0000FF",
        "link-purple": "#800080",
      },
      height: { 
        '10vh': '10vh',
        '50vh': '50vh',
        '60vh': '60vh',
        '70vh': '70vh',
        '80vh': '80vh',
       }
    },
  },
  plugins: [],
}

