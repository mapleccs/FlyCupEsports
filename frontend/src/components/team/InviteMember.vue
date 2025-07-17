<template>
  <div class="invite-member">
    <el-input v-model="searchQuery" placeholder="通过游戏ID或昵称搜索选手" class="search-input">
      <template #append>
        <el-button @click="searchPlayer" icon="el-icon-search"></el-button>
      </template>
    </el-input>

    <div v-if="isLoading" class="loading-state">正在搜索...</div>
    <div v-if="!isLoading && searchResults.length" class="results-list">
      <h4>搜索结果:</h4>
      <div v-for="Player in searchResults" :key="player.id" class="player-item">
        <div class="player-info">
          <span class="player-name">{{ Player.username }}</span>
          <span class="player-gameId"> ({{ Player.gameId }})</span>
        </div>
        <el-button type="primary" size="small" @click="sendInvite(player)" :disabled="player.isInvited">
          {{ Player.isInvited ? '已邀请' : '发送邀请' }}
        </el-button>
      </div>
    </div>
    <div v-if="!isLoading && searched && !searchResults.length" class="no-results">
        未找到相关选手。
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
const searchQuery = ref('');
const searchResults = ref([]);
const isLoading = ref(false);
const searched = ref(false); // 标记是否执行过搜索
const searchPlayer = () => {
  if (!searchQuery.value) return;
  isLoading.value = true;
  searched.value = true;
  // 模拟API调用
  setTimeout(() => {
    if (searchQuery.value.includes("路人")) {
      searchResults.value = [{ id: 10, username: '路人王', gameId: 'Player123', isInvited: false }];
    } else {
      searchResults.value = [];
    }
    isLoading.value = false;
  }, 500);
};
const sendInvite = (Player) => {
  // 此处调用API发送邀请
  console.log(`Inviting player:`, player);
  player.isInvited = true;
  ElMessage.success(`已向 ${player.username} 发送邀请`);
};
</script>
<style scoped>
.results-list { margin-top: 20px; }
.player-item { display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #eee; }
.player-gameId { color: #888; }
.loading-state, .no-results { text-align: center; color: #999; margin-top: 20px; }
</style>