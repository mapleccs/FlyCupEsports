import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Teams from '@/views/Teams.vue'
import Signup from "@/views/Signup.vue";
import Recruitment from "@/views/Recruitment.vue";
import Profile  from "@/views/Profile.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Live from "@/views/Live.vue";
import Schedule from "@/views/Schedule.vue";
import MatchControl from "@/views/MatchControl.vue";
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
        // 您已经正确地添加了 meta 标记
        { path: '/signup', name: 'Signup', component: Signup, meta: {requiresAuth: true} },
        { path: '/recruitment', name: 'Recruitment', component: Recruitment },
        // 假设个人资料页也需要登录
        { path: '/profile', name: 'Profile', component: Profile, meta: {requiresAuth: true} },
        { path: '/live', name: 'Live', component: Live },
        { path: '/schedule', name: 'Schedule', component: Schedule },
        // 假设比赛控制页也需要登录
        { path: '/match', name: 'MatchControl', component: MatchControl, meta: {requiresAuth: true} }
    ]
  },
]

// 创建路由实例，并将其赋值给 router 常量
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 70
      }
    } else if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫 (已优化)
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()

  // 尝试在每次路由切换时初始化用户信息（如果需要）
  // 这确保了用户刷新页面后，登录状态能被恢复
  if (localStorage.getItem('authToken') && !userStore.isAuthenticated) {
    try {
      await userStore.init()
    } catch (error) {
      console.error('路由守卫初始化用户失败:', error)
    }
  }

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !userStore.isAuthenticated) {
    // 情况1：页面需要认证，但用户未登录 -> 重定向到登录页
    next({ name: 'Login', query: { redirect: to.fullPath } });
  } else if (requiresAuth && userStore.isAuthenticated) {
    // 情况2：页面需要认证，且用户已登录 -> 检查角色权限
    const userRole = userStore.user?.role || 'user';
    const rolePermissions = {
      user: ['/', '/home', '/events', '/teams', '/recruitment', '/login', '/register'],
      player: ['/', '/home', '/events', '/teams', '/recruitment', '/profile', '/signup'],
      captain: ['/', '/home', '/events', '/teams', '/recruitment', '/profile', '/signup', '/team-manage'],
      admin: ['*']
    };

    const allowedRoutes = rolePermissions[userRole] || [];
    const canAccess = allowedRoutes.includes('*') || allowedRoutes.some(route => to.path.startsWith(route));

    if (userStore.isAdmin || canAccess) {
      next(); // 有权限，放行
    } else {
      // 角色无权限，可以跳转到无权限页面（如果创建了的话）
      // next({ name: 'NotAuthorized' });
      // 或者暂时先跳回首页
      next({ name: 'Home' });
    }
  } else {
    // 情况3：页面不需要认证 -> 直接放行
    next();
  }
})

// --- 已修正 ---
// 正确导出您配置好的 router 实例
export default router;