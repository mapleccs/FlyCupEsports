<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h2 class="auth-title">欢迎回来</h2>
        <p class="auth-subtitle">请登录您的账号</p>
      </div>

      <el-form :model="form" :rules="rules" ref="loginForm">
        <el-form-item prop="username">
          <el-input
            v-model="form.username"
            placeholder="用户名"
            prefix-icon="el-icon-user"
            size="large"
          />
        </el-form-item>

        <el-form-item prop="password">
          <el-input
            v-model="form.password"
            type="password"
            placeholder="密码"
            show-password
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <div class="auth-options">
          <el-checkbox v-model="rememberMe">记住我</el-checkbox>
          <router-link to="/reset-password" class="forgot-link">忘记密码?</router-link>
        </div>

        <el-button
          type="primary"
          size="large"
          class="auth-button"
          :loading="loading"
          @click="handleLogin"
        >
          登录
        </el-button>
      </el-form>

      <div class="auth-footer">
        <p>还没有账号? <router-link to="/register" class="link">立即注册</router-link></p>
      </div>
    </div>

    <div class="auth-banner">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'
import { ElMessage } from 'element-plus'

const router = useRouter()
const userStore = useUserStore()

const form = ref({
  username: '',
  password: ''
})

const rememberMe = ref(false)
const loading = ref(false)

const rules = {
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

// 添加角色重定向逻辑
const handleLogin = async () => {
  try {
    loading.value = true
    await userStore.login(form.value)

    // 根据角色重定向
    if (userStore.isAdmin) {
      await router.push('/')
    } else if (userStore.isCaptain) {
      await router.push('/')
    } else {
      await router.push('/profile')
    }

    ElMessage.success('登录成功！')
  } catch (error) {
    ElMessage.error(error.message || '登录失败，请检查用户名或密码')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-container {
  display: flex;
  min-height: 100vh;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.auth-card {
  flex: 1;
  max-width: 500px;
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(10px);
}

.auth-header {
  margin-bottom: 40px;
  text-align: center;
}

.auth-title {
  font-size: 2.2rem;
  color: white;
  margin-bottom: 10px;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.auth-subtitle {
  color: #94a3b8;
  font-size: 1.1rem;
}

.auth-options {
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
}

.forgot-link {
  color: #5d5fef;
  text-decoration: none;
  transition: color 0.3s;
}

.forgot-link:hover {
  color: #ff4655;
  text-decoration: underline;
}

.auth-button {
  width: 100%;
  padding: 15px;
  font-size: 1.1rem;
  background: linear-gradient(135deg, #5d5fef, #8b5cf6);
  border: none;
  transition: all 0.3s;
}

.auth-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(93, 95, 239, 0.4);
}

.auth-footer {
  margin-top: 30px;
  text-align: center;
  color: #94a3b8;
}

.auth-footer .link {
  color: #5d5fef;
  text-decoration: none;
  font-weight: 600;
}

.auth-footer .link:hover {
  text-decoration: underline;
}

.auth-banner {
  flex: 1.5;
  position: relative;
  background: url('@/assets/images/home-bg.png') no-repeat center center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth-banner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.banner-overlay {
  position: absolute;
  text-align: center;
  color: white;
  padding: 30px;
  max-width: 600px;
}

.banner-overlay h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
}

.banner-overlay p {
  font-size: 1.3rem;
  color: #e2e8f0;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .auth-banner {
    display: none;
  }

  .auth-card {
    max-width: 100%;
    padding: 40px 30px;
  }
}
</style>