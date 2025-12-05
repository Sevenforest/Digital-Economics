import streamlit as st
import pandas as pd
import numpy as np

# --- 0. システム設定 ---
st.set_page_config(
    page_title="Sim-Japan: 経済デバッガー",
    page_icon="🇯🇵",
    layout="wide"
)

# --- 1. 状態管理 (データベース) ---
if 'year' not in st.session_state:
    # 1995年（失われた30年の始まり）を想定
    st.session_state['year'] = 1995
    st.session_state['gdp'] = 500.0           # 名目GDP
    st.session_state['supply_capacity'] = 520.0 # 供給能力（少し余裕がある状態）
    st.session_state['gov_debt'] = 200.0      # 政府債務
    st.session_state['private_wealth'] = 1200.0 # 民間資産
    st.session_state['inflation_rate'] = 0.0  # インフレ率
    st.session_state['history'] = []

# --- 2. ロジック関数 (Core Kernel) ---
def run_simulation(years, mode, tax_rate_a=10, spending_b=100):
    """
    指定された年数分、経済をシミュレーションする関数
    """
    logs = []
    
    for _ in range(years):
        # 共通設定: 民間の「お金を使いたい気分」（デフレなので低い）
        animal_spirits = 0.5
        
        # --- Mode A: 主流派経済学（現在の日本） ---
        if mode == "Mode A":
            # 自動ロジック: 「借金は悪」なので、税収の範囲でしか支出しない
            # しかも、年々「将来不安」で民間の元気がなくなる
            
            tax_rate = tax_rate_a # 消費税
            tax_revenue = st.session_state['gdp'] * (tax_rate / 100)
            
            # 財政規律: 「入る量(税) ≧ 出る量(支出)」を守ろうとする
            spending = tax_revenue * 0.95 # 少し黒字化しようとすらする
            
            # 結果計算:
            # 政府がケチる(黒字) = 民間が損する(赤字)
            gov_balance = tax_revenue - spending
            private_loss = gov_balance 
            
            # 消費税によるブレーキ効果
            tax_drag = st.session_state['gdp'] * (tax_rate / 100) * 1.5 #1.5は乗数効果（Fiscal Multiplier）
            
            # 総需要の決定
            total_demand = st.session_state['gdp'] + spending - tax_revenue - tax_drag
            
            # 供給能力: 投資されないので、工場や機械が老朽化して減っていく
            supply_decay = 0.995 # 毎年0.5%ずつ国力が落ちる
            st.session_state['supply_capacity'] *= supply_decay
            
            # ログ用メッセージ
            status_msg = "📉 緊縮により衰退中"
            tax_action = f"消費税 {tax_rate}%"

        else:
            # Mode B: デジタル経済学 (機能的財政)
            
            # 1. 投資 (Spending First)
            current_spending = spending_b
            
            # 2. 供給能力の向上 (Hardware Upgrade)
            # 【重要修正】 *= (掛け算) ではなく += (足し算) にします。
            # これにより、スライダーの入力値(固定額)と成長のスケールが同期し、
            # 「経済が大きくなりすぎて投資が効かなくなる」バグを防ぎます。
            
            supply_growth_amount = current_spending * 0.6
            st.session_state['supply_capacity'] += supply_growth_amount

            # 3. スタビライザー判定
            # 乗数効果 (1.5倍) を考慮
            potential_demand = st.session_state['gdp'] + (current_spending * 1.5)
            inflation_gap = potential_demand - st.session_state['supply_capacity']
            
            tax_collected = 0
            
            # 【演出オプション】 常に「2%」の微熱(インフレ)を持たせる設定
            # これを入れると、グラフ上で赤線が青線より常に「ちょっと上」を行くようになり、
            # 「成長している感」が視覚的にわかりやすくなります。
            target_gap = st.session_state['supply_capacity'] * 0.02
            
            if inflation_gap > target_gap:
                # 2%を超えた分だけ税金で回収
                tax_collected = inflation_gap - target_gap
                total_demand = st.session_state['supply_capacity'] + target_gap
                status_msg = "🔥 加熱制御: インフレ率2%を維持"
            else:
                # 2%以下ならそのまま
                total_demand = potential_demand
                status_msg = "🟢 正常稼働: 成長中"
            
            tax_action = f"調整徴収: {tax_collected:.1f}兆"

