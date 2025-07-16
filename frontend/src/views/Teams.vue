<template>
  <div class="teams-page">
    <div class="container">
      <h1 class="page-title">战队平台</h1>

      <div class="tabs">
        <button
          :class="['tab-btn', { active: activeTab === 'ranking' }]"
          @click="activeTab = 'ranking'"
        >
          战队排名
        </button>
        <button
          v-if="userStore.isCaptain || userStore.isAdmin"
          :class="['tab-btn', { active: activeTab === 'training' }]"
          @click="activeTab = 'training'"
        >
          训练赛预约
        </button>
        <button
          v-if="userStore.isCaptain || userStore.isAdmin"
          :class="['tab-btn', { active: activeTab === 'my-training' }]"
          @click="activeTab = 'my-training'"
        >
          我的预约
        </button>
      </div>

      <div v-if="activeTab === 'ranking'" class="tab-content">
        <div class="filters">
          <el-select v-model="selectedRegion" placeholder="选择赛区" class="region-filter">
            <el-option label="全部赛区" value="all"></el-option>
            <el-option label="FLY" value="FLY"></el-option>
            <el-option label="FPF" value="FPF"></el-option>
            <el-option label="ACE" value="ACE"></el-option>
            <el-option label="ACC" value="ACC"></el-option>
          </el-select>

          <el-button
            type="primary"
            @click="openComparison"
            class="compare-btn"
          >
            <i class="el-icon-scale"></i> 对比战队
          </el-button>
        </div>

        <div v-if="isLoading" class="loading-placeholder">
          <i class="el-icon-loading"></i> 加载战队数据中...
        </div>

        <div v-else-if="error" class="error-message">
          <i class="el-icon-error"></i> {{ error }}
        </div>

        <div v-else class="teams-container">
          <el-table :data="filteredTeams" style="width: 100%" stripe v-loading="isLoading">
            <el-table-column prop="rank" label="排名" width="80" sortable>
              <template #default="{ $index }">
                <span class="rank-badge" :class="getRankClass($index + 1)">
                  {{ $index + 1 }}
                </span>
              </template>
            </el-table-column>
            <el-table-column label="战队" width="200">
              <template #default="{ row }">
                <div class="team-info">
                  <img :src="getLogoPath(row.logo)" class="team-logo" />
                  <div>
                    <div class="team-name">{{ row.name }}</div>
                    <div class="team-region">{{ row.region }}</div>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="win_rate" label="胜率" sortable>
              <template #default="{ row }">
                <div class="win-rate">
                  {{ (row.win_rate * 100).toFixed(1) }}%
                  <div class="win-loss">({{ row.win }}胜{{ row.loss }}负)</div>
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="kda" label="KDA" sortable />
            <el-table-column prop="gold_per_min" label="每分钟金币" sortable />
            <el-table-column label="操作">
              <template #default="{ row }">
                <el-button type="primary" size="small" @click="showTeamDetail(row)">
                  查看详情
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <el-dialog
          v-model="detailVisible"
          :title="currentTeam ? currentTeam.name : '战队详情'"
          width="80%"
        >
          <TeamCard v-if="currentTeam" :team="currentTeam" />
          <div v-else class="loading-placeholder">
            <i class="el-icon-loading"></i> 加载中...
          </div>
        </el-dialog>

        <el-dialog v-model="comparisonVisible" title="战队对比" width="90%">
          <TeamComparison
            v-if="teams.length > 0"
            :teams="teams"
            :selectedTeam1="selectedTeam1"
            :selectedTeam2="selectedTeam2"
            @update:selectedTeam1="selectedTeam1 = $event"
            @update:selectedTeam2="selectedTeam2 = $event"
          />
          <div v-else class="loading-placeholder">
            <i class="el-icon-loading"></i> 加载战队数据...
          </div>
        </el-dialog>
      </div>

      <div v-if="activeTab === 'training' && (userStore.isCaptain || userStore.isAdmin)" class="tab-content">
        <div class="training-header">
          <h2>训练赛预约市场</h2>
          <el-button type="primary" @click="showSessionForm">
            <i class="el-icon-plus"></i> 发布训练赛预约
          </el-button>
        </div>

        <TrainingSessionList
          :sessions="availableSessions"
          :is-my-sessions="false"
          @apply-session="applyForSession"
          @view-detail="viewSessionDetail"
        />
      </div>

      <div v-if="activeTab === 'my-training' && (userStore.isCaptain || userStore.isAdmin)" class="tab-content">
        <div class="training-header">
          <h2>我的训练赛预约</h2>
          <el-button type="primary" @click="showSessionForm">
            <i class="el-icon-plus"></i> 发布新预约
          </el-button>
        </div>

        <el-tabs v-model="mySessionsTab" class="my-sessions-tabs">
          <el-tab-pane label="我发布的" name="published">
            <TrainingSessionList
              :sessions="myPublishedSessions"
              :is-my-sessions="true"
              @edit-session="editSession"
              @view-applications="viewApplications"
              @cancel-session="cancelSession"
            />
          </el-tab-pane>
          <el-tab-pane label="我申请的" name="applied">
            <TrainingSessionList
              :sessions="myAppliedSessions"
              :is-my-sessions="false"
              @cancel-application="cancelMyApplication"
              @view-detail="viewSessionDetail"/>
          </el-tab-pane>
          <el-tab-pane label="历史记录" name="history">
            <TrainingSessionList
              :sessions="sessionHistory"
              :is-my-sessions="false"
              :show-status="true"
            />
          </el-tab-pane>
        </el-tabs>
      </div>

      <el-dialog
        v-model="sessionFormVisible"
        :title="isEditingSession ? '编辑训练赛预约' : '发布训练赛预约'"
        width="600px"
      >
        <TrainingSessionForm
          v-if="sessionFormVisible"
          :session="currentSession"
          @submit="handleSessionSubmit"
        />
      </el-dialog>

      <el-dialog
        v-model="sessionDetailVisible"
        :title="currentSessionDetail ? currentSessionDetail.title : '训练赛详情'"
        width="700px"
      >
        <div v-if="currentSessionDetail" class="session-detail">
          <div class="detail-header">
            <div class="team-info">
              <img :src="getLogoPath(currentSessionDetail.team.logo)" class="team-logo" />
              <div>
                <h3>{{ currentSessionDetail.team.name }}</h3>
                <div class="team-region">{{ currentSessionDetail.team.region }}</div>
              </div>
            </div>
            <div class="session-status" :class="currentSessionDetail.status">
              {{ getStatusText(currentSessionDetail.status) }}
            </div>
          </div>

          <div class="detail-content">
            <div class="detail-row">
              <div class="label">训练赛标题：</div>
              <div class="value">{{ currentSessionDetail.title }}</div>
            </div>
            <div class="detail-row">
              <div class="label">预约时间：</div>
              <div class="value">{{ formatDate(currentSessionDetail.date) }} {{ currentSessionDetail.time }}</div>
            </div>
            <div class="detail-row">
              <div class="label">预计时长：</div>
              <div class="value">{{ currentSessionDetail.duration }} 小时</div>
            </div>
            <div class="detail-row">
              <div class="label">训练模式：</div>
              <div class="value">{{ currentSessionDetail.mode }}</div>
            </div>
            <div class="detail-row">
              <div class="label">训练要求：</div>
              <div class="value">{{ currentSessionDetail.requirements || '无特殊要求' }}</div>
            </div>
            <div class="detail-row">
              <div class="label">备注说明：</div>
              <div class="value">{{ currentSessionDetail.description || '无' }}</div>
            </div>
          </div>

          <div v-if="currentSessionDetail.status === 'open' && !isMySession(currentSessionDetail)" class="apply-section">
            <el-button type="primary" @click="applyForSession(currentSessionDetail)">
              申请预约
            </el-button>
          </div>

          <div v-if="isMySession(currentSessionDetail) && currentSessionDetail.applications.length > 0" class="applications-section">
            <h3>申请列表</h3>
            <div v-for="app in currentSessionDetail.applications" :key="app.id" class="application-item">
              <div class="app-team">
                <img :src="getLogoPath(app.team.logo)" class="team-logo-sm" />
                <div>
                  <div class="team-name">{{ app.team.name }}</div>
                  <div class="team-region">{{ app.team.region }}</div>
                </div>
              </div>
              <div class="app-message">{{ app.message || '无留言' }}</div>
              <div class="app-actions">
                <el-button size="small" @click="acceptMyApplication(app)">
                  接受
                </el-button>
                <el-button size="small" @click="rejectMyApplication(app)">
                  拒绝
                </el-button>
              </div>
            </div>
          </div>
        </div>
      </el-dialog>

      <el-dialog
        v-model="applyFormVisible"
        title="申请训练赛预约"
        width="500px"
      >
        <div v-if="currentApplySession" class="apply-form">
          <div class="form-header">
            申请与 <span class="team-name">{{ currentApplySession.team.name }}</span> 进行训练赛
          </div>

          <el-form :model="applyForm" label-width="80px">
            <el-form-item label="留言">
              <el-input
                v-model="applyForm.message"
                type="textarea"
                :rows="4"
                placeholder="请简单介绍你的战队和训练赛计划"
              ></el-input>
            </el-form-item>
          </el-form>

          <div class="form-footer">
            <el-button @click="applyFormVisible = false">取消</el-button>
            <el-button type="primary" @click="submitApplication">提交申请</el-button>
          </div>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
