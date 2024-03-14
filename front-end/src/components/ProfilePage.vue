<template>
  <div class="container rounded bg-white mt-4">
    <div class="row">
      <div class="col-md-3 border-md-end">
        <div class="d-flex flex-column align-items-center text-center py-5">
          <img class="rounded-circle mt-5" :src="userIcon">
          <span class="font-weight-bold">{{ userInfo.username }}</span>
          <span class="text-black-50">{{ userInfo.email }}</span>
        </div>
      </div>
      <div class="col-md-5 border-right">
        <ProfileForm :userInfo="userInfo"></ProfileForm>
      </div>
      <div class="col-md-4">
        <div class="comments p-3 py-5">
          <div class="d-flex justify-content-between align-items-center experience pb-3">
            <h5>Мои коментари</h5>
          </div>
          <div class="scrollbar">
            <div v-for="review in userInfo.reviews" :key="review.id">
              <ProfileComment
                  :username="userInfo.username"
                  :comment="review.comment"
                  :rating="review.rating"
                  :id="review.id">
              </ProfileComment>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import userimg from '../assets/userimg.png';
import ProfileComment from "@/components/ProfileComment";
import ProfileForm from "@/components/ProfileForm";
import {store} from "@/store/store";
export default {
  name: "ProfilePage",
  components: {
    ProfileForm,
    ProfileComment
  },
  data() {
    return {
      userIcon: userimg,
      userInfo: Object,
      userReviews: Array,
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
      this.userReviews = this.userInfo.reviews

    },
  }
}
</script>

<style scoped>
  .container {
    margin-right: 2rem;
    margin-left: 2rem;
  }

  .row {
    margin-top: 2rem;
  }

  .col-md-3, .col-md-5 {
    background-color: var(--secondary-color);
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-bottom: 2.2rem;
  }

  .col-md-3 {
    border-bottom-right-radius: 0;
    border-top-right-radius: 0;
  }

  .col-md-5 {
    border-bottom-left-radius: 0;
    border-top-left-radius: 0;
  }

  img {
    width: 10rem;
  }

  .comments {
    background-color: var(--secondary-color);
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-left: 3rem;
    width: 31rem;
    height: 33rem;
  }

  .scrollbar {
    height: 98%;
    overflow-y: scroll;
    overflow-x: hidden;
    padding-right: .5rem;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: var(--secondary-color);
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }
</style>