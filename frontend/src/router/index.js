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

export default createRouter({
  history: createWebHistory(),
  routes,
})