// 1. 引入 useUserStore
import { useUserStore } from '@/stores/userStore';
import { getTeams } from '@/services/teamService';
import TeamCard from '@/components/ui/TeamCard.vue';
import TeamComparison from '@/components/ui/TeamComparison.vue';
import {
  getTrainingSessions,
  createTrainingSession,
  updateTrainingSession,
  applyForTrainingSession,
  getMyApplications,
  cancelTrainingSession,
  cancelApplication as cancelTrainingApplication,
  acceptApplication as acceptTrainingApplication,
  rejectApplication as rejectTrainingApplication,
  getTrainingHistory
} from '@/services/trainingService';
import TrainingSessionList from '@/components/ui/TrainingSessionList.vue';
import TrainingSessionForm from '@/components/ui/TrainingSessionForm.vue';

// 2. 初始化 userStore
const userStore = useUserStore();

// 当前用户（模拟）
// 注意：现在我们可以直接从 userStore 获取用户信息，不再需要模拟 currentUser
// const currentUser = ref({
//   id: 1,
//   name: "IG战队",
//   isCaptain: true
// })

// 状态管理
const activeTab = ref('ranking');
const mySessionsTab = ref('published');
const sessionFormVisible = ref(false);
const sessionDetailVisible = ref(false);
const applyFormVisible = ref(false);
const isEditingSession = ref(false);

