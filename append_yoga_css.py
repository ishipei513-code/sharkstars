import os

css_append = '''
/* ==========================================================================
   10. New Components (Deep Content)
   ========================================================================== */
/* Features Grid */
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
.feature-card { text-align: center; padding: 40px 30px; border-radius: 8px; border: 1px solid rgba(159, 179, 161, 0.2); transition: var(--transition); background: rgba(254, 253, 252, 0.5); }
.feature-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(74, 85, 104, 0.05); border-color: rgba(159, 179, 161, 0.5); }
.feature-icon-wrapper { width: 80px; height: 80px; border-radius: 50%; background: var(--c-cream); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: var(--c-sage); }

/* Voice Cards */
.voices-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; }
.voice-card { background: var(--c-white); padding: 40px; border-radius: 8px; position: relative; box-shadow: 0 5px 15px rgba(74, 85, 104, 0.03); }
.voice-quote-icon { position: absolute; top: 20px; right: 20px; color: var(--c-sage); opacity: 0.2; }
.voice-meta { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
.voice-avatar { width: 50px; height: 50px; border-radius: 50%; object-fit: cover; }
.voice-rating { color: #d4af37; display: flex; gap: 2px; }

/* FAQ Accordion */
.faq-list { max-width: 800px; margin: 0 auto; }
.faq-item { border-bottom: 1px solid rgba(159, 179, 161, 0.3); }
.faq-q { width: 100%; text-align: left; background: none; border: none; padding: 25px 0; font-size: 1.1rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--c-slate); }
.faq-icon { transition: transform 0.3s ease; color: var(--c-sage); }
.faq-item.active .faq-icon { transform: rotate(45deg); }
.faq-a { max-height: 0; overflow: hidden; transition: max-height 0.4s var(--ease-soft); }
.faq-a-inner { padding-bottom: 25px; color: var(--c-gray); font-size: 0.95rem; line-height: 2; }

/* Enhanced Typo */
.font-serif { font-family: var(--f-shippori); }
.letter-spacing-wide { letter-spacing: 0.1em; }
.letter-spacing-widest { letter-spacing: 0.2em; }
'''

with open(r'd:\sharkstars\demos\yoga-01\assist\css\style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("CSS appended successfully.")
