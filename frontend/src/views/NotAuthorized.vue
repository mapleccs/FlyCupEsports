<template>
  <div class="not-authorized">
    <div class="container">
      <el-result
        icon="warning"
        title="403 无访问权限"
        sub-title="您没有权限访问此页面"
      >
        <template #extra>
          <el-button type="primary" @click="goHome">返回首页</el-button>
          <el-button v-if="!userStore.isAuthenticated" @click="goToLogin">登录</el-button>
        </template>
      </el-result>

      <div class="role-info">
        <h3>您的当前角色: {{ currentRoleName }}</h3>
        <p>允许访问的内容:</p>
        <ul>
          <li v-for="item in allowedNavItems" :key="item.path">
            <router-link :to="item.path">{{ item.title }}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'

const router = useRouter()
const userStore = useUserStore()

const roleNames = {
  user: '普通用户',
  player: '选手',
  captain: '战队队长',
  admin: '管理员'
}

const currentRoleName = computed(() => {
  return roleNames[userStore.user?.role] || '未登录用户'
})

const goHome = () => {
  router.push('/')
}

const goToLogin = () => {
  router.push('/login')
}

// 获取允许访问的导航项
const allowedNavItems = computed(() => {
  return filteredNavItems.value.filter(item =>
    item.roles.includes(userStore.user?.role || 'user'))
})
</script>

<style scoped>
.not-authorized {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
  background: var(--darker);
}

.container {
  text-align: center;
  max-width: 600px;
}

.role-info {
  margin-top: 30px;
  padding: 20px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 8px;
  border: 1px solid rgba(255, 70, 85, 0.3);
}

.role-info h3 {
  color: var(--primary);
}

.role-info ul {
  list-style: none;
  padding: 0;
  margin-top: 10px;
}

.role-info li {
  margin: 8px 0;
}

.role-info a {
  color: var(--secondary);
  text-decoration: none;
}

.role-info a:hover {
  text-decoration: underline;
}
</style>