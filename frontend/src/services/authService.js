// services/authService.js
import axios from 'axios'


// 更新 API 基础路径
const API_URL = 'http://localhost:8000/api/v1/user'  // 确保与后端一致

// 登录方法
export const loginUser = async (credentials) => {
  try {
    const res = await axios.post(`${API_URL}/login`, {
      username: credentials.username,
      password: credentials.password
    })

    const data = res.data
    const { user_id, user_role_name, token } = data

    // 保本地一份，刷新页面还能拿到
    localStorage.setItem('authToken', token)
    localStorage.setItem('userRole', user_role_name)

    return {
      user: {
        id: user_id,
        // 把 "Admin"/"User"/"Competitor"/"Captain" 转成小写，跟 Store 里 ROLES 对齐
        role: user_role_name.toLowerCase()
      },
      token
    }
  } catch (error) {
    throw new Error(error.response?.data?.detail || '登录失败，请稍后再试')
  }
}

// 注册方法
export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/register`, {
      username: userData.username,
      password: userData.password,
      role: userData.role // 添加角色字段
    })

    return {
      success: response.data.success,
      message: response.data.message
    }
  } catch (error) {
    throw new Error(error.response?.data?.detail || '注册失败，请稍后再试')
  }
}

// 获取用户信息
export const fetchUserProfile = async () => {
  try {
    const token = localStorage.getItem('authToken')
    if (!token) return null

    const res = await axios.get(`${API_URL}/profile`, {
      headers: {Authorization: `Bearer ${token}`}
    })

    const data = res.data
    const { user_id, user_role_name } = data

    return {
      id: user_id,
      role: user_role_name.toLowerCase()
    }
  } catch (error) {
    throw new Error('获取用户信息失败')
  }
}

export const logoutUser = async () => {
  const token = localStorage.getItem('authToken')
  if (!token) return
  try {
    await axios.post(
      `${API_URL}/logout`,
      {},
      { headers: { Authorization: `Bearer ${token}` } }
    )
  } catch (err) {
    console.warn('注销请求失败，但仍清除本地登录状态', err)
  } finally {
    localStorage.removeItem('authToken')
    localStorage.removeItem('userRole')
  }
}