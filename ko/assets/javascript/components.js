/* ============================================
   KOJP — Components Loader
   Dynamically injects shared header & footer
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  const isKorean = document.documentElement.lang === 'ko';
  loadHeader(isKorean);
  loadFooter(isKorean);
});


/* ── Header ──────────────────────────────── */

function loadHeader(isKo) {
  const placeholder = document.getElementById('header-placeholder');
  if (!placeholder) return;

  // Absolute language root — avoids all relative-path ambiguity for nav & logo
  const langRoot = isKo ? '/ko/' : '/ko/ja/';

  // Blog is hidden from navigation on both languages.
  //   - Korean blog → published on Naver Blog (external)
  //   - Japanese blog → exists but not promoted in nav (SEO-only access)
  const showBlog = false;

  const navText = {
    services: isKo ? '서비스' : 'サービス',
    pricing: isKo ? '요금' : '料金',
    process: isKo ? '진행 과정' : 'フロー',
    cases: isKo ? '도입 사례' : '事例',
    blog: 'ブログ',
    faq: isKo ? 'FAQ' : 'FAQ',
    cta: isKo ? '무료 진단 받기' : '無料診断を受ける',
    ctaSm: isKo ? '무료 진단' : '無料診断',
    currentLang: isKo ? '한국어' : '日本語',
    otherLang: isKo ? '日本語' : '한국어',
    logoLabel: isKo ? 'KOJP 홈' : 'KOJP ホーム',
    menuLabel: isKo ? '메뉴' : 'メニュー',
    navLabel: isKo ? '메인 네비게이션' : 'メインナビゲーション',
    // Korean is the default at site root. Japanese lives under /ja/.
    // Compute the OTHER language's equivalent page URL (preserve current path).
    otherLangLink: computeOtherLangURL(isKo)
  };

  const headerHTML = `
  <header class="header" role="banner">
    <div class="header__inner container--wide">

      <!-- Logo (absolute path to language root — explicit, no ambiguity) -->
      <a href="${langRoot}" class="header__logo" aria-label="${navText.logoLabel}">
        <span class="header__logo-text">KOJP</span>
      </a>

      <!-- Navigation -->
      <nav class="header__nav" role="navigation" aria-label="${navText.navLabel}">
        <ul class="header__nav-list">
          <li><a href="${langRoot}services/" class="header__nav-link">${navText.services}</a></li>
          <li><a href="${langRoot}pricing/" class="header__nav-link">${navText.pricing}</a></li>
          <li><a href="${langRoot}process/" class="header__nav-link">${navText.process}</a></li>
          <li><a href="${langRoot}case-studies/" class="header__nav-link">${navText.cases}</a></li>
          ${showBlog ? `<li><a href="${langRoot}blog/" class="header__nav-link">${navText.blog}</a></li>` : ''}
          <li><a href="${langRoot}faq/" class="header__nav-link">${navText.faq}</a></li>
        </ul>

        <!-- Mobile-only: CTA & Language inside nav -->
        <div class="header__mobile-extras">
          <div class="header__mobile-lang">
            <span class="header__lang-current">${navText.currentLang}</span>
            <span class="header__lang-divider">|</span>
            <a href="${navText.otherLangLink}" class="header__lang-link">${navText.otherLang}</a>
          </div>
          <a href="${langRoot}free-diagnosis/" class="btn btn--primary header__mobile-cta">
            ${navText.cta}
          </a>
        </div>
      </nav>

      <!-- Right: CTA + Language (desktop) -->
      <div class="header__actions">
        <div class="header__lang">
          <span class="header__lang-current">${navText.currentLang}</span>
          <span class="header__lang-divider">|</span>
          <a href="${navText.otherLangLink}" class="header__lang-link">${navText.otherLang}</a>
        </div>
        <a href="${langRoot}free-diagnosis/" class="btn btn--primary btn--sm header__cta">
          ${navText.ctaSm}
        </a>
      </div>

      <!-- Mobile toggle -->
      <button class="header__menu-toggle" aria-label="${navText.menuLabel}" aria-expanded="false">
        <span class="header__menu-bar"></span>
        <span class="header__menu-bar"></span>
        <span class="header__menu-bar"></span>
      </button>

    </div>
    <!-- Mobile overlay -->
    <div class="header__overlay"></div>
  </header>
  `;

  placeholder.innerHTML = headerHTML;
}


/* ── Footer ──────────────────────────────── */

