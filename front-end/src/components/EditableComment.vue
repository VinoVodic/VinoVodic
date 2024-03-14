<template>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center top">
          <p class="left-side small mb-0">{{ username }}</p>
          <div class="right-side d-flex align-items-center">
            <i class="fas fa-star mx-2 fa-xs"></i>
            <input class="form-control" type="number" min="1" max="5" step="1" v-model="userRating"/>
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <textarea v-model="userComment" class="form-control"></textarea>
        <button @click="saveEdit" class="btn save-btn">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
import {store} from "@/store/store";
import router from "@/router";

export default {
  name: "EditableComment",
  data() {
    return {
      isEditing: false,
      userComment: this.comment,
      userRating: this.rating,
      componentKey: 0,
    }
  },
  props: {
    username: String,
    comment: String,
    rating: Number,
    id: Number,
  },
  methods: {
    async saveEdit() {
      const requestOptions = {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + sessionStorage.getItem("access")
        },
        body: JSON.stringify({
          "rating": this.userRating,
          "review_id": this.id,
          "comment": this.userComment
        })
      };
      await fetch(store.api_url + "/profiles/reviews/", requestOptions);

      router.go(0)
    },
  }
}
</script>

<style scoped>
  input {
    margin-left: -0.4rem;
    width: 5rem;
  }

  textarea {
    width: 80%;
  }

  .save-btn {
    background-color: var(--primary-color);
    color: white;
  }

  .save-btn:hover {
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
  }

  .card {
    background-color: white;
    width: 100%
  }

  .top {
    width: 100%;
  }

  .left-side {
    margin-right: auto;
  }

  .right-side {
    margin-left: auto;
  }

  .fa-star {
    color: var(--accent-color);
  }
</style>