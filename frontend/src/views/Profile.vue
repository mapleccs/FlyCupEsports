<template>
  <div class="profile-page">
    <div class="container">
      <UserProfileCard :user="user" :stats="userStats" />

      <!-- 使用封装好的雷达图组件 -->
      <PlayerStatsRadarChart
        v-if="isPlayer || isCaptain"
        :radar-data="positionalRadarData"
      />

      <div class="role-sections">
        <AdminPanel v-if="isAdmin" @navigate="navigateToAdminPage" />
        <CaptainPanel
          v-if="isCaptain"
          :team="userTeam"
          @edit-team="showEditTeamDialog"
          @invite-member="showInviteMemberDialog"
          @create-recruitment="showRecruitmentDialog"
          @disband-team="handleDisbandTeam"
          @transfer-captaincy="handleTransferCaptaincy"
          @remove-member="handleRemoveMember"
        />
        <PlayerPanel v-if="isPlayer" :events="userEvents" @go-to-signup="goToSignup" />
        <AccountSettings :settings="userSettings" @save="saveSettings" />
      </div>

      <el-dialog v-model="editTeamVisible" title="编辑战队信息" width="600px">
        <EditTeam v-if="editTeamVisible" :initial-team-data="userTeam" @close="editTeamVisible = false" />
      </el-dialog>
      <el-dialog v-model="inviteMemberVisible" title="邀请新队员" width="600px">
        <InviteMember v-if="inviteMemberVisible" @close="inviteMemberVisible = false" />
      </el-dialog>
      <el-dialog v-model="createRecruitmentVisible" title="发布招募信息" width="600px">
        <CreateRecruitment v-if="createRecruitmentVisible" @close="createRecruitmentVisible = false" />
      </el-dialog>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { ElMessage, ElMessageBox } from 'element-plus';

// 导入子组件
import UserProfileCard from '@/components/profile/UserProfileCard.vue';
import AdminPanel from '@/components/profile/AdminPanel.vue';
import CaptainPanel from '@/components/profile/CaptainPanel.vue';
import PlayerPanel from '@/components/profile/PlayerPanel.vue';
import AccountSettings from '@/components/profile/AccountSettings.vue';
import EditTeam from '@/components/team/EditTeam.vue';
import InviteMember from '@/components/team/InviteMember.vue';
import CreateRecruitment from '@/components/team/CreateRecruitment.vue';
import PlayerStatsRadarChart from "@/components/profile/PlayerStatsRadarChart.vue";

const router = useRouter();

// --- 模拟数据 ---
// 实际应用中，这些数据应该通过API从后端获取
const user = ref({
  id: 1,
  username: '万钧',
  role: 'captain', // 可切换 'guest', 'Player', 'captain', 'admin' 来测试不同视图
  avatar: null, // 可以是图片URL
  position: 'MIDDLE', // 玩家位置
  rank: '钻石Ⅲ', // 玩家段位
});

const userStats = ref({
  gamesPlayed: 42,
  winRate: '68%',
  teamCount: 1,
  // 详细统计数据，用于雷达图
  "伤害占比": 32,
  "每死承伤": 1800,
  "承受伤害": 25000,
  "经济": 15000,
  "补刀": 210,
  "参与击杀": 15,
  "参团率": 75,
  "生存": 8.5,
  "伤害": 45000,
  "伤害转换率": 1.4,
  "分均插眼": 1.2,
  "视野分": 65
});

const userTeam = ref({
  id: 101,
  name: '雷霆战队',
  logo: null,
  slogan: '我们的目标是星辰大海！',
  members: [
    { id: 1, username: '万钧', avatar: null, isCaptain: true },
    { id: 2, username: '小紫', avatar: null, isCaptain: false },
    { id: 3, username: '千术', avatar: null, isCaptain: false },
    { id: 4, username: '绿野', avatar: null, isCaptain: false },
  ],
});

const userEvents = ref([
  {
    id: 201,
    name: '2025夏季冠军杯',
    date: '2025-07-15',
    status: 'upcoming',
    statusText: '即将开始',
    statusClass: 'status-upcoming',
    team: 'IG战队',
  },
]);

const userSettings = ref({
  username: '雷霆万钧',
  gameId: 'ThunderKing',
  mainPosition: 'mid',
});

