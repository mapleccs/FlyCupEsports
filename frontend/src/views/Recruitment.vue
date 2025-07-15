<template>
  <div class="recruitment-page">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">电竞招募中心</h1>
        <p class="page-subtitle">寻找你的理想战队，或为你的战队招募精英</p>
      </div>

      <!-- 选项卡切换 -->
      <el-tabs v-model="activeTab" class="recruitment-tabs">
        <el-tab-pane label="战队招募" name="team">
          <TeamRecruitment />
        </el-tab-pane>

        <el-tab-pane label="选手求职" name="player">
          <PlayerRecruitment />
        </el-tab-pane>
      </el-tabs>

      <div class="create-post">
        <el-button
          type="primary"
          icon="el-icon-edit"
          @click="showCreateDialog"
          class="create-button"
          round
        >
          发布{{ activeTab === 'team' ? '招募' : '求职' }}信息
        </el-button>
      </div>

      <!-- 发布对话框 -->
      <RecruitmentDialog
        :visible="createDialogVisible"
        :type="activeTab"
        @close="closeDialog"
        @publish="handleNewPost"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRecruitmentStore } from '@/stores/recruitmentStore';
import TeamRecruitment from '@/components/recruitment/TeamRecruitment.vue';
import PlayerRecruitment from '@/components/recruitment/PlayerRecruitment.vue';
import RecruitmentDialog from '@/components/recruitment/RecruitmentDialog.vue';

const activeTab = ref('team');
const createDialogVisible = ref(false);
const recruitmentStore = useRecruitmentStore();

// 显示创建对话框
const showCreateDialog = () => {
  createDialogVisible.value = true;
};

// 关闭对话框
const closeDialog = () => {
  createDialogVisible.value = false;
};

// 处理新发布的招募信息
const handleNewPost = (newPost) => {
  if (activeTab.value === 'team') {
    recruitmentStore.addTeamPost(newPost);
  } else {
    recruitmentStore.addPlayerPost(newPost);
  }
  closeDialog();
};
</script>

<style scoped lang="scss">
.recruitment-page {
  padding: 30px 20px;
  background: linear-gradient(to bottom, #0f172a, #1e293b);
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 30px;
  padding: 15px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 10px;
  border: 1px solid rgba(93, 95, 239, 0.2);

  .page-title {
    font-size: 2.2rem;
    color: white;
    margin-bottom: 8px;
    background: linear-gradient(to right, #5d5fef, #ff4655);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
  }

  .page-subtitle {
    color: #94a3b8;
    font-size: 1rem;
  }
}

.recruitment-tabs {
  background: rgba(15, 23, 42, 0.7);
  border-radius: 10px;
  padding: 15px;
  border: 1px solid rgba(93, 95, 239, 0.2);

  :deep(.el-tabs__nav-wrap) {
    padding: 0 15px;
  }

  :deep(.el-tabs__item) {
    color: #94a3b8;
    font-size: 1rem;
    font-weight: 500;
    padding: 0 15px;
    height: 40px;

    &.is-active {
      color: #5d5fef;
      font-weight: 600;
    }
  }

  :deep(.el-tabs__active-bar) {
    background-color: #5d5fef;
    height: 3px;
  }
}

.create-post {
  margin-top: 30px;
  text-align: center;

  .create-button {
    padding: 12px 30px;
    font-size: 1rem;
    font-weight: 600;
    background: linear-gradient(135deg, #5d5fef, #8b5cf6);
    border: none;
    transition: all 0.3s ease;

    &:hover {
      transform: scale(1.05);
      box-shadow: 0 5px 15px rgba(93, 95, 239, 0.4);
    }
  }
}

/* 响应式调整 */
@media (max-width: 768px) {
  .create-button {
    width: 100%;
  }
}
</style>