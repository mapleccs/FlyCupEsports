<template>
  <div class="checkin-panel">
    <div class="panel-header">
      <h2><i class="el-icon-timer"></i> 比赛签到</h2>
      <p>请确认您的队伍已准备就绪，所有队伍签到完成后将自动进入BP阶段</p>
    </div>

    <div class="teams-container">
      <div
        v-for="team in teams"
        :key="team.id"
        class="team-card"
        :class="{ 'checked-in': checkInStatus[team.id] }"
      >
        <div class="team-logo">
          <img :src="teamLogo(team)" alt="队伍标志">
        </div>
        <div class="team-info">
          <h3>{{ team.name }}</h3>
          <p>{{ team.captain.name }} (队长)</p>
        </div>
        <div class="checkin-status">
          <el-tag v-if="checkInStatus[team.id]" type="success" effect="dark">
            <i class="el-icon-check"></i> 已签到
          </el-tag>
          <el-button
            v-else
            type="primary"
            size="medium"
            @click="handleCheckIn(team.id)"
            :disabled="!isCaptain(team.id)"
            :icon="isCaptain(team.id) ? 'el-icon-check' : 'el-icon-user'"
          >
            {{ isCaptain(team.id) ? '确认签到' : '等待队长' }}
          </el-button>
        </div>
      </div>
    </div>

    <div class="checkin-progress">
      <div class="progress-text">
        签到进度: {{ checkedInCount }} / {{ teams.length }}
      </div>
      <el-progress
        :percentage="progressPercentage"
        :color="progressColor"
        :stroke-width="12"
      />
    </div>

    <div class="action-note">
      <el-alert type="info" show-icon>
        提示：只有队长可以进行签到操作。签到完成后，请确保所有队员都已准备就绪。
      </el-alert>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useUserStore } from '@/stores/userStore'

// props 增加默认值，避免 undefined/null
const props = defineProps({
  teams: {
    type: Array,
    default: () => []
  },
  checkInStatus: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['check-in'])
const userStore = useUserStore()

// 队徽地址生成
const teamLogo = (team) => `/images/teams/${team.logo}`

// 判断当前用户是否为该队队长
const isCaptain = (teamId) =>
  userStore.isCaptain && userStore.user.teamId === teamId

// 点击签到按钮
const handleCheckIn = (teamId) => {
  if (isCaptain(teamId)) {
    emit('check-in', teamId)
  }
}

// 计算已签到队伍数（空值保护）
const checkedInCount = computed(() => {
  const statusMap = props.checkInStatus || {}
  return Object.values(statusMap).filter((status) => status).length
})

// 计算进度百分比（除零保护）
const progressPercentage = computed(() => {
  const total = props.teams.length
  return total ? (checkedInCount.value / total) * 100 : 0
})

// 根据进度选取进度条颜色
const progressColor = computed(() => {
  const pct = progressPercentage.value
  if (pct < 50) return '#ff4655'
  if (pct < 100) return '#ff9800'
  return '#4caf50'
})
</script>

<style scoped>
.checkin-panel {
  padding: 20px;
}

.panel-header {
  text-align: center;
  margin-bottom: 30px;
}

.panel-header h2 {
  font-size: 1.8rem;
  margin-bottom: 10px;
  color: white;
}

.panel-header p {
  color: var(--gray);
  font-size: 1rem;
}

.teams-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
  margin-bottom: 30px;
}

.team-card {
  background: rgba(40, 50, 70, 0.8);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: center;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.team-card.checked-in {
  border-color: #4caf50;
  background: rgba(76, 175, 80, 0.1);
}

.team-logo {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 15px;
  background: rgba(255, 255, 255, 0.1);
}

.team-logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-info {
  flex: 1;
}

.team-info h3 {
  margin: 0 0 5px;
  font-size: 1.3rem;
}

.team-info p {
  margin: 0;
  color: var(--gray);
  font-size: 0.9rem;
}

.checkin-status {
  margin-left: 10px;
}

.checkin-progress {
  margin-bottom: 25px;
}

.progress-text {
  text-align: center;
  margin-bottom: 10px;
  font-weight: 500;
}
</style>