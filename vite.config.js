import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  root: 'src/frontend',
  plugins: [vue()],
  envDir: '../../',
  build: {
    rollupOptions: {
      input: 'src/frontend/index.html',
    }
  },
});