// 雷达图数据
const positionStatsDictionary = {
    "BOTTOM": { labels: ["伤害", "生存", "参团率", "经济", "补刀", "视野分"], max: [50000, 10, 100, 20000, 300, 100]},
    "MIDDLE": { labels: ["伤害", "伤害转换率", "参团率", "经济", "生存", "视野分"], max: [60000, 2.0, 100, 20000, 10, 80]},
    "TOP":    { labels: ["承受伤害", "生存", "伤害", "经济", "补刀", "参团率"], max: [40000, 10, 35000, 18000, 300, 90]},
    "SUPPORT":{ labels: ["参团率", "视野分", "承受伤害", "经济", "生存", "分均插眼"], max: [100, 120, 30000, 12000, 10, 3.0]},
    "JUNGLE": { labels: ["参团率", "经济", "伤害", "承受伤害", "视野分", "参与击杀"], max: [100, 17000, 30000, 35000, 90, 25]},
};

const positionalRadarData = computed(() => {
  const position = user.value.position?.toUpperCase() || 'MIDDLE'; // 默认为中路
  const config = positionStatsDictionary[position] || positionStatsDictionary['MIDDLE'];

  const indicator = config.labels.map((label, index) => ({ name: label, max: config.max[index] }));
  const value = config.labels.map(label => userStats.value[label] || 0);

  return { indicator, value };
});

// --- 模拟数据结束 ---

// 角色计算属性
const isAdmin = computed(() => user.value.role === 'admin');
const isCaptain = computed(() => user.value.role === 'captain' || isAdmin.value);
const isPlayer = computed(() => user.value.role === 'player' || isCaptain.value);

// 弹窗状态管理
const editTeamVisible = ref(false);
const inviteMemberVisible = ref(false);
const createRecruitmentVisible = ref(false);

const showEditTeamDialog = () => (editTeamVisible.value = true);
const showInviteMemberDialog = () => (inviteMemberVisible.value = true);
const showRecruitmentDialog = () => (createRecruitmentVisible.value = true);

// 导航方法
const navigateToAdminPage = (path) => router.push(`/admin/${path}`);
const goToSignup = () => router.push('/signup');

// 处理解散战队
const handleDisbandTeam = () => {
  ElMessageBox.confirm(
    '此操作将永久解散您的战队，所有数据将无法恢复。是否确定要继续？',
    '警告：解散战队',
    {
      confirmButtonText: '确定解散',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(() => {
    // 在这里应调用后端的API来执行解散操作
    console.log('正在执行解散战队操作...');
    ElMessage.success('战队已成功解散 (模拟操作)');
  }).catch(() => {
    ElMessage.info('已取消解散操作');
  });
};

// 处理转让队长
const handleTransferCaptaincy = (member) => {
  ElMessageBox.confirm(
    `您确定要将队长职位转让给队员【${member.username}】吗？此操作不可撤销。`,
    '确认转让队长',
    {
      confirmButtonText: '确定转让',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(() => {
    // 在这里应调用后端的API来执行转让操作
    console.log(`正在将队长转让给 ${member.username}...`);
    ElMessage.success(`队长已成功转让给 ${member.username} (模拟操作)`);
  }).catch(() => {
    ElMessage.info('已取消转让操作');
  });
};

// 处理移除队员
const handleRemoveMember = (member) => {
  ElMessageBox.confirm(
    `您确定要从战队中移除队员【${member.username}】吗？`,
    '确认移除队员',
    {
      confirmButtonText: '确定移除',
      cancelButtonText: '取消',
      type: 'error',
      buttonSize: 'default'
    }
  ).then(() => {
    // 在这里应调用后端的API来执行移除操作
    console.log(`正在移除队员 ${member.username}...`);
    ElMessage.success(`队员 ${member.username} 已被移除 (模拟操作)`);
  }).catch(() => {
    ElMessage.info('已取消移除操作');
  });
};

// 设置保存逻辑
const saveSettings = (settings) => {
  // 此处应调用API将`settings`提交到后端
  console.log('Saving account settings:', settings);
  userSettings.value = { ...settings };
  ElMessage.success('账户设置已保存！');
};
</script>

<style scoped>
.profile-page {
  padding: 40px 20px;
  background: var(--darker);
  min-height: calc(100vh - 70px);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.role-sections {
  display: grid;
  grid-template-columns: 1fr;
  gap: 30px;
  margin-top: 30px;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .radar-chart-container {
    height: 300px;
  }

  .radar-legend {
    gap: 12px;
  }

  .legend-item {
    font-size: 0.85rem;
  }

  .section-title {
    font-size: 1.2rem;
  }
}

@media (max-width: 480px) {
  .player-radar-chart {
    padding: 15px;
  }

  .radar-chart-container {
    height: 250px;
  }

  .radar-legend {
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
}
</style>