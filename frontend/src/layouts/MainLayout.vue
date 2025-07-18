<template>
  <div class="main-layout">
    <!-- 顶部导航栏 -->
    <header class="app-header">
      <div class="container">
        <div class="logo">
          <RouterLink to="/">
            <span class="logo-text">Fly Cup</span>
            <span class="logo-sub">电竞平台</span>
          </RouterLink>
        </div>

        <nav class="main-nav">
          <ul class="nav-list">
            <li v-for="nav in filteredNavItems" :key="nav.path" class="nav-item">
              <RouterLink
                :to="nav.path"
                class="nav-link"
                :class="{ active: $route.path === nav.path }"
              >
                <i :class="nav.icon" class="nav-icon"></i>
                {{ nav.title }}
                <span v-if="nav.roleRequired" class="role-badge">{{ nav.roleRequired }}</span>
              </RouterLink>
            </li>
          </ul>
        </nav>

        <div class="user-actions">
          <!-- 已登录状态 -->
          <template v-if="userStore.isAuthenticated">
            <div class="user-info">
              <div class="role-indicator" :class="userRoleClass">
                {{ userRoleName }}
              </div>
              <el-dropdown>
                <div class="user-avatar">
                  <template v-if="userStore.user?.avatar">
                    <img :src="userStore.user.avatar" class="avatar-img" alt="用户头像" />
                  </template>
                  <i v-else class="el-icon-user-solid"></i>
                </div>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item @click="goToProfile">
                      <i class="el-icon-user"></i> 个人中心
                    </el-dropdown-item>
                    <el-dropdown-item v-if="userStore.isAdmin" @click="goToAdmin">
                      <i class="el-icon-s-tools"></i> 管理后台
                    </el-dropdown-item>
                    <el-dropdown-item v-if="userStore.isCaptain" @click="goToTeam">
                      <i class="el-icon-s-flag"></i> 我的战队
                    </el-dropdown-item>
                    <el-dropdown-item divided @click="logout">
                      <i class="el-icon-switch-button"></i> 退出登录
                    </el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
            <el-button
              v-if="userStore.isUser"
              type="primary"
              size="small"
              @click="goToSignup"
            >
              报名参赛
            </el-button>
          </template>

          <!-- 未登录状态 -->
          <template v-else>
            <el-button plain size="small" @click="goToLogin">
              登录
            </el-button>
            <el-button type="primary" size="small" @click="goToRegister">
              注册
            </el-button>
          </template>
        </div>
      </div>
    </header>

    <!-- 主要内容 -->
    <main class="app-main">
      <router-view></router-view>
    </main>

    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Footer from '@/components/layout/Footer.vue'
import { useUserStore } from '@/stores/userStore'

const router = useRouter()
const userStore = useUserStore()
const isInitialized = ref(false) // 添加初始化状态标志

// 初始化用户状态
onMounted(async () => {
  if (localStorage.getItem('authToken')) {
    await userStore.init() // 调用init方法
  }
  isInitialized.value = true
})

// 导航菜单项
const navItems = ref([
  { path: '/', title: '主页', icon: 'el-icon-house', roles: ['user', 'player', 'captain', 'admin'] },
  { path: '/live', title: '直播', icon: 'el-icon-video-camera', roles: ['user', 'player', 'captain', 'admin'] },
  { path: '/schedule', title: '赛程', icon: 'el-icon-date', roles: ['player', 'captain', 'admin'] },
  { path: '/teams', title: '战队', icon: 'el-icon-trophy', roles: ['user', 'player', 'captain', 'admin'] },
  { path: '/stats', title: '数据', icon: 'el-icon-data-analysis', roles: ['captain', 'admin']},
  { path: '/recruitment', title: '招募', icon: 'el-icon-user-solid', roles: ['player', 'captain', 'admin'] },
  { path: '/signup', title: '报名', icon: 'el-icon-edit', roles: ['user'] },
  { path: '/match', title: '比赛', icon: 'el-icon-edit', roles: ['user', 'player', 'captain', 'admin'] },
  { path: '/partners', title: '合作', icon: 'el-icon-handshake', roles: ['admin'] },
  { path: '/admin', title: '管理', icon: 'el-icon-s-tools', roles: ['admin'] }
])

