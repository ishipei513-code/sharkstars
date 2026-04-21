// Lenis smooth scroll + GSAP ScrollTrigger — orchestrates THE WALL anomalies
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.3,
  easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
});

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time: number) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);

const onReady = () => {
  // ---------- Entrance (quiet editorial) ----------
  gsap.set(
    [".hdr-left", ".hdr-right", ".hero-piece", ".hero-mercury", ".hero-meta", ".hero-scroll"],
    { autoAlpha: 0 }
  );
  gsap.set(".hero-title .line", { yPercent: 110 });

  const intro = gsap.timeline({ defaults: { ease: "power2.out" } });
  intro
    .to(".hdr-left", { autoAlpha: 1, duration: 0.9, delay: 0.15 }, 0)
    .to(".hdr-right", { autoAlpha: 1, duration: 0.9 }, 0.1)
    .fromTo(
      ".hero-piece",
      { autoAlpha: 0, y: -18 },
      { autoAlpha: 1, y: 0, duration: 1.4, ease: "power3.out" },
      0.4
    )
    .to(".hero-mercury", { autoAlpha: 1, duration: 1.6 }, 0.8)
    .to(
      ".hero-title .line",
      { yPercent: 0, autoAlpha: 1, duration: 1.2, stagger: 0.12, ease: "expo.out" },
      0.6
    )
    .to(".hero-meta", { autoAlpha: 1, y: 0, duration: 0.9 }, 1.2)
    .to(".hero-scroll", { autoAlpha: 1, duration: 0.9 }, 1.4);

  // ---------- Phase A: pinned hero anomalies ----------
  const mercury = () => (window as any).__wallMercury;

  const pinTL = gsap.timeline({
    scrollTrigger: {
      trigger: ".hero",
      start: "top top",
      end: "+=1800",
      pin: true,
      pinSpacing: true,
      scrub: 1.2,
      anticipatePin: 1,
    },
    defaults: { ease: "none" },
  });

  pinTL
    // インクが滴り切る + 雫が溜まる
    .to(".ink-path", { attr: { "stroke-dashoffset": 0 }, duration: 0.5 }, 0)
    .to(".ink-pool", { attr: { r: 2.4 }, duration: 0.2 }, 0.45)
    // 糸が伸びて絵が沈む
    .to(".wire", { scaleY: 1.35, duration: 0.8 }, 0)
    .to(".hero-piece", { y: 42, duration: 0.8 }, 0)
    // 寸法線がチリッと現れる
    .to(".dim", { opacity: 1, duration: 0.15 }, 0.18)
    .fromTo(
      ".dim .dim-line",
      { attr: { "stroke-dashoffset": 200 } },
      { attr: { "stroke-dashoffset": 0 }, duration: 0.25, stagger: 0.05 },
      0.2
    )
    // 水銀の雫が肥大化
    .to(
      {},
      {
        duration: 1,
        onUpdate() {
          const m = mercury();
          if (m) m.uniforms.uScroll.value = this.progress();
        },
      },
      0.1
    )
    // 文字 THE WALL が下から水銀で満たされる
    .to(".hero-title .line", { "--fill": "100%", duration: 0.7 }, 0.25)
    // 壁が左に微細ドリフト（歩く錯覚）
    .to(".wall", { x: -48, duration: 1 }, 0)
    // メタテキストが最後に浮かび上がる（SEO用の intro もここで）
    .from(".hero-intro p", { opacity: 0, y: 14, filter: "blur(6px)", duration: 0.5, stagger: 0.05 }, 0.5)
    // スクロール指示はフェードアウト
    .to(".hero-scroll", { autoAlpha: 0, duration: 0.15 }, 0.05);

  // 寸法線テキストの「チリチリ」ジッター（pin中のみ）
  const dimTextJitter = gsap.to(".dim-text", {
    x: () => gsap.utils.random(-0.6, 0.6),
    y: () => gsap.utils.random(-0.6, 0.6),
    duration: 0.08,
    repeat: -1,
    repeatRefresh: true,
    ease: "none",
    paused: true,
  });
  ScrollTrigger.create({
    trigger: ".hero",
    start: "top top",
    end: "+=1800",
    onEnter: () => dimTextJitter.play(),
    onLeave: () => dimTextJitter.pause(),
    onEnterBack: () => dimTextJitter.play(),
    onLeaveBack: () => dimTextJitter.pause(),
  });

  // ---------- Phase B: コンクリートが裂ける (manifesto reveal) ----------
  gsap.set(".manifesto", { autoAlpha: 1 });
  gsap.set(".manifesto-overlay .crack-path", { strokeDashoffset: 1200 });
  gsap.set(".manifesto-text", { autoAlpha: 0, filter: "blur(18px)" });

  gsap.timeline({
    scrollTrigger: {
      trigger: ".manifesto",
      start: "top 82%",
      end: "top 20%",
      scrub: 1,
    },
    defaults: { ease: "none" },
  })
    .to(".manifesto-overlay .crack-path", { strokeDashoffset: 0, duration: 1 }, 0)
    .to(".manifesto-overlay", { clipPath: "inset(0 0 0 0)", duration: 0.6 }, 0.2)
    .to(".manifesto-overlay", { opacity: 0.18, duration: 0.4 }, 0.5)
    .to(".manifesto-text", { autoAlpha: 1, filter: "blur(0px)", duration: 0.8 }, 0.35)
    .from(
      ".manifesto-text p",
      { y: 24, opacity: 0, duration: 0.3, stagger: 0.08 },
      0.5
    );

  // ---------- Phase C: artists — 糸が降りてくる ----------
  document.querySelectorAll<HTMLElement>(".artist-row").forEach((row) => {
    gsap.timeline({
      scrollTrigger: {
        trigger: row,
        start: "top 85%",
        end: "top 40%",
        scrub: 1,
      },
      defaults: { ease: "power2.out" },
    })
      .fromTo(
        row.querySelector(".artist-wire"),
        { scaleY: 0 },
        { scaleY: 1, duration: 0.7 },
        0
      )
      .fromTo(
        row.querySelector(".artist-tag"),
        { y: -40, opacity: 0, rotate: -1.2 },
        { y: 0, opacity: 1, rotate: 0, duration: 0.5 },
        0.35
      )
      .fromTo(
        row.querySelectorAll(".artist-meta > *"),
        { opacity: 0, x: -10 },
        { opacity: 1, x: 0, duration: 0.3, stagger: 0.08 },
        0.55
      );
  });

  // ---------- Phase D: visit — 彫り込み ----------
  gsap.timeline({
    scrollTrigger: {
      trigger: ".visit",
      start: "top 75%",
      end: "top 30%",
      scrub: 1,
    },
    defaults: { ease: "none" },
  })
    .from(".visit-inscribed", { "--carve": "0", filter: "blur(8px)", opacity: 0.15, duration: 1 }, 0)
    .from(".visit-body > *", { opacity: 0, y: 18, duration: 0.6, stagger: 0.08 }, 0.3);

  // refresh after fonts settle
  if ((document as any).fonts?.ready) {
    (document as any).fonts.ready.then(() => ScrollTrigger.refresh());
  }
};

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", onReady);
} else {
  onReady();
}
