<template>
  <div class="team-overview" :class="{ 'team-turn': isCurrentTurn }">
    <div class="team-header">
      <div class="team-logo">
        <img :src="teamLogo" alt="队伍标志">
      </div>
      <div class="team-info">
        <h3>{{ team.name }}</h3>
        <div class="team-captain">
          <span class="captain-avatar">
            <img :src="captainAvatar" alt="队长头像">
          </span>
          <span>{{ team.captain.name }} (队长)</span>
        </div>
      </div>
      <div class="team-status">
        <el-tag v-if="checkInStatus" type="success">已签到</el-tag>
        <el-tag v-else type="danger">未签到</el-tag>
      </div>
    </div>

    <div class="team-players">
      <div v-for="player in team.players" :key="player.id" class="player-item">
        <span class="player-position">{{ player.position }}:</span>
        <span class="player-name">{{ player.name }}</span>
      </div>
    </div>

    <div class="bp-section" v-if="bans.length > 0 || picks.length > 0">
      <div class="bp-category">
        <h4>禁用英雄</h4>
        <div class="bp-heroes">
          <div v-for="(hero, index) in bans" :key="`ban-${index}`" class="bp-hero">
            <img :src="heroAvatar(hero)" :alt="hero.name" class="hero-avatar">
            <span class="hero-name">{{ hero.name }}</span>
          </div>
          <div v-for="i in (3 - bans.length)" :key="`empty-ban-${i}`" class="bp-hero empty">
            <div class="empty-slot">禁用位</div>
          </div>
        </div>
      </div>

      <div class="bp-category">
        <h4>选择英雄</h4>
        <div class="bp-heroes">
          <div v-for="(hero, index) in picks" :key="`pick-${index}`" class="bp-hero">
            <img :src="heroAvatar(hero)" :alt="hero.name" class="hero-avatar">
            <span class="hero-name">{{ hero.name }}</span>
          </div>
          <div v-for="i in (5 - picks.length)" :key="`empty-pick-${i}`" class="bp-hero empty">
            <div class="empty-slot">选择位</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useMatchStore } from '@/stores/matchStore'

const props = defineProps({
  team: Object,
  checkInStatus: Boolean,
  bans: Array,
  picks: Array
})

const matchStore = useMatchStore()

const teamLogo = computed(() => {
  return `/images/teams/${props.team.logo}`
})

const captainAvatar = computed(() => {
  return `/images/avatars/${props.team.captain.avatar}`
})

const heroAvatar = (hero) => {
  return `/images/heroes/${hero.avatar}`
}

const isCurrentTurn = computed(() => {
  return matchStore.currentTeamTurn?.id === props.team.id
})
</script>

<style scoped>
.team-overview {
  background: rgba(30, 40, 60, 0.7);
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.team-overview.team-turn {
  border-color: var(--primary);
  box-shadow: 0 0 15px rgba(93, 95, 239, 0.5);
}

.team-header {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 15px;
}

.team-logo {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 15px;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.team-logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-info {
  flex: 1;
}

.team-info h3 {
  margin: 0 0 5px;
  font-size: 1.3rem;
}

.team-captain {
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  color: var(--gray);
}

.captain-avatar {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 8px;
}

.captain-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-players {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-bottom: 20px;
}

.player-item {
  background: rgba(255, 255, 255, 0.05);
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.9rem;
}

.player-position {
  color: var(--primary);
  font-weight: 500;
  margin-right: 8px;
}

.bp-section {
  margin-top: 15px;
}

.bp-category {
  margin-bottom: 15px;
}

.bp-category h4 {
  margin: 0 0 10px;
  font-size: 1rem;
  color: var(--gray);
}

.bp-heroes {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.bp-hero {
  width: 80px;
  text-align: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 6px;
  padding: 8px;
}

.bp-hero.empty {
  opacity: 0.5;
}

.hero-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin: 0 auto 5px;
  display: block;
  background: rgba(0, 0, 0, 0.3);
}

.hero-name {
  font-size: 0.8rem;
  display: block;
}

.empty-slot {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin: 0 auto 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.2);
  font-size: 0.7rem;
  text-align: center;
  color: var(--gray);
}
</style>