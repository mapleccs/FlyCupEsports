<template>
  <div class="signup-page">
    <div class="container">
      <div class="signup-header">
        <h1>赛事报名</h1>
        <p>选择赛区并注册成为选手或创建战队</p>
      </div>

      <div class="signup-container">
        <!-- 赛区选择 -->
        <div class="region-section">
          <h2><i class="el-icon-location"></i> 选择赛区</h2>
          <div class="region-cards">
            <div
              v-for="region in regions"
              :key="region.id"
              class="region-card"
              :class="{ active: selectedRegion === region.id }"
              @click="selectRegion(region.id)"
            >
              <div class="region-icon">
                <i :class="region.icon"></i>
              </div>
              <div class="region-info">
                <h3>{{ region.name }}</h3>
                <p>{{ region.description }}</p>
                <div class="region-stats">
                  <span>{{ region.teams }} 支战队</span>
                  <span>{{ region.players }} 名选手</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 报名选项 -->
        <div class="signup-options">
          <el-tabs v-model="activeTab" class="signup-tabs">
            <!-- 选手报名 -->
            <el-tab-pane label="选手报名" name="player">
              <div class="option-content">
                <div class="option-header">
                  <i class="el-icon-user"></i>
                  <h3>注册成为选手</h3>
                  <div class="price">报名费: ¥{{ playerFee }}</div>
                </div>

                <el-form
                  ref="playerForm"
                  :model="playerForm"
                  :rules="playerRules"
                  class="signup-form"
                >
                  <el-form-item label="昵称" prop="personal_name">
                    <el-input
                      v-model="playerForm.personal_name"
                      placeholder="输入您的昵称"
                    />
                  </el-form-item>

                  <el-form-item label="游戏ID" prop="gameId">
                    <el-input
                      v-model="playerForm.gameId"
                      placeholder="输入您的游戏ID"
                    />
                  </el-form-item>

                  <el-form-item label="主玩位置" prop="main_position">
                    <el-select
                      v-model="playerForm.main_position"
                      placeholder="选择主玩位置"
                    >
                      <el-option label="上单" value="top"></el-option>
                      <el-option label="打野" value="jungle"></el-option>
                      <el-option label="中单" value="mid"></el-option>
                      <el-option label="ADC" value="adc"></el-option>
                      <el-option label="辅助" value="support"></el-option>
                    </el-select>
                  </el-form-item>

                  <el-form-item label="次玩位置" prop="secondary_position">
                    <el-select
                      v-model="playerForm.secondary_position"
                      placeholder="选择次玩位置"
                    >
                      <el-option label="上单" value="top"></el-option>
                      <el-option label="打野" value="jungle"></el-option>
                      <el-option label="中单" value="mid"></el-option>
                      <el-option label="ADC" value="adc"></el-option>
                      <el-option label="辅助" value="support"></el-option>
                    </el-select>
                  </el-form-item>

                  <el-form-item label="最高段位" prop="highest_rank">
                    <el-select
                      v-model="playerForm.highest_rank"
                      placeholder="选择最高段位"
                    >
                      <el-option label="王者" value="challenger"></el-option>
                      <el-option label="宗师" value="grandmaster"></el-option>
                      <el-option label="大师" value="master"></el-option>
                      <el-option label="钻石" value="diamond"></el-option>
                      <el-option label="翡翠" value="emerald"></el-option>
                      <el-option label="铂金" value="platinum"></el-option>
                      <el-option label="黄金" value="gold"></el-option>
                      <el-option label="白银" value="silver"></el-option>
                      <el-option label="青铜" value="bronze"></el-option>
                      <el-option label="黑铁" value="iron"></el-option>
                    </el-select>
                  </el-form-item>

                  <el-form-item label="当前段位" prop="current_rank">
                    <el-select
                      v-model="playerForm.current_rank"
                      placeholder="选择当前段位"
                    >
                      <el-option label="王者" value="challenger"></el-option>
                      <el-option label="宗师" value="grandmaster"></el-option>
                      <el-option label="大师" value="master"></el-option>
                      <el-option label="钻石" value="diamond"></el-option>
                      <el-option label="翡翠" value="emerald"></el-option>
                      <el-option label="铂金" value="platinum"></el-option>
                      <el-option label="黄金" value="gold"></el-option>
                      <el-option label="白银" value="silver"></el-option>
                      <el-option label="青铜" value="bronze"></el-option>
                      <el-option label="黑铁" value="iron"></el-option>
                    </el-select>
                  </el-form-item>

                  <el-form-item label="QQ号" prop="QQ">
                    <el-input
                      v-model="playerForm.QQ"
                      placeholder="QQ"
                    />
                  </el-form-item>

                  <el-form-item label="联系方式" prop="contact">
                    <el-input
                      v-model="playerForm.contact"
                      placeholder="手机号或微信"
                    />
                  </el-form-item>

                  <el-form-item prop="agreement">
                    <el-checkbox v-model="playerForm.agreement">
                      我已阅读并同意 <a href="#">选手参赛协议</a>
                    </el-checkbox>
                  </el-form-item>

                  <el-button
                    type="primary"
                    class="submit-btn"
                    :loading="playerSubmitting"
                    @click="submitPlayerForm"
                  >
                    支付报名费并注册
                  </el-button>
                </el-form>
              </div>
            </el-tab-pane>

            <!-- 创建战队 -->
            <el-tab-pane label="创建战队" name="team">
              <div class="option-content">
                <div class="option-header">
                  <i class="el-icon-s-flag"></i>
                  <h3>创建新战队</h3>
                  <div class="price">创建费: ¥{{ teamFee }}</div>
                </div>

                <el-form
                  ref="teamForm"
                  :model="teamForm"
                  :rules="teamRules"
                  class="signup-form"
                >
                  <el-form-item label="战队名称" prop="name">
                    <el-input
                      v-model="teamForm.name"
                      placeholder="输入战队名称"
                    />
                  </el-form-item>

                  <el-form-item label="战队简称" prop="shortName">
                    <el-input
                      v-model="teamForm.shortName"
                      placeholder="输入战队简称（2-4字母）"
                    />
                  </el-form-item>

                  <el-form-item label="战队Logo" prop="logo">
                    <el-upload
                      class="logo-uploader"
                      action="/api/upload"
                      :show-file-list="false"
                      :on-success="handleLogoSuccess"
                    >
                      <img v-if="teamForm.logo" :src="teamForm.logo" class="logo" alt="">
                      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                  </el-form-item>

                  <el-form-item label="战队口号" prop="slogan">
                    <el-input
                      v-model="teamForm.slogan"
                      placeholder="输入战队口号"
                    />
                  </el-form-item>

                  <el-form-item prop="agreement">
                    <el-checkbox v-model="teamForm.agreement">
                      我已阅读并同意 <a href="#">战队创建协议</a>
                    </el-checkbox>
                  </el-form-item>

                  <el-button
                    type="primary"
                    class="submit-btn"
                    :loading="teamSubmitting"
                    @click="submitTeamForm"
                  >
                    支付创建费并注册
                  </el-button>
                </el-form>
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>

      <!-- 支付弹窗 -->
      <el-dialog
        v-model="paymentDialogVisible"
        :title="paymentTitle"
        width="400px"
        center
      >
        <div class="payment-content">
          <div class="payment-info">
            <div class="payment-item">
              <span>项目：</span>
              <strong>{{ paymentItem }}</strong>
            </div>
            <div class="payment-item">
              <span>金额：</span>
              <strong class="payment-amount">¥{{ paymentAmount }}</strong>
            </div>
          </div>

          <div class="payment-methods">
            <h4>选择支付方式</h4>
            <div class="methods-grid">
              <div
                v-for="method in paymentMethods"
                :key="method.id"
                class="method-card"
                :class="{ active: selectedMethod === method.id }"
                @click="selectPaymentMethod(method.id)"
              >
                <i :class="method.icon"></i>
                <span>{{ method.name }}</span>
              </div>
            </div>
          </div>

          <el-button
            type="primary"
            class="confirm-payment"
            :disabled="!selectedMethod"
            @click="processPayment"
          >
            确认支付
          </el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { regions, paymentMethods, positions, ranks } from "../../public/data/signupData";
