<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <div class="container-fluid px-5">
      <h2>ВиноВодич</h2>
      <div>
        <ul class="navbar-nav list-group-horizontal gap-5">
          <li class="nav-item"><router-link to="/">Почетна</router-link></li>
          <li class="nav-item" v-if="userLoggedIn"><router-link to="/profile">Профил</router-link></li>
          <li class="nav-item" v-if="userLoggedIn"><a @click="logout">Одјава</a></li>
          <li class="nav-item" v-else><router-link to="/login">Најава</router-link></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import {mutations, store} from "@/store/store";
import router from "@/router";

export default {
  name: "AppHeader",
  computed: {
    userLoggedIn() {
      if(store.loggedIn) {
        return store.loggedIn
      }
      else {
        return sessionStorage.getItem("loggedIn") === "true"
      }
    },
  },
  methods: {
    logout() {
      sessionStorage.removeItem("access");
      sessionStorage.removeItem("refresh");
      sessionStorage.setItem("loggedIn", "false");

      mutations.setLoggedIn(false);
      if(this.$route.path === "/profile") {
        router.push("/")
      } else {
        window.location.reload()
      }
    }
  }
}
</script>

<style scoped>
  nav {
    background-color: var(--primary-color);
    color: white;
  }

  .navbar-nav {
    margin-left: auto;
  }

  a {
    text-decoration: none;
    color: white;
    cursor: pointer;
  }

  .router-link-exact-active {
    color: white;
    text-decoration: underline;
  }
</style>