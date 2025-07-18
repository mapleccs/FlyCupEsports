<template>
  <div class="banpick-panel">
    <div class="panel-header">
      <h3>英雄选择阶段</h3>
      <p>禁用和选择英雄</p>
    </div>

    <div class="bp-container">
      <div class="ban-section">
        <h4>禁用阶段</h4>
        <div class="ban-cards">
          <HeroCard
            v-for="(hero, index) in bans"
            :key="`ban-${index}`"
            :hero="hero"
            type="ban"
          />
        </div>
      </div>

      <div class="pick-section">
        <h4>选择阶段</h4>
        <div class="pick-cards">
          <HeroCard
            v-for="(hero, index) in picks"
            :key="`pick-${index}`"
            :hero="hero"
            type="pick"
          />
        </div>
      </div>
    </div>

    <div class="hero-selector">
      <HeroSelector @select-hero="handleHeroSelection" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeroCard from '@/components/ui/HeroCard.vue'
import HeroSelector from '@/components/ui/HeroSelector.vue'

const bans = ref([])
const picks = ref([])

const handleHeroSelection = (hero, actionType) => {
  if (actionType === 'ban') {
    bans.value.push(hero)
  } else {
    picks.value.push(hero)
  }
}
</script>