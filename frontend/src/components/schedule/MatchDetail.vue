<template>
  <div class="match-detail" v-if="match">
    <div class="match-header">
      <div class="tournament">
        <img :src="match.tournament.logo" class="tournament-logo" />
        <h3>{{ match.tournament.name }}</h3>
      </div>
      <el-tag :type="statusTagType" effect="dark" class="status-tag">
        {{ statusText }}
      </el-tag>
    </div>

    <div class="match-body">
      <div class="team team-a">
        <img :src="match.teamA.logo" class="team-logo" />
        <div class="team-name">{{ match.teamA.name }}</div>
        <div class="team-score" v-if="match.status === 'completed'">
          {{ match.scoreA }}
        </div>
      </div>

      <div class="match-info">
        <div class="match-date">
          <i class="el-icon-time"></i>
          {{ match.date }} {{ match.time }}
        </div>
        <div class="vs">VS</div>
        <div class="match-stage">{{ match.stage }}</div>
      </div>

      <div class="team team-b">
        <img :src="match.teamB.logo" class="team-logo" />
        <div class="team-name">{{ match.teamB.name }}</div>
        <div class="team-score" v-if="match.status === 'completed'">
          {{ match.scoreB }}
        </div>
      </div>
    </div>

    <div class="match-stats" v-if="match.status === 'completed'">
      <h4>比赛数据</h4>
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-value">{{ match.stats.duration }}</div>
          <div class="stat-label">比赛时长</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{{ match.stats.killsA }} - {{ match.stats.killsB }}</div>
          <div class="stat-label">总击杀</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{{ match.stats.towersA }} - {{ match.stats.towersB }}</div>
          <div class="stat-label">推塔数</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{{ match.stats.dragonsA }} - {{ match.stats.dragonsB }}</div>
          <div class="stat-label">小龙</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">{{ match.stats.baronsA }} - {{ match.stats.baronsB }}</div>
          <div class="stat-label">大龙</div>
        </div>
      </div>
    </div>

    <div class="match-actions">
      <el-button
        v-if="match.status === 'live' && match.liveUrl"
        type="danger"
        size="large"
        @click="$emit('watch-live', match)"
      >
        <i class="el-icon-video-play"></i> 观看直播
      </el-button>

      <el-button
        v-if="match.status === 'completed' && match.replayUrl"
        type="info"
        size="large"
        @click="$emit('watch-replay', match)"
      >
        <i class="el-icon-video-pause"></i> 观看回放
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  match: Object
})

const emit = defineEmits(['watch-live', 'watch-replay'])

const statusTagType = computed(() => {
  switch(props.match.status) {
    case 'upcoming': return 'primary'
    case 'live': return 'danger'
    case 'completed': return 'success'
    default: return 'info'
  }
})

const statusText = computed(() => {
  switch(props.match.status) {
    case 'upcoming': return '未开始'
    case 'live': return '直播中'
    case 'completed': return '已结束'
    default: return props.match.status
  }
})
</script>

<style scoped>
.match-detail {
  padding: 20px;
}

.match-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.tournament {
  display: flex;
  align-items: center;
}

.tournament-logo {
  width: 40px;
  height: 40px;
  margin-right: 15px;
  object-fit: contain;
}

.status-tag {
  font-size: 1rem;
  padding: 8px 15px;
}

.match-body {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.team {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.team-logo {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin-bottom: 15px;
}

.team-name {
  font-size: 1.4rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.team-score {
  font-size: 2.5rem;
  font-weight: bold;
  color: #5d5fef;
}

.match-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 20px;
}

.match-date {
  color: #94a3b8;
  margin-bottom: 15px;
}

.vs {
  font-size: 1.8rem;
  font-weight: bold;
  color: #ff4655;
  margin-bottom: 10px;
}

.match-stage {
  background: rgba(93, 95, 239, 0.2);
  color: #5d5fef;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
}

.match-stats {
  margin-bottom: 30px;
}

.match-stats h4 {
  color: #e2e8f0;
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 15px;
}

.stat-item {
  background: rgba(30, 41, 59, 0.8);
  border-radius: 8px;
  padding: 15px 10px;
  text-align: center;
}

.stat-value {
  font-size: 1.4rem;
  font-weight: bold;
  margin-bottom: 5px;
  color: #5d5fef;
}

.stat-label {
  font-size: 0.9rem;
  color: #94a3b8;
}

.match-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
}

@media (max-width: 768px) {
  .match-body {
    flex-direction: column;
    gap: 30px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .team-logo {
    width: 80px;
    height: 80px;
  }

  .team-name {
    font-size: 1.2rem;
  }
}
</style>