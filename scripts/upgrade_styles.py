import sys

css_file = r'd:\sharkstars\assist\css\style.css'

with open(css_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_css = """
.pricing-detail-box {
  background: linear-gradient(145deg, #ffffff, #fafafa);
  border-radius: 24px;
  padding: 40px;
  border: 1px solid rgba(0,0,0,0.04);
  box-shadow: 0 10px 40px -10px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.02);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
  position: relative;
}

.pricing-detail-box:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px -10px rgba(0,0,0,0.12), 0 1px 3px rgba(0,0,0,0.02);
}

.pricing-detail-box.full-width {
  grid-column: 1 / -1;
  background: linear-gradient(145deg, #fafafa, #ffffff);
  border: 1px solid rgba(0,0,0,0.06);
}

.detail-title {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--gray-900);
  margin-bottom: 20px;
  line-height: 1.5;
  letter-spacing: -0.02em;
}

.detail-desc {
  font-size: 0.95rem;
  color: var(--gray-500);
  margin-bottom: 32px;
  font-weight: 500;
}

.detail-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.detail-list li {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  font-size: 0.95rem;
  color: var(--gray-800);
  line-height: 1.6;
}

.detail-list .icon-check {
  width: 24px;
  height: 24px;
  color: var(--white);
  background: var(--gray-900);
  border-radius: 50%;
  padding: 5px;
  flex-shrink: 0;
  margin-top: 2px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.detail-list strong {
  display: block;
  font-weight: 700;
  margin-bottom: 4px;
  font-size: 1.05rem;
}

.detail-list span {
  display: block;
  font-size: 0.85rem;
  color: var(--gray-500);
}

.detail-list.list-simple li {
  align-items: center;
  font-weight: 600;
  padding: 8px 0;
  border-bottom: 1px dashed var(--gray-200);
}
.detail-list.list-simple li:last-child {
  border-bottom: none;
}

.detail-features-flex {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  margin-top: 24px;
}

.df-item {
  text-align: center;
  padding: 24px 16px;
  border-radius: 20px;
  transition: background-color 0.3s ease;
}

.df-item:hover {
  background-color: var(--white);
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
}

.df-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, var(--gray-100), var(--white));
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  color: var(--gray-900);
  box-shadow: 0 8px 16px rgba(0,0,0,0.04), inset 0 2px 0 rgba(255,255,255,1);
  border: 1px solid var(--gray-200);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.df-item:hover .df-icon {
  transform: scale(1.08) translateY(-4px);
}

.df-icon svg {
  width: 28px;
  height: 28px;
}

.df-item strong {
  display: block;
  font-weight: 800;
  font-size: 1.15rem;
  margin-bottom: 12px;
  color: var(--gray-900);
}

.df-item p {
  font-size: 0.9rem;
  color: var(--gray-600);
  line-height: 1.6;
}
"""

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if ".pricing-detail-box {" in line:
        start_idx = i
    if "/* Options */" in line:
        end_idx = i - 1
        break

if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx] = [new_css.strip() + "\n\n"]
    with open(css_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Upgraded detail boxes styles.")
else:
    print(f"Failed to find indices. Start: {start_idx}, End: {end_idx}")

