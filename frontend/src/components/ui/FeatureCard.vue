<template>
  <div class="feature-card">
    <div class="card-icon">
      <i :class="iconClass"></i>
    </div>
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
    <div class="card-hover"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: String,
  description: String,
  icon: String,
})

const iconClass = computed(() => {
  const icons = {
    info: 'el-icon-info',
    signup: 'el-icon-user',
    team: 'el-icon-user-solid'
  }
  return icons[props.icon] || 'el-icon-question'
})
</script>

<style scoped>
.feature-card {
  background: rgba(15, 23, 42, 0.6);
  border-radius: var(--border-radius);
  padding: 40px 30px;
  text-align: center;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(93, 95, 239, 0.1);
  transition: var(--transition);
  z-index: 1;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.feature-card:hover {
  transform: translateY(-10px);
  border-color: rgba(93, 95, 239, 0.3);
  box-shadow: 0 15px 30px rgba(93, 95, 239, 0.2);
}

.card-icon {
  width: 80px;
  height: 80px;
  background: rgba(93, 95, 239, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 25px;
  position: relative;
  z-index: 2;
}

.card-icon i {
  font-size: 36px;
  color: var(--primary);
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: white;
  position: relative;
  z-index: 2;
}

.feature-card p {
  color: var(--gray);
  position: relative;
  z-index: 2;
}

.card-hover {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(93, 95, 239, 0.05) 0%, transparent 100%);
  opacity: 0;
  transition: var(--transition);
  z-index: 0;
}

.feature-card:hover .card-hover {
  opacity: 1;
}

@media (max-width: 768px) {
  .feature-card {
    padding: 30px 20px;
  }

  .card-icon {
    width: 70px;
    height: 70px;
  margin-bottom: 20px;
  }

  .card-icon i {
    font-size: 30px;
  }
}
</style>