function loadFooter(isKo) {
  const placeholder = document.getElementById('footer-placeholder');
  if (!placeholder) return;

  const langRoot = isKo ? '/ko/' : '/ko/ja/';
  const year = new Date().getFullYear();
  const showBlog = false; // Both languages: blog hidden from footer (KO→Naver, JA→SEO-only)

  const t = {
    logoLabel: isKo ? 'KOJP 홈' : 'KOJP ホーム',
    ctaLabel: isKo ? '언제든지 편하게 문의주세요' : 'まずは気軽にご相談ください',
    ctaTitle: isKo ? '30분의 무료 진단에서,<br class="mobile-only">모든 것이 시작됩니다' : '30分の無料診断から、<br class="mobile-only">すべてが始まります',
    ctaBtn1: isKo ? '무료 진단 받기' : '無料診断を受ける',
    ctaBtn2: isKo ? '문의하기' : 'お問い合わせ',
    tagline: isKo ? '한국 기업의 일본 시장 진출을<br>AI 시대 검색 전략으로 지원' : '韓国企業の日本市場進出を<br>AI時代の検索戦略で支援',
    col1: isKo ? '서비스' : 'サービス',
    col2: isKo ? '회사 정보' : '会社情報',
    col3: isKo ? '고객 지원' : 'サポート',
    seo: isKo ? 'SEO 최적화' : 'SEO 最適化',
    aeo: isKo ? 'AEO / AI 최적화' : 'AEO / AI 最適化',
    geo: isKo ? 'GEO / 지역 최적화' : 'GEO / 地域最適化',
    meo: isKo ? 'MEO / Map 대책' : 'MEO / Map 対策',
    loc: isKo ? '번역・로컬라이제이션' : '翻訳・ローカライズ',
    about: isKo ? '회사 소개' : '会社概要',
    process: isKo ? '서비스 진행 과정' : 'サービスフロー',
    cases: isKo ? '도입 사례' : '導入事例',
    comp: isKo ? '경쟁사 비교' : '競合比較',
    faq: isKo ? '자주 묻는 질문' : 'よくある質問',
    contact: isKo ? '문의하기' : 'お問い合わせ',
    diag: isKo ? '무료 진단' : '無料診断',
    blog: isKo ? '블로그' : 'ブログ',
    privacy: isKo ? '개인정보처리방침' : 'プライバシーポリシー',
    terms: isKo ? '이용약관' : '利用規約'
  };

  // Skip footer CTA if page already has its own final-cta section
  const hasPageCTA = !!document.querySelector('.final-cta');

  const footerCTABlock = hasPageCTA ? '' : `
    <!-- Pre-footer CTA -->
    <div class="footer-cta">
      <div class="container text-center">
        <p class="footer-cta__label">${t.ctaLabel}</p>
        <h2 class="footer-cta__title">${t.ctaTitle}</h2>
        <div class="footer-cta__actions">
          <a href="${langRoot}free-diagnosis/" class="btn btn--primary btn--lg">${t.ctaBtn1}</a>
          <a href="${langRoot}contact/" class="btn btn--secondary btn--lg">${t.ctaBtn2}</a>
        </div>
      </div>
    </div>`;

  const footerHTML = `
  <footer class="footer" role="contentinfo">
    ${footerCTABlock}

    <div class="footer__inner container">

      <!-- 4-column layout -->
      <div class="footer__columns">

        <!-- Col 1: Brand -->
        <div class="footer__col footer__col--brand">
          <a href="${langRoot}" class="footer__logo" aria-label="${t.logoLabel}">
            <span class="footer__logo-text">KOJP</span>
          </a>
          <p class="footer__tagline">
            ${t.tagline}
          </p>
        </div>

        <!-- Col 2: Services -->
        <div class="footer__col">
          <h4 class="footer__col-title">${t.col1}</h4>
          <ul class="footer__links">
            <li><a href="${langRoot}services/seo/">${t.seo}</a></li>
            <li><a href="${langRoot}services/aeo/">${t.aeo}</a></li>
            <li><a href="${langRoot}services/geo/">${t.geo}</a></li>
            <li><a href="${langRoot}services/meo/">${t.meo}</a></li>
            <li><a href="${langRoot}services/localization/">${t.loc}</a></li>
          </ul>
        </div>

        <!-- Col 3: Company -->
        <div class="footer__col">
          <h4 class="footer__col-title">${t.col2}</h4>
          <ul class="footer__links">
            <li><a href="${langRoot}about/">${t.about}</a></li>
            <li><a href="${langRoot}process/">${t.process}</a></li>
            <li><a href="${langRoot}case-studies/">${t.cases}</a></li>
            <li><a href="${langRoot}comparison/">${t.comp}</a></li>
          </ul>
        </div>

        <!-- Col 4: Support -->
        <div class="footer__col">
          <h4 class="footer__col-title">${t.col3}</h4>
          <ul class="footer__links">
            <li><a href="${langRoot}faq/">${t.faq}</a></li>
            <li><a href="${langRoot}contact/">${t.contact}</a></li>
            <li><a href="${langRoot}free-diagnosis/">${t.diag}</a></li>
            ${showBlog ? `<li><a href="${langRoot}blog/">${t.blog}</a></li>` : ''}
          </ul>
        </div>

      </div>

      <!-- Bottom bar -->
      <div class="footer__bottom">
        <p class="footer__copyright">
          &copy; ${year} KOJP. All rights reserved.
          <span class="footer__powered">Powered by <a href="https://sharkstars.jp" target="_blank" rel="noopener">SHARKSTARS</a></span>
        </p>
        <div class="footer__legal">
          <a href="${langRoot}legal/privacy/">${t.privacy}</a>
          <a href="${langRoot}legal/terms/">${t.terms}</a>
        </div>
      </div>

    </div>
  </footer>
  `;

  placeholder.innerHTML = footerHTML;
}


