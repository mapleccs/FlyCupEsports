<template>
  <div class="team-comparison">
    <div class="team-selectors">
      <div class="selector">
        <div class="selector-label">战队 1</div>
        <el-select
          :value="selectedTeam1"
          @change="handleTeam1Change"
          placeholder="选择战队"
        >
          <el-option
            v-for="team in teams"
            :key="team.id"
            :label="team.name"
            :value="team.id"
          >
            <div class="team-option">
              <img :src="getLogoPath(team.logo)" class="option-logo" />
              <span>{{ team.name }}</span>
            </div>
          </el-option>
        </el-select>
      </div>

      <div class="vs">VS</div>

      <div class="selector">
        <div class="selector-label">战队 2</div>
        <el-select
          :value="selectedTeam2"
          @change="handleTeam2Change"
          placeholder="选择战队"
        >
          <el-option
            v-for="team in teams"
            :key="team.id"
            :label="team.name"
            :value="team.id"
          >
            <div class="team-option">
              <img :src="getLogoPath(team.logo)" class="option-logo" />
              <span>{{ team.name }}</span>
            </div>
          </el-option>
        </el-select>
      </div>
    </div>

    <div v-if="team1 && team2" class="comparison-content">
      <div class="comparison-row header">
        <div class="metric">数据指标</div>
        <div class="team-value">{{ team1.abbreviation }}</div>
        <div class="comparison-chart"></div>
        <div class="team-value">{{ team2.abbreviation }}</div>
      </div>

      <div class="comparison-row">
        <div class="metric">胜率</div>
        <div class="team-value">{{ (team1.win_rate * 100).toFixed(1) }}%</div>
        <div class="comparison-chart">
          <div class="chart-bar">
            <div
              class="bar bar-1"
              :style="{ width: `${team1.win_rate * 50}%` }"
            ></div>
            <div
              class="bar bar-2"
              :style="{ width: `${team2.win_rate * 50}%` }"
            ></div>
          </div>
        </div>
        <div class="team-value">{{ (team2.win_rate * 100).toFixed(1) }}%</div>
      </div>

      <div class="comparison-row">
        <div class="metric">KDA</div>
        <div class="team-value">{{ team1.kda }}</div>
        <div class="comparison-chart">
          <div class="chart-bar">
            <div
              class="bar bar-1"
              :style="{ width: `${(team1.kda / maxKda) * 50}%` }"
            ></div>
            <div
              class="bar bar-2"
              :style="{ width: `${(team2.kda / maxKda) * 50}%` }"
            ></div>
          </div>
        </div>
        <div class="team-value">{{ team2.kda }}</div>
      </div>

      <div class="comparison-row">
        <div class="metric">场均金币</div>
        <div class="team-value">{{ team1.gold_per_min }}</div>
        <div class="comparison-chart">
          <div class="chart-bar">
            <div
              class="bar bar-1"
              :style="{ width: `${(team1.gold_per_min / maxGold) * 50}%` }"
            ></div>
            <div
              class="bar bar-2"
              :style="{ width: `${(team2.gold_per_min / maxGold) * 50}%` }"
            ></div>
          </div>
        </div>
        <div class="team-value">{{ team2.gold_per_min }}</div>
      </div>

      <div class="comparison-row">
        <div class="metric">场均推塔</div>
        <div class="team-value">{{ team1.tower_destroyed_per_game }}</div>
        <div class="comparison-chart">
          <div class="chart-bar">
            <div
              class="bar bar-1"
              :style="{ width: `${(team1.tower_destroyed_per_game / maxTowers) * 50}%` }"
            ></div>
            <div
              class="bar bar-2"
              :style="{ width: `${(team2.tower_destroyed_per_game / maxTowers) * 50}%` }"
            ></div>
          </div>
        </div>
        <div class="team-value">{{ team2.tower_destroyed_per_game }}</div>
      </div>

      <div class="comparison-row">
        <div class="metric">场均小龙</div>
        <div class="team-value">{{ team1.dragon_per_game }}</div>
        <div class="comparison-chart">
          <div class="chart-bar">
            <div
              class="bar bar-1"
              :style="{ width: `${(team1.dragon_per_game / maxDragons) * 50}%` }"
            ></div>
            <div
              class="bar bar-2"
              :style="{ width: `${(team2.dragon_per_game / maxDragons) * 50}%` }"
            ></div>
          </div>
        </div>
        <div class="team-value">{{ team2.dragon_per_game }}</div>
      </div>

      <div class="hero-comparison">
        <h3>常用英雄对比</h3>
        <div class="hero-charts">
          <div class="team-heroes">
            <h4>{{ team1.abbreviation }}</h4>
            <div v-for="hero in team1.top_heroes" :key="hero.name" class="hero-item">
              <div class="hero-name">{{ hero.name }}</div>
              <div class="hero-bar">
                <div class="bar-fill" :style="{ width: `${(hero.count / maxHeroCount1) * 100}%` }"></div>
              </div>
              <div class="hero-stats">{{ hero.count }}次 ({{ hero.win_rate }}%)</div>
            </div>
          </div>

          <div class="vs-hero">VS</div>

          <div class="team-heroes">
            <h4>{{ team2.abbreviation }}</h4>
            <div v-for="hero in team2.top_heroes" :key="hero.name" class="hero-item">
              <div class="hero-name">{{ hero.name }}</div>
              <div class="hero-bar">
                <div class="bar-fill" :style="{ width: `${(hero.count / maxHeroCount2) * 100}%` }"></div>
              </div>
              <div class="hero-stats">{{ hero.count }}次 ({{ hero.win_rate }}%)</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="no-selection">
      <i class="el-icon-info"></i>
      <p>请选择两个战队进行对比</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  teams: Array,
  selectedTeam1: Number,
  selectedTeam2: Number
})

