import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'


if (import.meta.hot) {
  import.meta.hot.on('vite:beforeUpdate', () => {
    console.log('[HMR] 热更新即将触发');
  });

  import.meta.hot.on('vite:afterUpdate', () => {
    console.log('[HMR] 热更新已完成');
  });

  import.meta.hot.on('vite:error', (error) => {
    console.error('[HMR] 热更新错误', error);
  });
}

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(ElementPlus)
app.mount('#app');