import { registerPlayer, createTeam, createPayment, uploadLogo } from "@/services/signupService";

// 状态变量
const selectedRegion = ref('fly')
const activeTab = ref('player')
const paymentDialogVisible = ref(false)
const selectedMethod = ref('')
const playerSubmitting = ref(false)
const teamSubmitting = ref(false)

// 选手表单
const playerForm = ref({
  personal_name: '',
  gameId: '',
  main_position: '',
  secondary_position: '',
  highest_rank: '',
  current_rank: '',
  QQ: '',
  contact: '',
  agreement: false
})

// 战队表单
const teamForm = ref({
  name: '',
  shortName: '',
  logo: '',
  slogan: '',
  agreement: false
})

// 支付相关变量
const paymentType = ref('player')
const paymentTitle = ref('')
const paymentItem = ref('')
const paymentAmount = ref(0)

// 费用计算
const playerFee = computed(() => {
  const region = regions.find(r => r.id === selectedRegion.value)
  return region ? region.fee : 50
})

const teamFee = computed(() => {
  const region = regions.find(r => r.id === selectedRegion.value)
  return region ? region.fee * 5 : 250
})

// 表单验证规则
const playerRules = {
  personal_name: [
    { required: true , message: '请输入昵称', trigger: 'blur' },
    { min: 1, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  gameId: [
    { required: true, message: '请输入游戏ID', trigger: 'blur' },
    { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  main_position: [
    { required: true, message: '请选择主玩位置', trigger: 'change' }
  ],
  secondary_position: [
    { message: '请选择次玩位置', trigger: 'change' }
  ],
  highest_rank: [
    { required: true, message: '请选择最高段位', trigger: 'change' }
  ],
  current_rank: [
    { required: true, message: '请选择当前段位', trigger: 'change' }
  ],
  QQ: [
    { required: true, message: '请输入QQ号', trigger: 'blur' }
  ],
  contact: [
    { message: '请输入联系方式', trigger: 'blur' }
  ],
  agreement: [
    {
      validator: (rule, value, callback) => {
        if (!value) {
          callback(new Error('请阅读并同意协议'))
        } else {
          callback()
        }
      },
      trigger: 'change'
    }
  ]
}

const teamRules = {
  name: [
    { required: true, message: '请输入战队名称', trigger: 'blur' },
    { min: 2, max: 16, message: '长度在 2 到 16 个字符', trigger: 'blur' }
  ],
  shortName: [
    { required: true, message: '请输入战队简称', trigger: 'blur' },
    { min: 2, max: 4, message: '简称应为2-4个字母', trigger: 'blur' }
  ],
  agreement: [
    {
      validator: (rule, value, callback) => {
        if (!value) {
          callback(new Error('请阅读并同意协议'))
        } else {
          callback()
        }
      },
      trigger: 'change'
    }
  ]
}

// 方法定义
const selectRegion = (regionId) => {
  selectedRegion.value = regionId
}


const handleLogoSuccess = async (response, file) => {
  try {
    if (response && response.url) {
      teamForm.value.logo = response.url
      ElMessage.success('Logo上传成功')
    } else {
      // 如果后端返回结构不同，尝试从file中获取URL
      teamForm.value.logo = URL.createObjectURL(file.raw)
      ElMessage.success('Logo上传成功 (本地预览)')
    }
  } catch (error) {
    ElMessage.error('Logo上传失败')
  }
}

  const submitPlayerForm = () => {
    // 实际开发中应调用表单验证
    paymentType.value = 'player'
    paymentTitle.value = '选手报名支付'
    paymentItem.value = '选手报名费'
    paymentAmount.value = playerFee.value
    paymentDialogVisible.value = true
  }

  const submitTeamForm = () => {
    // 实际开发中应调用表单验证
    paymentType.value = 'team'
    paymentTitle.value = '战队创建支付'
    paymentItem.value = '战队创建费'
    paymentAmount.value = teamFee.value
    paymentDialogVisible.value = true
  }

  const selectPaymentMethod = (methodId) => {
    selectedMethod.value = methodId
  }

const processPayment = async () => {
  try {
    // 创建支付记录
    const paymentData = {
      type: paymentType.value,
      amount: paymentAmount.value,
      method: selectedMethod.value,
      item: paymentItem.value
    }

    await createPayment(paymentData)

    if (paymentType.value === 'player') {
      // 提交选手报名
      const playerData = {
        region: selectedRegion.value,
        ...playerForm.value
      }
      await registerPlayer(playerData)

      ElMessage.success('选手注册成功！您已加入选手池')
    } else {
      // 提交战队创建
      const teamData = {
        region: selectedRegion.value,
        ...teamForm.value
      }
      await createTeam(teamData)

      ElMessage.success('战队创建成功！您现在可以邀请队员')
    }

    // 重置状态
    paymentDialogVisible.value = false
    selectedMethod.value = ''

    if (paymentType.value === 'player') {
      playerSubmitting.value = false
      // 重置选手表单
      playerForm.value = {
        gameId: '',
        position: '',
        rank: '',
        contact: '',
        agreement: false
      }
    } else {
      teamSubmitting.value = false
      // 重置战队表单
      teamForm.value = {
        name: '',
        shortName: '',
        logo: '',
        slogan: '',
        agreement: false
      }
    }
  } catch (error) {
    ElMessage.error(`操作失败: ${error.response?.data?.message || error.message}`)
  }
}
</script>

<style scoped>
.signup-page {
  padding: 40px 20px;
  background: var(--darker);
  min-height: calc(100vh - 70px);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.signup-header {
  text-align: center;
  margin-bottom: 40px;
}

.signup-header h1 {
  font-size: 2.5rem;
  margin-bottom: 15px;
  background: linear-gradient(to right, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.signup-header p {
  color: var(--gray);
  font-size: 1.1rem;
}

.signup-container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
}

.region-section h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.4rem;
  margin-bottom: 20px;
  color: white;
}

.region-cards {
  display: grid;
  gap: 15px;
}

.region-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(93, 95, 239, 0.2);
  border-radius: var(--border-radius);
  padding: 20px;
  display: flex;
  cursor: pointer;
  transition: var(--transition);
}

.region-card:hover {
  border-color: var(--primary);
  transform: translateY(-3px);
}

.region-card.active {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.1);
  box-shadow: 0 0 15px rgba(93, 95, 239, 0.2);
}

.region-icon {
  width: 60px;
  height: 60px;
  background: rgba(93, 95, 239, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
  flex-shrink: 0;
}

.region-icon i {
  font-size: 28px;
  color: var(--primary);
}

.region-info h3 {
  font-size: 1.2rem;
  margin-bottom: 5px;
  color: white;
}

.region-info p {
  color: var(--gray);
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.region-stats {
  display: flex;
  gap: 15px;
  font-size: 0.85rem;
  color: var(--primary);
}

.signup-options {
  background: rgba(15, 23, 42, 0.7);
  border-radius: var(--border-radius);
  padding: 25px;
  border: 1px solid rgba(93, 95, 239, 0.2);
}

.signup-tabs :deep(.el-tabs__nav-wrap)::after {
  background-color: rgba(255, 255, 255, 0.1);
}

.signup-tabs :deep(.el-tabs__item) {
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--gray);
}

.signup-tabs :deep(.el-tabs__item.is-active) {
  color: var(--primary);
}

.signup-tabs :deep(.el-tabs__active-bar) {
  background-color: var(--primary);
}

.option-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
  position: relative;
}

.option-header i {
  font-size: 28px;
  color: var(--primary);
}

.option-header h3 {
  font-size: 1.3rem;
  color: white;
}

.price {
  position: absolute;
  right: 0;
  top: 0;
  background: var(--secondary);
  color: white;
  padding: 5px 15px;
  border-radius: 20px;
  font-weight: bold;
  font-size: 0.9rem;
}

.signup-form .el-form-item {
  margin-bottom: 22px;
}

.signup-form :deep(.el-form-item__label) {
  color: var(--gray);
}

.submit-btn {
  width: 100%;
  padding: 15px;
  font-size: 1rem;
  font-weight: 600;
  margin-top: 10px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border: none;
}

.logo-uploader {
  width: 120px;
  height: 120px;
  border: 1px dashed var(--primary);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.05);
}

.logo-uploader:hover {
  border-color: var(--secondary);
}

.avatar-uploader-icon {
  font-size: 28px;
  color: var(--primary);
  width: 120px;
  height: 120px;
  line-height: 120px;
  text-align: center;
}

.logo {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

/* 支付弹窗样式 */
.payment-content {
  padding: 0 20px;
}

.payment-info {
  background: rgba(15, 23, 42, 0.5);
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 25px;
}

.payment-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-size: 1rem;
}

.payment-item:last-child {
  margin-bottom: 0;
}

.payment-amount {
  color: var(--secondary);
  font-size: 1.2rem;
}

.payment-methods h4 {
  margin-bottom: 15px;
  color: white;
  font-weight: 500;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  margin-bottom: 25px;
}

.method-card {
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 15px;
  text-align: center;
  cursor: pointer;
  transition: var(--transition);
}

.method-card:hover {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.1);
}

.method-card.active {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.2);
  box-shadow: 0 0 10px rgba(93, 95, 239, 0.2);
}

.method-card i {
  font-size: 32px;
  display: block;
  margin-bottom: 8px;
  color: var(--primary);
}

.method-card span {
  font-size: 0.9rem;
}

.confirm-payment {
  width: 100%;
  padding: 15px;
  font-size: 1rem;
  font-weight: 600;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border: none;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .signup-container {
    grid-template-columns: 1fr;
  }

  .methods-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .signup-header h1 {
    font-size: 2rem;
  }

  .region-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .region-icon {
    margin-right: 0;
    margin-bottom: 15px;
  }
}
</style>