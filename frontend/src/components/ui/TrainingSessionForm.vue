<template>
  <el-form :model="form" label-width="100px" class="training-session-form">
    <el-form-item label="训练赛标题" required>
      <el-input v-model="form.title" placeholder="例如：寻找实力相当的战队进行训练赛"></el-input>
    </el-form-item>

    <el-form-item label="预约日期" required>
      <el-date-picker
        v-model="form.date"
        type="date"
        placeholder="选择日期"
        value-format="YYYY-MM-DD"
      ></el-date-picker>
    </el-form-item>

    <el-form-item label="开始时间" required>
      <el-time-select
        v-model="form.time"
        :picker-options="{
          start: '09:00',
          step: '00:30',
          end: '23:30'
        }"
        placeholder="选择时间"
      ></el-time-select>
    </el-form-item>

    <el-form-item label="预计时长" required>
      <el-select v-model="form.duration" placeholder="选择时长">
        <el-option label="1小时" :value="1"></el-option>
        <el-option label="1.5小时" :value="1.5"></el-option>
        <el-option label="2小时" :value="2"></el-option>
        <el-option label="2.5小时" :value="2.5"></el-option>
        <el-option label="3小时" :value="3"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item label="训练模式" required>
      <el-select v-model="form.mode" placeholder="选择训练模式">
        <el-option label="标准模式" value="标准模式"></el-option>
        <el-option label="自定义模式" value="自定义模式"></el-option>
        <el-option label="BO3训练赛" value="BO3训练赛"></el-option>
        <el-option label="BO5训练赛" value="BO5训练赛"></el-option>
        <el-option label="单英雄练习" value="单英雄练习"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item label="训练要求">
      <el-input
        v-model="form.requirements"
        placeholder="例如：要求战队段位在钻石以上"
      ></el-input>
    </el-form-item>

    <el-form-item label="详细说明">
      <el-input
        v-model="form.description"
        type="textarea"
        :rows="4"
        placeholder="请详细描述训练赛的计划和目标"
      ></el-input>
    </el-form-item>

    <el-form-item class="form-footer">
      <el-button @click="$emit('cancel')">取消</el-button>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  session: Object
})

const emit = defineEmits(['submit'])

// 表单数据
const form = ref({
  title: '',
  date: '',
  time: '',
  duration: 2,
  mode: '标准模式',
  requirements: '',
  description: ''
})

// 如果传入session（编辑模式），填充表单
watch(() => props.session, (newSession) => {
  if (newSession) {
    form.value = { ...newSession }
  }
}, { immediate: true })

// 提交表单
function submitForm() {
  if (!validateForm()) return

  emit('submit', form.value)
}

// 表单验证
function validateForm() {
  if (!form.value.title) {
    ElMessage.error('请填写训练赛标题')
    return false
  }

  if (!form.value.date) {
    ElMessage.error('请选择预约日期')
    return false
  }

  if (!form.value.time) {
    ElMessage.error('请选择开始时间')
    return false
  }

  return true
}
</script>

<style scoped>
.training-session-form {
  padding: 10px 20px;
}

.form-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 30px;
}
</style>