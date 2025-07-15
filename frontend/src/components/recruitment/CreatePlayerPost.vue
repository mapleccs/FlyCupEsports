<template>
  <div class="create-player-post">
    <el-form :model="form" :rules="rules" ref="playerForm" label-position="top">
      <el-form-item label="求职标题" prop="title">
        <el-input v-model="form.title" placeholder="例如：钻石中单寻求稳定队伍"></el-input>
      </el-form-item>

      <el-form-item label="擅长位置" prop="positions">
        <el-checkbox-group v-model="form.positions">
          <el-checkbox label="Top">上单</el-checkbox>
          <el-checkbox label="Jungle">打野</el-checkbox>
          <el-checkbox label="Mid">中单</el-checkbox>
          <el-checkbox label="ADC">ADC</el-checkbox>
          <el-checkbox label="Support">辅助</el-checkbox>
        </el-checkbox-group>
      </el-form-item>

      <el-form-item label="当前段位" prop="rank">
        <el-select v-model="form.rank" placeholder="请选择段位" clearable>
          <el-option label="黑铁" value="黑铁"></el-option>
          <el-option label="青铜" value="青铜"></el-option>
          <el-option label="白银" value="白银"></el-option>
          <el-option label="黄金" value="黄金"></el-option>
          <el-option label="铂金" value="铂金"></el-option>
          <el-option label="翡翠" value="翡翠"></el-option>
          <el-option label="钻石" value="钻石"></el-option>
          <el-option label="大师" value="大师"></el-option>
          <el-option label="宗师" value="宗师"></el-option>
          <el-option label="王者" value="王者"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="个人介绍" prop="description">
        <el-input
          v-model="form.description"
          type="textarea"
          :rows="4"
          placeholder="请介绍你的游戏风格、擅长英雄、在线时间等信息"
        ></el-input>
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

const emit = defineEmits(['close', 'publish']);
const playerForm = ref(null);

const form = ref({
  title: '',
  positions: [],
  rank: '',
  description: ''
});

const rules = {
  title: [{ required: true, message: '请输入求职标题', trigger: 'blur' }],
  positions: [{ required: true, type: 'array', message: '请至少选择一个位置', trigger: 'change' }],
  rank: [{ required: true, message: '请选择段位', trigger: 'change' }],
  description: [{ required: true, message: '请输入个人介绍', trigger: 'blur' }]
};

const publish = () => {
  playerForm.value.validate((valid) => {
    if (valid) {
      // 验证通过，发布信息
      emit('publish', {
        ...form.value,
        playerName: '当前用户', // 实际应用中应从用户信息获取
        createdAt: new Date()
      });
    } else {
      ElMessage.error('请填写完整的信息');
      return false;
    }
  });
};
</script>

<style scoped>
.form-actions {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}
</style>