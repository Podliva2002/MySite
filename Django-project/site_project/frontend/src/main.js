import { createApp } from 'vue';
import { createPinia } from 'pinia';
import './style.css';
import App from './App.vue';
import router from './router';

const pinia = createPinia();
const app = createApp(App);

// Используем Pinia и Vue Router
app.use(pinia);
app.use(router);

// Монтируем приложение
app.mount('#app');
