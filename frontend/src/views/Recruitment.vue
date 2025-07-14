<template>
  <div class="recruitment-page">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">电竞招募中心</h1>
        <p class="page-subtitle">寻找你的理想战队，或为你的战队招募精英</p>
      </div>

      <el-tabs v-model="activeTab" class="recruitment-tabs">
        <el-tab-pane label="战队招募" name="team">
          <div class="filters">
            <el-select v-model="teamFilter.position" placeholder="筛选位置" clearable>
              <el-option v-for="pos in positions" :key="pos.value" :label="pos.label" :value="pos.value"></el-option>
            </el-select>
            <el-input v-model="teamFilter.keyword" placeholder="搜索关键词..." clearable suffix-icon="el-icon-search"></el-input>
          </div>

          <div v-if="filteredTeamPosts && filteredTeamPosts.length > 0" class="recruitment-list">
            <div v-for="post in filteredTeamPosts" :key="post.id" class="post-card">
              <div class="card-header">
                <div class="team-logo-wrapper">
                  <img :src="post.teamLogo || '/images/teams/default-logo.png'" class="team-logo" />
                </div>
                <div class="team-info">
                  <h3>{{ post.title }}</h3>
                  <div class="meta-info">
                    <span class="team-name">{{ post.teamName }}</span>
                    <el-tag effect="dark" size="mini" :type="post.rankType">{{ post.rank }}</el-tag>
                    <el-tag size="mini" type="info">{{ post.server }}</el-tag>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <div class="positions">
                  <strong>需要位置:</strong>
                  <el-tag
                    v-for="pos in post.positions"
                    :key="pos"
                    class="pos-tag"
                    size="small"
                    :type="positionTypes[pos]"
                  >
                    {{ positionNames[pos] }}
                  </el-tag>
                </div>
                <p class="description">{{ post.description }}</p>
              </div>
              <div class="card-footer">
                <span class="post-time">发布于: {{ formatTime(post.createdAt) }}</span>
                <el-button type="primary" size="small" @click="apply(post)" plain round>
                  申请加入
                </el-button>
              </div>
            </div>
          </div>
          <div v-else class="no-data">
            <el-empty description="暂无符合条件的招募信息" />
          </div>
        </el-tab-pane>

        <el-tab-pane label="选手求职" name="player">
          <div class="filters">
            <el-select v-model="playerFilter.position" placeholder="筛选位置" clearable>
              <el-option v-for="pos in positions" :key="pos.value" :label="pos.label" :value="pos.value"></el-option>
            </el-select>
            <el-select v-model="playerFilter.rank" placeholder="段位要求" clearable>
              <el-option v-for="rank in ranks" :key="rank.value" :label="rank.label" :value="rank.value"></el-option>
            </el-select>
            <el-input v-model="playerFilter.keyword" placeholder="搜索关键词..." clearable suffix-icon="el-icon-search"></el-input>
          </div>

          <div v-if="filteredPlayerPosts && filteredPlayerPosts.length > 0" class="recruitment-list">
            <div v-for="post in filteredPlayerPosts" :key="post.id" class="post-card">
              <div class="card-header">
                <div class="player-avatar-wrapper">
                  <img :src="post.avatar || '/images/users/default-avatar.png'" class="player-avatar" />
                </div>
                <div class="player-info">
                  <h3>{{ post.title }}</h3>
                  <div class="meta-info">
                    <span class="player-name">{{ post.playerName }}</span>
                    <el-tag effect="dark" size="mini" :type="post.rankType">{{ post.rank }}</el-tag>
                    <el-tag size="mini" type="info">{{ post.server }}</el-tag>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <div class="positions">
                  <strong>擅长位置:</strong>
                  <el-tag
                    v-for="pos in post.positions"
                    :key="pos"
                    class="pos-tag"
                    size="small"
                    :type="positionTypes[pos]"
                  >
                    {{ positionNames[pos] }}
                  </el-tag>
                </div>
                <p class="description">{{ post.description }}</p>
              </div>
              <div class="card-footer">
                <span class="post-time">发布于: {{ formatTime(post.createdAt) }}</span>
                <el-button type="success" size="small" @click="contactPlayer(post)" plain round>
                  联系选手
                </el-button>
              </div>
            </div>
          </div>
          <div v-else class="no-data">
            <el-empty description="暂无符合条件的求职信息" />
          </div>
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

      <el-dialog
        v-model="createDialogVisible"
        :title="'发布' + (createDialogType === 'team' ? '战队招募' : '选手求职')"
        width="600px"
        :before-close="() => createDialogVisible = false"
      >
        <CreateRecruitment
            v-if="createDialogType === 'team'"
            @submit="handleNewPost"
        />
        <CreatePlayerPost
            v-if="createDialogType === 'player'"
            @submit="handleNewPost"
        />
      </el-dialog>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { ElMessage, ElDialog } from 'element-plus';
import CreateRecruitment from '@/components/team/CreateRecruitment.vue';
import CreatePlayerPost from '@/components/recruitment/CreatePlayerPost.vue'; // <-- 引入新组件

const activeTab = ref('team');

