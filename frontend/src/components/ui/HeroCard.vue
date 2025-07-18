<template>
  <div class="hero-card" :class="type">
    <div class="hero-avatar">
      <img :src="heroAvatar" :alt="hero.name">
    </div>
    <div class="hero-info">
      <span class="hero-name">{{ hero.name }}</span>
      <span class="hero-role">{{ hero.role }}</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  hero: Object,
  type: {
    type: String,
    default: 'pick' // 'ban' or 'pick'
  }
})

const heroAvatar = computed(() => {
  return `/images/heroes/${props.hero.avatar}`
})
</script>

<style scoped>
.hero-card {
  display: flex;
  align-items: center;
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  transition: all 0.2s ease;
}

.hero-card.ban {
  border-left: 4px solid #ff4655;
}

.hero-card.pick {
  border-left: 4px solid #4CAF50;
}

.hero-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 12px;
  background: rgba(0, 0, 0, 0.3);
}

.hero-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-info {
  display: flex;
  flex-direction: column;
}

.hero-name {
  font-weight: 500;
  font-size: 0.95rem;
}

.hero-role {
  font-size: 0.8rem;
  color: var(--gray);
}
</style>