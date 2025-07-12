<template>
  <footer class="app-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h3 class="footer-title">Fly Cup 电竞平台</h3>
          <p class="footer-desc">
            专业级英雄联盟线上赛事管理平台，为赛事方和玩家提供一站式服务
          </p>
          <div class="social-links">
            <a href="#" class="social-link">
              <i class="el-icon-weibo"></i>
            </a>
            <a href="#" class="social-link">
              <i class="el-icon-chat-dot-round"></i>
            </a>
            <a href="#" class="social-link">
              <i class="el-icon-video-camera"></i>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4 class="footer-subtitle">快速链接</h4>
          <ul class="footer-links">
            <li><RouterLink to="/">首页</RouterLink></li>
            <li><RouterLink to="/events">赛事列表</RouterLink></li>
            <li><RouterLink to="/teams">战队排行</RouterLink></li>
            <li><RouterLink to="/videos">精彩视频</RouterLink></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-subtitle">赛事服务</h4>
          <ul class="footer-links">
            <li><RouterLink to="/signup">选手报名</RouterLink></li>
            <li><RouterLink to="/create-team">创建战队</RouterLink></li>
            <li><RouterLink to="/rules">赛事规则</RouterLink></li>
            <li><RouterLink to="/partners">合作申请</RouterLink></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-subtitle">联系我们</h4>
          <ul class="footer-contacts">
            <li><i class="el-icon-phone"></i> 400-888-8888</li>
            <li><i class="el-icon-message"></i> contact@flycup.com</li>
            <li><i class="el-icon-location"></i> 上海市浦东新区电竞中心</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2023 Fly Cup 电竞平台 - 英雄联盟地方赛事管理系统</p>
        <div class="footer-links">
          <RouterLink to="/privacy">隐私政策</RouterLink>
          <RouterLink to="/terms">服务条款</RouterLink>
          <RouterLink to="/help">帮助中心</RouterLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.app-footer {
  background: var(--dark);
  padding: 60px 0 20px;
  border-top: 1px solid rgba(93, 95, 239, 0.1);
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-col {
  margin-bottom: 20px;
}

.footer-title {
  font-size: 1.5rem;
  margin-bottom: 15px;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.footer-desc {
  color: var(--gray);
  line-height: 1.7;
  margin-bottom: 20px;
}

.social-links {
  display: flex;
  gap: 15px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  color: var(--gray);
  transition: all 0.3s ease;
}

.social-link:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-3px);
}

.footer-subtitle {
  font-size: 1.2rem;
  margin-bottom: 20px;
  color: white;
  position: relative;
  padding-bottom: 10px;
}

.footer-subtitle::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 3px;
  background: linear-gradient(to right, #5d5fef, #ff4655);
  border-radius: 2px;
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: var(--gray);
  transition: all 0.3s ease;
  text-decoration: none;
}

.footer-links a:hover {
  color: var(--primary);
  padding-left: 5px;
}

.footer-contacts {
  list-style: none;
  padding: 0;
}

.footer-contacts li {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  color: var(--gray);
}

.footer-contacts i {
  margin-right: 10px;
  color: var(--primary);
  font-size: 1.1rem;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding-top: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  color: var(--gray);
  font-size: 0.9rem;
}

.footer-bottom p {
  margin: 5px 0;
}

.footer-bottom .footer-links {
  display: flex;
  gap: 20px;
}

@media (max-width: 768px) {
  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: 10px;
  }

  .footer-bottom .footer-links {
    justify-content: center;
  }
}
</style>