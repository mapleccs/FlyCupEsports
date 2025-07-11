import axios from 'axios'

// 获取即将开始的赛事列表
export function getUpcomingEvents() {
  return axios.get('/api/events/upcoming')
}
