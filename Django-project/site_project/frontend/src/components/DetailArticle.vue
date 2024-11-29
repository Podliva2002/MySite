<template>
    <div class="article-container">
        <h1 class="article-title">{{ article.name }}</h1>
        <p class="article-description">Описание: {{ article.description }}</p>
        <div class="categories-container">
            <h2>Категории</h2>
            <ul class="categories-list">
                <li v-for="category in article.category" :key="category.id" class="category-item">
                    {{ category.name }}
                </li>
            </ul>
            <h2>Автор статьи: {{ article.author.username }}</h2>
        </div>
    </div>
</template>

<style scoped>
.article-container {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}

.article-title {
    font-size: 24px;
    color: #333;
    margin-bottom: 10px;
}

.article-description {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
}

.categories-container {
    margin-top: 20px;
}

.categories-list {
    list-style-type: none;
    padding: 0;
}

.category-item {
    background-color: #e7f3fe;
    border: 1px solid #b3d7ff;
    border-radius: 4px;
    padding: 8px;
    margin: 5px 0;
    transition: background-color 0.3s;
}

.category-item:hover {
    background-color: #d0e7ff;
}
</style>

<script>
export default {
    props: {
        article: Object,
    },
}
</script>
