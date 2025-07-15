<template>
  <div class="option-content">
    <div class="option-header">
      <i class="el-icon-s-flag"></i>
      <h3>创建新战队</h3>
      <div class="price">创建费: ¥{{ fee }}</div>
    </div>

    <el-form
      ref="formRef"
      :model="formData"
      :rules="rules"
      class="signup-form"
    >
      <el-form-item label="战队名称" prop="name">
        <el-input
          v-model="formData.name"
          placeholder="输入战队名称"
        />
      </el-form-item>

      <el-form-item label="战队简称" prop="shortName">
        <el-input
          v-model="formData.shortName"
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
          <img v-if="formData.logo" :src="formData.logo" class="logo" alt="">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>

      <el-form-item label="战队口号" prop="slogan">
        <el-input
          v-model="formData.slogan"
          placeholder="输入战队口号"
        />
      </el-form-item>

      <el-form-item prop="agreement">
        <el-checkbox v-model="formData.agreement">
          我已阅读并同意 <a href="#">战队创建协议</a>
        </el-checkbox>
      </el-form-item>

      <el-button
        type="primary"
        class="submit-btn"
        :loading="submitting"
        @click="validateAndSubmit"
      >
        支付创建费并注册
      </el-button>
    </el-form>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { ref } from 'vue'

const formRef = ref(null)

defineProps({
  formData: Object,
  rules: Object,
  fee: Number,
  submitting: Boolean
})

const emit = defineEmits(['submit', 'logo-uploaded'])

const handleLogoSuccess = (response, file) => {
  try {
    if (response && response.url) {
      emit('logo-uploaded', response.url)
      ElMessage.success('Logo上传成功')
    } else {
      emit('logo-uploaded', URL.createObjectURL(file.raw))
      ElMessage.success('Logo上传成功 (本地预览)')
    }
  } catch (error) {
    ElMessage.error('Logo上传失败')
  }
}

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