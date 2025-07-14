<template>
  <section class="player-section">
    <h2><i class="el-icon-user"></i> 我的赛事</h2>
    <div class="events-container">
      <div v-if="!events || events.length === 0" class="no-events">
        <i class="el-icon-info"></i>
        <p>您尚未报名任何赛事</p>
        <el-button type="primary" @click="$emit('goToSignup')">立即报名</el-button>
      </div>
      <div v-else class="events-list">
        <div v-for="event in events" :key="event.id" class="event-card">
          <div class="event-badge" :class="event.statusClass">{{ event.statusText }}</div>
          <div class="event-content">
            <h3>{{ event.name }}</h3>
            <div class="event-meta"><i class="el-icon-time"></i><span>{{ event.date }}</span></div>
            <div class="event-team"><span>所属战队:</span><strong>{{ event.team || '个人参赛' }}</strong></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
defineProps({ events: Array });
defineEmits(['goToSignup']);
</script>
<style scoped>
/* 样式与原Profile.vue中一致 */
section { background: rgba(15, 23, 42, 0.7); border-radius: var(--border-radius); padding: 25px; border: 1px solid rgba(93, 95, 239, 0.2); }
section h2 { display: flex; align-items: center; gap: 10px; font-size: 1.4rem; margin-bottom: 25px; color: white; padding-bottom: 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.no-events { text-align: center; padding: 40px 0; }
.no-events i { font-size: 3rem; color: var(--gray); margin-bottom: 15px; }
.no-events p { color: var(--gray); margin-bottom: 20px; }
.events-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
.event-card { position: relative; background: rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 20px; }
.event-badge { position: absolute; top: 15px; right: 15px; padding: 3px 10px; border-radius: 4px; font-size: 0.8rem; }
.status-upcoming { background: var(--primary); }
.event-content h3 { font-size: 1.2rem; margin-bottom: 10px; }
.event-meta { display: flex; align-items: center; gap: 8px; color: var(--gray); margin-bottom: 10px; }
.event-team { color: var(--gray); }
</style>