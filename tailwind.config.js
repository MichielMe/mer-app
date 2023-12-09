/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'media', // or 'media' or 'class'
  content: ['./app/templates/*.html', './app/templates/macros/*.html', "./templates/**/*.html", "./static/src/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Poppins', 'ui-sans-serif', 'system-ui'],
        'roobert': ['RoobertVRT-Regular', 'sans'],
        'roobertsemibold': ['RoobertVRT-SemiBold', 'sans'],
        'roobertbold': ['RoobertVRT-Bold', 'sans'],
        'roobertlight': ['RoobertVRT-Light', 'sans'],
        // ... other fontFamily settings
      },
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        vrttheme: {
        "primary": "#00BEAA",
        "secondary": "#5541F0",
        "accent": "#FF3C78",
        "neutral": "#3F4865",
        "base-100": "#F2EFF0",
        "info": "#0081FF",
        "success": "#3ECF6E",
        "warning": "#FFBE32",
        "error": "#FF4944",
        ...require("daisyui/src/theming/themes")["vrttheme"],
        },
      },
      {
        vrtdarkmode: {
        "primary": "#00BEAA",
        "secondary": "#5541F0",
        "accent": "#FF3C78",
        "neutral": "#c0c3cd",
        "base-100": "#020b26", // of#020b26
        "info": "#0081FF",
        "success": "#3ECF6E",
        "warning": "#FFBE32",
        "error": "#FF4944",
        ...require("daisyui/src/theming/themes")["vrtdarkmode"],
        }
      }, 
    ], // true: all themes | false: only light + dark | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "vrtdarkmode", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: ":root", // The element that receives theme color CSS variables
  },
}

