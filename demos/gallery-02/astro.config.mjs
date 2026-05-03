// @ts-check
import { defineConfig } from 'astro/config';

// Production: https://sharkstars.jp/demos/gallery-02/
export default defineConfig({
  site: 'https://sharkstars.jp',
  base: '/demos/gallery-02',
  trailingSlash: 'always',
  build: {
    assets: '_astro',
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
});
