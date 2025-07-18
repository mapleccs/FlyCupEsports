<template>
  <MainLayout>
    <div class="match-control-container">
      <MatchStatusBar
        :status="matchStatus"
        :phase="currentPhase"
        :currentTeam="currentTeamTurn"
      />

      <div class="match-header">
        <h1>{{ matchData?.name }}</h1>
        <p>比赛时间: {{ matchData?.date }} {{ matchData?.time }}</p>
      </div>

      <div class="teams-overview">
        <TeamOverview
          v-for="team in teams"
          :key="team.id"
          :team="team"
          :checkInStatus="checkInStatus[team.id]"
          :bans="bans[team.id === 1 ? 'team1' : 'team2']"
          :picks="picks[team.id === 1 ? 'team1' : 'team2']"
        />
      </div>

      <div class="match-content">
        <template v-if="!isBPEnabled">
          <CheckInPanel
            :teams="teams"
            :checkInStatus="checkInStatus"
            @check-in="handleCheckIn"
          />
        </template>

        <template v-else>
          <BanPickPanel
            :matchId="matchId"
            :availableHeroes="availableHeroes"
            :currentPhase="currentPhase"
            :currentTeam="currentTeamTurn"
            @bp-select="handleBPSelection"
          />
        </template>
      </div>

      <div v-if="isDevelopment" class="dev-tools">
        <el-button type="warning" @click="resetBP">重置BP</el-button>
        <el-button type="danger" @click="forceCheckIn">强制完成签到</el-button>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMatchStore } from '@/stores/matchStore'
import MatchStatusBar from '@/components/match/MatchStatusBar.vue'
import TeamOverview from '@/components/match/TeamOverview.vue'
import CheckInPanel from '@/components/match/CheckInPanel.vue'
import BanPickPanel from '@/components/match/BanPickPanel.vue'

const route = useRoute()
const matchId = route.params.matchId
const matchStore = useMatchStore()

// 开发环境开关
const isDevelopment = process.env.NODE_ENV === 'development'

// 各种状态／数据的计算属性，并对 undefined 做保护
const matchStatus = computed(() => {
  if (matchStore.currentPhase === 'completed') return 'BP已完成'
  if (matchStore.isBPEnabled) return 'BP进行中'
  // 在 checkInStatus 为空时，Object.values([]) 不会报错
  return Object.values(matchStore.checkInStatus || {}).some(s => s)
    ? '等待其他队伍签到'
    : '等待签到'
})
const currentPhase      = computed(() => matchStore.currentPhase)
const currentTeamTurn   = computed(() => matchStore.currentTeamTurn)
const teams             = computed(() => matchStore.teams || [])
const isBPEnabled       = computed(() => matchStore.isBPEnabled)
const availableHeroes   = computed(() => matchStore.availableHeroes || [])
const checkInStatus     = computed(() => matchStore.checkInStatus || {})
const bans              = computed(() => matchStore.bans || { team1: [], team2: [] })
const picks             = computed(() => matchStore.picks || { team1: [], team2: [] })

// 事件处理
const handleCheckIn = teamId => matchStore.handleCheckIn(teamId)
const handleBPSelection = ({ heroId, actionType }) =>
  matchStore.handleBPSelection(heroId, actionType)
const resetBP      = () => matchStore.resetBP()
const forceCheckIn = () => {
  matchStore.handleCheckIn(1)
  matchStore.handleCheckIn(2)
}

// 挂载时拉取比赛数据
onMounted(() => {
  matchStore.fetchMatch(matchId)
})
</script>

<style scoped>
.match-control-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background: var(--darker);
  color: white;
  min-height: calc(100vh - 70px);
}

.match-header {
  text-align: center;
  margin: 20px 0 30px;
}

.match-header h1 {
  font-size: 2rem;
  margin-bottom: 8px;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.match-header p {
  color: var(--gray);
}

.teams-overview {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  margin-bottom: 30px;
}

.match-content {
  background: rgba(25, 32, 50, 0.7);
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(93, 95, 239, 0.2);
}

.dev-tools {
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  gap: 10px;
  z-index: 1000;
}
</style>
