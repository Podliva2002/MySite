<template>
    <div id="app">

      <div>
        <h1 v-if="profile.isLoggedIn">Навигация</h1>
          <nav class="navbar">
            <router-link v-if="profile.isLoggedIn" to='/'>Мои статьи</router-link>
            <router-link to='/login'>{{ profile.isLoggedIn ? 'Выйти' : 'Войти' }}</router-link>
          </nav>
          <router-view />
      </div>
    </div>
  </template>
  
<script>
import LoginForm from './LoginForm.vue';
import { userProfile } from '../stores/user';

export default {
  name: 'App',
  
  setup () {
    const profile = userProfile();

    return {
      profile
    };
  }
};
</script>

<style scoped>
  .navbar {
      display: flex;
      justify-content: center;
      list-style: none;
      margin: 0;
      padding: 0;
  }
  a {
    display: flex;
    text-decoration: none;
    margin-right: 10px;
    justify-content: center
    
}

h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
    font-weight: bold;
    font-size: 40px;
}

.active {
    font-weight: bold;
    font-weight: 2000;
    text-decoration: underline;
}

</style>
  