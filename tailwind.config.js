/** @type {import('tailwindcss').Config} */
module.exports = {
  // darkMode: 'class',
  content: ['./app/templates/*.html', './app/templates/macros/*.html'],
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
        "neutral": "#031037",
        "base-100": "#ffffff",
        "info": "#0081FF",
        "success": "#3ECF6E",
        "warning": "#FFBE32",
        "error": "#FF4944",
          },
        },
      "emerald", 
      "business", 
      "black",
    ], // true: all themes | false: only light + dark | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "business", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    rtl: false, // rotate style direction from left-to-right to right-to-left. You also need to add dir="rtl" to your html tag and install `tailwindcss-flip` plugin for Tailwind CSS.
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
  },
}