// 根据用户角色过滤导航项
const filteredNavItems = computed(() => {
  // 管理员可以看到所有菜单
  if (userStore.isAdmin) {
    return navItems.value
  }

  const role = userStore.user?.role || 'user'
  return navItems.value.filter(item =>
    item.roles.includes(role)
  )
})

// 获取用户角色名称
const userRoleName = computed(() => {
  const roles = {
    'user': '普通用户',
    'player': '选手',
    'captain': '队长',
    'admin': '管理员'
  }
  return roles[userStore.user?.role] || '游客'
})

// 用户角色样式类
const userRoleClass = computed(() => {
  return {
    'user': userStore.isUser,
    'player': userStore.isPlayer,
    'captain': userStore.isCaptain,
    'admin': userStore.isAdmin
  }
})

function goToSignup() {
  router.push('/signup')
}

function goToLogin() {
  router.push('/login')
}

function goToRegister() {
  router.push('/register')
}

function goToProfile() {
  router.push('/profile')
}

function goToAdmin() {
  router.push('/admin')
}

function goToTeam() {
  router.push('/teams/my-team')
}

function logout() {
  userStore.logout()
  router.push('/')
}
</script>

<style scoped>
.main-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: var(--darker);
}

.app-header {
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(93, 95, 239, 0.2);
  position: sticky;
  top: 0;
  z-index: 1000;
  height: 70px;
  display: flex;
  align-items: center;
}

.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

.logo a {
  display: flex;
  align-items: baseline;
  text-decoration: none;
}

.logo-text {
  font-size: 1.8rem;
  font-weight: 800;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.logo-sub {
  font-size: 0.9rem;
  margin-left: 8px;
  color: var(--gray);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.main-nav {
  flex: 1;
  margin: 0 40px;
}

.nav-list {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  justify-content: center;
}

.nav-item {
  margin: 0 5px;
  position: relative;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  text-decoration: none;
  color: var(--gray);
  font-weight: 500;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  background: rgba(93, 95, 239, 0.1);
  color: white;
}

.nav-link.active {
  background: rgba(93, 95, 239, 0.2);
  color: white;
  font-weight: 600;
}

.nav-icon {
  margin-right: 8px;
  font-size: 1.2rem;
}

.user-actions {
  display: flex;
  align-items: center;
  gap: 15px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(93, 95, 239, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
}

.user-avatar:hover {
  background: rgba(93, 95, 239, 0.3);
  transform: scale(1.05);
}

.user-avatar i {
  font-size: 1.2rem;
  color: var(--primary);
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.role-indicator {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.role-indicator.user {
  background: rgba(94, 114, 228, 0.2);
  color: #5d72e4;
}

.role-indicator.player {
  background: rgba(76, 175, 80, 0.2);
  color: #4CAF50;
}

.role-indicator.captain {
  background: rgba(255, 152, 0, 0.2);
  color: #FF9800;
}

.role-indicator.admin {
  background: rgba(156, 39, 176, 0.2);
  color: #9C27B0;
}

.app-main {
  flex: 1;
}

.role-badge {
  position: absolute;
  top: -6px;
  right: -6px;
  background: #ff4655;
  color: white;
  font-size: 0.6rem;
  padding: 2px 6px;
  border-radius: 10px;
  font-weight: bold;
  line-height: 1;
}

/* 响应式调整 */
@media (max-width: 1024px) {
  .main-nav {
    margin: 0 20px;
  }

  .nav-link {
    padding: 10px 15px;
    font-size: 0.9rem;
  }

  .nav-icon {
    margin-right: 5px;
    font-size: 1rem;
  }
}

@media (max-width: 900px) {
  .nav-link span:not(.role-badge) {
    display: none;
  }

  .nav-icon {
    margin-right: 0;
    font-size: 1.2rem;
  }

  .role-indicator {
    display: none;
  }
}

@media (max-width: 768px) {
  .logo-text {
    font-size: 1.5rem;
  }

  .main-nav {
    display: none;
  }

  .container {
    justify-content: space-between;
  }
}
</style>