import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import axios from 'axios'
loadFonts()


let url="http://127.0.0.1:8000/user/"

axios.get(url)
.then(function(response){
  console.log(response);
})
.catch(function(response){
  console.log(response);
})
createApp(App)
  .use(vuetify)
  .mount('#app')
