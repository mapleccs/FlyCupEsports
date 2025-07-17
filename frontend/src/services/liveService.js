import axios from 'axios'

// 直播API基础URL
const LIVE_API = '/api/v1/live'

// 获取直播数据
export const fetchLiveData = async () => {
  try {
    const response = await axios.get(`${LIVE_API}/data`)
    return response.data
  } catch (error) {
    console.error('Error fetching live data:', error)
    throw error
  }
}

// 获取直播聊天消息
export const fetchChatMessages = async (roomId, platform) => {
  try {
    const response = await axios.get(`${LIVE_API}/chat`, {
      params: { roomId, platform }
    })
    return response.data.messages
  } catch (error) {
    console.error('Error fetching chat messages:', error)
    return []
  }
}

// 发送聊天消息
export const sendChatMessage = async (message) => {
  try {
    const response = await axios.post(`${LIVE_API}/chat/send`, { message })
    return response.data
  } catch (error) {
    console.error('Error sending chat message:', error)
    throw error
  }
}

// 获取赛事预告
export const fetchUpcomingEvents = async () => {
  try {
    const response = await axios.get(`${LIVE_API}/events`)
    return response.data.events
  } catch (error) {
    console.error('Error fetching upcoming events:', error)
    return []
  }
}