<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h2 class="auth-title">创建账号</h2>
        <p class="auth-subtitle">加入英雄联盟赛事社区</p>
      </div>

      <el-form :model="form" :rules="rules" ref="registerForm">
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

        <el-form-item prop="confirmPassword">
          <el-input
            v-model="form.confirmPassword"
            type="password"
            placeholder="确认密码"
            show-password
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <el-checkbox v-model="agreement">
          我已阅读并同意 <router-link to="/terms" class="link">服务条款</router-link> 和
          <router-link to="/privacy" class="link">隐私政策</router-link>
        </el-checkbox>

        <el-button
          type="primary"
          size="large"
          class="auth-button mt-6"
          :loading="loading"
          @click="handleRegister"
        >
          注册账号
        </el-button>
      </el-form>

      <div class="auth-footer">
        <p>已有账号? <router-link to="/login" class="link">立即登录</router-link></p>
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
  password: '',
  confirmPassword: '',
  role: 'user'
})

const agreement = ref(false)
const loading = ref(false)

const validatePassword = (rule, value, callback) => {
  if (value !== form.value.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    { validator: validatePassword, trigger: 'blur' }
  ]
}

const registerMessage = ref('')

async function handleRegister() {
  // 检查用户是否同意协议
  if (!agreement.value) {
    ElMessage.warning('请阅读并同意服务条款和隐私政策')
    return
  }

  loading.value = true
  try {
    const { success, message } = await userStore.register(form.value)

    if (success) {
      // 注册成功，显示消息并跳转到登录页面
      ElMessage.success({
        message: message || '注册成功，请登录',
        duration: 2000
      })

      // 延迟跳转让用户看到成功消息
      setTimeout(() => {
        router.push('/login')
      }, 1500)
    } else {
      // 注册失败，显示错误信息
      ElMessage.error(message || '注册失败，请稍后再试')
    }
  } catch (error) {
    // 捕获异常，特别是用户名重复的情况
    if (error.message.includes('用户名') || error.message.includes('已存在')) {
      ElMessage.error('用户名已被使用，请选择其他用户名')
    } else {
      ElMessage.error(error.message || '注册过程中发生错误')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 复用登录页的样式，根据需要调整 */
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

.link {
  color: #5d5fef;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
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