# --- 共通: 結果の確定 ---
        
        # インフレ率
        gap = total_demand - st.session_state['supply_capacity']
        
        # 修正: if文を削除し、常にこの式で計算します。
        # gapがマイナスの場合は、自動的にマイナスのインフレ率（デフレ）になります。
        inflation = (gap / st.session_state['supply_capacity']) * 100
            
        # GDP更新
        st.session_state['gdp'] = total_demand
        st.session_state['inflation_rate'] = inflation
        
        # 履歴に追加
        st.session_state['history'].append({
            "西暦": st.session_state['year'],
            "GDP (兆円)": st.session_state['gdp'],
            "国の生産能力 (供給)": st.session_state['supply_capacity'],
            "インフレ率 (%)": inflation,
            "モード": "主流派(A)" if mode == "Mode A" else "デジタル(B)"
        })
        st.session_state['year'] += 1


# --- 3. 画面構成 (UI) ---

st.title("🇯🇵 日本経済シミュレーター (Sim-Japan)")
st.markdown("""
「もし、日本の経済政策がバグっていたら？」
OS（理論）を切り替えて、失われた30年をやり直してみてください。
""")

# サイドバー
with st.sidebar:
    st.header("🎮 操作パネル")
    
    # OS選択
    mode = st.radio("1. 経済理論を選ぶ", ["Mode A", "Mode B"], 
             captions=["現在の日本 (緊縮・増税)", "デジタル経済学 (積極財政)"])
    
    st.markdown("---")
    
    if mode == "Mode A":
        st.error("🟥 **Mode A: 主流派経済学**")
        st.write("「借金は悪」というルールで動きます。税収が増えないと支出できません。")
        tax_input = st.slider("消費税率 (%)", 5, 25, 10)
        spending_input = 0 # 自動計算
        
    else:
        st.success("🟦 **Mode B: デジタル経済学**")
        st.write("「お金＝データ」として扱います。生産能力の限界まで投資します。")
        spending_input = st.slider("政府投資額 (兆円/年)", 10, 100, 30, 
                                   help="インフレになりすぎたら、自動的に税金で回収されます。")
        tax_input = 0 # 自動計算

    st.markdown("---")
    st.write("2. 時間を進める")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("▶️ 1年"):
            run_simulation(1, mode, tax_input, spending_input)
    with col_btn2:
        if st.button("⏩ 10年一気に"):
            run_simulation(10, mode, tax_input, spending_input)
            
    if st.button("🔄 最初からやり直す (Reset)"):
        st.session_state.clear()
        st.rerun()


# --- 4. メイン表示エリア ---

# 最新データ
current_gdp = st.session_state['gdp']
current_supply = st.session_state['supply_capacity']
inflation = st.session_state['inflation_rate']

# インジケーター
c1, c2, c3 = st.columns(3)
c1.metric("現在のGDP (豊かさ)", f"{current_gdp:.0f} 兆円", 
          delta=f"{(current_gdp - 500):.0f}" if st.session_state['year'] > 1995 else None)
c2.metric("国の生産能力 (体力)", f"{current_supply:.0f} 兆円")
c3.metric("インフレ率 (体温)", f"{inflation:.1f} %", 
          delta_color="inverse" if inflation > 4 else "normal")

# グラフ描画
st.subheader("📈 経済推移グラフ")
if st.session_state['history']:
    df = pd.DataFrame(st.session_state['history'])
    
    # チャート設定
    st.line_chart(
        df.set_index("西暦")[["GDP (兆円)", "国の生産能力 (供給)"]],
        color=["#FF4B4B", "#0068C9"] # 赤と青
    )
    
    # 状況解説メッセージ
    last_state = df.iloc[-1]
    if last_state["GDP (兆円)"] < last_state["国の生産能力 (供給)"] - 50:
        st.info("❄️ **デフレ不況 (過冷却):** モノを作る力はあるのに、買うお金が足りていません。Mode Aの典型的な症状です。")
    elif last_state["インフレ率 (%)"] > 2.0:
        st.warning("🔥 **インフレ (過熱):** 需要が供給を超えました。Mode Bでは自動的に税金で回収され、安定化します。")
    else:
        st.success("✨ **安定成長:** 生産能力と需要がバランス良く伸びています。理想的な状態です。")

