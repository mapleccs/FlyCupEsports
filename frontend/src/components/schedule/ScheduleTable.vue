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

      <el-table-column label="状态" width="120">
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

      <el-table-column label="操作" width="150">
        <template #default="{ row }">
          <el-button
            v-if="row.status === 'live'"
            type="danger"
            size="small"
            @click.stop="watchLive(row)"
          >
            <i class="el-icon-video-play"></i> 直播
          </el-button>

          <el-button
            v-if="row.status === 'completed' && row.replayUrl"
            type="info"
            size="small"
            @click.stop="watchReplay(row)"
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
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 30px;
}

.match-date {
  display: flex;
  flex-direction: column;
}

.date {
  font-weight: bold;
}

.time {
  font-size: 0.8rem;
  color: #94a3b8;
}

.match-teams {
  display: flex;
  align-items: center;
}

.team {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.team-logo {
  width: 40px;
  height: 40px;
  object-fit: contain;
  margin-bottom: 5px;
}

.vs {
  margin: 0 15px;
  color: #94a3b8;
  font-weight: bold;
}

.status-tag {
  font-weight: bold;
}

/* 表格行样式 */
:deep(.el-table) {
  --el-table-header-bg-color: rgba(30, 41, 59, 0.8);
  --el-table-tr-bg-color: rgba(15, 23, 42, 0.5);
  --el-table-row-hover-bg-color: rgba(56, 70, 100, 0.7);
  --el-table-border-color: rgba(255, 255, 255, 0.05);
  color: #e2e8f0;
}

:deep(.el-table th) {
  color: #cbd5e1;
  font-weight: bold;
}

:deep(.el-table tr) {
  background-color: var(--el-table-tr-bg-color);
}

:deep(.el-table__body tr:hover>td) {
  background-color: var(--el-table-row-hover-bg-color) !important;
}

:deep(.live-row) {
  --el-table-tr-bg-color: rgba(255, 70, 85, 0.1);
}

:deep(.live-row:hover) {
  background-color: rgba(255, 70, 85, 0.2) !important;
}

@media (max-width: 768px) {
  .vs {
    margin: 0 5px;
  }

  .team span {
    font-size: 0.8rem;
  }
}
</style>