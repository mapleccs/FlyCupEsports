<template>
  <div class="schedule-table">
    <el-table
      :data="matches"
      style="width: 100%"
      :row-class-name="tableRowClassName"
      @row-click="handleRowClick"
    >
      <el-table-column prop="date" label="日期" width="120">
        <template #default="{ row }">
          <div class="match-date">
            <div class="date">{{ formatDate(row.date) }}</div>
            <div class="time">{{ row.time }}</div>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="比赛">
        <template #default="{ row }">
          <div class="match-teams">
            <div class="team">
              <img :src="row.teamA.logo" class="team-logo" />
              <span>{{ row.teamA.name }}</span>
            </div>
            <div class="vs">VS</div>
            <div class="team">
              <img :src="row.teamB.logo" class="team-logo" />
              <span>{{ row.teamB.name }}</span>
            </div>
          </div>
        </template>
      </el-table-column>

      <el-table-column prop="tournament.name" label="赛事" width="180" />

      <el-table-column label="状态" width="120" align="center">
        <template #default="{ row }">
          <el-tag
            :type="statusTagType(row.status)"
            effect="dark"
            class="status-tag"
          >
            {{ statusText(row.status) }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="操作" width="150" align="center">
        <template #default="{ row }">
          <el-button
            v-if="row.status === 'live'"
            type="danger"
            size="small"
            @click.stop="watchLive(row)"
            class="action-btn live-btn"
          >
            <i class="el-icon-video-play"></i> 直播
          </el-button>

          <el-button
            v-if="row.status === 'completed' && row.replayUrl"
            type="info"
            size="small"
            @click.stop="watchReplay(row)"
            class="action-btn replay-btn"
          >
            <i class="el-icon-video-pause"></i> 回放
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import dayjs from 'dayjs'

const props = defineProps({
  matches: Array
})

const emit = defineEmits(['match-selected', 'watch-live', 'watch-replay'])

const formatDate = (dateStr) => {
  return dayjs(dateStr).format('MM/DD')
}

const statusTagType = (status) => {
  switch(status) {
    case 'upcoming': return 'primary'
    case 'live': return 'danger'
    case 'completed': return 'success'
    default: return 'info'
  }
}

const statusText = (status) => {
  switch(status) {
    case 'upcoming': return '未开始'
    case 'live': return '直播中'
    case 'completed': return '已结束'
    default: return status
  }
}

const tableRowClassName = ({ row }) => {
  if (row.status === 'live') {
    return 'live-row'
  }
  return ''
}

const handleRowClick = (row) => {
  emit('match-selected', row)
}

const watchLive = (match) => {
  emit('watch-live', match)
}

const watchReplay = (match) => {
  emit('watch-replay', match)
}
</script>

<style scoped>
.schedule-table {
  background: rgba(15, 23, 42, 0.8);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 30px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

.match-date {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.date {
  font-weight: bold;
  font-size: 1rem;
}

.time {
  font-size: 0.85rem;
  color: #94a3b8;
}

.match-teams {
  display: flex;
  align-items: center;
  justify-content: center;
}

.team {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.team-logo {
  width: 48px;
  height: 48px;
  object-fit: contain;
  margin-bottom: 8px;
  transition: transform 0.3s ease;
}

.team:hover .team-logo {
    transform: scale(1.1);
}

.team span {
    font-weight: 600;
}

.vs {
  margin: 0 20px;
  color: #64748b;
  font-weight: bold;
  font-size: 1.2rem;
}

.status-tag {
  font-weight: bold;
  border: none;
}

/* Action Buttons */
.action-btn {
    border: none;
    font-weight: bold;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.live-btn {
    background: linear-gradient(45deg, #ef4444, #f87171);
}

.replay-btn {
    background: linear-gradient(45deg, #64748b, #94a3b8);
}


/* Table Styles */
:deep(.el-table) {
  --el-table-bg-color: transparent;
  --el-table-header-bg-color: rgba(30, 41, 59, 0.7);
  --el-table-tr-bg-color: rgba(30, 41, 59, 0.5);
  --el-table-row-hover-bg-color: rgba(56, 70, 100, 0.8);
  --el-table-border-color: rgba(255, 255, 255, 0.15);
  color: #f1f5f9;
  border-radius: 8px;
  overflow: hidden;
}

:deep(.el-table th) {
  color: #e2e8f0;
  font-weight: bold;
  font-size: 0.95rem;
  text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
  /* This is the key change for centering header text */
  text-align: center;
}

:deep(.el-table tr) {
  background-color: var(--el-table-tr-bg-color);
  transition: background-color 0.3s ease;
}

:deep(.el-table__body tr:hover > td) {
  background-color: var(--el-table-row-hover-bg-color) !important;
}

:deep(.live-row) {
  --el-table-tr-bg-color: rgba(239, 68, 68, 0.15);
  border-left: 4px solid #ef4444;
}

:deep(.live-row:hover > td) {
  background-color: rgba(239, 68, 68, 0.25) !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .schedule-table {
    padding: 16px;
  }
  .vs {
    margin: 0 10px;
    font-size: 1rem;
  }
  .team-logo {
      width: 40px;
      height: 40px;
  }
  .team span {
    font-size: 0.8rem;
  }
  :deep(.el-table th) {
    font-size: 0.85rem;
  }
}
</style>