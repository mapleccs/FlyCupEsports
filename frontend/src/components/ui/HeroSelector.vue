<template>
  <div class="hero-selector">
    <div class="selector-header">
      <h3>英雄选择</h3>
      <div class="action-buttons">
        <el-button
          type="danger"
          :icon="actionIcon('ban')"
          @click="setActionType('ban')"
          :class="{ active: actionType === 'ban' }"
        >
          禁用
        </el-button>
        <el-button
          type="success"
          :icon="actionIcon('pick')"
          @click="setActionType('pick')"
          :class="{ active: actionType === 'pick' }"
        >
          选择
        </el-button>
      </div>
    </div>

    <div class="hero-grid">
      <div
        v-for="hero in filteredHeroes"
        :key="hero.id"
        class="hero-item"
        @click="selectHero(hero)"
      >
        <div class="hero-avatar">
          <img :src="heroAvatar(hero)" :alt="hero.name">
        </div>
        <div class="hero-name">{{ hero.name }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  heroes: Array
})

const emit = defineEmits(['select-hero'])

const actionType = ref('ban') // 'ban' or 'pick'
const searchText = ref('')
const selectedRole = ref('')

const filteredHeroes = computed(() => {
  return props.heroes.filter(hero =>
    hero.name.toLowerCase().includes(searchText.value.toLowerCase()) &&
    (!selectedRole.value || hero.role === selectedRole.value)
  )
})

const setActionType = (type) => {
  actionType.value = type
}

const selectHero = (hero) => {
  emit('select-hero', {
    heroId: hero.id,
    actionType: actionType.value
  })
}

const heroAvatar = (hero) => {
  return `/images/heroes/${hero.avatar}`
}

const actionIcon = (type) => {
  return type === 'ban' ? 'el-icon-circle-close' : 'el-icon-circle-check'
}
</script>

<style scoped>
.hero-selector {
  background: rgba(30, 40, 60, 0.8);
  border-radius: 12px;
  padding: 20px;
  margin-top: 20px;
}

.selector-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.action-buttons .el-button {
  margin-left: 10px;
}

.action-buttons .el-button.active {
  transform: scale(1.05);
  box-shadow: 0 0 10px currentColor;
}

.hero-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
  gap: 12px;
  max-height: 300px;
  overflow-y: auto;
}

.hero-item {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  padding: 10px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.hero-item:hover {
  background: rgba(93, 95, 239, 0.2);
  transform: translateY(-3px);
}

.hero-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 8px;
  background: rgba(0, 0, 0, 0.3);
}

.hero-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-name {
  font-size: 0.8rem;
  display: block;
}
</style>