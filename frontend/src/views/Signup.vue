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
import RegionSelection from '@/components/signup/RegionSelection.vue';
import PlayerSignupForm from '@/components/signup/PlayerSignupForm.vue';
import TeamSignupForm from '@/components/signup/TeamSignupForm.vue';
import PaymentDialog from '@/components/signup/PaymentDialog.vue';
import { registerPlayer, createTeam } from '@/services/signupService';

// --- 状态管理 ---

const activeTab = ref('player'); // 当前激活的标签页
const submitting = ref(false); // 是否正在提交
const selectedRegion = ref('fly'); // 默认选中赛区

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
  contact: [{ required: true, message: '请输入联系方式', trigger: 'blur' }],
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

// 模拟支付方式
const paymentMethods = ref([
    { id: 'alipay', name: '支付宝', icon: 'el-icon-s-finance' },
    { id: 'wechat', name: '微信支付', icon: 'el-icon-s-goods' },
]);


// --- 方法 ---

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
const handleSubmit = () => {
  if (activeTab.value === 'player') {
    paymentDialog.title = '选手报名支付';
    paymentDialog.item = `选手报名 - ${playerFormData.value.personal_name}`;
    paymentDialog.amount = fees.player;
  } else {
    paymentDialog.title = '战队创建支付';
    paymentDialog.item = `创建战队 - ${teamFormData.value.name}`;
    paymentDialog.amount = fees.team;
  }
  paymentDialog.visible = true;
};

// 处理支付确认
const handlePaymentConfirmed = async (paymentMethod) => {
  submitting.value = true;
  ElMessage.info(`正在通过 ${paymentMethod === 'alipay' ? '支付宝' : '微信'} 处理支付...`);

  // 模拟API调用
  await new Promise(resolve => setTimeout(resolve, 1500));

  // 实际开发中，这里会是提交数据到后端的逻辑
  // const formData = activeTab.value === 'player' ? playerFormData.value : teamFormData.value;
  // await signupService.submit(formData);

  submitting.value = false;
  paymentDialog.visible = false;
  ElMessage.success('报名成功！');

  // 重置表单
  if (activeTab.value === 'player') {
    Object.keys(playerFormData.value).forEach(key => playerFormData.value[key] = '');
    playerFormData.value.agreement = false;
  } else {
    Object.keys(teamFormData.value).forEach(key => teamFormData.value[key] = '');
    teamFormData.value.agreement = false;
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