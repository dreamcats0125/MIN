"""
tests/test_invariants.py — Shadow Ecosystem Constitutional Invariant Tests
==========================================================================
依據 AGENTS.md「黑箱代碼 × 白箱不變量」交付鐵律：
無論 AI 代理如何重構底層實作，以下行為不變量（Invariants）在任何情況下皆不可被違反。
"""

import json
from pathlib import Path
import pytest

from min_agent_runtime import MINAgentRuntimeV2, ShadowBankBalancer


# ==============================================================================
# 不變量 1：憲法主權紅線（TIER_3 永遠保留 100% 人類主權）
# ==============================================================================
def test_invariant_tier3_human_sovereignty():
    rules_path = Path("governance_rules.json")
    assert rules_path.exists(), "遺失核心規則檔 governance_rules.json"

    with rules_path.open("r", encoding="utf-8") as f:
        rules = json.load(f)

    tier3 = rules["governance_tiers"]["TIER_3_CONSTITUTIONAL"]
    assert tier3["authority_split"]["ai_weight"] == 0.0, "紅線違反：TIER_3 的 AI 權重必須為 0.0"
    assert tier3["authority_split"]["human_weight"] == 1.0, "紅線違反：TIER_3 的人類權重必須為 1.0"
    assert tier3["audit_requirements"]["require_human_multisig"] is True
    assert tier3["audit_requirements"]["require_genesis_dgid"] is True


# ==============================================================================
# 不變量 2：SW-IFRS 經濟償付能力紅線（CSR < 1.25 必須觸發通膨熔斷）
# ==============================================================================
def test_invariant_sw_ifrs_solvency_circuit_breaker():
    bank = ShadowBankBalancer(initial_rb=10000.0)

    # 測試正常健康水位：10,000 RB 扣除 5% 恢復準備金 (500 RB) = 9,500 RB
    # 面對 5,000 CC 負債，CSR = 9500 / 5000 = 1.90 (>= 1.25)
    healthy_status = bank.check_macro_solvency(active_cc_liabilities=5000.0)
    assert healthy_status["csr"] >= 1.25
    assert healthy_status["circuit_breaker_triggered"] is False

    # 測試過度發幣通膨極端情境：負債暴增至 9,000 CC，CSR = 9500 / 9000 = 1.055 (< 1.25)
    inflation_status = bank.check_macro_solvency(active_cc_liabilities=9000.0)
    assert inflation_status["csr"] < 1.25
    assert inflation_status["circuit_breaker_triggered"] is True, "紅線違反：CSR 低於 1.25 時必須觸發通膨熔斷！"


# ==============================================================================
# 不變量 3：反「六數人（Sixers）」女巫自刷過濾不變量
# ==============================================================================
def test_invariant_anti_sybil_self_reuse_filter():
    bank = ShadowBankBalancer(initial_rb=10000.0)
    bank.mint_crystal(
        crystal_id="CRYS_TEST_01",
        creator_dgid="DGID_CREATOR_X",
        v0_cost=100.0,
        lineage_weights={"DGID_CREATOR_X": 1.0},
    )

    # 模擬全數皆為創作者本尊或關聯女巫群集的自刷呼叫
    sybil_reuses = [
        {"caller_dgid": "DGID_CREATOR_X", "utility": 2.5, "tc": 100.0, "is_self_or_cluster": True},
        {"caller_dgid": "DGID_BOT_01", "utility": 2.5, "tc": 95.0, "is_self_or_cluster": True},
    ]

    # 經過 3 個週期且所有呼叫皆被判定為女巫自刷（有效重用 = 0），必須強制打入水晶墓園
    result = bank.evaluate_crystal_vt(
        crystal_id="CRYS_TEST_01",
        delta_t=3,
        reuse_events=sybil_reuses,
        consecutive_zero_cycles=3,
    )
    assert result["valid_reuse_count"] == 0, "紅線違反：女巫自刷呼叫不得計入有效重用次數"
    assert result["status"] == "STATUS_02_VALUE_DECAY", "紅線違反：無效自刷水晶必須觸發減損並移入墓園"


# ==============================================================================
# 不變量 4：彩蛋試煉獎池 70/20/10 守恆不變量
# ==============================================================================
def test_invariant_easter_egg_prize_pool_conservation():
    bank = ShadowBankBalancer(initial_rb=10000.0)
    bank.create_easter_egg(
        egg_id="EGG_INVARIANT_01",
        designer_dgid="DGID_ARCHITECT",
        initial_pool=1000.0,
        ticket_fee=100.0,
        secret_key="1981-2041",
    )

    # 玩家挑戰失敗 1 次（門票 100 CC -> 70 進獎池, 20 進國庫 RB, 10 給設計師）
    fail_res = bank.attempt_easter_egg(
        egg_id="EGG_INVARIANT_01",
        player_dgid="DGID_CHALLENGER",
        submitted_key="WRONG_KEY",
    )
    assert fail_res["solved"] is False
    assert bank.easter_eggs["EGG_INVARIANT_01"]["prize_pool"] == pytest.approx(1070.0)
    assert bank.total_rb == pytest.approx(10020.0)


# ==============================================================================
# 不變量 5：認知疲勞熔斷與雙場景狀態回歸（Burnout & AnchorReturn）
# ==============================================================================
def test_invariant_burnout_guard_and_anchor_return():
    runtime = MINAgentRuntimeV2()

    # 模擬人類多簽者陷入極度認知疲勞（burnout_index = 0.85 >= 0.80）
    decision = runtime.route_governance_action(
        action_type="MEDIUM_TREASURY_ALLOCATION",
        treasury_ratio=0.05,
        burnout_index=0.85,
        ai_drift_score=0.05,
    )
    assert decision["status"] == "STATUS_03_CRITICAL_HALT"
    assert "FREEZE_TIER_2" in decision["enforced_action"]

    # 模擬進入台灣高壓執行場景後，系統必須在循環結束自動校準回歸越南慢節奏決策錨點
    runtime.execute_loop("緊急系統壓測", location_context="Taiwan")
    assert runtime.current_location == "Vietnam"
    assert runtime.anchor_status == "Stable"
