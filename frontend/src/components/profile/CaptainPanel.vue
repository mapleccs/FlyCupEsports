<template>
  <section class="captain-section">
    <h2><i class="el-icon-s-flag"></i> 战队管理</h2>
    <div class="team-management">
      <div class="team-header">
        <h3>{{ team.name }}</h3>
        <div class="team-actions">
          <el-button type="primary" @click="$emit('editTeam')">编辑战队</el-button>
          <el-button type="success" @click="$emit('inviteMember')">邀请队员</el-button>
          <el-button type="warning" @click="$emit('createRecruitment')">发布招募</el-button>
        </div>
      </div>
      <div class="team-members">
        <h4>队员列表</h4>
        <div class="members-grid">
          <div v-for="member in team.members" :key="member.id" class="member-card">
            <div class="member-info">
              <span class="member-name">{{ member.username }}</span>
              <span class="member-role">{{ member.isCaptain ? '队长' : '队员' }}</span>
            </div>
            <div class="member-actions" v-if="!member.isCaptain">
              <el-button size="small" @click="removeMember(member)">移除</el-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { ElMessage } from 'element-plus';
defineProps({ team: Object });
defineEmits(['editTeam', 'inviteMember', 'createRecruitment']);
const removeMember = (member) => { ElMessage.warning(`移除队员: ${member.username} (模拟操作)`); };
</script>
<style scoped>
/* 样式与原Profile.vue中一致 */
section { background: rgba(15, 23, 42, 0.7); border-radius: var(--border-radius); padding: 25px; border: 1px solid rgba(93, 95, 239, 0.2); }
section h2 { display: flex; align-items: center; gap: 10px; font-size: 1.4rem; margin-bottom: 25px; color: white; padding-bottom: 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.team-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.team-header h3 { font-size: 1.5rem; color: white; }
.team-members h4 { font-size: 1.2rem; margin-bottom: 15px; color: var(--gray); }
.members-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; }
.member-card { display: flex; align-items: center; padding: 15px; background: rgba(255, 255, 255, 0.05); border-radius: 8px; }
.member-info { flex-grow: 1; }
.member-name { display: block; font-weight: 500; }
.member-role { font-size: 0.85rem; color: var(--gray); }
</style>