// 位置选项
const positions = ref([
  { label: '上单', value: 'Top' },
  { label: '打野', value: 'Jungle' },
  { label: '中单', value: 'Mid' },
  { label: 'ADC', value: 'ADC' },
  { label: '辅助', value: 'Support' }
]);

// 段位选项
const ranks = ref([
  { label: '黑铁', value: 'Iron' },
  { label: '青铜', value: 'Bronze' },
  { label: '白银', value: 'Silver' },
  { label: '黄金', value: 'Gold' },
  { label: '铂金', value: 'Platinum' },
  { label: '翡翠', value: 'Emerald' },
  { label: '钻石', value: 'Diamond' },
  { label: '大师', value: 'Master' },
  { label: '宗师', value: 'Grandmaster' },
  { label: '王者', value: 'Challenger' }
]);

// 位置类型映射
const positionTypes = ref({
  Top: 'success',
  Jungle: 'warning',
  Mid: 'danger',
  ADC: 'primary',
  Support: 'info'
});

// 位置名称映射
const positionNames = ref({
  Top: '上单',
  Jungle: '打野',
  Mid: '中单',
  ADC: 'ADC',
  Support: '辅助'
});

// 战队招募数据
const teamPosts = ref([]);
const teamFilter = ref({
  position: '',
  keyword: ''
});

// 选手求职数据
const playerPosts = ref([]);
const playerFilter = ref({
  position: '',
  rank: '',
  keyword: ''
});

// 创建对话框
const createDialogVisible = ref(false);
const createDialogType = ref('team');

// 模拟从API获取数据
onMounted(() => {
  // 战队招募数据
  teamPosts.value = [
    {
      id: 1,
      title: '钻石车队招募强力打野',
      teamName: '雷霆战队',
      teamLogo: null,
      positions: ['Jungle'],
      description: '要求钻石以上，心态好，能沟通，晚上稳定在线。每周训练赛3次，目标是城市赛冠军。',
      createdAt: new Date(Date.now() - 2 * 3600 * 1000),
      rank: '钻石',
      rankType: 'info',
      server: '艾欧尼亚'
    },
    {
      id: 2,
      title: '寻找默契辅助',
      teamName: '风暴之眼',
      teamLogo: null,
      positions: ['Support'],
      description: 'ADC寻找一个有缘的辅助，一起上分。要求不压力队友，会做视野，熟悉软辅硬辅。',
      createdAt: new Date(Date.now() - 5 * 3600 * 1000),
      rank: '铂金',
      rankType: '',
      server: '黑色玫瑰'
    },
    {
      id: 3,
      title: '战队招新，各位置都要',
      teamName: '不屈之师',
      teamLogo: null,
      positions: ['Top', 'Jungle', 'Mid', 'ADC', 'Support'],
      description: '新成立战队，欢迎各路好手加入，一起从零开始，目标是冠军！提供专业教练指导。',
      createdAt: new Date(Date.now() - 24 * 3600 * 1000),
      rank: '黄金+',
      rankType: 'warning',
      server: '比尔吉沃特'
    }
  ];

  // 选手求职数据
  playerPosts.value = [
    {
      id: 101,
      title: '王者中单寻求职业队',
      playerName: '风暴法神',
      avatar: null,
      positions: ['Mid'],
      description: '王者800点中单，擅长刺客和法师，有比赛经验。寻求半职业或职业队伍，可参加线下赛。',
      createdAt: new Date(Date.now() - 3 * 3600 * 1000),
      rank: '王者',
      rankType: 'danger',
      server: '峡谷之巅'
    },
    {
      id: 102,
      title: '黄金段位上单求职',
      playerName: '不屈战神',
      avatar: null,
      positions: ['Top'],
      description: '黄金段位上单，擅长坦克和战士英雄。时间稳定，学习能力强，寻求氛围好的车队一起上分。',
      createdAt: new Date(Date.now() - 8 * 3600 * 1000),
      rank: '黄金',
      rankType: 'warning',
      server: '诺克萨斯'
    },
    {
      id: 103,
      title: '钻石ADC找固定队',
      playerName: '寒冰射手',
      avatar: null,
      positions: ['ADC'],
      description: '钻石段位ADC，主玩霞、卡莎、EZ。寻求有配合的辅助和稳定车队，目标上大师。',
      createdAt: new Date(Date.now() - 12 * 3600 * 1000),
      rank: '钻石',
      rankType: 'info',
      server: '德玛西亚'
    }
  ];
});

