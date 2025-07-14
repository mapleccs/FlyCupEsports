<template>
  <div class="edit-team-form">
    <el-form :model="teamData" label-width="100px" label-position="top">
      <el-form-item label="战队名称">
        <el-input v-model="teamData.name" placeholder="请输入新的战队名称"></el-input>
      </el-form-item>
      <el-form-item label="战队口号">
        <el-input v-model="teamData.slogan" type="textarea" :rows="3" placeholder="输入响亮的口号"></el-input>
      </el-form-item>
      <el-form-item label="战队Logo">
        <el-upload
          class="logo-uploader"
          action="/api/upload"
          :show-file-list="false"
          :on-success="handleLogoSuccess"
          :before-upload="beforeLogoUpload"
        >
          <img v-if="teamData.logo" :src="teamData.logo" class="logo" alt="Team Logo">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <div class="form-actions">
            <el-button @click="$emit('close')">取消</el-button>
            <el-button type="primary" @click="save">保存更改</el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
const props = defineProps({ initialTeamData: Object });
const emit = defineEmits(['close']);
const teamData = ref({ ...props.initialTeamData });
const handleLogoSuccess = (response, file) => {
  teamData.value.logo = URL.createObjectURL(file.raw); // 模拟URL，实际应使用response.url
  ElMessage.success('Logo上传成功!');
};
const beforeLogoUpload = (file) => {
  const isJPGorPNG = file.type === 'image/jpeg' || file.type === 'image/png';
  if (!isJPGorPNG) { ElMessage.error('上传的Logo只能是 JPG/PNG 格式!'); }
  return isJPGorPNG;
};
const save = () => {
  // 此处调用API将 teamData.value 提交到后端
  console.log('Saving team data:', teamData.value);
  ElMessage.success('战队信息已更新！');
  emit('close');
};
</script>
<style scoped>
.logo-uploader { width: 120px; height: 120px; border: 1px dashed #d9d9d9; border-radius: 6px; cursor: pointer; display:flex; justify-content:center; align-items:center; }
.logo { width: 100%; height: 100%; object-fit: cover; }
.avatar-uploader-icon { font-size: 28px; color: #8c939d; }
.form-actions { display:flex; justify-content:flex-end; width:100%; }
</style>