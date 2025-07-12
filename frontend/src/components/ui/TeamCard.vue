<template>
  <div class="team-card" v-if="team">
    <div class="team-header">
      <img :src="getLogoPath(team.logo)" class="detail-logo" />
      <div class="team-stats">
        <div class="stat-item">
          <div class="stat-label">胜率</div>
          <div class="stat-value">{{ (team.win_rate * 100).toFixed(1) }}%</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">KDA</div>
          <div class="stat-value">{{ team.kda }}</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">场均金币</div>
          <div class="stat-value">{{ team.gold_per_min }}</div>
        </div>
        <div class="stat-item">
          <div class="stat-label">场均推塔</div>
          <div class="stat-value">{{ team.tower_destroyed_per_game }}</div>
        </div>
      </div>
    </div>

    <div class="section">
      <h3 class="section-title">常用英雄</h3>
      <div class="heroes-chart">
        <div v-for="hero in team.top_heroes" :key="hero.name" class="hero-item">
          <div class="hero-info">
            <div class="hero-name">{{ hero.name }}</div>
            <div class="hero-stats">
              <span>使用: {{ hero.count }}次</span>
              <span>胜率: {{ hero.win_rate }}%</span>
            </div>
          </div>
          <div class="hero-bar">
            <div
              class="bar-fill"
              :style="{ width: `${(hero.count / maxHeroCount) * 100}%` }"
            ></div>
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <h3 class="section-title">近期比赛</h3>
      <div class="recent-matches">
        <div
          v-for="(match, index) in team.recent_matches"
          :key="index"
          class="match-item"
        >
          <div class="match-date">{{ match.date }}</div>
          <div class="match-opponent">对阵 {{ match.opponent }}</div>
          <div :class="['match-result', match.result]">
            {{ match.result === 'win' ? '胜' : '负' }}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="no-team-data">
    <i class="el-icon-warning"></i>
    <p>无法加载战队数据</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  team: Object
})

const maxHeroCount = computed(() => {
  if (!props.team?.top_heroes) return 1
  return Math.max(...props.team.top_heroes.map(h => h.count))
})

function getLogoPath(logo) {
  return `/images/teams/${logo || 'default-logo.png'}`
}
</script>

<style scoped>
.team-card {
  background: rgba(15, 23, 42, 0.8);
  border-radius: 12px;
  padding: 25px;
  border: 1px solid rgba(93, 95, 239, 0.2);
}

.team-header {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
}

.detail-logo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-right: 30px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 10px;
  border: 2px solid var(--primary);
}

.team-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  flex: 1;
}

.stat-item {
  background: rgba(93, 95, 239, 0.1);
  border-radius: 8px;
  padding: 15px;
  text-align: center;
}

.stat-label {
  font-size: 0.9rem;
  color: var(--gray);
  margin-bottom: 5px;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
}

.section {
  margin-bottom: 30px;
}

.section-title {
  position: relative;
  padding-bottom: 10px;
  margin-bottom: 20px;
  color: white;
  font-size: 1.4rem;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 3px;
  background: linear-gradient(to right, var(--primary), var(--secondary));
  border-radius: 2px;
}

.heroes-chart {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  padding: 15px;
}

.hero-item {
  margin-bottom: 15px;
}

.hero-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.hero-name {
  font-weight: 600;
}

.hero-stats {
  display: flex;
  gap: 15px;
  font-size: 0.9rem;
  color: var(--gray);
}

.hero-bar {
  height: 10px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary), #ff4655);
  border-radius: 5px;
}

.recent-matches {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 15px;
}

.match-item {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.match-date {
  color: var(--gray);
  font-size: 0.9rem;
}

.match-opponent {
  font-weight: 500;
}

.match-result {
  padding: 3px 10px;
  border-radius: 15px;
  font-size: 0.9rem;
  font-weight: bold;
}

.match-result.win {
  background: rgba(76, 175, 80, 0.2);
  color: #4CAF50;
}

.match-result.loss {
  background: rgba(244, 67, 54, 0.2);
  color: #F44336;
}

.no-team-data {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  color: var(--gray);
  font-size: 1.2rem;
}

.no-team-data i {
  font-size: 3rem;
  margin-bottom: 20px;
  color: var(--secondary);
}
</style>