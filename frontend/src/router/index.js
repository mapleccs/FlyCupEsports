import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Teams from '@/views/Teams.vue'
import Signup from "@/views/Signup.vue";
import Recruitment from "@/views/Recruitment.vue";
import Profile  from "@/views/Profile.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import { useUserStore } from "@/stores/userStore";


const routes = [
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    children: [
        { path: '/', name: 'Home', component: Home },
        { path: '/login', name: 'Login', component: Login },
        { path: '/register', name: 'Register', component: Register },
        { path: '/teams', name: 'Teams', component: Teams },
        { path: '/signup', name: 'Signup', component: Signup },
        { path: '/recruitment', name: 'Recruitment', component: Recruitment },
        { path: '/profile', name: 'Profile', component: Profile },
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

// 路由守卫
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()

    // 如果用户未初始化但存在token，先初始化
  if (localStorage.getItem('authToken') && !userStore.isAuthenticated) {
    try {
      await userStore.init()
    } catch (error) {
      console.error('路由守卫初始化用户失败:', error)
    }
  }

  // 根据角色设置页面访问权限
  const rolePermissions = {
    user: ['/', '/home', '/events', '/teams', '/recruitment', '/login', '/register'],
    player: ['/', '/home', '/events', '/teams', '/recruitment', '/profile', '/signup'],
    captain: ['/', '/home', '/events', '/teams', '/recruitment', '/profile', '/signup', '/team-manage'],
    admin: ['*'] // 管理员可以访问所有页面
  }

  // 检查是否需要认证
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!userStore.isAuthenticated) {
      next({ name: 'Login', query: { redirect: to.fullPath } })
    } else {
      // 检查用户角色是否有权限访问
      const allowedRoutes = rolePermissions[userStore.user?.role] || []
      if (
        userStore.isAdmin() ||
        allowedRoutes.includes('*') ||
        allowedRoutes.includes(to.path) ||
        allowedRoutes.some(route => to.path.startsWith(route))
      ) {
        next()
      } else {
        next({ name: 'NotAuthorized' }) // 创建无权限页面
      }
    }
  }
  // ...其他验证逻辑...
})

export default createRouter({
  history: createWebHistory(),
  routes,
  router
})