const emit = defineEmits(['update:selectedTeam1', 'update:selectedTeam2'])

const team1 = computed(() => {
  return props.teams.find(t => t.id === props.selectedTeam1)
})

const team2 = computed(() => {
  return props.teams.find(t => t.id === props.selectedTeam2)
})

// 处理战队选择变化
function handleTeam1Change(value) {
  emit('update:selectedTeam1', value)
}

function handleTeam2Change(value) {
  emit('update:selectedTeam2', value)
}

// 计算最大值用于图表
const maxKda = computed(() => {
  return Math.max(team1.value?.kda || 0, team2.value?.kda || 0, 5)
})

const maxGold = computed(() => {
  return Math.max(team1.value?.gold_per_min || 0, team2.value?.gold_per_min || 0, 2000)
})

const maxTowers = computed(() => {
  return Math.max(team1.value?.tower_destroyed_per_game || 0, team2.value?.tower_destroyed_per_game || 0, 10)
})

const maxDragons = computed(() => {
  return Math.max(team1.value?.dragon_per_game || 0, team2.value?.dragon_per_game || 0, 5)
})

const maxHeroCount1 = computed(() => {
  if (!team1.value?.top_heroes) return 1
  return Math.max(...team1.value.top_heroes.map(h => h.count))
})

const maxHeroCount2 = computed(() => {
  if (!team2.value?.top_heroes) return 1
  return Math.max(...team2.value.top_heroes.map(h => h.count))
})

function getLogoPath(logo) {
  return `/images/teams/${logo || 'default-logo.png'}`
}
</script>

<style scoped>
.team-comparison {
  padding: 20px;
}

.team-selectors {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  margin-bottom: 40px;
}

.selector {
  width: 300px;
}

.selector-label {
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--gray);
}

.vs {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--secondary);
}

.team-option {
  display: flex;
  align-items: center;
}

.option-logo {
  width: 30px;
  height: 30px;
  margin-right: 10px;
  border-radius: 50%;
}

.comparison-content {
  background: rgba(15, 23, 42, 0.6);
  border-radius: 12px;
  padding: 20px;
  border: 1px solid rgba(93, 95, 239, 0.2);
}

.comparison-row {
  display: grid;
  grid-template-columns: 150px 100px 1fr 100px;
  gap: 15px;
  align-items: center;
  padding: 15px 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.comparison-row.header {
  font-weight: bold;
  color: var(--primary);
  border-bottom: 2px solid var(--primary);
}

.metric {
  font-weight: 500;
}

.team-value {
  text-align: center;
  font-weight: bold;
}

.comparison-chart {
  height: 30px;
  display: flex;
  align-items: center;
}

.chart-bar {
  display: flex;
  width: 100%;
  height: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  overflow: hidden;
}

.bar {
  height: 100%;
  transition: width 0.5s ease;
}

.bar-1 {
  background: linear-gradient(90deg, var(--primary), #6a5af9);
}

.bar-2 {
  background: linear-gradient(90deg, #ff4655, #ff6b6b);
}

.hero-comparison {
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.hero-comparison h3 {
  text-align: center;
  margin-bottom: 20px;
  color: white;
}

.hero-charts {
  display: flex;
  justify-content: space-between;
  gap: 40px;
}

.team-heroes {
  flex: 1;
}

.team-heroes h4 {
  text-align: center;
  margin-bottom: 15px;
  color: var(--primary);
}

.vs-hero {
  display: flex;
  align-items: center;
  font-weight: bold;
  color: var(--secondary);
}

.hero-item {
  margin-bottom: 15px;
}

.hero-name {
  font-weight: 500;
  margin-bottom: 5px;
}

.hero-bar {
  height: 10px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 5px;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary), #8a2be2);
  border-radius: 5px;
}

.hero-stats {
  font-size: 0.9rem;
  color: var(--gray);
  text-align: right;
}

.no-selection {
  text-align: center;
  padding: 40px;
  color: var(--gray);
  font-size: 1.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.no-selection i {
  font-size: 3rem;
  margin-bottom: 15px;
  color: var(--primary);
}
</style>