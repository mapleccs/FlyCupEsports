<template>
  <div class="schedule-container">
    <!-- 顶部筛选区域 -->
    <div class="schedule-header">
      <h1>赛事赛程</h1>
      <p class="subtitle">追踪你喜爱的战队比赛日程</p>

      <schedule-filter
        :teams="teams"
        :tournaments="tournaments"
        @filter-change="handleFilterChange"
      />
    </div>

    <!-- 视图切换 -->
    <div class="view-toggle">
      <el-radio-group v-model="activeView" size="large">
        <el-radio-button label="calendar">日历视图</el-radio-button>
        <el-radio-button label="table">表格视图</el-radio-button>
      </el-radio-group>
    </div>

    <!-- 加载状态 -->
    <div v-if="loading" class="loading-container">
      <el-skeleton :rows="6" animated />
    </div>

    <!-- 赛程内容 -->
    <div v-else>
      <!-- 日历视图 -->
      <schedule-calendar
        v-if="activeView === 'calendar'"
        :matches="filteredMatches"
        @match-selected="handleMatchSelect"
      />

      <!-- 表格视图 -->
      <schedule-table
        v-else
        :matches="filteredMatches"
        @match-selected="handleMatchSelect"
      />
    </div>

    <!-- 比赛详情弹窗 -->
    <el-dialog
      v-model="showMatchDetail"
      :title="selectedMatch?.title || '比赛详情'"
      width="80%"
      top="5vh"
    >
      <match-detail
        v-if="selectedMatch"
        :match="selectedMatch"
        @watch-live="watchLive"
        @watch-replay="watchReplay"
      />
    </el-dialog>

    <!-- 直播/回放弹窗 -->
    <el-dialog
      v-model="showVideoPlayer"
      :title="videoTitle"
      width="90%"
      top="5vh"
      destroy-on-close
    >
      <div class="video-container">
        <iframe
          v-if="videoUrl"
          :src="videoUrl"
          frameborder="0"
          allowfullscreen
          class="video-player"
        ></iframe>
        <div v-else class="no-video">
          <i class="el-icon-video-camera"></i>
          <p>视频加载中，请稍候...</p>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import ScheduleFilter from '@/components/schedule/ScheduleFilter.vue'
import ScheduleCalendar from '@/components/schedule/ScheduleCalendar.vue'
import ScheduleTable from '@/components/schedule/ScheduleTable.vue'
import MatchDetail from '@/components/schedule/MatchDetail.vue'
import { useScheduleStore } from '@/stores/scheduleStore'

const scheduleStore = useScheduleStore()

// 数据状态
const loading = ref(true)
const activeView = ref('calendar')
const filters = ref({
  tournament: 'all',
  team: 'all',
  status: 'all'
})

// UI状态
const showMatchDetail = ref(false)
const showVideoPlayer = ref(false)
const selectedMatch = ref(null)
const videoUrl = ref('')
const videoTitle = ref('')

// 计算属性
const matches = computed(() => scheduleStore.matches)
const teams = computed(() => scheduleStore.teams)
const tournaments = computed(() => scheduleStore.tournaments)

const filteredMatches = computed(() => {
  return matches.value.filter(match => {
    // 按赛事筛选
    if (filters.value.tournament !== 'all' &&
        match.tournament.id !== filters.value.tournament) {
      return false
    }

    // 按战队筛选
    if (filters.value.team !== 'all') {
      const teamIds = [match.teamA.id, match.teamB.id]
      if (!teamIds.includes(filters.value.team)) {
        return false
      }
    }

    // 按状态筛选
    if (filters.value.status !== 'all' &&
        match.status !== filters.value.status) {
      return false
    }

    return true
  })
})

// 方法
const handleFilterChange = (newFilters) => {
  filters.value = { ...filters.value, ...newFilters }
}

const handleMatchSelect = (match) => {
  selectedMatch.value = match
  showMatchDetail.value = true
}

const watchLive = (match) => {
  videoTitle.value = `直播: ${match.teamA.name} vs ${match.teamB.name}`
  videoUrl.value = match.liveUrl || ''
  showVideoPlayer.value = true
  showMatchDetail.value = false
}

const watchReplay = (match) => {
  videoTitle.value = `回放: ${match.teamA.name} vs ${match.teamB.name}`
  videoUrl.value = match.replayUrl || ''
  showVideoPlayer.value = true
  showMatchDetail.value = false
}

// 初始化
onMounted(async () => {
  try {
    await scheduleStore.fetchScheduleData()
  } catch (error) {
    console.error('加载赛程数据失败:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.schedule-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  background: linear-gradient(135deg, #0f172a, #1e293b);
  min-height: 100vh;
}

.schedule-header {
  text-align: center;
  margin-bottom: 30px;
  padding: 20px;
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.9));
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

.schedule-header h1 {
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 10px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.subtitle {
  color: #94a3b8;
  font-size: 1.1rem;
  margin-bottom: 20px;
}

.view-toggle {
  display: flex;
  justify-content: center;
  margin: 20px 0 30px;
}

.loading-container {
  padding: 40px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
}

.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
  height: 0;
  overflow: hidden;
  border-radius: 8px;
  background: #000;
}

.video-player {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}

.no-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #64748b;
  font-size: 1.2rem;
}

.no-video i {
  font-size: 3rem;
  margin-bottom: 15px;
}

@media (max-width: 1024px) {
  .schedule-header h1 {
    font-size: 2rem;
  }

  .view-toggle {
    margin: 10px 0 20px;
  }
}
</style>