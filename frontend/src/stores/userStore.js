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
    // 条件：当localStorage中有token，但store中的isAuthenticated状态还未同步时
    if (token.value && !isAuthenticated.value) {
      try {
        // 标记为已认证，这是最重要的一步
        // 这样后续的路由守卫和API请求都能立刻知道用户是登录状态
        isAuthenticated.value = true;

        // 异步在后台获取完整的用户信息，这不会阻塞UI
        // 即使用户信息还没获取完，API请求也已经可以带上token了
        const userData = await fetchUserProfile();
        user.value = userData;
        localStorage.setItem('userRole', user.value.role); // 更新本地的角色信息
      } catch (error) {
        console.error('初始化用户信息失败，将自动登出:', error);
        logout(); // 如果token无效或获取信息失败，则执行登出
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