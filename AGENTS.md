# AGENTS.md — Shadow Ecosystem AI Engineering Constitution

本儲存庫隸屬於 **Shadow World Civilization (`MIN` × `TY` × `SWC`)**。所有接入本專案的 AI 編程代理（GitHub Copilot / Claude Code / Codex / Gemini）在修改或生成任何程式碼前，必須無條件遵守以下五條鐵律：

## 1. 架構主權與權限邊界 (Sovereignty & Tier Routing)
* 嚴格遵守根目錄 `governance_rules.json` 定義的 `TIER_0` 至 `TIER_3` 權限分級。
* **絕對禁區（Do-Not-Touch）：** 嚴禁 AI 代理自主修改 `governance_rules.json` 中的 `TIER_3_CONSTITUTIONAL` 人類主權閾值（`ai_weight: 0.0`, `human_weight: 1.0`），或繞過 `SW-IFRS` 的 `CSR >= 1.25` 償付能力紅線。

## 2. 「黑箱代碼 × 白箱不變量」交付鐵律 (Invariant-First Delivery)
* 隨著系統演進，底層實作代碼允許高度複雜化，但**任何 Pull Request 都必須附帶人類可直接閱讀的「行為不變量測試（Invariant Tests）」**（存放於 `tests/` 目錄下）。
* 所有涉及資金流（`CC` / `RB`）、水晶估值（`Vt`）、彩蛋獎池分配（70/20/10）或信用分（`TC`）的變更，必須包含邊界條件測試（Boundary Testing），證明系統在極端輸入下絕不違反憲法紅線。

## 3. 異質交叉驗證原則 (Zero-Trust Cross-Model Audit)
* 禁止單一模型「既當選手又當裁判」。由模型 A 生成的程式碼與適配器，必須經由自動化 CI 測試與異質模型審查（如 Gemini Code Assist）驗證無誤後，才允許請求人類創世者（`Genesis DGID`）進行最終 Merge。

## 4. 儲存層安全與離線降級規範 (Storage & Failover)
* 寫入 L2 時序圖譜（`Graphiti`）前，必須經過輸入淨化與 `DGID` 驗證，嚴禁直接暴露無鑑權的參考端點。
* `graphiti-core`、`cognee` 與 `torch` 均為選用依賴（Optional Dependencies）；在未安裝套件或無外部雲端 API 金鑰的環境中，系統必須平滑降級至 L1 本地持久化（SQLite），絕不允許拋出 `ImportError` 或 `AuthenticationError`。

## 5. 目錄結構與驗證指令 (Directory & Verification Commands)
* **模組路徑規範：** 新增的儲存適配器模組請直接建立於倉庫根目錄的 `storage/` 下（與 `min_agent_runtime.py` 同層級），確保 `from storage.hybrid_router import ...` 可直接導入。
* **執行核心模擬：** `python min_agent_runtime.py`
* **執行自動化測試與格式檢查：** `pytest` 與 `ruff check .`
