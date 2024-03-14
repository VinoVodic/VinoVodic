<template>
  <div class="card mb-3">
    <div class="card-body">
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center top">
          <p class="left-side small mb-0">{{ username }}</p>
          <div class="right-side d-flex align-items-center">
            <i class="fas fa-star mx-2 fa-xs"></i>
            <p class="small mb-0" style="margin-left: -0.4rem;">{{ rating }}</p>
          </div>
        </div>
      </div>
      <p class="mb-0">{{ comment }}</p>
    </div>
  </div>
</template>

<script>
export default  {
  name: "CommentCard",
  props: {
    username: String,
    comment: String,
    rating: Number,
  },
}
</script>

<style scoped>
  .card {
    background-color: var(--secondary-color);
    width: 100%;
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