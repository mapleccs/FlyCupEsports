import axios from 'axios'
import { useUserStore } from '@/stores/userStore'

export async function getTeams() {
  try {
    // 实际开发中，这里应该是从后端API获取数据
    // 例如: const response = await axios.get('/api/teams')
    // 为了演示，我们使用public目录下的模拟数据
    const response = await axios.get('/data/teams.json')
    return response.data.teams
  } catch (error) {
    console.error('获取战队数据失败:', error)
    throw error
  }
}

export const createTeam = async (teamData) => {
  try {
    const response = await axios.post('/api/teams', teamData)
    const userStore = useUserStore()

    // 升级用户为队长
    userStore.upgradeToCaptain()

    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.message || '创建战队失败')
  }
}
