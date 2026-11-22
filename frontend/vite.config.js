import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  resolve: { preserveSymlinks: true },
  server: {
    proxy: {
      '/api': {
        target: process.env.AIRLEDGER_DEV_API_URL || 'http://127.0.0.1:5000',
        changeOrigin: true,
      }
    }
  }
})

