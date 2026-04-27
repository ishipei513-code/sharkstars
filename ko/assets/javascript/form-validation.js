/* ============================================
   KOJP — Form Validation (Free Diagnosis)
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('diagnosis-form');
  if (!form) return;

  const submitBtn = document.getElementById('submit-btn');
  const btnText = form.querySelector('.diag-form__btn-text');
  const btnLoading = form.querySelector('.diag-form__btn-loading');
  const modal = document.getElementById('thank-you-modal');
  const modalClose = document.getElementById('modal-close');

  // Field configs
  const fields = [
    { id: 'company',  msg: '会社名を入力してください' },
    { id: 'name',     msg: '担当者名を入力してください' },
    { id: 'email',    msg: '有効なメールアドレスを入力してください', type: 'email' },
    { id: 'website',  msg: '有効なURLを入力してください（https://～）', type: 'url' },
    { id: 'privacy',  msg: 'プライバシーポリシーに同意してください', type: 'checkbox' }
  ];


  // Validate single field
  function validateField(config) {
    const el = document.getElementById(config.id);
    const errorEl = document.getElementById(config.id + '-error');
    let valid = true;

    if (config.type === 'checkbox') {
      valid = el.checked;
    } else if (config.type === 'email') {
      valid = el.value.trim() !== '' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value);
    } else if (config.type === 'url') {
      valid = el.value.trim() !== '' && /^https?:\/\/.+\..+/.test(el.value);
    } else {
      valid = el.value.trim() !== '';
    }

    if (!valid) {
      if (config.type !== 'checkbox') {
        el.classList.add('is-error');
      }
      if (errorEl) errorEl.textContent = config.msg;
    } else {
      if (config.type !== 'checkbox') {
        el.classList.remove('is-error');
      }
      if (errorEl) errorEl.textContent = '';
    }

    return valid;
  }


  // Real-time validation on blur
  fields.forEach((config) => {
    const el = document.getElementById(config.id);
    if (!el) return;
    const event = config.type === 'checkbox' ? 'change' : 'blur';
    el.addEventListener(event, () => validateField(config));
  });


  // Form submit
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Validate all
    let allValid = true;
    fields.forEach((config) => {
      if (!validateField(config)) allValid = false;
    });

    if (!allValid) {
      // Focus first error field
      const firstError = form.querySelector('.is-error');
      if (firstError) firstError.focus();
      return;
    }

    // Show loading briefly for UX
    submitBtn.disabled = true;
    btnText.hidden = true;
    btnLoading.hidden = false;

    try {
      // Gather form data for mailto fallback (backend endpoint pending)
      const company = document.getElementById('company')?.value.trim() || '';
      const name = document.getElementById('name')?.value.trim() || '';
      const email = document.getElementById('email')?.value.trim() || '';
      const website = document.getElementById('website')?.value.trim() || '';
      const phone = document.getElementById('phone')?.value.trim() || '';
      const industry = document.getElementById('industry')?.value.trim() || '';
      const budget = document.getElementById('budget')?.value.trim() || '';
      const notes = document.getElementById('notes')?.value.trim() || '';

      const isKo = document.documentElement.lang === 'ko';
      const subject = encodeURIComponent(
        isKo ? `[KOJP 무료 진단 신청] ${company} / ${name}` : `[KOJP 無料診断申込] ${company} / ${name}`
      );
      const bodyLines = isKo ? [
        `회사명: ${company}`,
        `담당자: ${name}`,
        `이메일: ${email}`,
        `전화: ${phone || '(미기재)'}`,
        `웹사이트: ${website}`,
        `업종: ${industry || '(미선택)'}`,
        `예산: ${budget || '(미선택)'}`,
        '',
        '--- 한 줄 메모 ---',
        notes || '(없음)',
        '',
        '---',
        '개인정보처리방침 동의: 예',
      ] : [
        `会社名: ${company}`,
        `担当者: ${name}`,
        `メール: ${email}`,
        `電話: ${phone || '(未記入)'}`,
        `Webサイト: ${website}`,
        `業種: ${industry || '(未選択)'}`,
        `想定予算: ${budget || '(未選択)'}`,
        '',
        '--- ひとことメモ ---',
        notes || '(なし)',
        '',
        '---',
        'プライバシーポリシーに同意: はい',
      ];
      const body = encodeURIComponent(bodyLines.join('\n'));

      // Brief delay for UX consistency with "submitting" feel
      await new Promise((resolve) => setTimeout(resolve, 400));

      // Open user's mail client with pre-filled content
      window.location.href = `mailto:contact@sharkstars.jp?subject=${subject}&body=${body}`;

      // Show thank you modal as confirmation
      modal.hidden = false;
      document.body.style.overflow = 'hidden';
      form.reset();
    } catch (err) {
      alert(document.documentElement.lang === 'ko'
        ? '전송에 실패했습니다. 다시 시도해 주세요.'
        : '送信に失敗しました。もう一度お試しください。');
    } finally {
      submitBtn.disabled = false;
      btnText.hidden = false;
      btnLoading.hidden = true;
    }
  });


  // Modal close
  if (modalClose) {
    modalClose.addEventListener('click', () => {
      modal.hidden = true;
      document.body.style.overflow = '';
    });
  }

  // Close modal on overlay click
  if (modal) {
    modal.querySelector('.modal__overlay').addEventListener('click', () => {
      modal.hidden = true;
      document.body.style.overflow = '';
    });
  }
});
