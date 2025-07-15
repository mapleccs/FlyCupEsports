import { defineStore } from 'pinia';
import { ref } from 'vue';
import {
  POSITIONS,
  RANKS,
  POSITION_TYPES,
  POSITION_NAMES
} from '@/constants/recruitmentConst';
import { formatTime, getRankType } from '@/utils/recruitmentUtils';

export const useRecruitmentStore = defineStore('recruitment', () => {
  // 战队招募数据
  const teamPosts = ref([
    {
      id: 1,
      title: '钻石车队招募强力打野',
      teamName: '雷霆战队',
      teamLogo: null,
      positions: ['Jungle'],
      description: '要求钻石以上，心态好，能沟通，晚上稳定在线。',
      createdAt: new Date(Date.now() - 2 * 3600 * 1000),
      rank: '钻石',
      rankType: 'info',
      server: '艾欧尼亚'
    },
    // 其他初始数据...
  ]);

  // 选手求职数据
  const playerPosts = ref([
    {
      id: 101,
      title: '王者中单寻求职业队',
      playerName: '风暴法神',
      avatar: null,
      positions: ['Mid'],
      description: '王者800点中单，擅长刺客和法师，有比赛经验。',
      createdAt: new Date(Date.now() - 3 * 3600 * 1000),
      rank: '王者',
      rankType: 'danger',
      server: '峡谷之巅'
    },
    // 其他初始数据...
  ]);

  // 添加新战队招募
  const addTeamPost = (post) => {
    teamPosts.value.unshift({
      ...post,
      id: Date.now(),
      createdAt: new Date(),
      teamLogo: null,
      rankType: getRankType(post.rank),
      server: '艾欧尼亚'
    });
  };

  // 添加新选手求职
  const addPlayerPost = (post) => {
    playerPosts.value.unshift({
      ...post,
      id: Date.now() + 1000,
      createdAt: new Date(),
      avatar: null,
      rankType: getRankType(post.rank),
      server: '艾欧尼亚'
    });
  };

  return {
    teamPosts,
    playerPosts,
    POSITIONS,
    RANKS,
    POSITION_TYPES,
    POSITION_NAMES,
    formatTime,
    addTeamPost,
    addPlayerPost
  };
});