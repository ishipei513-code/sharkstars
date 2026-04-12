import sys

with open(r'd:\sharkstars\assist\css\style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Utility Classes added for Pricing Section */
.text-center { text-align: center !important; }
.mb-medium { margin-bottom: 24px !important; }
.mt-large { margin-top: 48px !important; }
.mt-xs { margin-top: 4px !important; }
.text-xs { font-size: 0.8rem !important; }
.text-gray-500 { color: var(--gray-500) !important; }
.display-block { display: block !important; }
.bg-light { background-color: var(--gray-50) !important; }

@media (max-width: 768px) {
  .sp-none { display: none !important; }
}
''')

print("Utility classes appended successfully.")
