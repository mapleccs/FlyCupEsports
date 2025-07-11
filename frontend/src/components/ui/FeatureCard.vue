<template>
  <div class="card">
<!--    <div class="icon">-->
<!--      <img :src="require(`@/assets/icons/${icon}.svg`)" alt="" />-->
<!--    </div>-->
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  description: String,
  icon: String,
})
</script>

<style scoped>
.card {
  text-align: center;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fff;
}
.icon img {
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
}
</style>
