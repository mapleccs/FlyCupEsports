// services/authService.js
import axios from 'axios'


// 更新 API 基础路径
const API_URL = 'http://localhost:8000/api/v1/auth'  // 确保与后端一致

// 登录方法 - 添加详细的错误处理
export const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/login`, credentials)
    return response.data
  } catch (error) {
    const errorMsg = error.response?.data?.detail ||
                    error.response?.data?.message ||
                    '登录失败，请检查用户名或密码'
    throw new Error(errorMsg)
  }
}

// 注册方法 - 添加详细的错误处理
export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/register`, userData)
    return response.data
  } catch (error) {
    const errorMsg = error.response?.data?.detail ||
                    error.response?.data?.message ||
                    '注册失败，请检查输入信息'
    throw new Error(errorMsg)
  }
}

// 用户登出
export const logoutUser = async () => {
  try {
    // 根据后端实现，可能需要发送请求
    // await axios.post(`${API_URL}/logout`)
    return true
  } catch (error) {
    console.error('登出失败:', error)
    return false
  }
}

// 获取用户信息
export const fetchUserProfile = async () => {
  try {
    const token = localStorage.getItem('authToken')
    if (!token) return null

    const response = await axios.get(`${API_URL}/profile`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    return response.data
  } catch (error) {
    throw new Error('获取用户信息失败')
  }
}

// 更新用户信息
export const updateUserProfile = async (userData) => {
  try {
    const token = localStorage.getItem('authToken')
    if (!token) return null

    const response = await axios.put(`${API_URL}/profile`, userData, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    return response.data
  } catch (error) {
    throw new Error('更新用户信息失败')
  }
}