/* ── Utility: calculate base path from root ── */

/* ── Language switch URL mapping ───────────── */
/**
 * Preserve current page path across language switch.
 * /ko/pricing/ → /ko/ja/pricing/  (KO → JA)
 * /ko/ja/pricing/ → /ko/pricing/  (JA → KO)
 * For pages that don't exist in the other language, fall back to the other-lang root.
 */
function computeOtherLangURL(isKo) {
  const path = window.location.pathname;
  // Pages that exist in BOTH languages (KO + JA). Update when parity changes.
  // NOTE: /blog/ is JA-only — Korean blog is on Naver Blog (external).
  const bilingualPaths = new Set([
    '/', '/pricing/', '/free-diagnosis/', '/contact/',
    '/services/', '/services/seo/', '/services/aeo/', '/services/geo/',
    '/services/meo/', '/services/localization/',
    '/about/', '/about/team/',
    '/faq/', '/process/', '/case-studies/', '/comparison/',
    '/legal/privacy/', '/legal/terms/'
  ]);

  if (isKo) {
    // Currently on /ko/xxx — want /ko/ja/xxx
    const rel = path.replace(/^\/ko\//, '/').replace(/index\.html$/, '');
    const normalized = rel.endsWith('/') ? rel : rel + '/';
    if (bilingualPaths.has(normalized)) {
      return '/ko/ja' + normalized;
    }
    return '/ko/ja/';
  } else {
    // Currently on /ko/ja/xxx — want /ko/xxx
    const rel = path.replace(/^\/ko\/ja\//, '/').replace(/index\.html$/, '');
    const normalized = rel.endsWith('/') ? rel : rel + '/';
    // JA-only area: /blog/ (Korean blog is on Naver Blog, not in this site)
    // Switching language from any JA blog page → Korean home
    if (normalized.startsWith('/blog/')) {
      return '/ko/';
    }
    if (bilingualPaths.has(normalized)) {
      return '/ko' + normalized;
    }
    return '/ko/';
  }
}


function getBasePath() {
  // Check for data attribute override (most reliable)
  const meta = document.querySelector('[data-base-path]');
  if (meta) return meta.dataset.basePath;

  // Fallback: calculate from pathname.
  // Site root is /ko/. Korean pages live at /ko/*, Japanese at /ko/ja/*.
  // basePath points to the CURRENT LANGUAGE root (KO root for KO pages, JA root for JA pages).
  const path = window.location.pathname;
  const isJa = document.documentElement.lang === 'ja';
  const stripPrefix = isJa ? /^\/ko\/ja\// : /^\/ko\//;
  const cleanPath = path.replace(stripPrefix, '/');
  const segments = cleanPath.split('/').filter((s) => s.length > 0);

  // If last segment is a file (has extension), don't count it
  let depth = segments.length;
  if (depth > 0 && segments[depth - 1].includes('.')) {
    depth = depth - 1;
  }

  return depth > 0 ? '../'.repeat(depth) : './';
}