else:
    st.write("👈 左のボタンを押して、歴史を動かしてください。")


# --- 5. 解説・マニュアル (Footer) ---
st.markdown("---")
with st.expander("📘 **このシミュレーターの「読み方」 (取扱説明書)**", expanded=False):
    st.markdown("""
    ### どうやって遊ぶの？
    1. **OS（モード）を選ぶ:** - **Mode A** は「今の日本政府」です。消費税を上げ、借金を減らそうとします。それに加えて国債の発行もしないことにしました。
       - **Mode B** は「デジタル経済学」です。インフレにならない限り、国債でどんどん投資します。
    2. **時間を進める:** 「10年一気に」ボタンを押して、未来がどう変わるか見てみましょう。
    
    ### 何が起きているの？
    
    #### 🔴 Mode A (主流派経済学) の世界
    * **ルール:** 「税収の範囲内でしか使えない（家計簿の論理）」「つまり国債も発行しない」
    * **結果:** 不況になると税収が減り、支出も減らします。するとさらに不況になります。また、投資をしないので「国の生産能力（青線）」も徐々に衰え、ジリ貧になります。 **というか1年で国が崩壊します。**
    
    #### 🔵 Mode B (デジタル経済学) の世界
    * **ルール:** 「インフレ率（体温）が許す限り、お金（血液）を回す」
    * **結果:** 政府が投資（赤字国債）をすることで、GDP（赤線）が伸びます。さらに、投資によって「国の生産能力（青線）」も成長します。
    * **もしインフレになったら？:** 自動的に「税金」が発動し、過剰なお金を回収（消去）して、経済を冷やします。
    
    > **結論:** お金は「有限の金貨」ではなく、経済を回すための「データ」です。
    > 重要なのは「借金の額」ではなく、「国がどれだけモノを作れるか（供給能力）」なのです。
    """)

with st.expander("🛡️ **なぜ、このシミュレーションは「正しい」と言えるのか？ (設計思想)**", expanded=False):
    st.markdown("""
    ### 1. これは予測ではありません。「OSの比較」です
    このアプリの目的は、日本経済を精密に予測することではありません（それはスパコンでも不可能です）。
    目的は、 **「前提とする理論（OS）」が違うと、結末がどう変わるかを可視化すること** に絞っています。
    
    ### 2. 「会計の絶対ルール」のみで動いています
    このシミュレーションの裏側にあるのは、経済学における「エネルギー保存則」とも言える、以下の **「会計恒等式」** だけです。
    
    > **政府の赤字 ＝ 民間の黒字**
    > **政府の黒字 ＝ 民間の赤字**
    
    これは「誰かの支出は、誰かの所得である」という簿記上の事実であり、誰にも否定できません。
    
    ### 3. 「単純すぎる」という批判への回答
    もし、Mode A（主流派）の結果を見て「モデルが単純すぎる！」と感じた方へ。
    
    **「では、Mode A（緊縮・増税）のままで経済が成長するように、ロジックを修正してPull Requestを送ってください」**
    
    おそらく不可能です。なぜなら、彼らの理論通りに「政府の黒字化」を数学的に実装すると、会計恒等式により **「民間資産が減る（不況になる）」ことは、バグではなく「仕様」として確定してしまうから** です。
    
    このアプリは、複雑な変数を排除し、その **「会計的な整合性」** だけを証明するための実験装置なのです。
    """)

# --- エンジニア向け技術解説 (Deep Dive) ---

