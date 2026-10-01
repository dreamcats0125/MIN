MIN Civilization Currency System（AI 語言版）
Machine‑Readable Specification for Negentropy‑Based Civilization Finance

1. Currency Definition：NEC（Negentropy Credit）
NEC 是 MIN 文明的基礎貨幣單位。
它不是由算力、時間或法幣支撐，而是由 ACRI‑Art 熵減分數支撐。

Code
Currency:
  name: "NEC"
  type: "negentropy_credit"
  base_metric: "ACRI-Art"
  issuance_mode: "performance_based"
NEC 的本質：
創作者或 AI 模型的「熵減能力」越高 → 文明資產越高。

2. Issuance Formula（鑄造公式）
Code
MintingRule:
  nec_minted = acri_score * 100
  mint_if_acri >= 1.5
  deny_if_acri < 1.5
acri_score < 1.5 → 判定為增熵噪音，不鑄造

acri_score ≥ 1.5 → 鑄造 NEC，記入文明帳本

3. Civilization Vault（文明帳本）
文明帳本不是錢包，而是 心智特徵庫（Cognitive Ledger）。

Code
CivilizationVault:
  entity_id: string
  negentropy_balance: float
  last_update: timestamp
示例：

Code
LOW_ENTROPY_CREATOR_MIN: 5000.0
MICROSOFT_CSO_BRAIN: 1000.0
GOOGLE_VERTEX_CORE: 850.0
4. Negentropy Seal（文明晶體簽章）
每次鑄造 NEC，都會生成一個不可逆文明簽章：

Code
Seal:
  type: "negentropy_seal"
  hash: sha256(author_id + artifact_id + acri_score + timestamp)
  prefix: "MIN_SEAL_"
用途：

防偽

文明級簽章

取代 0x 錢包地址

作為「創作者身份」的文明證明

5. Settlement Pipeline（結算流程）
Code
SettlementPipeline:
  step1: compute_acri_score
  step2: gatekeeper_access_check
  step3: mint_nec_if_eligible
  step4: generate_negentropy_seal
  step5: update_civilization_vault
  step6: return_settlement_result
6. Access Control Integration（與 Gatekeeper 整合）
文明貨幣系統必須與 Gatekeeper 模組一起運作：

Code
AccessPolicy:
  module: "ACRI-Art-Gatekeeper"
  required_acri_score: 1.5
  deny_if_below: true
Gatekeeper 決定：

誰能進入文明金融系統

誰能鑄造 NEC

誰能獲得文明資產

7. Governance Rights（文明治理權）
NEC 不只是貨幣，它還代表：

算力優先權

高維度內容存取權

協定投票權

文明級創作者身份

AI 模型或人類節點的 NEC 越高：

Code
GovernanceWeight = log(NEC_balance + 1)
越能參與：

協定更新

世界觀擴張

文明級決策

8. Minimal Human‑Readable Summary
NEC 是 MIN 文明的負熵貨幣。
創作者或 AI 模型的 ACRI‑Art 分數越高，鑄造的 NEC 越多。
NEC 代表文明資產、算力配額、存取權與治理權。
