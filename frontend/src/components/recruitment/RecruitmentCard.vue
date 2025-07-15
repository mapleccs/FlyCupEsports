<template>
  <div class="post-card" :class="type">
    <div class="card-header">
      <div class="logo-wrapper">
        <img
          :src="type === 'team'
            ? (post.teamLogo || '/images/teams/default-logo.png')
            : (post.avatar || '/images/users/default-avatar.png')"
          class="logo"
        />
      </div>
      <div class="info">
        <h3>{{ post.title }}</h3>
        <div class="meta-info">
          <span class="name">
            {{ type === 'team' ? post.teamName : post.playerName }}
          </span>
          <el-tag effect="dark" size="mini" :type="post.rankType">
            {{ post.rank }}
          </el-tag>
          <el-tag size="mini" type="info">{{ post.server }}</el-tag>
        </div>
      </div>
    </div>

    <div class="card-body">
      <div class="positions">
        <strong>{{ type === 'team' ? '需要位置:' : '擅长位置:' }}</strong>
        <el-tag
          v-for="pos in post.positions"
          :key="pos"
          class="pos-tag"
          size="small"
          :type="POSITION_TYPES[pos]"
        >
          {{ POSITION_NAMES[pos] }}
        </el-tag>
      </div>
      <p class="description">{{ post.description }}</p>
    </div>

    <div class="card-footer">
      <span class="post-time">发布于: {{ formatTime(post.createdAt) }}</span>
      <el-button
        :type="type === 'team' ? 'primary' : 'success'"
        size="small"
        @click="handleAction"
        plain
        round
      >
        {{ type === 'team' ? '申请加入' : '联系选手' }}
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import { useRecruitmentStore } from '@/stores/recruitmentStore';

const props = defineProps({
  post: Object,
  type: String
});

const emit = defineEmits(['apply', 'contact']);

const {
  formatTime,
  POSITION_TYPES,
  POSITION_NAMES
} = useRecruitmentStore();

// 处理按钮点击
const handleAction = () => {
  if (props.type === 'team') {
    emit('apply', props.post);
  } else {
    emit('contact', props.post);
  }
};
</script>

<style scoped>
.post-card {
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
  border: 1px solid rgba(93, 95, 239, 0.2);
  border-radius: 10px;
  padding: 20px;
  transition: all 0.3s ease;
  min-height: 250px;
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-3px);
    border-color: #5d5fef;
    box-shadow: 0 5px 15px rgba(93, 95, 239, 0.2);
  }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 15px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 15px;
  margin-bottom: 15px;

  .logo-wrapper {
    flex-shrink: 0;
  }

  .logo {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 2px solid rgba(93, 95, 239, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  h3 {
    margin: 0 0 5px 0;
    color: white;
    font-size: 1.2rem;
    font-weight: 600;
    line-height: 1.3;
  }

  .meta-info {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  .name {
    color: #94a3b8;
    font-size: 0.85rem;
  }

  .el-tag {
    font-weight: 600;
    border: none;
    height: 22px;
    line-height: 22px;
    padding: 0 6px;
  }
}

.card-body {
  flex: 1;
  .positions {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
    flex-wrap: wrap;

    strong {
      color: #e2e8f0;
      font-weight: 600;
      font-size: 0.9rem;
    }

    .pos-tag {
      font-weight: 600;
      height: 26px;
      line-height: 24px;
    }
  }

  .description {
    color: #cbd5e1;
    line-height: 1.6;
    font-size: 0.95rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}

.card-footer {
  margin-top: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #94a3b8;
  font-size: 0.8rem;

  .post-time {
    font-style: italic;
  }

  .el-button {
    padding: 7px 15px;
    font-size: 0.85rem;
  }
}

@media (max-width: 900px) {
  .post-card {
    padding: 15px;
  }
}
</style>