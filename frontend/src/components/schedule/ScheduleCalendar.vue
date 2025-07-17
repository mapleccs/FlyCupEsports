<template>
  <div class="schedule-calendar">
    <div class="calendar-header">
      <el-button class="nav-btn" icon="el-icon-arrow-left" circle @click="prevMonth" />
      <h2>{{ currentMonth }}</h2>
      <el-button class="nav-btn" icon="el-icon-arrow-right" circle @click="nextMonth" />
    </div>

    <div class="weekdays">
      <div v-for="day in weekdayNames" :key="day" class="weekday">
        {{ day }}
      </div>
    </div>

    <div class="calendar-grid">
      <div
        v-for="(date, index) in calendarDays"
        :key="index"
        class="calendar-day"
        :class="{
          'not-current-month': !date.isCurrentMonth,
          'today': date.isToday,
          'has-match': date.matches.length > 0
        }"
        @click="selectDate(date)"
      >
        <div class="day-number-wrapper">
            <span class="day-number">{{ date.day }}</span>
        </div>

        <div class="day-matches">
          <div
            v-for="match in date.matches"
            :key="match.id"
            class="match-badge"
            @click.stop="$emit('match-selected', match)"
          >
            <span class="match-status-dot" :class="match.status"></span>
            <div class="match-info">
                <div class="teams">
                {{ match.teamA.abbr }} vs {{ match.teamB.abbr }}
                </div>
                <div class="time">{{ match.time }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import dayjs from 'dayjs'
import 'dayjs/locale/zh-cn'

dayjs.locale('zh-cn')

const props = defineProps({
  matches: Array
})

const emit = defineEmits(['match-selected'])

const currentDate = ref(dayjs())

const weekdayNames = computed(() => {
  return ['日', '一', '二', '三', '四', '五', '六']
})

const currentMonth = computed(() => {
  return currentDate.value.format('YYYY年 MMMM')
})

const calendarDays = computed(() => {
  const startOfMonth = currentDate.value.startOf('month')
  const endOfMonth = currentDate.value.endOf('month')
  const startDay = startOfMonth.startOf('week')
  const endDay = endOfMonth.endOf('week')

  const days = []
  let day = startDay

  while (day.isBefore(endDay.add(1, 'day'))) {
    const dateStr = day.format('YYYY-MM-DD')
    const matchesOnDate = props.matches
      .filter(match => dayjs(match.date).isSame(day, 'day'))
      .sort((a, b) => a.time.localeCompare(b.time)); // 按时间排序

    days.push({
      date: dateStr,
      day: day.date(),
      isCurrentMonth: day.isSame(currentDate.value, 'month'),
      isToday: day.isSame(dayjs(), 'day'),
      matches: matchesOnDate
    })
    day = day.add(1, 'day')
  }

  return days
})

const selectDate = (date) => {
  if (date.matches.length > 0) {
    emit('match-selected', date.matches[0])
  }
}

const prevMonth = () => {
  currentDate.value = currentDate.value.subtract(1, 'month')
}

const nextMonth = () => {
  currentDate.value = currentDate.value.add(1, 'month')
}
</script>

<style scoped>
/* 整体容器：增加玻璃拟态效果和精致边框 */
.schedule-calendar {
  background: rgba(25, 35, 59, 0.6); /* 加深背景以便玻璃效果更明显 */
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 30px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

/* 头部优化 */
.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding: 0 10px;
}

.calendar-header h2 {
  color: #f1f5f9;
  margin: 0;
  font-size: 1.8rem;
  font-weight: 600;
  letter-spacing: 1px;
}

.nav-btn {
    background-color: rgba(255, 255, 255, 0.1);
    border: none;
    color: #cbd5e1;
}
.nav-btn:hover {
    background-color: rgba(255, 255, 255, 0.2);
    color: #fff;
}


/* 星期标题 */
.weekdays {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
  margin-bottom: 12px;
}

.weekday {
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 10px 0;
}

/* 日期网格 */
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: minmax(140px, auto); /* 保证格子有最小高度，且可自适应增高 */
  gap: 8px;
}

/* 日期格子 */
.calendar-day {
  background: rgba(30, 41, 59, 0.6);
  border-radius: 8px;
  padding: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid transparent;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.calendar-day:hover {
  background: rgba(56, 70, 100, 0.8);
  transform: translateY(-4px);
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

/* 非当前月份的日期 */
.calendar-day.not-current-month {
  background: rgba(15, 23, 42, 0.4);
}
.calendar-day.not-current-month .day-number,
.calendar-day.not-current-month .teams,
.calendar-day.not-current-month .time {
  color: #64748b;
  opacity: 0.7;
}

/* “今日”高亮效果 */
.calendar-day.today {
  position: relative;
  background: rgba(93, 95, 239, 0.2);
  border: 1px solid rgba(93, 95, 239, 0.8);
  box-shadow: 0 0 20px rgba(93, 95, 239, 0.5);
}
.calendar-day.today .day-number {
    color: #fff;
}


/* 日期数字 */
.day-number-wrapper {
    margin-bottom: 8px;
}
.day-number {
  font-size: 1rem;
  font-weight: bold;
  color: #cbd5e1;
  padding: 4px 6px;
  border-radius: 50%;
  transition: all 0.3s ease;
}


/* 比赛列表容器 */
.day-matches {
  overflow-y: auto;
  flex-grow: 1; /* 占据剩余空间 */
}

/* 赛事标签美化 */
.match-badge {
  display: flex;
  align-items: center;
  padding: 5px;
  margin-bottom: 6px;
  border-radius: 6px;
  background: rgba(15, 23, 42, 0.5);
  transition: background 0.2s ease;
  width: 100%;
}
.match-badge:hover {
  background: rgba(93, 95, 239, 0.3);
}
/* 状态小圆点 */
.match-status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 8px;
    flex-shrink: 0;
    background-color: #64748b; /* 默认/未开始 */
}
.match-status-dot.live {
    background-color: #ef4444; /* 直播中 */
    box-shadow: 0 0 5px #ef4444;
}
.match-status-dot.completed {
    background-color: #22c55e; /* 已结束 */
}

.match-info {
    overflow: hidden;
}

.match-badge .teams {
  font-size: 0.75rem;
  font-weight: bold;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: #e2e8f0;
}

.match-badge .time {
  font-size: 0.65rem;
  color: #94a3b8;
}

/* 滚动条美化 */
.day-matches::-webkit-scrollbar {
  width: 4px;
}
.day-matches::-webkit-scrollbar-thumb {
  background: rgba(93, 95, 239, 0.5);
  border-radius: 2px;
}
.day-matches::-webkit-scrollbar-track {
  background: transparent;
}


/* 响应式布局 */
@media (max-width: 768px) {
  .schedule-calendar { padding: 16px; }
  .calendar-header h2 { font-size: 1.5rem; }
  .calendar-grid { grid-auto-rows: minmax(100px, auto); }
  .day-number { font-size: 0.85rem; }
  .match-badge .teams { font-size: 0.65rem; }
}
</style>