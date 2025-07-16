// services/authService.js
import axios from 'axios'


// 更新 API 基础路径
const API_URL = 'http://localhost:8000'  // 确保与后端一致

// 登录方法
export const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/login`, {
      username: credentials.username,
      password: credentials.password
    })
    return response.data
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
    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.detail || '注册失败，请稍后再试')
  }
}

// 获取用户信息
export const fetchUserProfile = async () => {
  try {
    const token = localStorage.getItem('authToken')
    if (!token) return null

    const response = await axios.get(`${API_URL}/profile`, {
      headers: {Authorization: `Bearer ${token}`}
    })
    return response.data
  } catch (error) {
    throw new Error('获取用户信息失败')
  }
}