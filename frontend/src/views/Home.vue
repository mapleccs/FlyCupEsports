<template>
  <div class="home">
    <HeroSection />
    <section id="intro" class="features">
      <div class="section-header">
        <h2 class="section-title">核心功能</h2>
        <p class="section-subtitle">一站式英雄联盟赛事管理平台</p>
      </div>
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

    <section class="events">
      <div class="section-header">
        <h2 class="section-title">即将开始的赛事</h2>
        <p class="section-subtitle">不要错过这些精彩比赛</p>
      </div>
      <div class="events-list">
        <div
          v-for="event in upcomingEvents"
          :key="event.id"
          class="event-card"
        >
          <div class="event-badge">即将开始</div>
          <div class="event-content">
            <h3>{{ event.name }}</h3>
            <div class="event-meta">
              <i class="el-icon-time"></i>
              <span>{{ formatDate(event.start_time) }}</span>
            </div>
            <RouterLink :to="`/events/${event.id}`" class="event-link">
              查看详情 <i class="el-icon-right"></i>
            </RouterLink>
          </div>
        </div>
      </div>
      <div class="view-all">
        <RouterLink to="/events" class="btn-secondary">
          查看全部赛事 <i class="el-icon-right"></i>
        </RouterLink>
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
    upcomingEvents.value = data.slice(0, 4) // 只显示前4个
  } catch (err) {
    console.error('Failed to load events:', err)
  }
}

function formatDate(isoString) {
  return format(new Date(isoString), 'yyyy年MM月dd日 HH:mm')
}

onMounted(fetchEvents)
</script>

<style scoped>
.home {
  padding: 0;
  max-width: 1400px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 40px;
}

.section-title {
  font-size: 2.2rem;
  font-weight: 700;
  background: linear-gradient(to right, #5d5fef, #DE4344);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 12px;
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(to right, #5d5fef, #DE4344);
  border-radius: 2px;
}

.section-subtitle {
  color: var(--gray);
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto;
}

/* 功能区域 */
.features {
  padding: 100px 20px 80px;
  background: var(--dark);
  position: relative;
  overflow: hidden;
}

.features::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(to right, #171624, #DE4344);
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

/* 赛事区域 */
.events {
  padding: 0 20px 80px;
  background: url('@/assets/images/dot-pattern.png') var(--darker);
}

.events-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
  max-width: 1200px;
  margin: 0 auto 40px;
}

.event-card {
  background: rgba(15, 23, 42, 0.7);
  border-radius: var(--border-radius);
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(93, 95, 239, 0.2);
  transition: var(--transition);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

.event-card:hover {
  transform: translateY(-8px);
  border-color: rgba(93, 95, 239, 0.5);
  box-shadow: 0 15px 35px rgba(93, 95, 239, 0.3);
}

.event-badge {
  position: absolute;
  top: 15px;
  right: -30px;
  background: var(--secondary);
  color: white;
  padding: 5px 30px;
  font-size: 0.85rem;
  font-weight: 600;
  transform: rotate(45deg);
  box-shadow: 0 2px 10px rgba(255, 70, 85, 0.3);
}

.event-content {
  padding: 30px;
}

.event-card h3 {
  font-size: 1.4rem;
  margin-bottom: 15px;
  color: white;
}

.event-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--gray);
  margin-bottom: 20px;
  font-size: 0.95rem;
}

.event-meta i {
  color: var(--primary);
}

.event-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--primary);
  font-weight: 600;
  transition: var(--transition);
}

.event-link:hover {
  color: var(--secondary);
  text-decoration: none;
  gap: 12px;
}

.view-all {
  text-align: center;
  margin-top: 30px;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
  padding: 12px 30px;
  border-radius: 30px;
  font-weight: 600;
  transition: var(--transition);
}

.btn-secondary:hover {
  background: rgba(93, 95, 239, 0.1);
  color: white;
  text-decoration: none;
  gap: 12px;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .section-title {
    font-size: 1.8rem;
  }

  .features, .events {
    padding: 60px 20px;
  }

  .feature-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .event-card {
    margin-bottom: 20px;
  }
}
</style>