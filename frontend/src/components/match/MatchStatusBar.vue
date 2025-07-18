<template>
  <div class="status-bar" :class="statusClass">
    <div class="status-content">
      <span class="status-text">{{ statusText }}</span>

      <template v-if="phase !== 'checkin'">
        <span class="divider">|</span>
        <span class="phase-text">当前阶段: {{ phaseText }}</span>
      </template>

      <template v-if="currentTeam">
        <span class="divider">|</span>
        <span class="turn-text">轮到: {{ currentTeam.name }}</span>
      </template>
    </div>

    <div class="progress-bar" v-if="phase !== 'completed'">
      <div class="progress-fill" :style="{ width: progressWidth }"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  status: String,
  phase: String,
  currentTeam: Object
})

const statusClass = computed(() => {
  return {
    'checkin': props.phase === 'checkin',
    'banning': props.phase === 'banning',
    'picking': props.phase === 'picking',
    'completed': props.phase === 'completed'
  }
})

const statusText = computed(() => {
  switch (props.phase) {
    case 'checkin': return props.status
    case 'banning': return '禁用阶段'
    case 'picking': return '选择阶段'
    case 'completed': return 'BP已完成'
    default: return props.status
  }
})

const phaseText = computed(() => {
  switch (props.phase) {
    case 'banning': return '禁用英雄'
    case 'picking': return '选择英雄'
    default: return ''
  }
})

const progressWidth = computed(() => {
  switch (props.phase) {
    case 'banning': return '30%'
    case 'picking': return '70%'
    default: return '0%'
  }
})
</script>

<style scoped>
.status-bar {
  position: relative;
  padding: 12px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  font-weight: 600;
  overflow: hidden;
  transition: all 0.3s ease;
}

.status-content {
  display: flex;
  align-items: center;
  gap: 15px;
  position: relative;
  z-index: 2;
}

.divider {
  opacity: 0.6;
}

.status-bar.checkin {
  background: rgba(94, 114, 228, 0.3);
  color: #5d72e4;
}

.status-bar.banning {
  background: rgba(255, 152, 0, 0.3);
  color: #FF9800;
}

.status-bar.picking {
  background: rgba(76, 175, 80, 0.3);
  color: #4CAF50;
}

.status-bar.completed {
  background: rgba(156, 39, 176, 0.3);
  color: #9C27B0;
}

.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 4px;
  width: 100%;
  background: rgba(255, 255, 255, 0.1);
}

.progress-fill {
  height: 100%;
  background: currentColor;
  transition: width 0.5s ease;
}
</style>