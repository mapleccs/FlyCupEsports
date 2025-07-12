<template>
  <div class="hero">
    <div class="hero-content">
      <p>专业级英雄联盟线上赛事管理平台</p>
      <div class="hero-buttons">
        <button @click="scrollToIntro" class="btn-primary">了解更多</button>
        <RouterLink to="/events" class="btn-outline">查看赛事</RouterLink>
      </div>
    </div>
    <div class="hero-pattern"></div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function scrollToIntro() {
  // 如果已经在首页，直接滚动到锚点
  if (router.currentRoute.value.name === 'Home') {
    const introElement = document.getElementById('intro')
    if (introElement) {
      window.scrollTo({
        top: introElement.offsetTop,
        behavior: 'smooth'
      })
    }
  } else {
    // 如果不在首页，导航到首页并滚动
    router.push({ name: 'Home', hash: '#intro' })
  }
}
</script>

<style scoped>
.hero {
  /* 核心：让大图自动等比裁剪并充满 */
  background-image: url(~@/assets/images/home-bg.png);
  background-size: cover;            /* 等比裁剪，始终填满 */
  background-position: center center;/* 中心对齐 */
  background-repeat: no-repeat;      /* 不重复 */

  /* 原有布局 */
  height: 80vh;
  min-height: 600px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  overflow: hidden;
}

/* 网格叠加层（可选保留） */
.hero::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  /* background: url(~@/assets/images/grid-pattern1.png); */
  opacity: 0.15;
  z-index: 1;
}

/* 内容置顶 */
.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 800px;
  padding: 0 20px;
}

.hero h1 {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  background: linear-gradient(to right, #fff 0%, #ff4655 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.hero p {
  /* 基础字体设置 */
  font-size: 1.3rem;                /* 略微缩小一点，避免太“霸占”视野 */
  line-height: 1.6;                 /* 宽松行高，更易阅读 */
  letter-spacing: 0.02em;           /* 轻微字距，让字形更通透 */
  text-align: center;               /* 居中排版 */

  /* 颜色&阴影 */
  color: rgba(255, 255, 255, 0.9);   /* 半透明白，既不会死白也有足够对比 */
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);

  /* 宽度&间距 */
  max-width: 600px;
  margin: 0 auto 2.5rem;            /* 底部留白：2.5rem */

  /* 背景高亮（可选） */
  padding: 0.6rem 1rem;
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 6px;

  /* 动画效果（可选） */
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.8s ease-out 0.4s forwards;
}

/* 伪元素装饰（可选） */
.hero p::before {
  content: 'Fly Cup';
  display: block;
  font-size: 3rem;
  line-height: 1;
  margin-bottom: 0.5rem;
  color: var(--primary);
  opacity: 0.8;
}

/* Fade-in 动画 keyframes */
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-buttons {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.btn-primary {
  background: var(--primary);
  color: #fff;
  padding: 14px 36px;
  border-radius: 30px;
  font-weight: 600;
  font-size: 1.1rem;
  border: none;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 4px 15px rgba(93, 95, 239, 0.4);
}
.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-3px);
  box-shadow: 0 7px 20px rgba(93, 95, 239, 0.6);
  text-decoration: none;
}

.btn-outline {
  background: transparent;
  color: #fff;
  padding: 14px 36px;
  border-radius: 30px;
  font-weight: 600;
  font-size: 1.1rem;
  border: 2px solid #fff;
  cursor: pointer;
  transition: var(--transition);
}
.btn-outline:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-3px);
  text-decoration: none;
}

/* 底部光斑 */
.hero-pattern {
  position: absolute;
  bottom: -10%;
  left: -10%;
  width: 50%;
  height: 50%;
  background: radial-gradient(circle, rgba(93, 95, 239, 0.15) 0%, transparent 70%);
  border-radius: 50%;
  z-index: 1;
}

@media (max-width: 768px) {
  .hero {
    height: 70vh;
    min-height: 500px;
  }
  .hero h1 {
    font-size: 2.5rem;
  }
  .hero p {
    font-size: 1.1rem;
  }
  .btn-primary,
  .btn-outline {
    padding: 12px 24px;
    font-size: 1rem;
  }
}
</style>
