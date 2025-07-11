import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  // … 其他路由
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
