<template>
  <section>
    <div class="container pt-2">
      <div class="row d-flex justify-content-center align-items-center">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card shadow-2-strong" style="border-radius: 1rem;">
            <div class="card-body pad text-center">

              <h3 class="mb-4">Регистрирајте се</h3>
              <form @submit.prevent="register">
                <div class="d-flex justify-content-around gap-3">
                  <div class="form-outline mb-2">
                    <input type="text" class="form-control form-control-lg" v-model="firstname" placeholder="Име"/>
                  </div>

                  <div class="form-outline mb-2">
                    <input type="text" class="form-control form-control-lg" v-model="lastname" placeholder="Презиме"/>
                  </div>
                </div>

                <div class="form-outline mb-2">
                  <input type="text" class="form-control form-control-lg" v-model="email" placeholder="Email"/>
                </div>

                <div class="form-outline mb-2">
                  <input type="text" class="form-control form-control-lg" v-model="username" placeholder="Корисничко име"/>
                </div>

                <div class="form-outline mb-2">
                  <input type="password" class="form-control form-control-lg" v-model="password" placeholder="Лозинка"/>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" class="form-control form-control-lg" v-model="repeatPassword" placeholder="Лозинка"/>
                </div>

                <button class="btn btn-lg btn-block" type="submit">Регистрација</button>
              </form>

              <div v-if="showErrorMessage" class="error-message">
                {{ this.errorMessage }}
              </div>

              <hr class="my-4">
              <div>
                <p class="mb-0">Веќе имате профил? <router-link to="/login">Најавете се!</router-link>
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
import { store} from "@/store/store";

export default {
  name: "RegisterComponent",
  data() {
    return {
      showErrorMessage: false,
      errorMessage: "",
    }
  },
  methods: {
    async register() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ "username":this.username, "password":this.password, "password2": this.repeatPassword,
          "email": this.email, "first_name": this.firstname, "last_name": this.lastname})
      };
      const response = await fetch(store.api_url + "/auth/register/", requestOptions);
      if (response.status === 201) {
        const data = await response.json();
        this.handleSuccessfulRegister(data);
        await router.push("/login");

      } else {
        this.handleFailedRegister();
      }
    },
    handleSuccessfulRegister(data) {
      sessionStorage.setItem("access", data.access);
      sessionStorage.setItem("refresh", data.refresh);
    },
    handleFailedRegister() {
      this.showErrorMessage = true
      this.errorMessage = this.username === undefined || this.password === undefined || this.repeatPassword === undefined
      || this.email === undefined || this.firstname === undefined || this.lastname === undefined
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
    margin-bottom: 4rem;
  }

  .card {
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    height: 77vh;
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
    padding: 2rem!important;
  }

  a {
    color: var(--primary-color);
    text-decoration: underline;
    font-weight: 700;
  }

  .error-message {
    position: fixed;
    top: 70px;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--primary-color);
    color: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
</style>