// 战队排名相关状态
const selectedRegion = ref('all');
const detailVisible = ref(false);
const comparisonVisible = ref(false);
const currentTeam = ref(null);
const selectedTeam1 = ref(null);
const selectedTeam2 = ref(null);
const isLoading = ref(false);
const error = ref(null);

// 数据
const teams = ref([]);
const availableSessions = ref([]);
const myPublishedSessions = ref([]);
const myAppliedSessions = ref([]);
const sessionHistory = ref([]);
const currentSession = ref(null);
const currentSessionDetail = ref(null);
const currentApplySession = ref(null);

// 申请表单
const applyForm = ref({
  message: ''
});

// 计算胜率并排序
const processedTeams = computed(() => {
  return teams.value
    .map(team => ({
      ...team,
      win_rate: team.win / (team.win + team.loss),
      total_matches: team.win + team.loss
    }))
    .sort((a, b) => b.win_rate - a.win_rate);
});

// 按赛区筛选
const filteredTeams = computed(() => {
  if (selectedRegion.value === 'all') return processedTeams.value;
  return processedTeams.value.filter(t => t.region === selectedRegion.value);
});

// 加载数据
onMounted(async () => {
  try {
    // 加载战队数据
    isLoading.value = true;
    teams.value = await getTeams(); //
    // 确保有数据再设置默认值
    if (teams.value.length >= 2) {
      selectedTeam1.value = teams.value[0].id;
      selectedTeam2.value = teams.value[1].id;
    }
    isLoading.value = false;

    // 加载训练赛数据
    await loadTrainingData();
  } catch (err) {
    console.error('加载数据失败:', err);
    error.value = '加载战队数据失败，请稍后再试';
  }
});

