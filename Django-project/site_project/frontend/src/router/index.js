import { createRouter, createMemoryHistory } from 'vue-router';
import Article from '../components/MyArticle.vue';
import LoginForm from '../components/LoginForm.vue';

const routes = [
    { path: '/', component: Article},
    { path: '/login', component: LoginForm},
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
});

export default router;