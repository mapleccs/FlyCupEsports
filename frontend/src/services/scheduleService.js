import axios from 'axios'

// API基础路径
const API_BASE = '/api/v1/schedule'

// 获取所有比赛
export const fetchMatches = async () => {
  try {
    const response = await axios.get(`${API_BASE}/matches`)
    return response.data.map(match => ({
      ...match,
      // 添加直播/回放链接
      liveUrl: match.status === 'live' ?
        generateLiveUrl(match) : null,
      replayUrl: match.status === 'completed' ?
        generateReplayUrl(match) : null
    }))
  } catch (error) {
    console.error('获取比赛数据失败:', error)
    return []
  }
}

// 获取所有战队
export const fetchTeams = async () => {
  try {
    const response = await axios.get(`${API_BASE}/teams`)
    return response.data
  } catch (error) {
    console.error('获取战队数据失败:', error)
    return []
  }
}

// 获取所有赛事
export const fetchTournaments = async () => {
  try {
    const response = await axios.get(`${API_BASE}/tournaments`)
    return response.data
  } catch (error) {
    console.error('获取赛事数据失败:', error)
    return []
  }
}

// 生成直播链接
const generateLiveUrl = (match) => {
  // 这里可以根据实际平台生成直播链接
  return `https://live.bilibili.com/${match.platforms.bilibili}`
}

// 生成回放链接
const generateReplayUrl = (match) => {
  // 这里可以根据实际平台生成回放链接
  return match.replayId ?
    `https://www.bilibili.com/video/${match.replayId}` :
    null
}