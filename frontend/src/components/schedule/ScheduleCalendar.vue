<template>
  <div class="schedule-calendar">
    <!-- 月份导航 -->
    <div class="calendar-header">
      <el-button icon="el-icon-arrow-left" circle @click="prevMonth" />
      <h2>{{ currentMonth }}</h2>
      <el-button icon="el-icon-arrow-right" circle @click="nextMonth" />
    </div>

    <!-- 星期标题 -->
    <div class="weekdays">
      <div v-for="day in weekdayNames" :key="day" class="weekday">
        {{ day }}
      </div>
    </div>

    <!-- 日期格子 -->
    <div class="calendar-grid">
      <div
        v-for="(date, index) in calendarDays"
        :key="index"
        class="calendar-day"
        :class="{
          'current-month': date.isCurrentMonth,
          'today': date.isToday,
          'has-match': date.matches.length > 0
        }"
        @click="selectDate(date)"
      >
        <div class="day-number">{{ date.day }}</div>

        <div class="day-matches">
          <div
            v-for="match in date.matches"
            :key="match.id"
            class="match-badge"
            :class="match.status"
            @click.stop="$emit('match-selected', match)"
          >
            <div class="teams">
              {{ match.teamA.abbr }} vs {{ match.teamB.abbr }}
            </div>
            <div class="time">{{ match.time }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import dayjs from 'dayjs'
import 'dayjs/locale/zh-cn'

dayjs.locale('zh-cn')

const props = defineProps({
  matches: Array
})

const emit = defineEmits(['match-selected'])

// 当前显示的月份（默认为当前月）
const currentDate = ref(dayjs())

// 星期名称
const weekdayNames = computed(() => {
  return ['日', '一', '二', '三', '四', '五', '六']
})

// 当前月份文本
const currentMonth = computed(() => {
  return currentDate.value.format('YYYY年MM月')
})

// 生成日历天数
const calendarDays = computed(() => {
  const startOfMonth = currentDate.value.startOf('month')
  const endOfMonth = currentDate.value.endOf('month')

  // 从周日开始
  const startDay = startOfMonth.startOf('week')
  const endDay = endOfMonth.endOf('week')

  const days = []
  let day = startDay

  while (day.isBefore(endDay.add(1, 'day'))) {
    const dateStr = day.format('YYYY-MM-DD')
    const matches = props.matches.filter(match =>
      dayjs(match.date).isSame(day, 'day')
    )

    days.push({
      date: dateStr,
      day: day.date(),
      isCurrentMonth: day.isSame(currentDate.value, 'month'),
      isToday: day.isSame(dayjs(), 'day'),
      matches: matches
    })

    day = day.add(1, 'day')
  }

  return days
})

// 选择日期
const selectDate = (date) => {
  if (date.matches.length > 0) {
    // 默认选择该日期的第一场比赛
    emit('match-selected', date.matches[0])
  }
}

// 上个月
const prevMonth = () => {
  currentDate.value = currentDate.value.subtract(1, 'month')
}

// 下个月
const nextMonth = () => {
  currentDate.value = currentDate.value.add(1, 'month')
}
</script>

<style scoped>
.schedule-calendar {
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 30px;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.calendar-header h2 {
  color: #fff;
  margin: 0;
}

.weekdays {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  margin-bottom: 10px;
}

.weekday {
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
  padding: 8px 0;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
}

.calendar-day {
  min-height: 120px;
  background: rgba(30, 41, 59, 0.5);
  border-radius: 8px;
  padding: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.calendar-day:hover {
  background: rgba(56, 70, 100, 0.7);
  transform: translateY(-3px);
}

.calendar-day.current-month {
  background: rgba(30, 41, 59, 0.8);
}

.calendar-day:not(.current-month) {
  background: rgba(15, 23, 42, 0.3);
  color: #64748b;
}

.calendar-day.today {
  border: 2px solid #5d5fef;
}

.day-number {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 5px;
  color: #e2e8f0;
}

.calendar-day:not(.current-month) .day-number {
  color: #64748b;
}

.day-matches {
  overflow-y: auto;
  max-height: 90px;
}

.match-badge {
  font-size: 0.7rem;
  padding: 4px 6px;
  margin-bottom: 5px;
  border-radius: 4px;
  background: rgba(93, 95, 239, 0.2);
  color: #e2e8f0;
  cursor: pointer;
  transition: all 0.2s ease;
}

.match-badge:hover {
  background: rgba(93, 95, 239, 0.4);
}

.match-badge.live {
  background: rgba(255, 70, 85, 0.2);
  color: #ff4655;
}

.match-badge.completed {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.match-badge .teams {
  font-weight: bold;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.match-badge .time {
  font-size: 0.6rem;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .calendar-day {
    min-height: 80px;
    padding: 5px;
  }

  .day-number {
    font-size: 1rem;
  }

  .match-badge {
    font-size: 0.6rem;
    padding: 2px 4px;
  }
}
</style>