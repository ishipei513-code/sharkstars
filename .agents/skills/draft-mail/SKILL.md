---
name: draft-mail
description: Compose a SHARKSTARS-tone Japanese reply to an inbound inquiry and save it as a Gmail draft via the Gmail MCP. Use when the user pastes an inquiry email and asks for a reply. Invocation form -- /draft-mail <subject hint or industry>
disable-model-invocation: true
---

# /draft-mail — draft an inquiry reply and save to Gmail

Use this skill to turn an inbound customer inquiry into a polished Japanese reply, then push the reply to Gmail as a **draft** (never auto-send) using the connected Gmail MCP server.

## Prerequisites

- Gmail MCP server is connected (visible in `/plugin → Installed`).
- The user has pasted the inbound inquiry into the chat. If they haven't, ask for it before doing anything else.

## Inputs to gather (in one round-trip if missing)

1. **Inbound message** (full text, including signature if available)
2. **Recipient email address** (extract from headers if pasted, otherwise ask)
3. **Industry / business type** (e.g., 整体院, 再生医療クリニック, 飲食店). Used to tailor tone and pitch.
4. **Referral context** — was the inquiry through a personal connection? If yes, who referred? (Used to insert a warm acknowledgment.)
5. **Any specific points to address** the user wants emphasized (optional).

## Composition rules

The SHARKSTARS reply tone:

- 丁寧 + やや人間味のあるビジネス日本語。固すぎない。
- Always sign as **石橋昇平** (SHARKSTARS代表). Never use any other name. The PreToolUse hook will block if you try.
- Lead with thanks + (if applicable) a one-line warm acknowledgment of the personal referral.
- Mirror the inquirer's stated goals (集客, デザイン, 公開時期, etc.) before pitching.
- State the baseline service: **初期費用0円・月額3,980円（税込）**. Note that bespoke scope (撮影, 規制対応, LP追加, etc.) may be quoted separately.
- Ask 4–8 concrete intake questions tailored to the industry. Don't dump a generic checklist.
- Close with a 30–60 minute オンライン or 対面 打ち合わせ proposal, asking for 2–3 candidate slots from the recipient.
- Signature block:
  ```
  SHARKSTARS
  代表：石橋 昇平（いしばし しょうへい）
  〒／福岡県福岡市〜
  TEL：
  Mail：ishipei513@gmail.com
  URL：https://sharkstars.jp
  ```

## Industry-specific tweaks

- **医療系（再生医療、美容医療、歯科 etc.）**: mention 医療広告ガイドライン compliance as a known consideration.
- **飲食 / 物販**: emphasize MEO (Googleマップ) and写真撮影の重要性.
- **士業 / コンサル**: emphasize SEO / 信頼感 / 著者性 (E-E-A-T) framing.
- **再生医療 specifically**: do not promise 集客効果 in absolute terms; suggest LP + 記事更新 + MEO の組み合わせで段階的に育てる framing.

## Workflow

### Step 1 — Compose

Draft the reply in Markdown so the user can review it in chat first. Show the user the draft and ask if any adjustments are needed before pushing to Gmail.

### Step 2 — Confirm before saving

Before calling the Gmail MCP, **explicitly confirm with the user**:

> 「この内容でGmail下書きに保存します。よろしいですか？」

Do not push to Gmail without that confirmation.

### Step 3 — Save as Gmail draft

Use the Gmail MCP tool `mcp__claude_ai_Gmail__create_draft` with:

- `to`: recipient email (verified with user)
- `subject`: e.g., `Re: お問い合わせの件（SHARKSTARS）` or thread-aware subject if replying to an existing thread
- `body`: the finalized plain-text version of the reply (convert from Markdown — strip Markdown emphasis, preserve line breaks)
- (If responding to a thread the user identified: `threadId` so it threads correctly)

### Step 4 — Confirm save

After the MCP call succeeds, report the draft ID and remind the user:
> 「Gmailの下書きに保存しました。送信前に最終確認をお願いします。」

Never call the send equivalent. This skill is draft-only by policy.

## Boundaries

- **Draft only, never send.** Hard rule.
- **Never invent recipient email or signature details.** Ask the user when in doubt.
- **Never use a name other than 石橋昇平 in the signature.**
- **Never quote unverifiable specifics** (案件実績の具体名、料金以外の数字など) without user-provided source.
