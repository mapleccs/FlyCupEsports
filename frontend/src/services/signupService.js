import { useUserStore } from '@/stores/userStore'
import apiClient from "./api.js";


const getV1Url = (path) => `/api/v1${path}`;

// 选手报名
export function createPlayerSignup(playerData) {
  return apiClient.post(getV1Url('/player/register'), playerData)
}

// 创建战队
export function createTeamSignup(teamData) {
  return apiClient.post(getV1Url('/team'), teamData)
}

// 发起微信支付
export function createWechatPayment(orderData) {
  return apiClient.post(getV1Url('/payments/wechat'), orderData)
}

// 检查支付状态
export function checkPaymentStatus(orderId) {
  return apiClient.get(getV1Url(`/payments/status/${orderId}`))
}

// 上传Logo
export function uploadLogo(file) {
  const formData = new FormData();
  formData.append('file', file);

  // 已修正: 使用带版本号的、正确的API上传路径
  return apiClient.post(getV1Url('/upload'), formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
}
