<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* 全局样式 */
:root {
  --primary: #5d5fef;
  --primary-dark: #4a4cbf;
  --secondary: #ff4655;
  --dark: #0f172a;
  --darker: #0a0f1f;
  --light: #f8fafc;
  --gray: #94a3b8;
  --border-radius: 12px;
  --transition: all 0.3s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: var(--darker);
  color: var(--light);
  line-height: 1.6;
}

/* 滚动条美化 */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: var(--darker);
}

::-webkit-scrollbar-thumb {
  background: var(--primary);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--primary-dark);
}

/* 链接样式 */
a {
  color: var(--primary);
  text-decoration: none;
  transition: var(--transition);
}

a:hover {
  color: var(--secondary);
  text-decoration: underline;
}
</style>