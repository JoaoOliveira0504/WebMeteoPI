import { createApp } from 'vue'
import App from './App.vue'
import RadarImage from './components/RadarImage.vue'

import 'bootstrap/dist/css/bootstrap.min.css'

createApp(App)
  .component('radar-image', RadarImage)
  .mount('#app')
