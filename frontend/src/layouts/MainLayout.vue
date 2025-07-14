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
            <li v-for="nav in navItems" :key="nav.path" class="nav-item">
              <RouterLink
                :to="nav.path"
                class="nav-link"
                :class="{ active: $route.path === nav.path }"
              >
                <i :class="nav.icon" class="nav-icon"></i>
                {{ nav.title }}
              </RouterLink>
            </li>
          </ul>
        </nav>

        <div class="user-actions">
          <el-dropdown>
            <div class="user-avatar">
              <i class="el-icon-user-solid"></i>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="goToProfile">
                  <i class="el-icon-user"></i> 个人中心
                </el-dropdown-item>
                <el-dropdown-item @click="logout">
                  <i class="el-icon-switch-button"></i> 退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <el-button type="primary" size="small" @click="goToSignup">
            报名参赛
          </el-button>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Footer from '@/components/layout/Footer.vue'

const router = useRouter()

// 导航菜单项
const navItems = ref([
  { path: '/', title: '主页', icon: 'el-icon-house' },
  { path: '/live', title: '直播', icon: 'el-icon-video-camera' },
  { path: '/schedule', title: '赛程', icon: 'el-icon-date' },
  { path: '/teams', title: '战队', icon: 'el-icon-trophy' },
  { path: '/stats', title: '数据', icon: 'el-icon-data-analysis' },
  { path: '/recruitment', title: '招募', icon: 'el-icon-user-solid' },
  { path: '/signup', title: '报名', icon: 'el-icon-edit' },
  { path: '/partners', title: '合作', icon: 'el-icon-handshake' }
])

function goToSignup() {
  router.push('/signup')
}

function goToProfile() {
  router.push('/profile')
}

function logout() {
  // 退出登录逻辑
  router.push('/login')
}
</script>

<style scoped>
.main-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
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
}

.user-avatar:hover {
  background: rgba(93, 95, 239, 0.3);
}

.user-avatar i {
  font-size: 1.2rem;
  color: var(--primary);
}

.app-main {
  flex: 1;
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

@media (max-width: 768px) {
  .logo-text {
    font-size: 1.5rem;
  }

  .main-nav {
    display: none; /* 移动端隐藏导航，可以添加汉堡菜单 */
  }

  .container {
    justify-content: space-between;
  }
}
</style>