import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,     // Exposes to 0.0.0.0 inside Docker
    port: 3000      // Port to match your docker-compose exposed port
  }
});
