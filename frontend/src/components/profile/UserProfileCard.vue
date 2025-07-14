<template>
  <div class="user-card">
    <div class="avatar-container">
      <img :src="user.avatar || '/images/teams/default-logo.png'" class="avatar" alt="用户头像">
      <div class="role-badge" :class="userRoleClass">{{ userRoleText }}</div>
    </div>
    <div class="user-info">
      <h1>{{ user.username }}</h1>
      <p v-if="user.email" class="email">{{ user.email }}</p>
      <div class="stats">
        <div class="stat-item">
          <span class="stat-value">{{ stats.gamesPlayed || 0 }}</span>
          <span class="stat-label">参赛场次</span>
        </div>
        <div class="stat-item">
          <span class="stat-value">{{ stats.winRate || '0%' }}</span>
          <span class="stat-label">胜率</span>
        </div>
        <div class="stat-item">
          <span class="stat-value">{{ stats.teamCount || 0 }}</span>
          <span class="stat-label">所属战队</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { computed } from 'vue';
const props = defineProps({ user: Object, stats: Object });
const userRoleText = computed(() => {
  switch(props.user.role) {
    case 'guest': return '游客';
    case 'player': return '选手';
    case 'captain': return '队长';
    case 'admin': return '管理员';
    default: return '未知';
  }
});
const userRoleClass = computed(() => 'role-' + props.user.role);
</script>
<style scoped>
/* 样式与原Profile.vue中一致 */
.user-card {
  display: flex;
  background: rgba(15, 23, 42, 0.7);
  border-radius: var(--border-radius);
  padding: 30px;
  border: 1px solid rgba(93, 95, 239, 0.2);
}
.avatar-container { position: relative; margin-right: 30px; }
.avatar { width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--primary); background-color: #1e293b; }
.role-badge { position: absolute; bottom: 0; right: 0; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; }
.role-guest { background: var(--gray); }
.role-player { background: var(--primary); }
.role-captain { background: linear-gradient(135deg, var(--primary), #ff6b6b); }
.role-admin { background: linear-gradient(135deg, var(--primary), #f9c74f); }
.user-info h1 { font-size: 2rem; margin-bottom: 10px; color: white; }
.email { color: var(--gray); margin-bottom: 20px; }
.stats { display: flex; gap: 30px; }
.stat-item { text-align: center; }
.stat-value { display: block; font-size: 1.8rem; font-weight: bold; color: var(--primary); }
.stat-label { color: var(--gray); font-size: 0.95rem; }
</style>