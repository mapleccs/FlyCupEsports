<template>
  <div class="live-container">
    <!-- 直播平台选择器 -->
    <div class="platform-selector">
      <el-radio-group v-model="selectedPlatform" @change="changePlatform">
        <el-radio-button label="bilibili">
          <i class="iconfont icon-bilibili"></i> B站直播
        </el-radio-button>
        <el-radio-button label="douyin">
          <i class="iconfont icon-douyin"></i> 抖音直播
        </el-radio-button>
      </el-radio-group>
    </div>

    <!-- 直播内容区域 -->
    <div class="live-content">
      <!-- 直播主画面 -->
      <div class="live-player">
        <div v-if="selectedPlatform === 'bilibili'">
          <iframe
            :src="bilibiliEmbedUrl"
            frameborder="0"
            allowfullscreen="true"
            class="live-iframe"
          ></iframe>
        </div>
        <div v-else-if="selectedPlatform === 'douyin'" class="douyin-container">
          <iframe
            :src="douyinEmbedUrl"
            frameborder="0"
            allowfullscreen="true"
            class="live-iframe"
          ></iframe>
          <div v-if="isMobile" class="mobile-tip">
            <p>抖音直播建议在移动端APP观看最佳体验</p>
            <el-button type="primary" @click="openDouyinApp">
              打开抖音APP
            </el-button>
          </div>
        </div>
      </div>

      <!-- 直播聊天室 -->
      <div class="live-chat">
        <div class="chat-header">
          <h3>直播聊天室</h3>
          <el-tag type="danger" effect="dark">实时互动</el-tag>
        </div>
        <div class="chat-messages">
          <div v-for="(msg, index) in chatMessages" :key="index" class="message">
            <div class="avatar">
              <img :src="msg.avatar" alt="avatar" />
            </div>
            <div class="content">
              <span class="username">{{ msg.username }}</span>
              <span class="text">{{ msg.text }}</span>
            </div>
            <div class="time">{{ msg.time }}</div>
          </div>
        </div>
        <div class="chat-input">
          <el-input
            v-model="newMessage"
            placeholder="和大家说点什么..."
            @keyup.enter="sendMessage"
          >
            <template #append>
              <el-button icon="el-icon-s-promotion" @click="sendMessage" />
            </template>
          </el-input>
        </div>
      </div>
    </div>

    <!-- 赛事直播预告 -->
    <div class="live-schedule">
      <h3>近期赛事直播预告</h3>
      <el-timeline>
        <el-timeline-item
          v-for="(event, index) in upcomingEvents"
          :key="index"
          :timestamp="event.time"
          placement="top"
        >
          <el-card>
            <div class="event-card">
              <div class="teams">
                <div class="team">
                  <img :src="event.teamA.logo" :alt="event.teamA.name" />
                  <span>{{ event.teamA.name }}</span>
                </div>
                <div class="vs">VS</div>
                <div class="team">
                  <img :src="event.teamB.logo" :alt="event.teamB.name" />
                  <span>{{ event.teamB.name }}</span>
                </div>
              </div>
              <div class="event-info">
                <div class="tournament">
                  <i class="el-icon-trophy"></i> {{ event.tournament }}
                </div>
                <div class="platform">
                  <i class="el-icon-video-camera"></i> {{ event.platform }}
                </div>
              </div>
            </div>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLiveStore } from '@/stores/liveStore'

// 使用Pinia store管理直播状态
const liveStore = useLiveStore()

// 响应式数据
const selectedPlatform = ref('bilibili')
const newMessage = ref('')
const chatMessages = ref([])
const upcomingEvents = ref([])

// 计算属性
const bilibiliEmbedUrl = computed(() => {
  return `https://live.bilibili.com/embed/${liveStore.bilibiliRoomId}`
})

const douyinEmbedUrl = computed(() => {
  return `https://live.douyin.com/${liveStore.douyinRoomId}`
})

const isMobile = computed(() => {
  return window.innerWidth <= 768
})

