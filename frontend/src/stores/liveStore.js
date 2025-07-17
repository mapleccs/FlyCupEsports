import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { fetchLiveData } from '@/services/liveService'

export const useLiveStore = defineStore('live', () => {
  // 状态
  const bilibiliRoomId = ref('25079843') // 默认B站直播间ID
  const douyinRoomId = ref('123456789') // 默认抖音直播间ID
  const currentPlatform = ref('bilibili')
  const chatMessages = ref([])
  const upcomingEvents = ref([])

  // 计算属性
  const currentRoomId = computed(() => {
    return currentPlatform.value === 'bilibili'
      ? bilibiliRoomId.value
      : douyinRoomId.value
  })

  // Actions
  const setBilibiliRoomId = (id) => {
    bilibiliRoomId.value = id
  }

  const setDouyinRoomId = (id) => {
    douyinRoomId.value = id
  }

  const setCurrentPlatform = (platform) => {
    currentPlatform.value = platform
  }

  const fetchLiveData = async () => {
    try {
      const data = await fetchLiveData()
      upcomingEvents.value = data.upcomingEvents
      // 可以在此处设置直播间ID
      if (data.bilibiliRoomId) {
        setBilibiliRoomId(data.bilibiliRoomId)
      }
      if (data.douyinRoomId) {
        setDouyinRoomId(data.douyinRoomId)
      }
    } catch (error) {
      console.error('Failed to fetch live data:', error)
    }
  }

  return {
    bilibiliRoomId,
    douyinRoomId,
    currentPlatform,
    chatMessages,
    upcomingEvents,
    currentRoomId,
    setBilibiliRoomId,
    setDouyinRoomId,
    setCurrentPlatform,
    fetchLiveData
  }
})