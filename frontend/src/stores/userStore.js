// stores/userStore.js
import { defineStore } from 'pinia'
import {computed, ref} from 'vue'
import { loginUser, registerUser, logoutUser, fetchUserProfile } from '@/services/authService'
import { useRouter } from 'vue-router'

// 添加角色常量
const ROLES = {
  USER: 'user',
  PLAYER: 'player',
  CAPTAIN: 'captain',
  ADMIN: 'admin'
}

export const useUserStore = defineStore('user', () => {
  const saveRole = localStorage.getItem('userRole')
  const user = ref(saveRole? {role: saveRole} : null)
  const token = ref(localStorage.getItem('authToken') || null)
  const isAuthenticated = ref(!!token.value)
  const router = useRouter()

    // 添加计算属性
  const userRole = computed(() => user.value?.role || ROLES.USER)
  const isUser = computed(() => userRole.value === ROLES.USER)
  const isPlayer = computed(() => userRole.value === ROLES.PLAYER)
  const isCaptain = computed(() => userRole.value === ROLES.CAPTAIN)
  const isAdmin = computed(() => userRole.value === ROLES.ADMIN)

  // 添加初始化方法
  const init = async () => {
    if (token.value && !user.value) {
      try {
        user.value = await fetchUserProfile()
        localStorage.setItem('userRole', user.value.role)
      } catch (error) {
        console.error('初始化用户信息失败:', error)
        logout()
      }
    }
  }

// 在 login 方法中添加调试信息
const login = async (credentials) => {
  try {
    console.log('尝试登录:', credentials)
    const { user: userData, token: authToken } = await loginUser(credentials)
    console.log('登录响应:', { userData, authToken })

    user.value = userData
    token.value = authToken
    isAuthenticated.value = true

    localStorage.setItem('authToken', authToken)
    localStorage.setItem('userRole', userData.role)

    await router.push('/')
    return userData
  } catch (error) {
    console.error('登录错误:', error)
    throw error
  }
}

// 在 register 方法中添加调试信息
const register = async (userData) => {
  try {
    console.log('尝试注册:', userData)
    const { success, message } = await registerUser(userData)
    console.log('注册接口返回:', {success, message})

    if (success) {
      const { user: newUser, token: authToken } = await loginUser({
        username: userData.username,
        password: userData.password
      })

      user.value = newUser
      token.value = authToken
      isAuthenticated.value = true
      localStorage.setItem('authToken', authToken)
      localStorage.setItem('userRole', userData.role)
      await router.push('/')
    }

    return {success, message}
  } catch (error) {
    console.error('注册错误:', error)
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
    localStorage.removeItem('userRole')

    router.push('/login')
  }

  // 更新用户信息
  const updateUser = (newUserData) => {
    user.value = { ...user.value, ...newUserData }
  }

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
    init,
    isUser,
    isAdmin,
    isCaptain,
    isPlayer,
    upgradeToPlayer,
    upgradeToCaptain,
    userRole,
    ROLES
  }
})