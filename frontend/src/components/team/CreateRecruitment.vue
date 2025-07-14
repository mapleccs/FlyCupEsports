<template>
  <div class="create-recruitment">
    <el-form :model="form" :rules="rules" ref="recruitmentForm" label-position="top">
      <el-form-item label="招募标题" prop="title">
        <el-input v-model="form.title" placeholder="例如：白金分段招募一名强力上单"></el-input>
      </el-form-item>
      <el-form-item label="需要位置" prop="positions">
        <el-checkbox-group v-model="form.positions">
          <el-checkbox label="Top">上单</el-checkbox>
          <el-checkbox label="Jungle">打野</el-checkbox>
          <el-checkbox label="Mid">中单</el-checkbox>
          <el-checkbox label="ADC">ADC</el-checkbox>
          <el-checkbox label="Support">辅助</el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="招募详情" prop="description">
        <el-input v-model="form.description" type="textarea" :rows="4" placeholder="请填写段位要求、在线时间、战队风格等具体信息"></el-input>
      </el-form-item>
      <el-form-item>
          <div class="form-actions">
            <el-button @click="$emit('close')">取消</el-button>
            <el-button type="primary" @click="publish">确认发布</el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
const emit = defineEmits(['close']);
const recruitmentForm = ref(null);
const form = ref({ title: '', positions: [], description: '' });
const rules = {
  title: [{ required: true, message: '请输入招募标题', trigger: 'blur' }],
  positions: [{ required: true, type: 'array', message: '请至少选择一个位置', trigger: 'change' }],
  description: [{ required: true, message: '请输入招募详情', trigger: 'blur' }],
};
const publish = () => {
  recruitmentForm.value.validate((valid) => {
    if (valid) {
      // 此处调用API发布招募信息
      console.log('Publishing recruitment:', form.value);
      ElMessage.success('招募信息已成功发布到招募中心！');
      emit('close');
    } else {
      ElMessage.error('请填写完整的招募信息');
      return false;
    }
  });
};
</script>
<style scoped>
.form-actions { display:flex; justify-content:flex-end; width:100%; }
</style>