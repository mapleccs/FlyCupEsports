// 格式化时间
export const formatTime = (date) => {
  const now = new Date();
  const diff = Math.floor((now - date) / 1000);

  if (diff < 60) return '刚刚';
  if (diff < 3600) return `${Math.floor(diff / 60)}分钟前`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}小时前`;

  return date.toLocaleDateString();
};

// 根据段位获取标签类型
export const getRankType = (rank) => {
  if (!rank) return '';
  if (rank.includes('王者')) return 'danger';
  if (rank.includes('宗师') || rank.includes('大师')) return 'danger';
  if (rank.includes('钻石')) return 'info';
  if (rank.includes('铂金')) return '';
  if (rank.includes('黄金')) return 'warning';
  return '';
};

// 过滤帖子
export const filterPosts = (posts, filterConfig) => {
  return posts.filter(post => {
    // 位置匹配
    const positionMatch = filterConfig.position
      ? post.positions.includes(filterConfig.position)
      : true;

    // 段位匹配
    const rankMatch = filterConfig.rank
      ? post.rank.includes(filterConfig.rank)
      : true;

    // 关键词匹配
    let keywordMatch = true;
    if (filterConfig.keyword) {
      const keyword = filterConfig.keyword.toLowerCase();
      keywordMatch = (
        (post.title && post.title.toLowerCase().includes(keyword)) ||
        (post.description && post.description.toLowerCase().includes(keyword)) ||
        (post.teamName && post.teamName.toLowerCase().includes(keyword)) ||
        (post.playerName && post.playerName.toLowerCase().includes(keyword))
      );
    }

    // 组合匹配条件
    return positionMatch &&
           (filterConfig.rank ? rankMatch : true) &&
           keywordMatch;
  });
};