<template>
  <div class="login">
    <h2 v-if="!profile.isLoggedIn">Вход в систему</h2>
    <form v-if="!profile.isLoggedIn" @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="username">Логин:</label>
        <input
          id="username"
          type="text"
          v-model="username"
          required
          class="form-input"
          placeholder="Введите ваш логин"
        />
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input
          id="password"
          type="password"
          v-model="password"
          required
          class="form-input"
          placeholder="Введите ваш пароль"
        />
      </div>
      <button type="submit" class="submit-button">Войти</button>
    </form>
    <p v-if="profile.message" class="error-message">{{ profile.message }}</p>
    <button class="submit-button" v-if="profile.isLoggedIn" @click="profile.logout()">Выйти</button>
  </div>
</template>

<script>
import { userProfile } from '../stores/user'; // Импортируем store
import { ref, computed } from 'vue';

export default {
  setup() {
    const profile = userProfile();
    const username = ref('');
    const password = ref('');


    // Метод для входа
    const login = async () => {
      await profile.login(username.value, password.value); // Вызываем метод login из store
    };

    return {
      username,
      password,
      login,
      profile,
    };
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.form-input {
  width: 80%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.form-input:focus {
  border-color: #007bff;
  outline: none;
}

.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