// 格式化时间
const formatTime = (date) => {
  const now = new Date();
  const diff = Math.floor((now - date) / 1000);

  if (diff < 60) return '刚刚';
  if (diff < 3600) return `${Math.floor(diff / 60)}分钟前`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}小时前`;

  return date.toLocaleDateString();
};

// 战队招募过滤
const filteredTeamPosts = computed(() => {
  return teamPosts.value.filter(post => {
    const positionMatch = teamFilter.value.position
      ? post.positions.includes(teamFilter.value.position)
      : true;

    const keywordMatch = teamFilter.value.keyword
      ? (post.title.includes(teamFilter.value.keyword) ||
         post.description.includes(teamFilter.value.keyword) ||
         post.teamName.includes(teamFilter.value.keyword))
      : true;

    return positionMatch && keywordMatch;
  });
});

// 选手求职过滤
const filteredPlayerPosts = computed(() => {
  return playerPosts.value.filter(post => {
    const positionMatch = playerFilter.value.position
      ? post.positions.includes(playerFilter.value.position)
      : true;

    const rankMatch = playerFilter.value.rank
      ? post.rank.includes(playerFilter.value.rank)
      : true;

    const keywordMatch = playerFilter.value.keyword
      ? (post.title.includes(playerFilter.value.keyword) ||
         post.description.includes(playerFilter.value.keyword) ||
         post.playerName.includes(playerFilter.value.keyword))
      : true;

    return positionMatch && rankMatch && keywordMatch;
  });
});

// 申请加入战队
const apply = (post) => {
  ElMessage.info(`已向 [${post.teamName}] 发送加入申请`);
};

// 联系选手
const contactPlayer = (post) => {
  ElMessage.success(`已向选手 [${post.playerName}] 发送联系请求`);
};

// 显示创建对话框
const showCreateDialog = () => {
  createDialogType.value = activeTab.value;
  createDialogVisible.value = true;
};

// 处理新发布的招募信息
const handleNewPost = (newPost) => {
  // 实际开发中，这里会调用API服务将数据发送到后端
  if (createDialogType.value === 'team') {
    teamPosts.value.unshift({
      ...newPost,
      id: Date.now(),
      createdAt: new Date(),
      teamLogo: null, // 假设默认logo
      rankType: 'info'
    });
  } else {
    playerPosts.value.unshift({
      ...newPost,
      id: Date.now() + 1000, // 确保ID唯一
      createdAt: new Date(),
      avatar: null, // 假设默认头像
      rankType: 'info'
    });
  }

  ElMessage.success('发布成功！');
  createDialogVisible.value = false;
};
</script>

<style scoped lang="scss">
.recruitment-page {
  padding: 40px 20px;
  background: linear-gradient(to bottom, #0f172a, #1e293b);
  min-height: 100vh;
}

.container {
  max-width: 900px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
  padding: 20px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  border: 1px solid rgba(93, 95, 239, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);

  .page-title {
    font-size: 2.5rem;
    color: white;
    margin-bottom: 10px;
    background: linear-gradient(to right, #5d5fef, #ff4655);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
  }

  .page-subtitle {
    color: #94a3b8;
    font-size: 1.1rem;
  }
}

.recruitment-tabs {
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  padding: 20px;
  border: 1px solid rgba(93, 95, 239, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);

  :deep(.el-tabs__nav-wrap) {
    padding: 0 20px;
  }

  :deep(.el-tabs__item) {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 500;

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

.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 30px;
  background: rgba(30, 41, 59, 0.5);
  padding: 20px;
  border-radius: 8px;
  border: 1px solid rgba(93, 95, 239, 0.1);
}

.recruitment-list {
  display: grid;
  gap: 25px;
  margin-top: 20px;
}

.post-card {
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
  border: 1px solid rgba(93, 95, 239, 0.2);
  border-radius: 12px;
  padding: 25px;
  transition: all 0.3s ease;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);

  &:hover {
    transform: translateY(-5px);
    border-color: #5d5fef;
    box-shadow: 0 10px 25px rgba(93, 95, 239, 0.3);
  }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 20px;
  margin-bottom: 20px;

  .team-logo-wrapper, .player-avatar-wrapper {
    flex-shrink: 0;
  }

  .team-logo, .player-avatar {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 2px solid rgba(93, 95, 239, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  h3 {
    margin: 0 0 8px 0;
    color: white;
    font-size: 1.4rem;
    font-weight: 600;
  }

  .meta-info {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .team-name, .player-name {
    color: #94a3b8;
    font-size: 1rem;
  }

  .el-tag {
    font-weight: 600;
    border: none;
  }
}

.card-body {
  .positions {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 15px;
    flex-wrap: wrap;

    strong {
      color: #e2e8f0;
      font-weight: 600;
    }

    .pos-tag {
      font-weight: 600;
    }
  }

  .description {
    color: #cbd5e1;
    line-height: 1.8;
    font-size: 1.05rem;
  }
}

.card-footer {
  margin-top: 25px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #94a3b8;
  font-size: 0.9rem;

  .post-time {
    font-style: italic;
  }
}

.no-data {
  text-align: center;
  padding: 50px 20px;
  color: #94a3b8;
  background: rgba(15, 23, 42, 0.5);
  border-radius: 12px;
  border: 1px dashed rgba(93, 95, 239, 0.3);
}

.create-post {
  margin-top: 40px;
  text-align: center;

  .create-button {
    padding: 15px 35px;
    font-size: 1.1rem;
    font-weight: 600;
    background: linear-gradient(135deg, #5d5fef, #8b5cf6);
    border: none;
    transition: all 0.3s ease;

    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 20px rgba(93, 95, 239, 0.4);
    }
  }
}
</style>