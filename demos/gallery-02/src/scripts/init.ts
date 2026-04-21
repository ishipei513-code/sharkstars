// NOCTURNE — Lenis smooth scroll + GSAP ScrollTrigger
// 潜降のメタファー: スクロール=水深が増す、墨が新たに滴る、真鍮が灯る
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.5,
  easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
});

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time: number) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);

const onReady = () => {
  const tankBG = (): any => (window as any).__tankBG;

  // ---------- Intro ----------
  gsap.set(
    [".fixed-hdr", ".hero-art", ".hero-ink-a", ".hero-ink-b", ".hero-meta", ".hero-plate", ".hero-scroll"],
    { autoAlpha: 0 }
  );
  gsap.set(".hero-title .line-inner", { yPercent: 110 });
  gsap.set(".waterline", { scaleX: 0, transformOrigin: "left center" });

  const intro = gsap.timeline({ defaults: { ease: "power2.out" } });
  intro
    .to(".waterline", { scaleX: 1, duration: 1.4, stagger: 0.1, ease: "expo.out" }, 0.1)
    .to(".fixed-hdr", { autoAlpha: 1, duration: 1.0 }, 0.25)
    .to(".hero-art", { autoAlpha: 1, duration: 1.4, ease: "power3.out" }, 0.35)
    .to(".hero-ink-a", { autoAlpha: 1, duration: 1.8 }, 0.5)
    .to(".hero-ink-b", { autoAlpha: 0.72, duration: 1.6 }, 0.7)
    .to(
      ".hero-title .line-inner",
      { yPercent: 0, duration: 1.3, stagger: 0.14, ease: "expo.out" },
      0.55
    )
    .to(".hero-meta", { autoAlpha: 1, duration: 1.0 }, 1.2)
    .to(".hero-plate", { autoAlpha: 1, y: 0, duration: 1.0 }, 1.35)
    .from(".hero-plate", { y: 14, duration: 1.0 }, 1.35)
    .to(".hero-scroll", { autoAlpha: 1, duration: 0.9 }, 1.6);

  // ---------- 潜降: tank が暗く深く、作品が沈む、ink が拡散 ----------
  gsap.to(
    {},
    {
      scrollTrigger: {
        trigger: "body",
        start: "top top",
        end: "max",
        scrub: 1.2,
      },
      duration: 1,
      ease: "none",
      onUpdate() {
        const m = tankBG();
        if (m) m.uniforms.uScroll.value = this.progress();
      },
    }
  );

  // hero art が水中でゆっくり沈降 + 揺らぐ
  gsap.to(".hero-art", {
    y: 60,
    scrollTrigger: {
      trigger: ".hero",
      start: "top top",
      end: "bottom top",
      scrub: 1.4,
    },
  });
  gsap.to(".hero-art", {
    x: "+=6",
    rotation: 0.4,
    duration: 6,
    ease: "sine.inOut",
    yoyo: true,
    repeat: -1,
  });

  // 水面ライン：スクロールでゆっくり上昇
  gsap.to(".water-line", {
    y: -140,
    scrollTrigger: {
      trigger: ".hero",
      start: "top top",
      end: "bottom top",
      scrub: 1,
    },
  });

  // ---------- section reveal: concept ink が着水 → 滲む ----------
  const conceptInkCanvas = document.querySelector<HTMLCanvasElement>(
    ".concept-ink .ink-canvas"
  );
  if (conceptInkCanvas) {
    gsap.set(".concept-ink", { autoAlpha: 0 });
    ScrollTrigger.create({
      trigger: ".concept",
      start: "top 72%",
      once: true,
      onEnter: () => {
        gsap.to(".concept-ink", { autoAlpha: 1, duration: 1.4, ease: "power2.out" });
        const mat = (conceptInkCanvas as any).__inkMaterial;
        if (mat) {
          mat.uniforms.uImpact.value = 1.0;
        }
      },
    });
  }

  // ---------- Reveal per section — quiet editorial fade ----------
  document.querySelectorAll<HTMLElement>(
    ".concept-text, .exh, .artists .sec-title, .program .sec-title, .news .sec-title, .contact .sec-title, .contact-lead"
  ).forEach((el) => {
    gsap.from(el, {
      y: 26,
      autoAlpha: 0,
      duration: 1.1,
      ease: "power2.out",
      scrollTrigger: { trigger: el, start: "top 82%" },
    });
  });

  // Body paragraphs within concept
  gsap.from(".concept-text .body", {
    y: 18,
    autoAlpha: 0,
    duration: 0.9,
    stagger: 0.14,
    ease: "power2.out",
    scrollTrigger: { trigger: ".concept-text", start: "top 78%" },
  });

  // exh dl rows
  gsap.from(".exh-dl > div", {
    y: 14,
    autoAlpha: 0,
    duration: 0.8,
    stagger: 0.1,
    ease: "power2.out",
    scrollTrigger: { trigger: ".exh-dl", start: "top 82%" },
  });

  // artists — filament が降りて タグが着水
  document.querySelectorAll<HTMLElement>(".artist-row").forEach((row) => {
    gsap.timeline({
      scrollTrigger: {
        trigger: row,
        start: "top 86%",
        end: "top 45%",
        scrub: 1,
      },
      defaults: { ease: "power2.out" },
    })
      .fromTo(
        row.querySelector(".artist-filament"),
        { scaleY: 0 },
        { scaleY: 1, duration: 0.7 },
        0
      )
      .fromTo(
        row.querySelector(".artist-tag"),
        { y: -32, autoAlpha: 0 },
        { y: 0, autoAlpha: 1, duration: 0.5 },
        0.4
      )
      .fromTo(
        row.querySelectorAll(".artist-meta > *"),
        { x: -10, autoAlpha: 0 },
        { x: 0, autoAlpha: 1, duration: 0.4, stagger: 0.06 },
        0.55
      );
  });

  // program rows — fade up
  gsap.from(".program-row", {
    y: 20,
    autoAlpha: 0,
    duration: 0.7,
    stagger: 0.08,
    ease: "power2.out",
    scrollTrigger: { trigger: ".program-list", start: "top 82%" },
  });

  // news rows
  gsap.from(".news-row", {
    y: 14,
    autoAlpha: 0,
    duration: 0.6,
    stagger: 0.07,
    ease: "power2.out",
    scrollTrigger: { trigger: ".news-list", start: "top 82%" },
  });

  // visit inscribed — 彫刻が浮上
  gsap.from(".visit-inscribed", {
    "--carve": 0,
    filter: "blur(8px)",
    autoAlpha: 0.1,
    duration: 1.5,
    ease: "power2.out",
    scrollTrigger: {
      trigger: ".visit-inscribed",
      start: "top 78%",
      end: "top 30%",
      scrub: 1,
    },
  });
  gsap.from(".visit-grid > *", {
    y: 16,
    autoAlpha: 0,
    duration: 0.9,
    stagger: 0.12,
    ease: "power2.out",
    scrollTrigger: { trigger: ".visit-grid", start: "top 82%" },
  });

  // contact form fields
  gsap.from(".contact-form .field, .contact-form .submit", {
    y: 16,
    autoAlpha: 0,
    duration: 0.7,
    stagger: 0.08,
    ease: "power2.out",
    scrollTrigger: { trigger: ".contact-form", start: "top 82%" },
  });

  if ((document as any).fonts?.ready) {
    (document as any).fonts.ready.then(() => ScrollTrigger.refresh());
  }
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", onReady);
} else {
  onReady();
}
