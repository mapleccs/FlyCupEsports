<template>
  <div class="training-session-list">
    <div v-if="sessions.length === 0" class="empty-list">
      <i class="el-icon-folder-opened"></i>
      <p>{{ emptyMessage }}</p>
    </div>

    <div v-else>
      <TrainingSessionCard
        v-for="session in sessions"
        :key="session.id"
        :session="session"
        :is-my-sessions="isMySessions"
        :show-status="showStatus"
        :show-applications="isMySessions"
        @edit-session="$emit('edit-session', session)"
        @cancel-session="$emit('cancel-session', session)"
        @view-applications="$emit('view-applications', session)"
        @apply-session="$emit('apply-session', session)"
        @view-detail="$emit('view-detail', session)"
      />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import TrainingSessionCard from './TrainingSessionCard.vue'

const props = defineProps({
  sessions: Array,
  isMySessions: Boolean,
  showStatus: Boolean
})

// 空列表消息
const emptyMessage = computed(() => {
  if (props.isMySessions) {
    return '您还没有发布任何训练赛预约'
  } else {
    return '当前没有可用的训练赛预约'
  }
})
</script>

<style scoped>
.training-session-list {
  margin-top: 20px;
}

.empty-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 200px;
  color: var(--gray);
  font-size: 1.1rem;
}

.empty-list i {
  font-size: 3rem;
  margin-bottom: 15px;
  color: var(--primary);
}
</style>