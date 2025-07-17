<template>
  <div class="schedule-filter">
    <el-row :gutter="20" justify="center">
      <el-col :xs="24" :sm="8" :md="6">
        <div class="filter-item">
          <label>赛事类型:</label>
          <el-select
            v-model="tournamentFilter"
            placeholder="选择赛事"
            clearable
          >
            <el-option label="全部赛事" value="all" />
            <el-option
              v-for="tournament in tournaments"
              :key="tournament.id"
              :label="tournament.name"
              :value="tournament.id"
            />
          </el-select>
        </div>
      </el-col>

      <el-col :xs="24" :sm="8" :md="6">
        <div class="filter-item">
          <label>战队筛选:</label>
          <el-select
            v-model="teamFilter"
            placeholder="选择战队"
            clearable
          >
            <el-option label="全部战队" value="all" />
            <el-option
              v-for="team in teams"
              :key="team.id"
              :label="team.name"
              :value="team.id"
            >
              <div class="team-option">
                <img :src="team.logo" class="team-logo" />
                <span>{{ team.name }}</span>
              </div>
            </el-option>
          </el-select>
        </div>
      </el-col>

      <el-col :xs="24" :sm="8" :md="6">
        <div class="filter-item">
          <label>比赛状态:</label>
          <el-select
            v-model="statusFilter"
            placeholder="选择状态"
            clearable
          >
            <el-option label="全部状态" value="all" />
            <el-option label="未开始" value="upcoming" />
            <el-option label="进行中" value="live" />
            <el-option label="已结束" value="completed" />
          </el-select>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  teams: Array,
  tournaments: Array
})

const emit = defineEmits(['filter-change'])

const tournamentFilter = ref('all')
const teamFilter = ref('all')
const statusFilter = ref('all')

watch([tournamentFilter, teamFilter, statusFilter], () => {
  emit('filter-change', {
    tournament: tournamentFilter.value,
    team: teamFilter.value,
    status: statusFilter.value
  })
})
</script>

<style scoped>
.schedule-filter {
  margin: 20px 0;
}

.filter-item {
  display: flex;
  flex-direction: column;
}

.filter-item label {
  margin-bottom: 8px;
  color: #cbd5e1;
  font-size: 0.9rem;
}

.team-option {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 24px;
  height: 24px;
  margin-right: 10px;
  object-fit: contain;
}

@media (max-width: 768px) {
  .el-col {
    margin-bottom: 15px;
  }
}
</style>