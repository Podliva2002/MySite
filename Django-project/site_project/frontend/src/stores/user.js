import { defineStore } from "pinia";
import axios from "axios";

export const userProfile = defineStore("profile", {
    state: () => ({
        articles: [],
        token: localStorage.getItem("token"),
        isLoggedIn: !!localStorage.getItem('token'),
        message: '',
        userId: localStorage.getItem("userId") || '',
    }),
    actions: {
        async fetchArticles() {
            if (!this.token || !this.userId) {
                console.warn("Token или userId отсутствуют");
                return; // Проверяем наличие token и userId
            }

            const headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + this.token,
            };

            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/site/creatorarticles/${this.userId}/`, { headers });
                this.articles = response.data;
                console.log("Полученные статьи:", this.articles);
            } catch (error) {
                console.error("Ошибка при получении статей:", error.response ? error.response.data : error.message);
                this.message = 'Ошибка при получении статей: ' + (error.response.data.detail || error.message);
            }
        },
        async login(username, password) {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api-token-auth/', {
                    username,
                    password
                });
                this.token = response.data.token;
                localStorage.setItem("token", this.token);
                this.isLoggedIn = true;

                // Получаем информацию о текущем пользователе
                await this.fetchCurrentUser();

                this.message = 'Вы вошли!';
            } catch (error) {
                console.error("Ошибка входа:", error.response ? error.response.data : error.message);
                this.message = 'Ошибка входа: ' + (error.response.data.non_field_errors ? error.response.data.non_field_errors[0] : error.message);
            }
        },
        async fetchCurrentUser() {
            const headers = {
                'Authorization': `Token ${this.token}`, // Используем токен для авторизации
            };

            try {
                const response = await axios.get('http://127.0.0.1:8000/api/current-user/', { headers });
                this.userId = response.data.id;
                localStorage.setItem("userId", this.userId);
                await this.fetchArticles();
            } catch (error) {
                console.error("Ошибка при получении текущего пользователя:", error.response ? error.response.data : error.message);
                this.message = 'Ошибка при получении текущего пользователя: ' + (error.response.data.detail || error.message);
            }
        },
        logout() {
            this.clearToken();
            this.message = 'Вы вышли.';
        },
        clearToken() {
            this.token = null;
            this.userId = '';
            localStorage.removeItem("token");
            localStorage.removeItem("userId");
            this.articles = [];
            this.isLoggedIn = false;
        },  
    }
});