// 加载训练赛相关数据
async function loadTrainingData() {
  // 仅当用户是队长时才加载训练赛数据
  if (userStore.isCaptain) {
    availableSessions.value = await getTrainingSessions('available');
    myPublishedSessions.value = await getTrainingSessions('my-published');
    myAppliedSessions.value = await getMyApplications();
    sessionHistory.value = await getTrainingHistory();
  }
}

// 显示预约表单
function showSessionForm() {
  isEditingSession.value = false;
  currentSession.value = null;
  sessionFormVisible.value = true;
}

// 编辑预约
function editSession(session) {
  isEditingSession.value = true;
  currentSession.value = { ...session };
  sessionFormVisible.value = true;
}

// 处理预约提交
async function handleSessionSubmit(sessionData) {
  if (isEditingSession.value) {
    await updateTrainingSession(sessionData);
  } else {
    await createTrainingSession(sessionData);
  }
  sessionFormVisible.value = false;
  loadTrainingData();
}

// 查看预约详情
function viewSessionDetail(session) {
  currentSessionDetail.value = session;
  sessionDetailVisible.value = true;
}

// 查看申请列表
function viewApplications(session) {
  currentSessionDetail.value = session;
  sessionDetailVisible.value = true;
}

// 申请预约
function applyForSession(session) {
  currentApplySession.value = session;
  applyForm.value = { message: '' };
  applyFormVisible.value = true;
}

// 提交申请
async function submitApplication() {
  if (!currentApplySession.value) return;

  await applyForTrainingSession({
    sessionId: currentApplySession.value.id,
    message: applyForm.value.message
  });

  applyFormVisible.value = false;
  loadTrainingData();
}

// 取消预约
async function cancelSession(session) {
  await cancelTrainingSession(session.id);
  loadTrainingData();
}

// 取消申请
async function cancelMyApplication(application) {
  await cancelTrainingApplication(application.id);
  loadTrainingData();
}

// 接受申请
async function acceptMyApplication(application) {
  await acceptTrainingApplication(application.id);
  loadTrainingData();
  sessionDetailVisible.value = false;
}

// 拒绝申请
async function rejectMyApplication(application) {
  await rejectTrainingApplication(application.id);
  loadTrainingData();
}

// 判断是否是我的预约
function isMySession(session) {
  // 使用 userStore 中的用户信息进行判断
  return session.team.id === userStore.user?.teamId; // 假设 user 对象中有 teamId
}

// 获取状态文本
function getStatusText(status) {
  const statusMap = {
    open: '开放预约',
    pending: '待处理',
    accepted: '已接受',
    rejected: '已拒绝',
    completed: '已完成',
    cancelled: '已取消'
  };
  return statusMap[status] || status;
}

// 格式化日期
function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
}

// 获取Logo路径
function getLogoPath(logo) {
  return `/images/teams/${logo || 'default-logo.png'}`;
}

// 战队排名相关方法
function showTeamDetail(team) {
  currentTeam.value = team;
  detailVisible.value = true;
}

function openComparison() {
  comparisonVisible.value = true;
  // 确保有数据再设置默认值
  if (teams.value.length >= 2) {
    selectedTeam1.value = teams.value[0].id;
    selectedTeam2.value = teams.value[1].id;
  }
}

