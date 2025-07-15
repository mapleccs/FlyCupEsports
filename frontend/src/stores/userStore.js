// stores/userStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { loginUser, registerUser, logoutUser, fetchUserProfile } from '@/services/authService'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('authToken') || null)
  const isAuthenticated = ref(!!token.value)
  const router = useRouter()

  // 初始化时尝试获取用户信息
  const init = async () => {
    if (token.value) {
      try {
        const userData = await fetchUserProfile()
        user.value = userData
      } catch (error) {
        console.error('获取用户信息失败:', error)
        logout()
      }
    }
  }

  // 登录方法
  const login = async (credentials) => {
    try {
      const { user: userData, token: authToken } = await loginUser(credentials)
      user.value = userData
      token.value = authToken
      isAuthenticated.value = true
      localStorage.setItem('authToken', authToken)
      return userData
    } catch (error) {
      throw error
    }
  }

  // 注册方法
  const register = async (userData) => {
    try {
      const { user: newUser, token: authToken } = await registerUser(userData)
      user.value = newUser
      token.value = authToken
      isAuthenticated.value = true
      localStorage.setItem('authToken', authToken)
      return newUser
    } catch (error) {
      throw error
    }
  }

  // 登出方法
  const logout = () => {
    logoutUser()
    user.value = null
    token.value = null
    isAuthenticated.value = false
    localStorage.removeItem('authToken')
    router.push('/login')
  }

  // 更新用户信息
  const updateUser = (newUserData) => {
    user.value = { ...user.value, ...newUserData }
  }

  // 角色检查方法
  const isUser = () => user.value?.role === 'user'
  const isPlayer = () => user.value?.role === 'player'
  const isCaptain = () => user.value?.role === 'captain'
  const isAdmin = () => user.value?.role === 'admin'

  // 升级用户角色
  const upgradeToPlayer = () => {
    if (user.value) {
      user.value.role = 'player'
    }
  }

  const upgradeToCaptain = () => {
    if (user.value) {
      user.value.role = 'captain'
    }
  }


  // 初始化用户状态
  init()

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
    logout,
    updateUser,
    isUser,
    isAdmin,
    isCaptain,
    isPlayer,
    upgradeToPlayer,
    upgradeToCaptain,
  }
})