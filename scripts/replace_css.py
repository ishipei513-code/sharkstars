import sys

with open(r'd:\sharkstars\assist\css\style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_css = """
.pricing-card {
  max-width: 640px;
  margin: 0 auto 40px;
  background-color: var(--white);
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid var(--gray-200);
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.pricing-header {
  background-color: var(--gray-900);
  color: var(--white);
  text-align: center;
  padding: 48px 40px 32px;
}

.pricing-label {
  font-size: 0.9rem;
  font-weight: 700;
  opacity: 0.9;
  margin-bottom: 16px;
  letter-spacing: 0.05em;
}

.pricing-amount {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 4px;
}

.pricing-currency {
  font-size: 1.5rem;
  font-weight: 700;
}

.pricing-number {
  font-size: 4.5rem;
  font-weight: 900;
  line-height: 1;
  letter-spacing: -0.04em;
}

.pricing-period {
  font-size: 1.1rem;
  font-weight: 500;
  opacity: 0.8;
}

.pricing-tax {
  font-size: 0.85rem;
  opacity: 0.6;
  margin-top: 8px;
}

.pricing-initial {
  display: inline-block;
  margin-top: 24px;
  padding: 8px 24px;
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 100px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #fff;
}

.pricing-note-box {
  padding: 24px 32px;
  background-color: var(--gray-50);
  text-align: center;
  border-top: 1px solid var(--gray-200);
}

.pricing-note-box p {
  font-size: 0.9rem;
  color: var(--gray-600);
  line-height: 1.6;
}

/* Details Grid */
.pricing-details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 40px;
}

.pricing-detail-box {
  background-color: var(--white);
  border-radius: 16px;
  padding: 32px;
  border: 1px solid var(--gray-200);
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}

.pricing-detail-box.full-width {
  grid-column: 1 / -1;
}

.detail-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--gray-900);
  margin-bottom: 12px;
  line-height: 1.4;
}

.detail-desc {
  font-size: 0.95rem;
  color: var(--gray-500);
  margin-bottom: 24px;
}

.detail-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.detail-list li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 0.95rem;
  color: var(--gray-800);
  line-height: 1.5;
}

.detail-list .icon-check {
  width: 20px;
  height: 20px;
  color: var(--gray-900);
  flex-shrink: 0;
  margin-top: 2px;
}

.detail-list strong {
  display: block;
  font-weight: 700;
  margin-bottom: 2px;
}

.detail-list span {
  font-size: 0.85rem;
  color: var(--gray-500);
}

.detail-list.list-simple li {
  align-items: center;
}

.detail-features-flex {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.df-item {
  text-align: center;
}

.df-icon {
  width: 48px;
  height: 48px;
  background-color: var(--gray-100);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  color: var(--gray-900);
}

.df-icon svg {
  width: 24px;
  height: 24px;
}

.df-item strong {
  display: block;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 8px;
}

.df-item p {
  font-size: 0.9rem;
  color: var(--gray-600);
  line-height: 1.5;
}

/* Options */
.pricing-options {
  background-color: var(--white);
  border-radius: 16px;
  padding: 40px;
  border: 1px solid var(--gray-200);
  margin-bottom: 40px;
}

.options-title {
  font-size: 1.4rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 24px;
}

.options-desc {
  font-size: 0.95rem;
  color: var(--gray-600);
  line-height: 1.6;
  background-color: var(--gray-50);
  padding: 24px;
  border-radius: 12px;
  border-left: 4px solid var(--gray-900);
  margin-bottom: 32px;
}

.options-table {
  width: 100%;
  border-collapse: collapse;
}

.options-table th, .options-table td {
  padding: 16px;
  border-bottom: 1px solid var(--gray-200);
  font-size: 0.95rem;
}

.options-table th {
  text-align: left;
  font-weight: 700;
  color: var(--gray-800);
  width: 40%;
}

.options-table td {
  color: var(--gray-700);
}

.options-table tr:last-child th,
.options-table tr:last-child td {
  border-bottom: none;
}

/* Terms */
.pricing-terms {
  margin-bottom: 40px;
}

.terms-title {
  font-size: 1.2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 24px;
  color: var(--gray-700);
}

.terms-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.term-item {
  background-color: var(--white);
  border-radius: 12px;
  padding: 24px;
  border: 1px dashed var(--gray-300);
}

.term-item strong {
  display: block;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--gray-900);
  margin-bottom: 8px;
}

.term-item p {
  font-size: 0.85rem;
  color: var(--gray-600);
  line-height: 1.6;
}
"""

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith(".pricing-card {"):
        start_idx = i
    if "/* ============================================" in line and "FLOW" in lines[i+1]:
        end_idx = i - 1
        break

if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx] = [new_css.strip() + "\n\n"]
    with open(r'd:\sharkstars\assist\css\style.css', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("CSS replaced successfully!")
else:
    print(f"Indices not found. start={start_idx}, end={end_idx}")
