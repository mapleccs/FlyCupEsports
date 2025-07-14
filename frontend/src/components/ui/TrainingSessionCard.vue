<template>
  <div class="training-session-card">
    <div class="session-header">
      <div class="team-info">
        <img :src="getLogoPath(session.team.logo)" class="team-logo" />
        <div>
          <div class="team-name">{{ session.team.name }}</div>
          <div class="team-region">{{ session.team.region }}</div>
        </div>
      </div>
      <div class="session-status" :class="session.status">
        {{ getStatusText(session.status) }}
      </div>
    </div>

    <div class="session-content">
      <h3 class="session-title">{{ session.title }}</h3>

      <div class="session-meta">
        <div class="meta-item">
          <i class="el-icon-time"></i>
          <span>{{ formatDate(session.date) }} {{ session.time }}</span>
        </div>
        <div class="meta-item">
          <i class="el-icon-timer"></i>
          <span>约 {{ session.duration }} 小时</span>
        </div>
        <div class="meta-item">
          <i class="el-icon-s-flag"></i>
          <span>{{ session.mode }}</span>
        </div>
      </div>

      <div class="session-description">
        {{ session.description || '暂无详细说明' }}
      </div>
    </div>

    <div class="session-footer">
      <div class="applications-count" v-if="showApplications">
        <i class="el-icon-user"></i>
        {{ session.applications.length }} 个申请
      </div>

      <div class="session-actions">
        <el-button
          v-if="isMySessions && session.status === 'open'"
          size="small"
          @click.stop="$emit('edit-session', session)"
        >
          编辑
        </el-button>

        <el-button
          v-if="isMySessions && session.status === 'open'"
          size="small"
          type="danger"
          @click.stop="$emit('cancel-session', session)"
        >
          取消
        </el-button>

        <el-button
          v-if="isMySessions && session.applications.length > 0"
          size="small"
          type="primary"
          @click.stop="$emit('view-applications', session)"
        >
          查看申请
        </el-button>

        <el-button
          v-if="!isMySessions && session.status === 'open'"
          size="small"
          type="primary"
          @click.stop="$emit('apply-session', session)"
        >
          申请预约
        </el-button>

        <el-button
          v-if="showViewDetail"
          size="small"
          @click.stop="$emit('view-detail', session)"
        >
          查看详情
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  session: Object,
  isMySessions: Boolean,
  showStatus: Boolean,
  showApplications: Boolean,
  showViewDetail: {
    type: Boolean,
    default: true
  }
})

// 获取状态文本
function getStatusText(status) {
  const statusMap = {
    open: '开放预约',
    pending: '待处理',
    accepted: '已接受',
    rejected: '已拒绝',
    completed: '已完成',
    cancelled: '已取消'
  }
  return statusMap[status] || status
}

// 格式化日期
function formatDate(dateString) {
  const options = { month: 'short', day: 'numeric' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}

// 获取Logo路径
function getLogoPath(logo) {
  return `/images/teams/${logo || 'default-logo.png'}`
}
</script>

<style scoped>
.training-session-card {
  background: rgba(15, 23, 42, 0.6);
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid rgba(93, 95, 239, 0.2);
  transition: all 0.3s ease;
}

.training-session-card:hover {
  transform: translateY(-5px);
  border-color: var(--primary);
  box-shadow: 0 5px 15px rgba(93, 95, 239, 0.2);
}

.session-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 12px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 3px;
}

.team-name {
  font-weight: 600;
  font-size: 1.1rem;
}

.team-region {
  font-size: 0.8rem;
  color: var(--gray);
}

.session-status {
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: bold;
}

.session-status.open {
  background: rgba(76, 175, 80, 0.2);
  color: #4CAF50;
}

.session-status.pending {
  background: rgba(255, 152, 0, 0.2);
  color: #FF9800;
}

.session-status.accepted {
  background: rgba(33, 150, 243, 0.2);
  color: #2196F3;
}

.session-title {
  margin: 0 0 15px 0;
  font-size: 1.2rem;
  color: white;
}

.session-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 15px;
}

.meta-item {
  display: flex;
  align-items: center;
  color: var(--gray);
  font-size: 0.9rem;
}

.meta-item i {
  margin-right: 5px;
  color: var(--primary);
}

.session-description {
  color: var(--gray);
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 15px;
}

.session-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.applications-count {
  display: flex;
  align-items: center;
  color: var(--gray);
  font-size: 0.9rem;
}

.applications-count i {
  margin-right: 5px;
  color: var(--primary);
}

.session-actions {
  display: flex;
  gap: 10px;
}
</style>