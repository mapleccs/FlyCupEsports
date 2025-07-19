<template>
  <div class="option-content">
    <div class="option-header">
      <i class="el-icon-user"></i>
      <h3>注册成为选手</h3>
      <div class="price">报名费: ¥{{ fee }}</div>
    </div>

    <el-form
      ref="formRef"
      :model="formData"
      :rules="rules"
      class="signup-form"
    >
      <!-- 昵称 -->
      <el-form-item label="昵称" prop="personal_name">
        <el-input
          v-model="formData.personal_name"
          placeholder="输入您的昵称"
        />
      </el-form-item>

      <!-- 游戏ID -->
      <el-form-item label="游戏ID" prop="gameId">
        <el-input
          v-model="formData.gameId"
          placeholder="输入您的游戏ID"
        />
      </el-form-item>

      <!-- 主玩位置 -->
      <el-form-item label="主玩位置" prop="main_position">
        <el-select
          v-model="formData.main_position"
          placeholder="选择主玩位置"
        >
          <el-option
            v-for="position in positionOptions"
            :key="position.value"
            :label="position.label"
            :value="position.value"
          />
        </el-select>
      </el-form-item>

      <!-- 次玩位置 -->
      <el-form-item label="次玩位置" prop="secondary_position">
        <el-select
          v-model="formData.secondary_position"
          placeholder="选择次玩位置"
        >
          <el-option
            v-for="position in positionOptions"
            :key="position.value"
            :label="position.label"
            :value="position.value"
          />
        </el-select>
      </el-form-item>

      <!-- 最高段位 -->
      <el-form-item label="最高段位" prop="highest_rank">
        <el-select
          v-model="formData.highest_rank"
          placeholder="选择最高段位"
        >
          <el-option
            v-for="rank in rankOptions"
            :key="rank.value"
            :label="rank.label"
            :value="rank.value"
          />
        </el-select>
      </el-form-item>

      <!-- 当前段位 -->
      <el-form-item label="当前段位" prop="current_rank">
        <el-select
          v-model="formData.current_rank"
          placeholder="选择当前段位"
        >
          <el-option
            v-for="rank in rankOptions"
            :key="rank.value"
            :label="rank.label"
            :value="rank.value"
          />
        </el-select>
      </el-form-item>

      <!-- QQ号 -->
      <el-form-item label="QQ号" prop="QQ">
        <el-input
          v-model="formData.QQ"
          placeholder="QQ"
        />
      </el-form-item>

      <!-- 联系方式 -->
      <el-form-item label="联系方式" prop="contact">
        <el-input
          v-model="formData.contact"
          placeholder="手机号或微信"
        />
      </el-form-item>

      <!-- 协议 -->
      <el-form-item prop="agreement">
        <el-checkbox v-model="formData.agreement">
          我已阅读并同意 <a href="#">选手参赛协议</a>
        </el-checkbox>
      </el-form-item>

      <!-- 提交按钮 -->
      <el-button
        type="primary"
        class="submit-btn"
        :loading="submitting"
        @click="validateAndSubmit"
      >
        支付报名费并注册
      </el-button>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const formRef = ref(null)
const emit = defineEmits(["submit"])

// 位置选项
const positionOptions = [
  { label: '上单', value: 'top' },
  { label: '打野', value: 'jungle' },
  { label: '中单', value: 'mid' },
  { label: 'ADC', value: 'adc' },
  { label: '辅助', value: 'support' }
]

// 段位选项
const rankOptions = [
  { label: '王者', value: '王者' },
  { label: '宗师', value: '宗师' },
  { label: '大师', value: '大师' },
  { label: '钻石', value: '钻石' },
  { label: '翡翠', value: '翡翠' },
  { label: '铂金', value: '铂金' },
  { label: '黄金', value: '黄金' },
  { label: '白银', value: '白银' },
  { label: '青铜', value: '青铜' },
  { label: '黑铁', value: '黑铁' }
]

defineProps({
  formData: Object,
  rules: Object,
  fee: Number,
  submitting: Boolean
})

const validateAndSubmit = async () => {
  try {
    const valid = await formRef.value.validate()
    if (valid) {
      emit('submit')
    }
  } catch (error) {
    console.error('表单验证失败:', error)
  }
}
</script>

<style scoped>
/* 样式保持原样 */
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

.form-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

.form-item {
  width: 100%;
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--gray-light);
}

.form-input, .form-select {
  width: 100%;
  min-width: 250px;
}

/* 调整上传组件大小 */
.logo-uploader {
  width: 100%;
  max-width: 150px;
  height: 150px;
}

/* 调整按钮位置 */
.submit-btn {
  margin-top: 20px;
}
</style>