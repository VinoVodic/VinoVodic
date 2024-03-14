<template>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />
  </head>
  <AppHeader></AppHeader>
  <router-view/>
  <AppFooter></AppFooter>
</template>

<script>
import AppHeader from "@/components/Header";
import AppFooter from "@/components/Footer";
export default {
  components: {
    AppFooter,
    AppHeader
  },
}
</script>

<style>
  :root {
    --primary-color: #820000;
    --secondary-color: #f6f1f1;
    --accent-color: #efb810;
  }
</style>
