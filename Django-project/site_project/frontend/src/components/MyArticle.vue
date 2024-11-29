<template>
    <div v-if="profile.isLoggedIn">
        <h1>Данные</h1>
        <div class="card-container">
            <div class="card" v-for="a in profile.articles" :key="a.id" @click="selectArticle(a)">
                <h2 class="card-title">{{ a.name }}</h2>
            </div>
        </div>
        <ArticleDetail v-if="selectedArticle" :article="selectedArticle" />
    </div>
</template>

<script>
import { ref } from 'vue';
import { userProfile } from '../stores/user';
import ArticleDetail from './DetailArticle.vue'

export default {
    components: {
        ArticleDetail,
    },

    setup() {
        const profile = userProfile();
        profile.fetchArticles();
        const selectedArticle = ref(null);

        const selectArticle = (article) => {
            selectedArticle.value = article;
        }

        return {
            profile,
            selectArticle,
            selectedArticle,
        }
    }
}
</script>


<style scoped>
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 16px; /* Отступы между карточками */
}

.card {
    background-color: #f9f9f9; /* Цвет фона карточки */
    border: 1px solid #ddd; /* Граница карточки */
    border-radius: 8px; /* Закругление углов */
    padding: 16px; /* Внутренние отступы */
    width: 200px; /* Ширина карточки */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Тень для карточки */
    transition: transform 0.2s; /* Плавный эффект при наведении */
}

.card:hover {
    transform: scale(1.05); /* Увеличение карточки при наведении */
}

.card-title {
    font-size: 1.2em; /* Размер шрифта заголовка */
    margin: 0 0 8px; /* Отступы */
}

.card-description {
    font-size: 0.9em; /* Размер шрифта описания */
    color: #666; /* Цвет текста описания */
}
</style>
