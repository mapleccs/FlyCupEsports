<template>
  <div class="banpick-panel">
    <div class="panel-header">
      <h2>
        <i class="el-icon-s-opportunity"></i>
        英雄选择阶段
        <span class="phase-tag">{{ phaseText }}</span>
      </h2>
      <p>当前轮到: <span class="current-team">{{ currentTeam?.name }}</span></p>
    </div>

    <div class="bp-actions">
      <el-button
        type="danger"
        :icon="actionIcon('ban')"
        :disabled="currentPhase !== 'banning'"
        @click="setActionType('ban')"
        :class="{ active: actionType === 'ban' }"
      >
        禁用英雄
      </el-button>

      <el-button
        type="success"
        :icon="actionIcon('pick')"
        :disabled="currentPhase !== 'picking'"
        @click="setActionType('pick')"
        :class="{ active: actionType === 'pick' }"
      >
        选择英雄
      </el-button>
    </div>

    <div class="hero-selector">
      <div class="hero-filter">
        <el-input
          v-model="searchText"
          placeholder="搜索英雄..."
          clearable
          prefix-icon="el-icon-search"
          size="medium"
        />

        <el-select v-model="selectedRole" placeholder="所有位置" clearable>
          <el-option
            v-for="role in heroRoles"
            :key="role"
            :label="role"
            :value="role"
          />
        </el-select>
      </div>

      <div class="hero-grid">
        <div
          v-for="hero in filteredHeroes"
          :key="hero.id"
          class="hero-card"
          @click="selectHero(hero)"
        >
          <div class="hero-avatar">
            <img :src="heroAvatar(hero)" :alt="hero.name">
          </div>
          <div class="hero-info">
            <span class="hero-name">{{ hero.name }}</span>
            <span class="hero-role">{{ hero.role }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="bp-history">
      <h3>BP历史记录</h3>
      <div class="history-list">
        <div v-for="(action, index) in history" :key="index" class="history-item">
          <span class="action-type" :class="action.type">{{ action.type === 'ban' ? '禁用' : '选择' }}</span>
          <span class="action-hero">{{ action.hero.name }}</span>
          <span class="action-team">by {{ action.team.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useMatchStore } from '@/stores/matchStore'

const props = defineProps({
  matchId: String,
  availableHeroes: Array,
  currentPhase: String,
  currentTeam: Object
})

const emit = defineEmits(['bp-select'])

const matchStore = useMatchStore()

const actionType = ref('ban') // 'ban' or 'pick'
const searchText = ref('')
const selectedRole = ref('')
const history = ref([])

const heroRoles = computed(() => {
  return [...new Set(props.availableHeroes.map(hero => hero.role))]
})

const filteredHeroes = computed(() => {
  let result = [...props.availableHeroes]

  if (searchText.value) {
    const search = searchText.value.toLowerCase()
    result = result.filter(hero =>
      hero.name.toLowerCase().includes(search)
    )
  }

  if (selectedRole.value) {
    result = result.filter(hero => hero.role === selectedRole.value)
  }

  return result
})

const phaseText = computed(() => {
  return props.currentPhase === 'banning' ? '禁用阶段' : '选择阶段'
})

const setActionType = (type) => {
  actionType.value = type
}

const selectHero = (hero) => {
  if (!props.currentTeam) return

  emit('bp-select', {
    heroId: hero.id,
    actionType: actionType.value
  })

  // 添加到历史记录
  history.value.unshift({
    type: actionType.value,
    hero: hero,
    team: props.currentTeam,
    time: new Date().toLocaleTimeString()
  })
}

const heroAvatar = (hero) => {
  return `/images/heroes/${hero.avatar}`
}

const actionIcon = (type) => {
  return type === 'ban' ? 'el-icon-circle-close' : 'el-icon-circle-check'
}

// 当阶段变化时重置操作类型
watch(() => props.currentPhase, (newPhase) => {
  actionType.value = newPhase === 'banning' ? 'ban' : 'pick'
})
</script>

<style scoped>
.banpick-panel {
  padding: 20px;
}

.panel-header {
  text-align: center;
  margin-bottom: 25px;
}

.panel-header h2 {
  font-size: 1.8rem;
  margin-bottom: 10px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.phase-tag {
  background: var(--primary);
  color: white;
  font-size: 0.9rem;
  padding: 3px 10px;
  border-radius: 20px;
  vertical-align: middle;
}

.panel-header p {
  color: var(--gray);
  font-size: 1.1rem;
}

.current-team {
  color: #ff9800;
  font-weight: 600;
}

.bp-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 30px;
}

.bp-actions .el-button {
  width: 150px;
  font-size: 1.1rem;
  padding: 15px 0;
}

.bp-actions .el-button.active {
  transform: scale(1.05);
  box-shadow: 0 0 15px currentColor;
}

.hero-filter {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.hero-filter .el-input {
  flex: 1;
}

.hero-filter .el-select {
  width: 150px;
}

.hero-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 15px;
  max-height: 300px;
  overflow-y: auto;
  padding: 10px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
}

.hero-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  padding: 10px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.hero-card:hover {
  background: rgba(93, 95, 239, 0.2);
  transform: translateY(-3px);
}

.hero-avatar {
  width: 70px;
  height: 70px;
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
  display: block;
  font-weight: 500;
  font-size: 0.9rem;
}

.hero-role {
  display: block;
  font-size: 0.8rem;
  color: var(--gray);
}

.bp-history {
  margin-top: 30px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  padding: 15px;
}

.bp-history h3 {
  margin-top: 0;
  margin-bottom: 15px;
  text-align: center;
  color: var(--gray);
}

.history-list {
  max-height: 150px;
  overflow-y: auto;
}

.history-item {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  margin-bottom: 8px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 6px;
}

.action-type {
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-right: 10px;
}

.action-type.ban {
  background: rgba(255, 70, 85, 0.3);
  color: #ff4655;
}

.action-type.pick {
  background: rgba(76, 175, 80, 0.3);
  color: #4CAF50;
}

.action-hero {
  flex: 1;
  font-weight: 500;
}

.action-team {
  color: var(--gray);
  font-size: 0.9rem;
}
</style>