import sys

with open(r'd:\sharkstars\assist\css\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

responsive_css = """
@media (max-width: 1024px) {
  .pricing-details-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .detail-features-flex {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .terms-grid {
    grid-template-columns: 1fr;
  }
  .options-table th, .options-table td {
    display: block;
    width: 100%;
  }
  .options-table tr {
    display: block;
    border-bottom: 1px solid var(--gray-200);
    padding-bottom: 16px;
    margin-bottom: 16px;
  }
  .options-table td {
    border-bottom: none;
    padding-top: 0;
  }
  .pricing-card {
    border-radius: 16px;
  }
  .pricing-header {
    padding: 32px 24px;
  }
  .pricing-options, .pricing-detail-box {
    padding: 24px;
  }
}
"""

with open(r'd:\sharkstars\assist\css\style.css', 'a', encoding='utf-8') as f:
    f.write(responsive_css)

print("Responsive CSS appended successfully!")
