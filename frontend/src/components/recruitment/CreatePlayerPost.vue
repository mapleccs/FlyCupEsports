<template>
  <div class="create-player-post-form">
    <el-form :model="form" :rules="rules" ref="playerPostForm" label-position="top">
      <el-form-item label="求职标题" prop="title">
        <el-input v-model="form.title" placeholder="例如：钻石全能补位选手求职" />
      </el-form-item>

      <el-form-item label="擅长位置 (可多选)" prop="positions">
        <el-select v-model="form.positions" multiple placeholder="请选择你擅长的位置" style="width: 100%;">
          <el-option label="上单" value="Top"></el-option>
          <el-option label="打野" value="Jungle"></el-option>
          <el-option label="中单" value="Mid"></el-option>
          <el-option label="ADC" value="ADC"></el-option>
          <el-option label="辅助" value="Support"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="当前段位" prop="rank">
        <el-select v-model="form.rank" placeholder="请选择你当前的段位" style="width: 100%;">
          <el-option label="王者" value="Challenger"></el-option>
          <el-option label="宗师" value="Grandmaster"></el-option>
          <el-option label="大师" value="Master"></el-option>
          <el-option label="钻石" value="Diamond"></el-option>
          <el-option label="翡翠" value="Emerald"></el-option>
          <el-option label="铂金" value="Platinum"></el-option>
          <el-option label="黄金" value="Gold"></el-option>
          <el-option label="白银" value="Silver"></el-option>
          <el-option label="青铜" value="Bronze"></el-option>
          <el-option label="黑铁" value="Iron"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="所在服务器" prop="server">
        <el-input v-model="form.server" placeholder="例如：艾欧尼亚" />
      </el-form-item>

      <el-form-item label="自我介绍" prop="description">
        <el-input
          v-model="form.description"
          type="textarea"
          :rows="4"
          placeholder="介绍你的游戏风格、在线时间、目标等..."
        />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm" style="width: 100%;">确认发布</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

const emit = defineEmits(['submit']);
const playerPostForm = ref(null);

// 表单数据模型
const form = ref({
  title: '',
  positions: [],
  rank: '',
  server: '',
  description: '',
  playerName: '当前登录用户' // 实际开发中应从store或prop获取
});

// 表单验证规则
const rules = ref({
  title: [{ required: true, message: '请输入一个吸引人的标题', trigger: 'blur' }],
  positions: [{ required: true, message: '请至少选择一个擅长位置', trigger: 'change' }],
  rank: [{ required: true, message: '请选择你的当前段位', trigger: 'change' }],
  description: [{ required: true, message: '请填写自我介绍', trigger: 'blur' }],
});

// 提交表单
const submitForm = () => {
  playerPostForm.value.validate((valid) => {
    if (valid) {
      // 触发 'submit' 事件，并传递表单数据
      emit('submit', { ...form.value });
    } else {
      ElMessage.error('请检查表单并填写所有必填项');
      return false;
    }
  });
};
</script>

<style scoped>
.create-player-post-form {
  padding: 10px 20px;
}
</style>