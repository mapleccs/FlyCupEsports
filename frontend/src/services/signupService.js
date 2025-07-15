import axios from 'axios' // 使用统一的axios实例
import { useUserStore } from '@/stores/userStore'



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

export const submitSignup = async (formData, type) => {
  try {
    const response = await axios.post('/api/signup', { ...formData, type })
    const userStore = useUserStore()

    // 根据报名类型升级用户角色
    if (type === 'player') {
      userStore.upgradeToPlayer()
    } else if (type === 'team') {
      userStore.upgradeToCaptain()
    }

    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.message || '报名失败')
  }
}