<template>
  <div class="profile-page">
    <div class="container">
      <UserProfileCard :user="user" :stats="userStats" />

      <!-- 添加雷达图展示区域 -->
      <div class="player-radar-chart" v-if="isPlayer || isCaptain">
        <h3 class="section-title">个人选手数据雷达图</h3>
        <div ref="radarChart" class="radar-chart-container"></div>
        <div class="radar-legend">
          <div v-for="(item, index) in radarData.indicator" :key="index" class="legend-item">
            <div class="legend-color" :style="{ backgroundColor: legendColors[index] }"></div>
            <span>{{ item.name }}: {{ radarData.value[index] }}</span>
          </div>
        </div>
      </div>

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
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import * as echarts from 'echarts';

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
  role: 'player', // 可切换 'guest', 'player', 'captain', 'admin' 来测试不同视图
  avatar: null, // 可以是图片URL
  position: 'mid', // 玩家位置
  rank: '钻石Ⅲ', // 玩家段位
});

const userStats = ref({
  gamesPlayed: 42,
  winRate: '68%',
  teamCount: 1,
  kda: 4.2, // KDA数据
  csPerMin: 7.8, // 分均补刀
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

// 雷达图数据
const radarData = ref({
  indicator: [
    { name: 'KDA', max: 5 },
    { name: '分均补刀', max: 10 },
    { name: '参团率', max: 100 },
    { name: '伤害转化', max: 150 },
    { name: '视野控制', max: 5 },
    { name: '生存能力', max: 10 }
  ],
  value: [4.2, 7.8, 68, 127, 3.4, 7.2]
});

const legendColors = ref(['#5d5fef', '#ff4655', '#0ea5e9', '#10b981', '#f59e0b', '#8b5cf6']);
// --- 模拟数据结束 ---

// ECharts实例管理
const radarChart = ref(null);
const radarChartRef = ref(null);

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

// 初始化雷达图
const initRadarChart = () => {
  if (!radarChartRef.value) {
    console.error('雷达图容器未找到');
    return;
  }

  // 如果已经存在实例，先销毁
  if (radarChart.value && typeof radarChart.value.dispose === 'function') {
    radarChart.value.dispose();
    radarChart.value = null;
  }

  try {
    // 创建新的图表实例
    radarChart.value = echarts.init(radarChartRef.value, 'dark');

    const option = {
      tooltip: {
        trigger: 'item',
        formatter: function(params) {
          return `${params.name}: ${params.value}`;
        }
      },
      radar: {
        indicator: radarData.value.indicator,
        radius: '65%',
        center: ['50%', '50%'],
        axisName: {
          color: '#94a3b8',
          fontSize: 12,
          padding: [3, 5],
          backgroundColor: 'rgba(15, 23, 42, 0.7)',
          borderRadius: 3
        },
        splitArea: {
          areaStyle: {
            color: ['rgba(30, 41, 59, 0.5)', 'rgba(30, 41, 59, 0.3)']
          }
        },
        splitLine: {
          lineStyle: {
            color: 'rgba(148, 163, 184, 0.3)'
          }
        },
        axisLine: {
          lineStyle: {
            color: 'rgba(148, 163, 184, 0.5)'
          }
        }
      },
      series: [{
        type: 'radar',
        data: [{
          value: radarData.value.value,
          name: '选手能力值',
          symbol: 'circle',
          symbolSize: 8,
          lineStyle: {
            width: 2,
            color: '#5d5fef'
          },
          areaStyle: {
            color: new echarts.graphic.RadialGradient(0.5, 0.5, 1, [
              { offset: 0, color: 'rgba(93, 95, 239, 0.4)' },
              { offset: 1, color: 'rgba(93, 95, 239, 0.1)' }
            ])
          },
          itemStyle: {
            color: '#5d5fef'
          },
          label: {
            show: true,
            formatter: function(params) {
              return params.value;
            },
            position: 'top',
            color: '#e2e8f0',
            fontSize: 12
          }
        }]
      }],
      backgroundColor: 'transparent',
      textStyle: {
        color: '#e2e8f0'
      }
    };

    radarChart.value.setOption(option);

    console.log('雷达图初始化成功');

    // 添加窗口大小变化监听
    window.addEventListener('resize', handleResize);
  } catch (error) {
    console.error('雷达图初始化失败:', error);
  }
};

// 窗口大小调整处理函数
const handleResize = () => {
  if (radarChart.value && typeof radarChart.value.resize === 'function') {
    radarChart.value.resize();
  }
};

// 组件挂载后初始化图表
onMounted(() => {
  nextTick(() => {
    if (isPlayer.value || isCaptain.value) {
      initRadarChart();
    }
  });
});

// 组件卸载前清理资源
onBeforeUnmount(() => {
  // 销毁图表实例
  if (radarChart.value && typeof radarChart.value.dispose === 'function') {
    radarChart.value.dispose();
    radarChart.value = null;
  }

  // 移除事件监听器
  window.removeEventListener('resize', handleResize);
});
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

/* 雷达图样式 */
.player-radar-chart {
  margin-top: 30px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  padding: 20px;
  border: 1px solid rgba(93, 95, 239, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.section-title {
  color: white;
  font-size: 1.4rem;
  margin-bottom: 20px;
  text-align: center;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.radar-chart-container {
  height: 400px;
  width: 100%;
}

.radar-legend {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.legend-color {
  width: 16px;
  height: 16px;
  border-radius: 4px;
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