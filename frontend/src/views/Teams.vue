<template>
  <div class="teams-page">
    <div class="container">
      <h1 class="page-title">战队排行榜</h1>

      <!-- 筛选区域 -->
      <div class="filters">
        <el-select v-model="selectedRegion" placeholder="选择赛区" class="region-filter">
          <el-option label="全部赛区" value="all"></el-option>
          <el-option label="FLY" value="FLY"></el-option>
          <el-option label="FPF" value="FPF"></el-option>
          <el-option label="ACE" value="ACE"></el-option>
          <el-option label="ACC" value="ACC"></el-option>
        </el-select>

        <el-button
          type="primary"
          @click="openComparison"
          class="compare-btn"
        >
          <i class="el-icon-scale"></i> 对比战队
        </el-button>
      </div>

      <!-- 加载状态 -->
      <div v-if="isLoading" class="loading-placeholder">
        <i class="el-icon-loading"></i> 加载战队数据中...
      </div>

      <!-- 错误状态 -->
      <div v-else-if="error" class="error-message">
        <i class="el-icon-error"></i> {{ error }}
      </div>

      <!-- 战队排行榜 -->
      <div v-else class="teams-container">
        <el-table :data="filteredTeams" style="width: 100%" stripe v-loading="isLoading">
          <el-table-column prop="rank" label="排名" width="80" sortable>
            <template #default="{ $index }">
              <span class="rank-badge" :class="getRankClass($index + 1)">
                {{ $index + 1 }}
              </span>
            </template>
          </el-table-column>
          <el-table-column label="战队" width="200">
            <template #default="{ row }">
              <div class="team-info">
                <img :src="getLogoPath(row.logo)" class="team-logo" />
                <div>
                  <div class="team-name">{{ row.name }}</div>
                  <div class="team-region">{{ row.region }}</div>
                </div>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="win_rate" label="胜率" sortable>
            <template #default="{ row }">
              <div class="win-rate">
                {{ (row.win_rate * 100).toFixed(1) }}%
                <div class="win-loss">({{ row.win }}胜{{ row.loss }}负)</div>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="kda" label="KDA" sortable />
          <el-table-column prop="gold_per_min" label="每分钟金币" sortable />
          <el-table-column label="操作">
            <template #default="{ row }">
              <el-button type="primary" size="small" @click="showTeamDetail(row)">
                查看详情
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!-- 战队详情弹窗 -->
      <el-dialog
        v-model="detailVisible"
        :title="currentTeam ? currentTeam.name : '战队详情'"
        width="80%"
      >
        <TeamCard v-if="currentTeam" :team="currentTeam" />
        <div v-else class="loading-placeholder">
          <i class="el-icon-loading"></i> 加载中...
        </div>
      </el-dialog>

      <!-- 战队对比弹窗 -->
      <el-dialog v-model="comparisonVisible" title="战队对比" width="90%">
        <TeamComparison
          v-if="teams.length > 0"
          :teams="teams"
          :selectedTeam1="selectedTeam1"
          :selectedTeam2="selectedTeam2"
          @update:selectedTeam1="selectedTeam1 = $event"
          @update:selectedTeam2="selectedTeam2 = $event"
        />
        <div v-else class="loading-placeholder">
          <i class="el-icon-loading"></i> 加载战队数据...
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { getTeams } from '@/services/teamService'
import TeamCard from '@/components/ui/TeamCard.vue'
import TeamComparison from '@/components/ui/TeamComparison.vue'

const teams = ref([])
const selectedRegion = ref('all')
const detailVisible = ref(false)
const comparisonVisible = ref(false)
const currentTeam = ref(null)
const selectedTeam1 = ref(null)
const selectedTeam2 = ref(null)

// 加载状态和错误处理
const isLoading = ref(false)
const error = ref(null)

// 计算胜率并排序
const processedTeams = computed(() => {
  return teams.value
    .map(team => ({
      ...team,
      win_rate: team.win / (team.win + team.loss),
      total_matches: team.win + team.loss
    }))
    .sort((a, b) => b.win_rate - a.win_rate)
})

// 按赛区筛选
const filteredTeams = computed(() => {
  if (selectedRegion.value === 'all') return processedTeams.value
  return processedTeams.value.filter(t => t.region === selectedRegion.value)
})

onMounted(async () => {
  try {
    isLoading.value = true
    teams.value = await getTeams()
    // 确保有数据再设置默认值
    if (teams.value.length >= 2) {
      selectedTeam1.value = teams.value[0].id
      selectedTeam2.value = teams.value[1].id
    }
  } catch (err) {
    console.error('加载战队数据失败:', err)
    error.value = '加载战队数据失败，请稍后再试'
  } finally {
    isLoading.value = false
  }
})

function showTeamDetail(team) {
  currentTeam.value = team
  detailVisible.value = true
}

function openComparison() {
  comparisonVisible.value = true
  // 确保有数据再设置默认值
  if (teams.value.length >= 2) {
    selectedTeam1.value = teams.value[0].id
    selectedTeam2.value = teams.value[1].id
  }
}

function getRankClass(rank) {
  if (rank === 1) return 'rank-1'
  if (rank === 2) return 'rank-2'
  if (rank === 3) return 'rank-3'
  return ''
}

function getLogoPath(logo) {
  return `/images/teams/${logo || 'default-logo.png'}`
}
</script>

<style scoped>
.teams-page {
  padding: 40px 20px;
  background: var(--darker);
  min-height: calc(100vh - 70px);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  text-align: center;
  margin-bottom: 40px;
  font-size: 2.2rem;
  color: white;
  position: relative;
}

.page-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(to right, var(--primary), var(--secondary));
  border-radius: 2px;
}

.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.region-filter {
  width: 200px;
}

.compare-btn {
  background: linear-gradient(135deg, var(--primary), #8a2be2);
  border: none;
}

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 5px;
}

.team-name {
  font-weight: 600;
}

.team-region {
  font-size: 0.8rem;
  color: var(--gray);
}

.rank-badge {
  display: inline-block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border-radius: 50%;
  background: #4a5568;
  color: white;
  font-weight: bold;
}

.rank-1 {
  background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
}

.rank-2 {
  background: linear-gradient(135deg, #d7d7d7 0%, #a1a1a1 100%);
}

.rank-3 {
  background: linear-gradient(135deg, #cd7f32 0%, #a56a2b 100%);
}

.win-rate {
  display: flex;
  flex-direction: column;
}

.win-loss {
  font-size: 0.75rem;
  color: var(--gray);
}

.loading-placeholder, .error-message {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
  font-size: 1.2rem;
  color: var(--gray);
}

.loading-placeholder i {
  font-size: 1.5rem;
  margin-right: 10px;
  animation: rotating 2s linear infinite;
}

.error-message i {
  font-size: 1.5rem;
  margin-right: 10px;
  color: var(--secondary);
}

@keyframes rotating {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>