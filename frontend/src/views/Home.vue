<template>
  <div class="home">
    <!-- 1. 顶栏大图 / 引导 -->
    <HeroSection />

    <!-- 2. 核心功能模块 -->
    <section class="features">
      <div class="feature-grid">
        <FeatureCard
          title="比赛信息"
          description="查看和管理本地赛事"
          icon="info"
        />
        <FeatureCard
          title="选手报名"
          description="安全报名参加赛事"
          icon="signup"
        />
        <FeatureCard
          title="创建队伍"
          description="与队友一起组队"
          icon="team"
        />
      </div>
    </section>

    <!-- 3. 即将开始的赛事列表 -->
    <section class="events">
      <h2>即将开始的赛事</h2>
      <div class="events-list">
        <div
          v-for="event in upcomingEvents"
          :key="event.id"
          class="event-card"
        >
          <h3>{{ event.name }}</h3>
          <p>{{ formatDate(event.start_time) }}</p>
          <RouterLink :to="`/events/${event.id}`">查看详情</RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { getUpcomingEvents } from '@/services/eventService'
import HeroSection from '@/components/ui/HeroSection.vue'
import FeatureCard from '@/components/ui/FeatureCard.vue'
import { format } from 'date-fns'

const upcomingEvents = ref([])

async function fetchEvents() {
  try {
    const { data } = await getUpcomingEvents()
    upcomingEvents.value = data
  } catch (err) {
    console.error('Failed to load events:', err)
  }
}

function formatDate(isoString) {
  return format(new Date(isoString), 'yyyy-MM-dd HH:mm')
}

onMounted(fetchEvents)
</script>

<style scoped>
.home {
  padding: 20px;
}
.features {
  margin: 40px 0;
}
.feature-grid {
  display: flex;
  gap: 20px;
  justify-content: space-around;
}
.events {
  margin-top: 60px;
}
.events-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}
.event-card {
  border: 1px solid #ddd;
  padding: 16px;
  border-radius: 8px;
  background: #fafafa;
}
.event-card h3 {
  margin-bottom: 8px;
}
.event-card p {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 12px;
}
</style>
