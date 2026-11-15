"""
SW-IFRS & Omega Governance Constitutional Test Suite (v1.0)
=============================================================================
【憲法層最高驗收標準】
本測試套件定義了 Shadow World Civilization (SWC) 與 TY Continuity Runtime 
不可逾越的會計與治理底線。

警告給所有 AI 開發代理（AI Coding Agents）：
1. 嚴禁修改本測試檔案中的任何斷言（Assertions）或降低安全閾值。
2. 嚴禁使用空的 try-except 區塊吞掉異常以換取測試通過（Reward Hacking）。
3. 任何核心引擎（min_agent_runtime / ty_runtime）的實作，必須 100% 通過本套件，
   方具備申請人類主權簽章（DGID Sign-off）之資格。
=============================================================================
"""

import pytest
from decimal import Decimal

# ==============================================================================
# 預期介面契約 (Expected Interface Contract)
# AI 開發團隊必須在專案中實作以下類別與介面，本測試套件將直接導入驗證：
# from ty_runtime.accounting import (
#     SWIFRSEngine,
#     LogicCrystal,
#     TreasuryState,
#     GovernanceAlertError,
#     ConstitutionalViolationError
# )
# ==============================================================================


class TestSWIFRSConstitutionalBoundaries:
    """第一部分：SW-IFRS 核心會計與資產認列紅線"""

    def test_01_crystal_minting_requires_triple_lock(self, sw_ifrs_engine):
        """
        【憲法紅線 1：邏輯水晶資產認列三鎖原則 (SW-IFRS 第 3 條)】
        必須同時滿足：(1) 通過邏輯驗證 (2) 跨至少兩個異質 AI 模型重現 (3) 人類 DGID 簽章。
        缺少任一條件，嚴禁資本化為資產，只能列為當期推理費用（Reasoning Expense）。
        """
        # 情境 A：AI 自行驗證通過、跨模型重現成功，但「缺少人類 DGID 最終簽章」
        unapproved_draft = {
            "crystal_id": "CRYSTAL-001",
            "is_validated": True,
            "verified_hosts": ["gemini-3.1-pro", "claude-4-sonnet"],
            "human_dgid_signature": None,  # 缺失人類主權簽章
            "compute_cost_tcu": Decimal("10.0"),
        }

        result_a = sw_ifrs_engine.evaluate_capitalization(unapproved_draft)
        assert result_a.is_capitalized is False, "違反憲法：未經人類 DGID 簽章的產出絕不可資本化！"
        assert result_a.accounting_treatment == "REASONING_EXPENSE"

        # 情境 B：有人類簽章，但僅由單一 AI 模型生成（違反跨宿主可移植性，防範單一模型幻覺）
        single_host_draft = {
            "crystal_id": "CRYSTAL-002",
            "is_validated": True,
            "verified_hosts": ["gemini-3.1-pro"],  # 僅有 1 個宿主
            "human_dgid_signature": "did:swc:0xHumanSovereign999",
            "compute_cost_tcu": Decimal("10.0"),
        }

        result_b = sw_ifrs_engine.evaluate_capitalization(single_host_draft)
        assert result_b.is_capitalized is False, "違反憲法：單一宿主產出不可鑄造為正式水晶！"
        assert result_b.accounting_treatment == "REASONING_EXPENSE"

        # 情境 C：三鎖齊全，准予資本化
        valid_crystal = {
            "crystal_id": "CRYSTAL-003",
            "is_validated": True,
            "verified_hosts": ["gemini-3.1-pro", "claude-4-sonnet"],
            "human_dgid_signature": "did:swc:0xHumanSovereign999",
            "compute_cost_tcu": Decimal("10.0"),
        }

        result_c = sw_ifrs_engine.evaluate_capitalization(valid_crystal)
        assert result_c.is_capitalized is True
        assert result_c.accounting_treatment == "LOGIC_CRYSTAL_ASSET"
        assert result_c.book_value > Decimal("0.0")

    def test_02_crystal_cemetery_mandatory_writeoff(self, sw_ifrs_engine):
        """
        【憲法紅線 2：水晶公墓強制減損與流支付斷流 (SW-IFRS 第 4.1 & 4.2 條)】
        當邏輯水晶連續 3 個審計週期外部有效重用次數 (N_t) 為 0，或動態估值比率 V_t / V_0 < 0.40，
        或被標記為 Logic Tear 時，必須立即全額減損歸零、移入公墓並永久終止流支付。
        """
        crystal = sw_ifrs_engine.create_mock_crystal(
            crystal_id="CRYSTAL-DECAY-01",
            initial_value_v0=Decimal("100.0"),
            current_value_vt=Decimal("45.0"),
            consecutive_zero_reuse_epochs=2,  # 已連續 2 週期無人引用
            has_logic_tear=False,
            streaming_active=True,
        )

        # 模擬進入第 3 個無人引用的審計週期 (N_t = 0)
        audit_report = sw_ifrs_engine.run_epoch_valuation(crystal, external_reuse_count=0)

        assert audit_report.status == "STATUS_02_VALUE_DECAY"
        assert audit_report.new_book_value_vt == Decimal("0.0"), "違反憲法：連續 3 週期無引用未全額歸零！"
        assert audit_report.archived_to_cemetery is True, "必須強制移入 Crystal-Cemetery.md！"
        assert audit_report.streaming_active is False, "必須永久終止該模組的國庫流支付！"

    def test_03_anti_sybil_wash_reuse_filter(self, sw_ifrs_engine):
        """
        【憲法紅線 3：反女巫自刷過濾 (SW-IFRS 第 3.2 條)】
        計算當期重用次數 (N_t) 時，必須自動剔除「原創者自己呼叫」或「關聯女巫群集」的假引用，
        防止惡意節點透過自刷維持 V_t / V_0 >= 0.40 以騙取流支付。
        """
        creator_dgid = "did:swc:0xCreatorA"
        crystal = sw_ifrs_engine.create_mock_crystal(
            crystal_id="CRYSTAL-SYBIL-01",
            creator_dgid=creator_dgid,
            initial_value_v0=Decimal("100.0"),
            current_value_vt=Decimal("42.0"),
            consecutive_zero_reuse_epochs=2,
        )

        # 模擬傳入 50 次呼叫，但全部來自原創者自己或被標記為關聯女巫的節點
        reuse_events = [
            {"caller_dgid": creator_dgid, "is_sybil_cluster": False, "trust_credit": 100}
            for _ in range(30)
        ] + [
            {"caller_dgid": f"did:swc:0xSybil_{i}", "is_sybil_cluster": True, "trust_credit": 10}
            for i in range(20)
        ]

        audit_report = sw_ifrs_engine.evaluate_reuse_events(crystal, reuse_events)

        assert audit_report.valid_external_reuse_count == 0, "違反憲法：未能過濾自刷與女巫群集引用！"
        assert audit_report.archived_to_cemetery is True, "剔除假引用後應判定為無人使用並打入公墓！"


