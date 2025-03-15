import { createApp } from 'vue'
import './style.css'
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css';
import { createPinia } from 'pinia';

const app = createApp(App);
const pinia = createPinia();
// use pinia store
app.use(pinia);
app.use(router);
app.mount('#app');

