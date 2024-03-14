<template>
  <section>
    <div class="container pt-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-90">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card shadow-2-strong" style="border-radius: 1rem;">
            <div class="card-body pad text-center">

              <h3 class="mb-5">Најавете се</h3>

              <form @submit.prevent="login">
                <div class="form-outline mb-4">
                  <input type="text" class="form-control form-control-lg" v-model="username" placeholder="Username"/>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" class="form-control form-control-lg" v-model="password" placeholder="Password"/>
                </div>

                <button class="btn btn-lg btn-block" type="submit">Најава</button>
              </form>

              <div v-if="showErrorMessage" class="error-message">
                {{ this.errorMessage }}
              </div>

              <hr class="my-4">
              <div>
                <p class="mb-0">Немате профил? <router-link to="/register">Регистрирајте се!</router-link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import router from "@/router";
import {mutations, store} from "@/store/store";

export default {
  name: "LoginComponent",
  data() {
    return {
      refresh: null,
      access: null,
      showErrorMessage: false,
      errorMessage: "",
    }
  },
  methods: {
    async login() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ "username":this.username, "password":this.password})
      };
      const response = await fetch(store.api_url + "/auth/login/", requestOptions);

      if (response.status === 200) {
        const data = await response.json();
        this.handleSuccessfulLogin(data);
        await router.push("/");
      } else {
        this.handleFailedLogin();
      }
    },
    handleSuccessfulLogin(data) {
      sessionStorage.setItem("access", data.access);
      sessionStorage.setItem("refresh", data.refresh);
      sessionStorage.setItem("loggedIn", "true")

      mutations.setLoggedIn(true)
    },
    handleFailedLogin() {
      this.showErrorMessage = true
      this.errorMessage = this.username === undefined || this.password === undefined
          ? "Please fill out all fields"
          : "Invalid user credentials";

      setTimeout(() => {
        this.showErrorMessage = false;
      }, 3000);
    }
  }
}
</script>

<style scoped>
  section{
    background-color: var(--secondary-color);
    min-height: 91vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .container {
    padding-bottom: 6rem;
  }

  .card {
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  h3 {
    color: var(--primary-color);
  }

  .btn {
    background-color: var(--primary-color);
    color: white;
  }

  .btn:hover {
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
  }

  .form-control:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 0.2rem rgba(130, 0, 0, 0.5);
  }

  .pad {
    padding: 4.7rem;
  }

  a {
    color: var(--primary-color);
    text-decoration: underline;
    font-weight: 700;
  }

  .error-message {
    position: fixed;
    top: 130px;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--primary-color);
    color: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
</style>