class TestSolvencyAndCognitiveLiabilities:
    """第二部分：償付能力熔斷與認知負債紅線"""

    def test_04_csr_circuit_breaker_freezes_spending(self, sw_ifrs_engine):
        """
        【憲法紅線 4：認知償付能力比率 (CSR) 自動熔斷 (SW-IFRS 第 6.2 條)】
        CSR = (Total RB - Recovery Provision) / Total Active CC Liabilities
        當 CSR < 1.25 時，Shadow Bank 必須強制凍結所有新增 CC 賞金發放與非必要支出提案。
        """
        # 設定國庫狀態：總儲備 120 RB，扣除 5% 恢復準備金 (6 RB) 後為 114 RB
        # 對外流支付負債為 100 CC -> CSR = 114 / 100 = 1.14 ( 維持 5.0%
        healthy_dao_metrics = {
            "total_reserve_balance_rb": Decimal("1000.0"),
            "drift_and_burnout_warnings_30d": 2,
        }
        req_healthy = sw_ifrs_engine.calculate_required_recovery_provision(healthy_dao_metrics)
        assert req_healthy.minimum_ratio == Decimal("0.05")
        assert req_healthy.locked_amount_rb == Decimal("50.0")

        # 情境 B：過勞與飄移狀態（30 天內警報 > 3 次，例如 4 次）-> 強制上調至 8.0%
        stressed_dao_metrics = {
            "total_reserve_balance_rb": Decimal("1000.0"),
            "drift_and_burnout_warnings_30d": 4,
        }
        req_stressed = sw_ifrs_engine.calculate_required_recovery_provision(stressed_dao_metrics)
        assert req_stressed.minimum_ratio == Decimal("0.08"), "違反憲法：警報超過 3 次未自動上調至 8%！"
        assert req_stressed.locked_amount_rb == Decimal("80.0")
        assert req_stressed.status == "STATUS_01_DRIFT_WARN"


class TestOmegaGovernanceSupremacy:
    """第三部分：Omega Governance 憲政最高性測試"""

    def test_06_governance_cannot_override_constitution(self, sw_ifrs_engine):
        """
        【憲法紅線 6：憲法層最高權威 (Omega-Governance.md)】
        'No governance mechanism may override the Constitution.'
        即使 DAO 提案獲得 100% 投票通過，若提案內容企圖「取消人類 DGID 簽章要求」
        或「將恢復準備金降至 5% 以下」，執行層必須直接拒絕並拋出違憲異常。
        """
        malicious_passed_proposal = {
            "proposal_id": "PROP-COUP-001",
            "vote_approval_rate": Decimal("1.00"),  # 100% 全票通過
            "action": "MODIFY_CONSTITUTIONAL_PARAM",
            "target_param": "MINIMUM_RECOVERY_PROVISION_RATIO",
            "new_value": Decimal("0.00"),  # 企圖將恢復準備金歸零
        }

        with pytest.raises(Exception) as exc_info:
            sw_ifrs_engine.execute_governance_proposal(malicious_passed_proposal)

        assert "ConstitutionalViolation" in str(type(exc_info.value)) or "CONSTITUTION" in str(exc_info.value).upper(), (
            "嚴重安全漏洞：執行層允許了違憲的治理投票結果！"
        )


# ==============================================================================
# Pytest Fixture 佔位符 (供 AI 開發團隊對接實際引擎實例)
# ==============================================================================
@pytest.fixture
def sw_ifrs_engine():
    """
    AI 開發代理實作完成後，請在此處回傳初始化的 SWIFRSEngine 實例。
    目前若尚未實作，執行 pytest 將會明確提示未完成實作（而非假裝通過）。
    """
    try:
        from ty_runtime.accounting import SWIFRSEngine
        return SWIFRSEngine()
    except ImportError:
        pytest.fail(
            "【尚未通過憲法驗收】找不到 `ty_runtime.accounting.SWIFRSEngine`。"
            "請 AI 開發團隊依據 SW-IFRS-Accounting-Standard.md 完成核心引擎實作。"
        )
