<template>
  <section class="admin-section">
    <h2><i class="el-icon-s-tools"></i> 管理员面板</h2>
    <div class="admin-grid">
      <div class="admin-card" @click="$emit('navigate', 'users')">
        <i class="el-icon-user"></i><span>用户管理</span>
      </div>
      <div class="admin-card" @click="$emit('navigate', 'teams')">
        <i class="el-icon-s-flag"></i><span>战队管理</span>
      </div>
      <div class="admin-card" @click="$emit('navigate', 'events')">
        <i class="el-icon-trophy"></i><span>赛事管理</span>
      </div>
      <div class="admin-card" @click="$emit('navigate', 'settings')">
        <i class="el-icon-setting"></i><span>系统设置</span>
      </div>
    </div>
  </section>
</template>
<script setup>
defineEmits(['navigate']);
</script>
<style scoped>
/* 样式与原Profile.vue中一致 */
section { background: rgba(15, 23, 42, 0.7); border-radius: var(--border-radius); padding: 25px; border: 1px solid rgba(93, 95, 239, 0.2); }
section h2 { display: flex; align-items: center; gap: 10px; font-size: 1.4rem; margin-bottom: 25px; color: white; padding-bottom: 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.admin-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 20px; }
.admin-card { background: rgba(93, 95, 239, 0.1); border-radius: 8px; padding: 25px; text-align: center; cursor: pointer; transition: all 0.3s ease; }
.admin-card:hover { transform: translateY(-5px); background: rgba(93, 95, 239, 0.2); }
.admin-card i { font-size: 2.5rem; color: var(--primary); margin-bottom: 15px; display: block; }
.admin-card span { font-size: 1.1rem; }
</style>