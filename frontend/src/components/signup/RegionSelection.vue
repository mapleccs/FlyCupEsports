<template>
  <div class="region-section">
    <h2><i class="el-icon-location"></i> 选择赛区</h2>
    <div class="region-cards">
      <div
        v-for="region in regions"
        :key="region.id"
        class="region-card"
        :class="{ active: selectedRegion === region.id }"
        @click="$emit('region-selected', region.id)"
      >
        <div class="region-icon">
          <i :class="region.icon"></i>
        </div>
        <div class="region-info">
          <h3>{{ region.name }}</h3>
          <p>{{ region.description }}</p>
          <div class="region-stats">
            <span>{{ region.teams }} 支战队</span>
            <span>{{ region.players }} 名选手</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  regions: Array,
  selectedRegion: String
})

defineEmits(['region-selected'])
</script>

<style scoped>
/* 样式保持原样 */
.region-section h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.4rem;
  margin-bottom: 20px;
  color: white;
}

.region-cards {
  display: grid;
  gap: 15px;
}

.region-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(93, 95, 239, 0.2);
  border-radius: var(--border-radius);
  padding: 20px;
  display: flex;
  cursor: pointer;
  transition: var(--transition);
}

.region-card:hover {
  border-color: var(--primary);
  transform: translateY(-3px);
}

.region-card.active {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.1);
  box-shadow: 0 0 15px rgba(93, 95, 239, 0.2);
}

.region-icon {
  width: 60px;
  height: 60px;
  background: rgba(93, 95, 239, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
  flex-shrink: 0;
}

.region-icon i {
  font-size: 28px;
  color: var(--primary);
}

.region-info h3 {
  font-size: 1.2rem;
  margin-bottom: 5px;
  color: white;
}

.region-info p {
  color: var(--gray);
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.region-stats {
  display: flex;
  gap: 15px;
  font-size: 0.85rem;
  color: var(--primary);
}

@media (max-width: 768px) {
  .region-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .region-icon {
    margin-right: 0;
    margin-bottom: 15px;
  }
}
</style>