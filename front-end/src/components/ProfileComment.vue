<template>
  <div class="d-flex gap-2 justify-content-end pb-2 pe-3">
    <button class="btn" @click="editComment"><i class="fas fa-pen"></i></button>
    <button class="btn" @click="deleteComment"><i class="fas fa-trash"></i></button>
  </div>
  <div v-if="!isEditing">
    <CommentCard :comment="comment" :rating="rating" :username="username"></CommentCard>
  </div>
  <div v-else>
    <EditableComment :id="id" :comment="comment" :rating="rating" :username="username"></EditableComment>
  </div>
</template>

<script>
import CommentCard from "@/components/CommentCard";
import EditableComment from "@/components/EditableComment";
import router from "@/router";
import {store} from "@/store/store";

export default {
  name: "ProfileComment",
  components: {
    EditableComment,
    CommentCard
  },
  data() {
    return {
      isEditing: false,
    }
  },
  props: {
    username: String,
    comment: String,
    rating: Number,
    id: Number,
  },
  methods: {
    editComment() {
      this.isEditing = !this.isEditing
    },
    async deleteComment() {
      const requestOptions = {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + sessionStorage.getItem("access")
        },
        body: JSON.stringify({
          "review_id": this.id,
        })
      };
      await fetch(store.api_url + "/profiles/reviews/", requestOptions);

      router.go(0)
    }
  }
}
</script>

<style scoped>
.card {
  background-color: white;
}

i {
  color: var(--primary-color);
}
</style>