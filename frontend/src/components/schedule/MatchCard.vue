<template>
  <div
    class="match-card"
    :class="{
      'upcoming': match.status === 'upcoming',
      'live': match.status === 'live',
      'completed': match.status === 'completed'
    }"
    @click="$emit('match-selected', match)"
  >
    <div class="match-status">
      <span v-if="match.status === 'upcoming'">即将开始</span>
      <span v-else-if="match.status === 'live'" class="live-indicator">
        <span class="pulse"></span> 直播中
      </span>
      <span v-else>已结束</span>
    </div>

    <div class="match-time">
      <i class="el-icon-time"></i>
      {{ match.date }} {{ match.time }}
    </div>

    <div class="teams">
      <div class="team">
        <img :src="match.teamA.logo" :alt="match.teamA.name" />
        <span>{{ match.teamA.name }}</span>
      </div>

      <div class="vs">
        <div>VS</div>
        <div class="score" v-if="match.status === 'completed'">
          {{ match.scoreA }} : {{ match.scoreB }}
        </div>
      </div>

      <div class="team">
        <img :src="match.teamB.logo" :alt="match.teamB.name" />
        <span>{{ match.teamB.name }}</span>
      </div>
    </div>

    <div class="match-tournament">
      <i class="el-icon-trophy"></i>
      {{ match.tournament.name }}
    </div>

    <div class="match-actions">
      <el-button
        v-if="match.status === 'live'"
        type="danger"
        size="small"
        @click.stop="watchLive(match)"
      >
        <i class="el-icon-video-play"></i> 观看直播
      </el-button>

      <el-button
        v-if="match.status === 'completed' && match.replayUrl"
        type="info"
        size="small"
        @click.stop="watchReplay(match)"
      >
        <i class="el-icon-video-pause"></i> 观看回放
      </el-button>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['match-selected', 'watch-live', 'watch-replay'])

const props = defineProps({
  match: {
    type: Object,
    required: true
  }
})

const watchLive = (match) => {
  emit('watch-live', match)
}

const watchReplay = (match) => {
  emit('watch-replay', match)
}
</script>

<style scoped>
.match-card {
  background: rgba(30, 41, 59, 0.8);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(93, 95, 239, 0.2);
  position: relative;
  overflow: hidden;
}

.match-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(93, 95, 239, 0.2);
  border-color: rgba(93, 95, 239, 0.5);
}

.match-card.live {
  border-left: 4px solid #ff4655;
}

.match-card.completed {
  border-left: 4px solid #10b981;
}

.match-card.upcoming {
  border-left: 4px solid #3b82f6;
}

.match-status {
  position: absolute;
  top: 0;
  right: 0;
  padding: 5px 15px;
  border-bottom-left-radius: 8px;
  font-size: 0.8rem;
  font-weight: bold;
}

.match-card.upcoming .match-status {
  background: rgba(59, 130, 246, 0.2);
  color: #3b82f6;
}

.match-card.live .match-status {
  background: rgba(255, 70, 85, 0.2);
  color: #ff4655;
}

.match-card.completed .match-status {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.live-indicator {
  display: flex;
  align-items: center;
}

.pulse {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ff4655;
  margin-right: 5px;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.4; }
  100% { opacity: 1; }
}

.match-time {
  color: #94a3b8;
  margin-bottom: 15px;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
}

.match-time i {
  margin-right: 5px;
}

.teams {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
}

.team {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.team img {
  width: 60px;
  height: 60px;
  object-fit: contain;
  margin-bottom: 10px;
}

.team span {
  font-weight: 600;
  font-size: 1.1rem;
}

.vs {
  padding: 0 15px;
  font-weight: bold;
  color: #94a3b8;
  text-align: center;
}

.score {
  font-size: 1.4rem;
  font-weight: bold;
  color: #fff;
  margin-top: 5px;
}

.match-tournament {
  background: rgba(15, 23, 42, 0.6);
  padding: 8px 15px;
  border-radius: 20px;
  color: #e2e8f0;
  display: inline-flex;
  align-items: center;
  font-size: 0.9rem;
  margin-top: 15px;
}

.match-tournament i {
  margin-right: 5px;
  color: #fbbf24;
}

.match-actions {
  margin-top: 15px;
  display: flex;
  justify-content: center;
}

@media (max-width: 768px) {
  .teams {
    flex-direction: column;
    gap: 15px;
  }

  .vs {
    padding: 10px 0;
  }
}
</style>