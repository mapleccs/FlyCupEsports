import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    children: [
        { path: '/', name: 'Home', component: Home },
        // 其他页面路由
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      // 处理带 hash 的导航
      return {
        el: to.hash,
        behavior: 'smooth',
        // 偏移量（导航栏高度）
        top: 70
      }
    } else if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default createRouter({
  history: createWebHistory(),
  routes,
  router
})