function getRankClass(rank) {
  if (rank === 1) return 'rank-1';
  if (rank === 2) return 'rank-2';
  if (rank === 3) return 'rank-3';
  return '';
}
</script>

<style scoped>
/* 样式保持不变 */
.teams-page {
  padding: 40px 20px;
  background: var(--darker);
  min-height: calc(100vh - 70px);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  text-align: center;
  margin-bottom: 40px;
  font-size: 2.2rem;
  color: white;
  position: relative;
}

.page-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(to right, var(--primary), var(--secondary));
  border-radius: 2px;
}

.tabs {
  display: flex;
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.tab-btn {
  padding: 10px 20px;
  background: transparent;
  border: none;
  color: var(--gray);
  font-size: 1rem;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.tab-btn:hover {
  color: white;
}

.tab-btn.active {
  color: var(--primary);
  font-weight: bold;
}

.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--primary);
  border-radius: 2px;
}

.tab-content {
  margin-top: 20px;
}

.training-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.my-sessions-tabs {
  margin-top: 20px;
}

.session-detail {
  padding: 10px;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-right: 15px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 5px;
}

.session-status {
  padding: 5px 15px;
  border-radius: 15px;
  font-weight: bold;
  font-size: 0.9rem;
}

.session-status.open {
  background: rgba(76, 175, 80, 0.2);
  color: #4CAF50;
}

.session-status.pending {
  background: rgba(255, 152, 0, 0.2);
  color: #FF9800;
}

.session-status.accepted {
  background: rgba(33, 150, 243, 0.2);
  color: #2196F3;
}

.detail-content {
  margin-bottom: 20px;
}

.detail-row {
  display: flex;
  margin-bottom: 15px;
}

.label {
  width: 100px;
  font-weight: bold;
  color: var(--gray);
}

.value {
  flex: 1;
}

.apply-section {
  text-align: center;
  margin-top: 30px;
}

.applications-section {
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.application-item {
  display: flex;
  align-items: center;
  padding: 15px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  margin-bottom: 10px;
}

.app-team {
  display: flex;
  align-items: center;
  width: 40%;
}

.team-logo-sm {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 3px;
}

.app-message {
  flex: 1;
  padding: 0 15px;
  color: var(--gray);
  font-size: 0.9rem;
}

.app-actions {
  width: 150px;
  text-align: right;
}

.apply-form {
  padding: 10px;
}

.form-header {
  margin-bottom: 20px;
  font-size: 1.1rem;
  text-align: center;
}

.team-name {
  color: var(--primary);
  font-weight: bold;
}

.form-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

/* 战队排名样式 */
.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.region-filter {
  width: 200px;
}

.compare-btn {
  background: linear-gradient(135deg, var(--primary), #8a2be2);
  border: none;
}

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
  object-fit: cover;
  background: rgba(255, 255, 255, 0.1);
  padding: 5px;
}

.team-name {
  font-weight: 600;
}

.team-region {
  font-size: 0.8rem;
  color: var(--gray);
}

.rank-badge {
  display: inline-block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  border-radius: 50%;
  background: #4a5568;
  color: white;
  font-weight: bold;
}

.rank-1 {
  background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
}

.rank-2 {
  background: linear-gradient(135deg, #d7d7d7 0%, #a1a1a1 100%);
}

.rank-3 {
  background: linear-gradient(135deg, #cd7f32 0%, #a56a2b 100%);
}

.win-rate {
  display: flex;
  flex-direction: column;
}

.win-loss {
  font-size: 0.75rem;
  color: var(--gray);
}

.loading-placeholder, .error-message {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
  font-size: 1.2rem;
  color: var(--gray);
}

.loading-placeholder i {
  font-size: 1.5rem;
  margin-right: 10px;
  animation: rotating 2s linear infinite;
}

.error-message i {
  font-size: 1.5rem;
  margin-right: 10px;
  color: var(--secondary);
}

@keyframes rotating {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>