<template>
  <div class="player-radar-chart">
    <h3 class="section-title">个人选手数据雷达图</h3>
    <div ref="radarChartRef" class="radar-chart-container"></div>
    <div class="radar-legend">
      <div v-for="(item, index) in radarData.indicator" :key="index" class="legend-item">
        <div class="legend-color" :style="{ backgroundColor: legendColors[index] }"></div>
        <span>{{ item.name }}: {{ radarData.value[index] }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue';
import * as echarts from 'echarts';

const props = defineProps({
  radarData: {
    type: Object,
    required: true,
    default: () => ({ indicator: [], value: [] })
  }
});

const legendColors = ref(['#5d5fef', '#ff4655', '#0ea5e9', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444', '#f97316', '#84cc16', '#14b8a6', '#3b82f6', '#a855f7']);
const radarChartRef = ref(null);
let chartInstance = null;

const initChart = () => {
  if (!radarChartRef.value) return;
  if (chartInstance) {
    chartInstance.dispose();
  }

  chartInstance = echarts.init(radarChartRef.value, 'dark');

  const option = {
    tooltip: { trigger: 'item' },
    radar: {
      indicator: props.radarData.indicator,
      radius: '80%',
      center: ['50%', '50%'],
      axisName: {
        color: '#94a3b8',
        fontSize: 12,
        padding: [3, 5],
        backgroundColor: 'rgba(15, 23, 42, 0.7)',
        borderRadius: 3
      },
      splitArea: { areaStyle: { color: ['rgba(30, 41, 59, 0.5)', 'rgba(30, 41, 59, 0.3)'] } },
      splitLine: { lineStyle: { color: 'rgba(148, 163, 184, 0.3)' } },
      axisLine: { lineStyle: { color: 'rgba(148, 163, 184, 0.5)' } }
    },
    series: [{
      type: 'radar',
      data: [{
        value: props.radarData.value,
        name: '选手能力值',
        symbol: 'circle',
        symbolSize: 8,
        lineStyle: { width: 2, color: '#5d5fef' },
        areaStyle: {
          color: new echarts.graphic.RadialGradient(0.5, 0.5, 1, [
            { offset: 0, color: 'rgba(93, 95, 239, 0.4)' },
            { offset: 1, color: 'rgba(93, 95, 239, 0.1)' }
          ])
        },
        itemStyle: { color: '#5d5fef' },
        label: { show: true, formatter: params => params.value, position: 'top', color: '#e2e8f0', fontSize: 12 }
      }]
    }],
    backgroundColor: 'transparent',
    textStyle: { color: '#e2e8f0' }
  };

  chartInstance.setOption(option);
};

const handleResize = () => {
  if (chartInstance) {
    chartInstance.resize();
  }
};

onMounted(() => {
  nextTick(() => {
    initChart();
    window.addEventListener('resize', handleResize);
  });
});

onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.dispose();
  }
  window.removeEventListener('resize', handleResize);
});

// 监听数据变化，重新渲染图表
watch(() => props.radarData, (newData) => {
  if (newData) {
    initChart();
  }
}, { deep: true });
</script>

<style scoped>
/* 样式与原Profile.vue中一致 */
.player-radar-chart {
  margin-top: 30px;
  background: rgba(15, 23, 42, 0.7);
  border-radius: 12px;
  padding: 20px;
  border: 1px solid rgba(93, 95, 239, 0.2);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.section-title {
  color: white;
  font-size: 1.4rem;
  margin-bottom: 20px;
  text-align: center;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.radar-chart-container {
  height: 400px;
  width: 100%;
}

.radar-legend {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.legend-color {
  width: 16px;
  height: 16px;
  border-radius: 4px;
}
</style>