// 方法
const changePlatform = () => {
  liveStore.setCurrentPlatform(selectedPlatform.value)
}

const sendMessage = () => {
  if (newMessage.value.trim()) {
    chatMessages.value.push({
      id: Date.now(),
      username: '我',
      avatar: '/default-avatar.png',
      text: newMessage.value,
      time: new Date().toLocaleTimeString()
    })
    newMessage.value = ''
    // 滚动到底部
    setTimeout(() => {
      const chatContainer = document.querySelector('.chat-messages')
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight
      }
    }, 100)
  }
}

const openDouyinApp = () => {
  window.location.href = `douyin://live.douyin.com/${liveStore.douyinRoomId}`
}

// 初始化
onMounted(() => {
  // 从store加载直播数据
  liveStore.fetchLiveData().then(() => {
    chatMessages.value = liveStore.chatMessages
    upcomingEvents.value = liveStore.upcomingEvents
  })

  // 模拟实时聊天
  setInterval(() => {
    const messages = [
      '比赛什么时候开始？',
      '这个选手太强了！',
      '支持蓝色方！',
      '有人知道下场比赛时间吗？',
      '加油啊！！！',
      '这个操作太秀了！'
    ]
    const users = [
      { name: '电竞爱好者', avatar: '/avatar1.png' },
      { name: 'LOL老玩家', avatar: '/avatar2.png' },
      { name: '赛事分析师', avatar: '/avatar3.png' },
      { name: '战队粉丝', avatar: '/avatar4.png' }
    ]

    const randomUser = users[Math.floor(Math.random() * users.length)]
    const randomMessage = messages[Math.floor(Math.random() * messages.length)]

    chatMessages.value.push({
      id: Date.now(),
      username: randomUser.name,
      avatar: randomUser.avatar,
      text: randomMessage,
      time: new Date().toLocaleTimeString()
    })
  }, 5000)
})
</script>

<style scoped>
.live-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.platform-selector {
  margin-bottom: 20px;
  text-align: center;
}

.live-content {
  display: flex;
  gap: 20px;
  margin-bottom: 40px;
}

.live-player {
  flex: 3;
  position: relative;
  background: #000;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.live-iframe {
  width: 100%;
  height: 600px;
  display: block;
}

.douyin-container {
  position: relative;
}

.mobile-tip {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  text-align: center;
  color: white;
  background: rgba(0, 0, 0, 0.6);
  padding: 10px;
  border-radius: 4px;
  margin: 0 20px;
}

.live-chat {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: rgba(15, 23, 42, 0.8);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.chat-header {
  padding: 15px;
  background: rgba(93, 95, 239, 0.8);
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-messages {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
  max-height: 500px;
}

.message {
  display: flex;
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 10px;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content {
  flex: 1;
}

.username {
  font-weight: bold;
  color: #5d5fef;
  margin-right: 8px;
}

.text {
  color: #e2e8f0;
}

.time {
  font-size: 0.8rem;
  color: #94a3b8;
  align-self: flex-end;
}

.chat-input {
  padding: 15px;
  background: rgba(30, 41, 59, 0.8);
}

.live-schedule {
  background: rgba(15, 23, 42, 0.6);
  padding: 20px;
  border-radius: 8px;
}

.live-schedule h3 {
  color: #fff;
  margin-bottom: 20px;
  text-align: center;
  font-size: 1.5rem;
}

.event-card {
  padding: 15px;
}

.teams {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 15px;
}

.team {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.team img {
  width: 60px;
  height: 60px;
  object-fit: contain;
  margin-bottom: 8px;
}

.vs {
  font-size: 1.2rem;
  font-weight: bold;
  color: #ff4655;
}

.event-info {
  display: flex;
  justify-content: space-between;
  color: #64748b;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .live-content {
    flex-direction: column;
  }

  .live-iframe {
    height: 500px;
  }
}

@media (max-width: 768px) {
  .live-iframe {
    height: 300px;
  }

  .chat-messages {
    max-height: 300px;
  }
}
</style>