import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import axios from 'axios'
import router from './router'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
loadFonts()


// let url="http://127.0.0.1:8000/user/"

// axios.get(url)
// .then(function(response){
//   console.log(response);
// })
// .catch(function(response){
//   console.log(response);
// })
createApp(App)
.use(BootstrapVue3)
  .use(router)
  .use(vuetify)
  .mount('#app')
