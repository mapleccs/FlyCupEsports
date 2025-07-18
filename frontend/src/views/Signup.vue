<template>
  <div class="signup-page">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">赛事报名</h1>
        <p class="page-subtitle">选择你的赛区，以选手或战队身份加入我们！</p>
      </div>

      <div class="signup-container">
        <div class="region-selection-wrapper">
          <RegionSelection
            :regions="regions"
            :selected-region="selectedRegion"
            @region-selected="handleRegionSelect"
          />
        </div>

        <div class="signup-forms-wrapper">
          <el-tabs v-model="activeTab" class="signup-tabs">
            <el-tab-pane label="选手报名" name="player">
              <PlayerSignupForm
                :form-data="playerFormData"
                :rules="playerRules"
                :fee="fees.player"
                :submitting="submitting"
                @submit="handleSubmit"
              />
            </el-tab-pane>

            <el-tab-pane label="创建战队" name="team">
              <TeamSignupForm
                :form-data="teamFormData"
                :rules="teamRules"
                :fee="fees.team"
                :submitting="submitting"
                @submit="handleSubmit"
                @logo-uploaded="handleLogoUpload"
              />
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
    </div>

    <PaymentDialog
      :visible="paymentDialog.visible"
      :title="paymentDialog.title"
      :item="paymentDialog.item"
      :amount="paymentDialog.amount"
      :methods="paymentMethods"
      @update:visible="paymentDialog.visible = $event"
      @payment-confirmed="handlePaymentConfirmed"
    />
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { ElMessage } from 'element-plus';
import {useUserStore} from "@/stores/userStore";
import RegionSelection from '@/components/signup/RegionSelection.vue';
import PlayerSignupForm from '@/components/signup/PlayerSignupForm.vue';
import TeamSignupForm from '@/components/signup/TeamSignupForm.vue';
import PaymentDialog from '@/components/signup/PaymentDialog.vue';
import { createPlayerSignup, createTeamSignup, createWechatPayment, checkPaymentStatus } from '@/services/signupService';


// 初始化用户
const userStore = useUserStore()
// --- 状态管理 ---

const activeTab = ref('player'); // 当前激活的标签页
const submitting = ref(false); // 是否正在提交
const selectedRegion = ref('fly'); // 默认选中赛区
const currentOrderId = ref(null)

// 报名费用
const fees = {
  player: 10,
  team: 50,
};

// 支付对话框状态
const paymentDialog = reactive({
  visible: false,
  title: '',
  item: '',
  amount: 0,
});

// 模拟赛区数据
const regions = ref([
  { id: 'fly', name: 'FLY赛区', description: '高手云集，精英对决', teams: 16, players: 80, icon: 'el-icon-trophy' },
  { id: 'fpf', name: 'FPF赛区', description: '新秀崛起，潜力无限', teams: 24, players: 120, icon: 'el-icon-star-on' },
]);

// 选手报名表单数据和规则
const playerFormData = ref({
  personal_name: '', gameId: '', main_position: '', secondary_position: '',
  highest_rank: '', current_rank: '', QQ: '', contact: '', agreement: false,
});
const playerRules = {
  personal_name: [{ required: true, message: '请输入昵称', trigger: 'blur' }],
  gameId: [{ required: true, message: '请输入游戏ID', trigger: 'blur' }],
  main_position: [{ required: true, message: '请选择主玩位置', trigger: 'change' }],
  QQ: [{ required: true, message: '请输入QQ号', trigger: 'blur' }],
  agreement: [{ required: true, message: '请同意协议', trigger: 'change', validator: (rule, value) => value }],
};

// 战队报名表单数据和规则
const teamFormData = ref({
  name: '', shortName: '', logo: '', slogan: '', agreement: false,
});
const teamRules = {
  name: [{ required: true, message: '请输入战队名称', trigger: 'blur' }],
  shortName: [{ required: true, message: '请输入战队简称', trigger: 'blur' }],
  agreement: [{ required: true, message: '请同意协议', trigger: 'change', validator: (rule, value) => value }],
};

// 处理赛区选择
const handleRegionSelect = (regionId) => {
  selectedRegion.value = regionId;
  ElMessage.success(`已切换到 ${regions.value.find(r => r.id === regionId).name}`);
};

// 处理Logo上传
const handleLogoUpload = (url) => {
  teamFormData.value.logo = url;
};

// 触发表单提交，打开支付对话框
const handleSubmit = async () => {
  submitting.value = true;
  try {
    const type = activeTab.value;
    const formData = type === 'player' ? playerFormData.value : teamFormData.value;
    const dataToSend = {
      ...formData,
      region_id: selectedRegion.value // 假设后端需要 'region_id'
    };

    let response;
    if (type === 'player') {
      response = await createPlayerSignup(dataToSend);
      // 注册成功后，更新用户角色为 'player'
      if (response.data.success) {
        userStore.upgradeToPlayer(); //
        // 重置表单
        Object.keys(playerFormData.value).forEach(key => { playerFormData.value[key] = ''; });
        playerFormData.value.agreement = false;
      }
    } else { // 'team'
      response = await createTeamSignup(dataToSend);
      // 创建战队成功后，更新用户角色为 'captain'
      if (response.data.success) { // 假设创建战队有相似的响应
        userStore.upgradeToCaptain(); //
        // 重置表单
        Object.keys(teamFormData.value).forEach(key => { teamFormData.value[key] = ''; });
        teamFormData.value.agreement = false;
      }
    }

    // 处理后端返回的响应
    if (response.data.success) {
      ElMessage.success('报名成功！您的角色已更新。');
    } else {
      // 如果可用，显示后端的错误信息
      ElMessage.error(`报名失败: ${response.data.message || '未知错误'}`);
    }

  } catch (error) {
    // 处理网络或其他意外错误
    ElMessage.error(`报名请求失败: ${error.response?.data?.message || error.message}`);
  } finally {
    submitting.value = false;
  }
};
</script>

<style scoped>
.signup-page {
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
}

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

.signup-container {
  display: grid;
  grid-template-columns: 3fr 7fr;
  gap: 30px;
  align-items: flex-start;
}

.signup-forms-wrapper {
  background: rgba(15, 23, 42, 0.7);
  border-radius: var(--border-radius);
  padding: 25px;
  border: 1px solid rgba(93, 95, 239, 0.2);
}

.signup-tabs {
  border: none;
}

:deep(.el-tabs__header) {
  margin-bottom: 25px;
}

:deep(.el-tabs__item) {
  color: var(--gray);
  font-size: 1.1rem;
}

:deep(.el-tabs__item.is-active) {
  color: var(--primary);
}

:deep(.el-tabs__active-bar) {
  background-color: var(--primary);
}

@media (max-width: 992px) {
  .signup-container {
    grid-template-columns: 1fr;
  }
}
</style>