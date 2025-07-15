<template>
  <div class="filters">
    <el-select
      v-model="filter.position"
      :placeholder="filterType === 'team' ? '筛选位置' : '筛选位置'"
      clearable
    >
      <el-option
        v-for="pos in positions"
        :key="pos.value"
        :label="pos.label"
        :value="pos.value"
      />
    </el-select>

    <el-select
      v-if="filterType === 'player'"
      v-model="filter.rank"
      placeholder="段位要求"
      clearable
    >
      <el-option
        v-for="rank in ranks"
        :key="rank.value"
        :label="rank.label"
        :value="rank.value"
      />
    </el-select>

    <el-input
      v-model="filter.keyword"
      placeholder="搜索关键词..."
      clearable
      suffix-icon="el-icon-search"
    />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  positions: Array,
  ranks: Array,
  filterType: String
});

const emit = defineEmits(['filter-change']);

// 过滤器状态
const filter = ref({
  position: '',
  rank: '',
  keyword: ''
});

// 监听过滤器变化
watch(
  filter,
  (newFilter) => {
    emit('filter-change', { ...newFilter });
  },
  { deep: true }
);
</script>

<style scoped>
.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  margin-bottom: 25px;
  background: rgba(30, 41, 59, 0.5);
  padding: 15px;
  border-radius: 8px;
  border: 1px solid rgba(93, 95, 239, 0.1);
}

@media (max-width: 768px) {
  .filters {
    grid-template-columns: 1fr;
  }
}
</style>