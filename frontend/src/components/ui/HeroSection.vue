<template>
  <div class="hero">
    <h1>欢迎来到 Fly Cup 平台</h1>
    <p>在这里，组织和参与地方英雄联盟赛事变得前所未有的简单。</p>
    <RouterLink to="/signup" class="btn">立即注册</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.hero {
  text-align: center;
  padding: 80px 0;
  //background: url('@/assets/images/hero-bg.jpg') center/cover no-repeat;
  color: #fff;
}
.btn {
  display: inline-block;
  margin-top: 20px;
  background: #409eff;
  color: #fff;
  padding: 12px 24px;
  border-radius: 4px;
  text-decoration: none;
}
</style>
