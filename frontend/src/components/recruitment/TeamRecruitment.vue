<template>
  <div class="team-recruitment">
    <RecruitmentFilter
      :positions="POSITIONS"
      :ranks="[]"
      filter-type="team"
      @filter-change="handleFilterChange"
    />

    <div v-if="filteredTeamPosts.length" class="recruitment-list">
      <RecruitmentCard
        v-for="post in filteredTeamPosts"
        :key="post.id"
        :post="post"
        type="team"
        @apply="apply(post)"
      />
    </div>
    <div v-else class="no-data">
      <el-empty description="暂无符合条件的招募信息" />
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { ElMessage } from 'element-plus';
import { useRecruitmentStore } from '@/stores/recruitmentStore';
import { filterPosts } from '@/utils/recruitmentUtils';
import RecruitmentFilter from './RecruitmentFilter.vue';
import RecruitmentCard from './RecruitmentCard.vue';

const recruitmentStore = useRecruitmentStore();
const {
  teamPosts,
  POSITIONS,
  POSITION_TYPES,
  POSITION_NAMES
} = recruitmentStore;

// 过滤器状态
const teamFilter = ref({
  position: '',
  keyword: ''
});

// 处理过滤变化
const handleFilterChange = (filter) => {
  teamFilter.value = filter;
};

// 过滤后的帖子
const filteredTeamPosts = computed(() => {
  return filterPosts(teamPosts, teamFilter.value);
});

// 申请加入战队
const apply = (post) => {
  ElMessage.info(`已向 [${post.teamName}] 发送加入申请`);
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