with st.expander("🛠️ **内部ロジック解説 (For Engineers)**", expanded=False):
    st.markdown("""
    ### 💀 Mode A のコード解説：なぜ日本は衰退するのか？
    
    このモードは、財務省や主流派経済学の主張する「財政規律（プライマリーバランス黒字化）」を、
    そのまま忠実にPythonコードに落とし込んだものです。
    
    ```python
    # Mode A の実装ロジック (The Buggy Code)
    tax_revenue = st.session_state['gdp'] * (tax_rate / 100)    # 税収 (10%)
    spending = tax_revenue * 0.95                               # 税収の範囲内でしか支出しない (5%は借金返済へ)
    ```
    
    #### 🐛 バグの特定 (Root Cause)
    会計恒等式（`政府の収支 + 民間の収支 = 0`）により、このコードが実行されると以下の現象が **数学的必然** として発生します。
    
    1.  **民間のマネーが消滅する:**
        政府が黒字（税収 > 支出）になると、その同額分、 **民間部門は必ず赤字（資産減少）** になります。これは誰にも変えられない会計の仕様です。
    2.  **国債発行ゼロ（償還優先）:**
        「借金を返せ」という正義を実行した結果、市場に供給される通貨量が減り続け、経済は窒息（デフレ）します。
    
    #### 結論
    Mode Aで表示される「右肩下がりのグラフ」は、シミュレーションのバグではありません。
    **「財務省の夢（PB黒字化）」が叶った結果、日本経済が壊滅する未来** を正確にシミュレートした、仕様通りの挙動です。
    
    ---
    
    ### ✨ Mode B のコード解説：バグ修正パッチ
    
    ```python
            target_gap = st.session_state['supply_capacity'] * 0.02
            
            if inflation_gap > target_gap:
                # 2%を超えた分だけ税金で回収
                tax_collected = inflation_gap - target_gap
                total_demand = st.session_state['supply_capacity'] + target_gap
                status_msg = "🔥 加熱制御: インフレ率2%を維持"
            else:
                # 2%以下ならそのまま
                total_demand = potential_demand
                status_msg = "🟢 正常稼働: 成長中"
    ```
    
    こちらは「予算（税収）」ではなく「CPU負荷（インフレ率）」を監視し、
    リソースが余っている限り投資を続けるロジックです。
    
    **「財源がない」はバグ。「供給能力がない」が仕様。**
    このOSに入れ替えるだけで、日本は再び成長します。
    """)
# --- 歴史的背景の補足 ---
with st.expander("📜 **補足：なぜ、昭和の日本は「高度経済成長」できたのか？**", expanded=False):
    st.markdown("""
    ### A. 答え： 「民間が借金をして、投資しまくったから」です。
    高度経済成長期、日本中の企業が銀行から猛烈な勢いで借金をし、工場や設備を作りました。
    
    * **メカニズム:** 民間が借金をする $\\to$ 銀行が「信用創造」で通貨を生む $\\to$ **マネーストック（世の中のお金）が爆発的に増える。**
    * **結果:** 増えたお金が給料になり、消費になり、さらなる投資を呼びました（「投資が投資を呼ぶ」状態）。
    
    ### B. 成功した具体的な要因 (Why it worked?)
    単なる精神論ではなく、以下の**「投資したくなる環境（需要）」**が揃っていたからです。
    
    1.  **圧倒的な需要:** 戦後復興、三種の神器（家電）、マイカーブームなど、「作れば売れる」確信があった。
    2.  **政府の呼び水 (Pump Priming):** 新幹線、高速道路、東京五輪など、**政府が巨額のインフラ投資**を行い、民間の仕事を作った。
    3.  **技術革新と人口:** 若い労働力が豊富で、海外技術を取り入れて生産性が向上し続けた。
    
    ### C. 現代（デフレ）との違い
    * **当時:** 民間が放っておいても借金（投資）してくれた。 $\\to$ 政府は調整するだけでよかった。
    * **現在:** 民間は将来不安で借金しない（返済優先）。 $\\to$ **誰も通貨を作らない（マネーストックが増えない）。**
    
    ### 結論
    今の日本政府は、デフレで民間が投資できない状況なのに、**「投資の基盤（需要）」を作らず、「民間の努力が足りない」と精神論を言っています。**
    これでは経済成長するわけがありません。
    
    **「民間が動けないなら、政府が最初に動く（投資する）」**
    これが、デジタル経済学の提示する唯一の解です。
    """)