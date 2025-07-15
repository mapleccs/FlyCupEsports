import axios from 'axios' // 使用统一的axios实例


const API_URL = "/api"
// 选手报名
export function registerPlayer(playerData) {
  return axios.post('/api/players', playerData)
}

// 创建战队
export function createTeam(teamData) {
  return axios.post('/api/teams', teamData)
}

// 发起支付
export function createPayment(paymentData) {
  return axios.post('/api/payments', paymentData)
}

// 上传Logo
export function uploadLogo(file) {
  const formData = new FormData()
  formData.append('file', file)

  return axios.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}