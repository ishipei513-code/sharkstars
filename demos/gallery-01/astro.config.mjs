// @ts-check
import { defineConfig } from "astro/config";

// Production: https://{domain}/demos/gallery-01/
// If hosting on a different sub-path, adjust `base` (and `site` when domain is known).
export default defineConfig({
  site: "https://sharkstars.jp",
  base: "/demos/gallery-01",
  trailingSlash: "always",
  build: {
    assets: "_astro",
    inlineStylesheets: "auto",
  },
  compressHTML: true,
});
