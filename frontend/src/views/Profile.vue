<template>
  <div class="profile-page">
    <div class="container">
      <UserProfileCard :user="user" :stats="userStats" />

      <div class="role-sections">
        <AdminPanel v-if="isAdmin" @navigate="navigateToAdminPage" />

        <CaptainPanel
          v-if="isCaptain"
          :team="userTeam"
          @edit-team="showEditTeamDialog"
          @invite-member="showInviteMemberDialog"
          @create-recruitment="showRecruitmentDialog"
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
import { ElMessage } from 'element-plus';

// 导入子组件
import UserProfileCard from '@/components/profile/UserProfileCard.vue';
import AdminPanel from '@/components/profile/AdminPanel.vue';
import CaptainPanel from '@/components/profile/CaptainPanel.vue';
import PlayerPanel from '@/components/profile/PlayerPanel.vue';
import AccountSettings from '@/components/profile/AccountSettings.vue';
import EditTeam from '@/components/team/EditTeam.vue';
import InviteMember from '@/components/team/InviteMember.vue';
import CreateRecruitment from '@/components/team/CreateRecruitment.vue';

const router = useRouter();

// --- 模拟数据 ---
// 实际应用中，这些数据应该通过API从后端获取
const user = ref({
  id: 1,
  username: '雷霆万钧',
  email: 'thunder@example.com',
  role: 'captain', // 可切换 'guest', 'player', 'captain', 'admin' 来测试不同视图
  avatar: null, // 可以是图片URL
});

const userStats = ref({
  gamesPlayed: 42,
  winRate: '68%',
  teamCount: 1,
});

const userTeam = ref({
  id: 101,
  name: '雷霆战队',
  logo: null,
  slogan: '我们的目标是星辰大海！',
  members: [
    { id: 1, username: '雷霆万钧', avatar: null, isCaptain: true },
    { id: 2, username: '风暴之眼', avatar: null, isCaptain: false },
    { id: 3, username: '疾风剑豪', avatar: null, isCaptain: false },
    { id: 4, username: '寒冰射手', avatar: null, isCaptain: false },
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
    team: '雷霆战队',
  },
]);

const userSettings = ref({
  username: '雷霆万钧',
  email: 'thunder@example.com',
  phone: '13800138000',
  gameId: 'ThunderKing',
  mainPosition: 'mid',
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
</style>