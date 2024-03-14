<template>
  <footer class="fixed-bottom d-flex flex-wrap justify-content-between px-5 pt-3">
    <div>
      <p><i class="fas fa-envelope pe-2"></i>contact@vinovodic.mk</p>
    </div>
    <div>
      <i class="fab fa-github pe-2"></i>
      <a href="https://github.com/nikolapetrusev/DIANS-Domasno/tree/master" class="text-reset text-decoration-none">Github</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "AppFooter"
}
</script>

<style scoped>
  footer {
    background-color: var(--primary-color);
    color: white;
  }
</style>