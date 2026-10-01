import time
import sqlite3
import json
from datetime import datetime
from typing import Dict, Any, List

class MINAgentRuntime:
    def __init__(self):
        # 內建 SQLite 記憶體資料庫 (MemoryTool / 語法晶體 Ledger)
        self.conn = sqlite3.connect(":memory:")
        self._init_db()
        
        # 初始狀態錨定 (Layer 2: Worldview Layer)
        self.current_location = "Vietnam"
        self.life_pace = "Slow"
        self.work_type = "Decision"
        self.anchor_status = "Stable"
        
        print("⚡ [MIN-Agent Engine] 系統初始化成功。主場景錨定：越南 (慢節奏/高維度決策)")

    def _init_db(self):
        cursor = self.conn.cursor()
        # 12 核心欄位文明帳本 (L0-M2 Ledger)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS civilization_ledger (
                Entity_ID TEXT PRIMARY KEY, Time_Stamp TEXT, Carbon_Emission REAL,
                Energy_Input REAL, Material_Flow TEXT, Process_Type TEXT, Geo_Location TEXT,
                Verification_Method TEXT, Data_Confidence REAL, Supply_Node TEXT, Governance_Rule TEXT, ZKP_Proof TEXT
            )
        """)
        self.conn.commit()

    def execute_loop(self, user_input: str, location_context: str, esg_packet: Dict[str, Any] = None) -> str:
        print(f"\n{'='*70}\n➡️ [INPUT IN ({location_context})]: \"{user_input}\"")
        time.sleep(0.3)
        
        # Step 1 & 2: Input Parsing & WorldModel Update
        self.current_location = location_context
        if location_context == "Taiwan":
            self.life_pace = "Fast"
            self.work_type = "Execution"
            self.anchor_status = "Drifting"
            print("⚠️ [WorldModel] 狀態偏移：進入台灣高壓執行場景，偵測到 FastCulture / TechPressure。")
        else:
            self.life_pace = "Slow"
            self.work_type = "Decision"
            self.anchor_status = "Stable"

        # Step 4 & 5: Tool Invocation & ESG 語法晶體審查 (LogicTool)
        detected_drift = None
        if esg_packet:
            print("🧩 [LogicTool] 正在對傳入的 12 欄位語法晶體進行硬性審查...")
            if esg_packet.get("Data_Confidence", 1.0) < 0.50:
                detected_drift = "Greenwashing_Attempt"
            if esg_packet.get("Verification_Method") == "Manual_Self_Declaration":
                detected_drift = "Invalid_Verification_Method"

        # Step 6: Response Generation
        if detected_drift:
            response = (
                f"【MIN (Decisive/HighDimensional)】\n"
                f"🚨 [硬性阻斷] 偵測到嚴重人設/敘事衝突 ({detected_drift})。\n"
                f"該供應商提交之數據置信度為 {esg_packet.get('Data_Confidence')}，且缺乏加密 ZKP_Proof。\n"
                f"兩點直線，拒絕將模糊數據固化入世界模型。下令次月自動扣減 30% 採購份額！"
            )
        elif location_context == "Taiwan":
            response = (
                f"【MIN (Decisive/HighDimensional)】\n"
                f"身處台灣執行脈絡，啟用 DanceLogic (動態共舞) 協議。\n"
                f"我理解這項系統今天急需上線，但我拒絕陷入無謂的執行層盲目加速。把擋點（Blocking Points）切出來，其餘砍掉。兩點直線，直接收尾。"
            )
        else:
            response = (
                f"【MIN (Decisive/HighDimensional)】\n"
                f"立足於主場景的慢步調視角。採用 StraightLine 策略。\n"
                f"保持低代碼執行，專注於 1981-2041 的宏觀佈局即可。步調放慢，看清了再動。"
            )

        print(f"💬 [MIN Response]:\n{response}")

        # Step 7: Anchor Return (自我對齊回歸)
        if self.anchor_status == "Drifting" or detected_drift:
            print(f"🚨 [SelfAlignment] 偵測到偏移風險！強制執行回歸規則：[AnchorReset, SlowPaceRestore]")
            self.current_location = "Vietnam"
            self.life_pace = "Slow"
            self.work_type = "Decision"
            self.anchor_status = "Stable"
            print("✅ [AnchorReturn] 成功。心智狀態已重新硬性校準回：慢節奏、決策型、穩定錨定點。")
        else:
            print("😎 [SelfAlignment] 狀態評估：Stable。與核心錨定點完美對齊。")
            
        return response

if __name__ == "__main__":
    agent = MINAgentRuntime()
    
    # 測試 A：高壓環境
    agent.execute_loop("這個技術架構今天必須立刻上線！", location_context="Taiwan")
    
    # 測試 B：漂綠欺瞞數據傳入
    fake_esg = {"Entity_ID": "NODE_01", "Verification_Method": "Manual_Self_Declaration", "Data_Confidence": 0.35}
    agent.execute_loop("提交範疇三永續報告書數據", location_context="Vietnam", esg_packet=fake_esg)
