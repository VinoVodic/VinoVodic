<template>
  <h2 class="pt-2">Коментари</h2>
  <div class="row d-flex">
    <div class="col-md-8 col-lg-6 cards scrollbar" v-if="reviews.length>0">
      <div class="outer-card card shadow-0 border" style="background-color: #f0f2f5; width: 32.9vw">
        <div class="card-body">
          <div v-for="review in reviews" :key="review.id">
            <CommentCard
                :username="review.user.username"
                :comment="review.comment"
                :rating="review.rating">
            </CommentCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CommentCard from "@/components/CommentCard";
export default {
  name: "CommentBox",
  components: { CommentCard },
  computed: {
    selectedWinery() {
      const storedWinery = sessionStorage.getItem("selectedWinery");
      return JSON.parse(storedWinery);
    },
    reviews() {
      const storedReviews = sessionStorage.getItem("selectedWineryReviews");
      return JSON.parse(storedReviews);
    }
  },
}
</script>

<style scoped>

  .card-body {
    background-color: var(--primary-color);
    border-radius: 8px;
  }

  .scrollbar {
    height: 71.2vh;
    width: 98%;
    overflow-y: scroll;
    overflow-x: hidden;
    padding: 0 10px;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: #e7e7e7;
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }

</style>