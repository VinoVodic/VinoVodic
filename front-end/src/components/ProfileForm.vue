<template>
  <div class="p-3 py-5">
    <form @submit="saveInformation">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h4 class="text-right">Подесување на профилот</h4>
      </div>
      <div class="row mt-2">
        <div class="col-md-6">
          <label class="labels">Име</label>
          <input type="text" class="form-control" placeholder="Име" v-model="userInfo.first_name">
        </div>
        <div class="col-md-6">
          <label class="labels">Презиме</label>
          <input type="text" class="form-control" value="" placeholder="Презиме" v-model="userInfo.last_name">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-12">
          <label class="labels">Email</label>
          <input type="text" class="form-control" placeholder="Еmail" value="" v-model="userInfo.email">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-12">
          <label class="labels">Корисничко име</label>
          <input type="text" class="form-control" placeholder="Корисничко име" value="" v-model="userInfo.username">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-12">
          <label class="labels">Нова лозинка</label>
          <input type="text" class="form-control" value="" placeholder="Нова лозинка" v-model="newPassword">
        </div>
      </div>
      <div class="mt-5 text-center"><button class="btn" type="submit">Зачувај</button></div>
    </form>
  </div>
</template>

<script>
import {store} from "@/store/store";
import router from "@/router";

export default {
  name: "ProfileForm",
  data() {
    return {
      userInfo: Object,
    }
  },
  mounted() {
    this.fetchUserInfo();
  },
  methods: {
    async fetchUserInfo() {
      const requestOptions = {
        method: "GET",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
      };
      const response = await fetch(store.api_url + "/profiles/profile/", requestOptions);
      this.userInfo = await response.json();
      this.userInfo = this.userInfo["user"];
    },
    async saveInformation() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
        body: JSON.stringify({
          "first_name": this.userInfo.first_name,
          "last_name": this.userInfo.last_name,
          "email": this.userInfo.email,
          "username": this.userInfo.username,
          "old_password": this.oldPassword,
          "new_password": this.newPassword,
        })
      };

      await fetch(store.api_url + "/profiles/profile/", requestOptions);
      router.go(0)
    }
  }
}
</script>

<style scoped>
.btn:hover {
  background-color: var(--secondary-color);
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.btn {
  background-color: var(--primary-color);
  color: white;
}
</style>