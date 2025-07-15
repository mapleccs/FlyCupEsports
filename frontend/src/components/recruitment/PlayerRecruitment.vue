<template>
  <div class="player-recruitment">
    <RecruitmentFilter
      :positions="POSITIONS"
      :ranks="RANKS"
      filter-type="player"
      @filter-change="handleFilterChange"
    />

    <div v-if="filteredPlayerPosts.length" class="recruitment-list">
      <RecruitmentCard
        v-for="post in filteredPlayerPosts"
        :key="post.id"
        :post="post"
        type="player"
        @contact="contactPlayer(post)"
      />
    </div>
    <div v-else class="no-data">
      <el-empty description="暂无符合条件的求职信息" />
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useRecruitmentStore } from '@/stores/recruitmentStore';
import { ElMessage } from 'element-plus';
import { filterPosts } from '@/utils/recruitmentUtils';
import RecruitmentFilter from './RecruitmentFilter.vue';
import RecruitmentCard from './RecruitmentCard.vue';

const recruitmentStore = useRecruitmentStore();
const {
  playerPosts,
  POSITIONS,
  RANKS,
  POSITION_TYPES,
  POSITION_NAMES
} = recruitmentStore;

// 过滤器状态
const playerFilter = ref({
  position: '',
  rank: '',
  keyword: ''
});

// 处理过滤变化
const handleFilterChange = (filter) => {
  playerFilter.value = filter;
};

// 过滤后的帖子
const filteredPlayerPosts = computed(() => {
  return filterPosts(playerPosts, playerFilter.value);
});

// 联系选手
const contactPlayer = (post) => {
  ElMessage.success(`已向选手 [${post.playerName}] 发送联系请求`);
};
</script>

<style scoped>
.recruitment-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
  gap: 20px;
}

.no-data {
  text-align: center;
  padding: 30px 15px;
  color: #94a3b8;
  background: rgba(15, 23, 42, 0.5);
  border-radius: 10px;
  border: 1px dashed rgba(93, 95, 239, 0.3);
  grid-column: 1 / -1;
}

/* 响应式调整 */
@media (max-width: 1100px) {
  .recruitment-list {
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  }
}

@media (max-width: 900px) {
  .recruitment-list {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 15px;
  }
}

@media (max-width: 768px) {
  .recruitment-list {
    grid-template-columns: 1fr;
  }
}
</style>