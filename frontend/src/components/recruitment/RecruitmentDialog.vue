<template>
  <el-dialog
    :model-value="visible"
    :title="type === 'team' ? '发布战队招募' : '发布选手求职'"
    width="600px"
    center
    @update:model-value="$emit('update:visible', $event)"
  >
    <CreateRecruitment
      v-if="type === 'team'"
      @publish="handlePublish"
    />

    <CreatePlayerPost
      v-if="type === 'player'"
      @publish="handlePublish"
    />
  </el-dialog>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import CreateRecruitment from '@/components/team/CreateRecruitment.vue';
import CreatePlayerPost from '@/components/recruitment/CreatePlayerPost.vue';

// 从父组件接收 Props
defineProps({
  visible: Boolean,
  type: String
});

// 定义该组件可以向父组件触发的事件
const emit = defineEmits(['update:visible', 'publish']);

// 当子组件 (例如 CreateRecruitment) 发布一个帖子时调用此函数
const handlePublish = (post) => {
  emit('publish', post);
  // 发布成功后，通知父组件关闭对话框
  emit('update:visible', false);
};
</script>