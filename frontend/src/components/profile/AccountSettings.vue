<template>
  <section class="public-section">
    <h2><i class="el-icon-setting"></i> 账户设置</h2>
    <el-form :model="form" label-width="100px">
      <el-form-item label="用户名">
        <el-input v-model="form.username" disabled></el-input>
      </el-form-item>
      <el-form-item label="电子邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="手机号码">
        <el-input v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item label="游戏ID">
        <el-input v-model="form.gameId"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="$emit('save', form)">保存设置</el-button>
      </el-form-item>
    </el-form>
  </section>
</template>
<script setup>
import { ref } from 'vue';
const props = defineProps({ settings: Object });
const emit = defineEmits(['save']);
const form = ref({ ...props.settings });
</script>
<style scoped>
/* 样式与原Profile.vue中一致 */
section { background: rgba(15, 23, 42, 0.7); border-radius: var(--border-radius); padding: 25px; border: 1px solid rgba(93, 95, 239, 0.2); }
section h2 { display: flex; align-items: center; gap: 10px; font-size: 1.4rem; margin-bottom: 25px; color: white; padding-bottom: 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
</style>