import { useUserStore } from '@/stores/userStore'
import apiClient from "./api.js";



const API_URL = "/api/v1/player/register"
// 选手报名
export function createPlayerSignup(playerData) {
  return apiClient.post(`/api/v1/player/register`, playerData)
}

// 创建战队
export function createTeamSignup(teamData) {
  return apiClient.post(`${API_URL}/teams`, teamData)
}

// 发起微信支付
export function createWechatPayment(orderData) {
  return apiClient.post(`${API_URL}/payments/wechat`, orderData)
}

// 检查支付状态
export function checkPaymentStatus(orderId) {
  return apiClient.get(`${API_URL}/payments/status/${orderId}`)
}

// 上传Logo
export function uploadLogo(file) {
  const formData = new FormData()
  formData.append('file', file)

  return apiClient.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
