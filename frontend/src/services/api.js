import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

// 创建一个新的axios实例
const apiClient = axios.create({
  // 您可以在这里设置基础URL等全局配置
  // baseURL: '/api/v1'
});

// 添加请求拦截器
apiClient.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么
    const userStore = useUserStore();
    const token = userStore.token; // 从Pinia store获取token

    if (token) {
      // 如果token存在，则将其添加到每个请求的Authorization头中
      // 格式为 'Bearer <token>'
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

export default apiClient;