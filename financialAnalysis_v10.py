import streamlit as st
import pandas as pd
import datetime # タイムスタンプ用
import json # テキストをJavaScriptに安全に渡すため # 今回は不要になる

# (既存の company_text, df_pl, df_bs_assets, df_bs_liabilities_netassets の定義はそのまま)
# 会社の状況に関するテキスト
company_text = """
麺屋 匠は、資本金300万円、総資産約8000万円、年間売上高約1億2000万円、従業員8名（正社員2名、アルバイト6名）の、創業10年になる個人経営のラーメン屋です。店主の長年のこだわりである「国産・無添加素材」を前面に押し出し、特に化学調味料を一切使用せず、厳選した国産豚骨と鶏ガラ、香味野菜を長時間煮込んだ濃厚かつ後味の良いスープが自慢です。麺も国産小麦を使用した自家製麺で、常連客からは「一度食べたら忘れられない味」と高い評価を得ています。
　店舗は駅前の好立地にあり、カウンター席とテーブル席を合わせて20席ほどの小規模な店舗です。主な顧客層は地元住民や近隣のオフィスワーカーで、特にランチタイムや週末は行列ができるほどの人気を誇っていました。テイクアウトやデリバリーは行っておらず、店舗での飲食提供のみに特化しています。
　しかし、ここ数年、麺屋 匠の周辺地域に大手ラーメンチェーン店や個性的なラーメン店が次々と出店し、競争が激化しています。その影響で、ピーク時の客足が鈍り始め、売上が徐々に減少傾向にあります。さらに、昨今の世界情勢の影響を受け、こだわりの国産原材料の仕入れ価格が高騰しており、特にスープの主原料である豚骨や鶏ガラ、小麦粉の価格上昇が経営を圧迫しています。
　このような状況に対し、店主は「お客様に本物の味を提供し続ける」という信念から、安易な食材の変更や値上げには慎重な姿勢です。当面は、SNSでの情報発信強化や、ランチタイム限定のセットメニュー導入などで客数増加を図ろうとしていますが、人件費や固定費の削減は考えておらず、むしろ従業員のモチベーション維持のため、待遇改善も視野に入れています。
　また、現状打破のため、新たな取り組みとして、これまで培ってきたスープのノウハウを活かした「お土産用冷凍ラーメン」の開発・販売を検討し始めました。これは、店舗に来られない遠方の顧客や、家庭でも「麺屋 匠」の味を楽しみたいというニーズに応えるものです。ただし、冷凍ラーメンの製造には新たな設備投資が必要となるほか、パッケージデザインや販路開拓など、これまで経験のない課題も山積しています。店主は、この新事業が起爆剤となることを期待しつつも、資金繰りや採算性を慎重に見極める必要があると考えています。
"""

# 財務諸表データ (単位: 千円)
data_pl = {
    '勘定科目': ['売上高', '売上原価', '売上総利益', '販売費及び一般管理費', '営業利益', '営業外収益', '営業外費用', '経常利益', '特別利益', '特別損失', '税引前当期純利益', '法人税等', '当期純利益'],
    '令和3年度': [125000, 50000, 75000, 32000, 43000, 100, 150, 42950, 0, 0, 42950, 12885, 30065],
    '令和4年度': [115000, 51750, 63250, 32500, 30750, 120, 170, 30700, 0, 0, 30700, 9210, 21490]
}
df_pl = pd.DataFrame(data_pl)

data_bs_assets = {
    '資産の部': ['流動資産', '現金・預金', '売掛金・受取手形', '製品・原材料', 'その他の流動資産', '固定資産', '建物・工具等', '無形固定資産', '投資その他の資産', '資産合計'],
    '令和3年度': [31000, 15000, 2500, 12000, 1500, 44000, 32500, 500, 11000, 75000],
    '令和4年度': [38000, 25000, 2000, 10000, 1000, 42000, 30000, 500, 11500, 80000]
}
df_bs_assets = pd.DataFrame(data_bs_assets)

data_bs_liabilities_netassets = {
    '負債・純資産の部': ['流動負債', '買掛金', '短期借入金', '未払金', '未払法人税等', 'その他の流動負債', '固定負債', '長期借入金', 'リース債務', '負債合計', '純資産の部', '資本金', '利益剰余金', '純資産合計', '負債純資産合計'],
    '令和3年度': [38490, 4167, 18000, 2500, 12885, 938, 20000, 20000, 0, 58490, '', 3000, 13510, 16510, 75000],
    '令和4年度': [26000, 4313, 10000, 2000, 9210, 477, 16000, 15000, 1000, 42000, '', 3000, 35000, 38000, 80000]
}
df_bs_liabilities_netassets = pd.DataFrame(data_bs_liabilities_netassets)


# Streamlit アプリケーション
st.set_page_config(layout="wide")

st.title('経営分析学習支援ツール: 麺屋 匠')

# サイドバーのコンテンツ (変更なし)
st.sidebar.title("学習支援情報")
with st.sidebar.expander("📊 収益性分析の基礎知識", expanded=False):
    st.markdown("""**収益性分析とは？**\n企業がどれだけ効率的に利益を上げているかを評価する分析です。\n\n**代表的な収益性指標（売上高利益率）**\n* **売上高総利益率:** `(売上総利益 ÷ 売上高) × 100`\n 商品やサービスの基本的なマージンを示します。\n* **売上高営業利益率:** `(営業利益 ÷ 売上高) × 100`\n 企業の本業での稼ぐ力を示す重要な指標です。\n* **売上高経常利益率:** `(経常利益 ÷ 売上高) × 100`\n 財務活動も含めた企業全体の通常の活動から得られる収益力を示します。\n* **売上高当期純利益率:** `(当期純利益 ÷ 売上高) × 100`\n 最終的な企業の儲けを示す指標です。\n\n**関連するコスト率**\n* **売上高原価率:** `(売上原価 ÷ 売上高) × 100`\n* **売上高販管費率:** `(販売費及び一般管理費 ÷ 売上高) × 100`""")
with st.sidebar.expander(" SWOT分析のフレームワーク", expanded=False):
    st.markdown("""SWOT分析は、企業の内部環境と外部環境を分析し、戦略立案に役立てるフレームワークです。\n\n* **S (Strengths - 強み):** 内部の長所。\n* **W (Weaknesses - 弱み):** 内部の短所。\n* **O (Opportunities - 機会):** 外部の要因や環境変化。\n* **T (Threats - 脅威):** 外部の要因や環境変化。\n\n**クロスSWOT分析による戦略立案のヒント**\n* **SO戦略:** 強みを活かして機会を最大限に活用。\n* **WO戦略:** 弱みを克服しつつ機会を活かす。\n* **ST戦略:** 強みを活かして脅威の影響を回避・軽減。\n* **WT戦略:** 最悪の事態を避けるための防衛策。""")
with st.sidebar.expander("📝 記述問題のポイント解説", expanded=False):
    st.markdown("""
    課題の記述問題に取り組む上での考え方のヒントです。

    1.  **着眼点を見つける**
        * 計算した財務指標の中で、特に大きく悪化しているものはどれか？
        * 「麺屋 匠の状況」の文章の中に、その悪化の原因を示唆する記述はどこにあるか？
        * （例：原材料費の高騰、競争の激化、売上の落ち込み、コスト削減の難しさなど）

    2.  **論理的に説明する**
        * 「【企業の状況A】によって【財務数値B】が変動（悪化or改善）し、さらに【企業の状況C】によって【財務数値D】が影響を受けた（悪化したor改善した）結果、【指標の構成要素E（財務指標の分子or分母）】が変化（減少or増加）し、指標全体が悪化（改善）した」
        * というように、企業の具体的な状況、それが財務数値に与える影響、そして指標の計算構造を結びつけて説明しましょう。

    3.  **簡潔にまとめる**
        * 80字以内という文字数制限があります。最も重要な要因に絞り込み、無駄のない言葉で表現する練習です。
        * キーワードを効果的に使いましょう。
    """)

st.header('課題')
st.markdown("「麺屋 匠」の状況を読み、直近の経営状況において悪化したと考えられる収益性の財務指標を1つ挙げ、その主な理由を合わせて80字以内で述べなさい。")
st.markdown("---")

# session_stateの初期化
if 'calculated_ratios' not in st.session_state:
    st.session_state.calculated_ratios = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()


tab1, tab2, tab3, tab4 = st.tabs(["企業の状況と財務諸表", "財務指標の計算", "SWOT分析", "課題への取り組み"])

with tab1: #変更なし
    st.header('麺屋 匠の状況')
    st.markdown(company_text)
    st.markdown("---")
    st.header('財務諸表（単位：千円）')
    st.subheader('損益計算書')
    st.dataframe(df_pl.set_index('勘定科目'))
    st.markdown("---")
    st.subheader('貸借対照表')
    col_bs_left, col_bs_right = st.columns(2)
    with col_bs_left:
        st.markdown("##### 資産の部")
        def style_total_row_assets(row):
            if row.name == '資産合計': return ['font-weight: bold'] * len(row)
            return [''] * len(row)
        st.dataframe(df_bs_assets.set_index('資産の部').style.apply(style_total_row_assets, axis=1))
    with col_bs_right:
        st.markdown("##### 負債・純資産の部")
        def style_total_row_liab_net(row):
            if row.name in ['負債合計', '純資産合計', '負債純資産合計', '純資産の部']:
                return ['font-weight: bold'] * len(row)
            return [''] * len(row)
        st.dataframe(df_bs_liabilities_netassets.set_index('負債・純資産の部').style.apply(style_total_row_liab_net, axis=1))
    st.info("上記のテキストと財務諸表をよく読んで、経営状況を把握しましょう。")

with tab2: #変更なし
    st.header('収益性分析 - 各種利益率の計算')
    st.markdown("以下の各収益性指標について、計算式の[ ]に財務諸表から適切な数値を入力してください。数値（千円単位）を入力すると、自動的に比率が計算され、前年度からの変化（ポイント差）も表示されます。")
    def get_pl_value(item_name, year_column_name):
        try:
            value = df_pl[df_pl['勘定科目'] == item_name][year_column_name].iloc[0]
            return int(value)
        except (IndexError, ValueError): return None

    def show_ratio_calculation(ratio_name, numerator_name, denominator_name, key_prefix, r3_num_actual, r3_den_actual, r4_num_actual, r4_den_actual):
        st.subheader(ratio_name)
        st.markdown(f"**計算式:** `{numerator_name} ÷ {denominator_name} × 100`")
        result_r3, result_r4 = None, None
        num_r3_input_val, den_r3_input_val = None, None
        num_r4_input_val, den_r4_input_val = None, None

        col_calc_1, col_calc_2 = st.columns(2)
        with col_calc_1:
            st.markdown("##### 令和3年度")
            num_r3_input_val = st.number_input(f"{numerator_name}【R3】", key=f"{key_prefix}_num_r3", value=None, placeholder=f"例: {r3_num_actual or '数値'}", format="%d", step=1, help=f"損益計算書から令和3年度の「{numerator_name}」を入力")
            den_r3_input_val = st.number_input(f"{denominator_name}【R3】", key=f"{key_prefix}_den_r3", value=None, placeholder=f"例: {r3_den_actual or '数値'}", format="%d", step=1, help=f"損益計算書から令和3年度の「{denominator_name}」を入力")
            if num_r3_input_val is not None and den_r3_input_val is not None:
                if den_r3_input_val != 0:
                    result_r3 = (num_r3_input_val / den_r3_input_val) * 100
                    st.metric(label=f"{ratio_name} (令和3年度)", value=f"{result_r3:.2f} %")
                    st.session_state.calculated_ratios[f"{key_prefix}_r3_num"] = num_r3_input_val
                    st.session_state.calculated_ratios[f"{key_prefix}_r3_den"] = den_r3_input_val
                    st.session_state.calculated_ratios[f"{key_prefix}_r3_res"] = result_r3
                    st.session_state.calculated_ratios[f"{key_prefix}_ratio_name"] = ratio_name
                else: st.warning("計算不能 (分母が0です)")
            else: st.info("分子と分母の数値を入力してください。")
        with col_calc_2:
            st.markdown("##### 令和4年度")
            num_r4_input_val = st.number_input(f"{numerator_name}【R4】", key=f"{key_prefix}_num_r4", value=None, placeholder=f"例: {r4_num_actual or '数値'}", format="%d", step=1, help=f"損益計算書から令和4年度の「{numerator_name}」を入力")
            den_r4_input_val = st.number_input(f"{denominator_name}【R4】", key=f"{key_prefix}_den_r4", value=None, placeholder=f"例: {r4_den_actual or '数値'}", format="%d", step=1, help=f"損益計算書から令和4年度の「{denominator_name}」を入力")
            if num_r4_input_val is not None and den_r4_input_val is not None:
                if den_r4_input_val != 0:
                    result_r4 = (num_r4_input_val / den_r4_input_val) * 100
                    st.metric(label=f"{ratio_name} (令和4年度)", value=f"{result_r4:.2f} %")
                    st.session_state.calculated_ratios[f"{key_prefix}_r4_num"] = num_r4_input_val
                    st.session_state.calculated_ratios[f"{key_prefix}_r4_den"] = den_r4_input_val
                    st.session_state.calculated_ratios[f"{key_prefix}_r4_res"] = result_r4
                    st.session_state.calculated_ratios[f"{key_prefix}_ratio_name"] = ratio_name
                else: st.warning("計算不能 (分母が0です)")
            else: st.info("分子と分母の数値を入力してください。")

        if result_r3 is not None and result_r4 is not None:
            change = result_r4 - result_r3
            st.session_state.calculated_ratios[f"{key_prefix}_change"] = change
            delta_color_val = "off"
            if ratio_name in ["売上高総利益率", "売上高営業利益率", "売上高経常利益率", "売上高当期純利益率"]:
                if change > 0.005: delta_color_val = "normal"
                elif change < -0.005: delta_color_val = "inverse"
            elif ratio_name in ["売上高原価率", "売上高販管費率"]:
                if change < -0.005: delta_color_val = "normal"
                elif change > 0.005: delta_color_val = "inverse"
            st.metric(label="変化 (令和4年度 - 令和3年度)", value=f"{change:+.2f} pt", delta_color=delta_color_val)
        else: st.markdown("変化 (令和4年度 - 令和3年度): `両年度の計算後に表示`")
        st.markdown("---")

    show_ratio_calculation("売上高総利益率", "売上総利益", "売上高", "gpm", get_pl_value("売上総利益", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("売上総利益", "令和4年度"), get_pl_value("売上高", "令和4年度"))
    show_ratio_calculation("売上高原価率", "売上原価", "売上高", "cosr", get_pl_value("売上原価", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("売上原価", "令和4年度"), get_pl_value("売上高", "令和4年度"))
    show_ratio_calculation("売上高販管費率", "販売費及び一般管理費", "売上高", "sgar", get_pl_value("販売費及び一般管理費", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("販売費及び一般管理費", "令和4年度"), get_pl_value("売上高", "令和4年度"))
    show_ratio_calculation("売上高営業利益率", "営業利益", "売上高", "opm", get_pl_value("営業利益", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("営業利益", "令和4年度"), get_pl_value("売上高", "令和4年度"))
    show_ratio_calculation("売上高経常利益率", "経常利益", "売上高", "rpm", get_pl_value("経常利益", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("経常利益", "令和4年度"), get_pl_value("売上高", "令和4年度"))
    show_ratio_calculation("売上高当期純利益率", "当期純利益", "売上高", "npm", get_pl_value("当期純利益", "令和3年度"), get_pl_value("売上高", "令和3年度"), get_pl_value("当期純利益", "令和4年度"), get_pl_value("売上高", "令和4年度"))

    st.info("**考察のポイント：**\n* 各利益率はどのように変化しましたか？\n* その変化の背景には、「麺屋 匠の状況」で述べられているどのような出来事が影響していると考えられますか？")

with tab3: #変更なし
    st.header('SWOT分析')
    st.markdown("「麺屋 匠」の状況を踏まえ、内部環境（強み・弱み）と外部環境（機会・脅威）を分析してみましょう。")
    col_s, col_w = st.columns(2)
    with col_s: st.subheader("強み (Strengths)"); st.text_area("（例：こだわりの味、国産・無添加素材、自家製麺、駅前の好立地など）", height=150, key="swot_s")
    with col_w: st.subheader("弱み (Weaknesses)"); st.text_area("（例：テイクアウト・デリバリー未対応、小規模店舗、価格戦略への柔軟性の欠如など）", height=150, key="swot_w")
    col_o, col_t = st.columns(2)
    with col_o: st.subheader("機会 (Opportunities)"); st.text_area("（例：お土産用冷凍ラーメンの開発、SNS活用、健康志向の高まりなど）", height=150, key="swot_o")
    with col_t: st.subheader("脅威 (Threats)"); st.text_area("（例：競争激化、原材料価格の高騰、顧客ニーズの変化など）", height=150, key="swot_t")

    if st.button("SWOT分析を元に考察する", key="swot_analyze"):
        if st.session_state.get("swot_s") or st.session_state.get("swot_w") or \
           st.session_state.get("swot_o") or st.session_state.get("swot_t"):
            st.info("""**考察のポイント：**\n* 強みを活かして機会を掴むには？ (SO戦略)\n* 弱みを克服しつつ機会を活かすには？ (WO戦略)\n* 強みを活かして脅威を切り抜けるには？ (ST戦略)\n* 弱みと脅威が重なった場合のリスクと対策は？ (WT戦略)""")
        else: st.warning("SWOTの各項目に何か一つでも入力してから考察を進めてみましょう。")

with tab4:
    st.header('記述問題への取り組み')
    st.markdown("ここまでの分析を踏まえて、冒頭の記述問題に挑戦してみましょう。")
    st.subheader("解答のヒント")
    st.markdown("""1.  **悪化した収益性指標の特定**\n2.  **主な理由の分析**\n3.  **80字以内での記述**""")

    st.subheader("解答入力欄")
    profitability_ratios_options = ["売上高総利益率", "売上高原価率", "売上高販管費率", "売上高営業利益率", "売上高経常利益率", "売上高当期純利益率"]
    selected_ratio = st.selectbox("悪化したと考えられる収益性の財務指標を選択してください:", options=profitability_ratios_options, index=None, placeholder="指標を選択してください...", key="tab4_selected_ratio")
    reason_text = st.text_area("選択した指標が悪化した主な理由を80字以内で記述してください:", height=100, max_chars=80, key="tab4_reason_input")
    student_id_input = st.text_input("学生ID（または識別番号）を入力してください（任意）:", key="student_id_input_tab4_v2") # 修正: student_id_input に変更

    if st.button("提出用テキストファイルを自動生成", key="generate_submission_file_button"): # ボタンのラベルとキーを変更
        if not selected_ratio:
            st.warning("財務指標を選択してください。")
        elif not reason_text:
            st.warning("理由を記述してください。")
        else:
            submission_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            timestamp_str_for_text = submission_time.strftime("%Y-%m-%d %H:%M:%S JST")
            timestamp_str_for_filename = submission_time.strftime("%Y%m%d_%H%M%S") # ファイル名用のタイムスタンプ

            elapsed_time_delta = submission_time.replace(tzinfo=None) - st.session_state.start_time
            total_seconds = int(elapsed_time_delta.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_time_str = ""
            if hours > 0:
                elapsed_time_str += f"{hours}時間"
            if minutes > 0 or hours > 0:
                 elapsed_time_str += f"{minutes}分"
            elapsed_time_str += f"{seconds}秒"
            if not elapsed_time_str:
                elapsed_time_str = "0秒"

            swot_s = st.session_state.get("swot_s", "未入力")
            swot_w = st.session_state.get("swot_w", "未入力")
            swot_o = st.session_state.get("swot_o", "未入力")
            swot_t = st.session_state.get("swot_t", "未入力")

            calculated_ratios_summary = "【計算した財務指標（「財務指標の計算」タブより）】\n"
            any_ratio_calculated = False
            ratio_key_prefixes = ["gpm", "cosr", "sgar", "opm", "rpm", "npm"]

            for key_prefix in ratio_key_prefixes:
                if f"{key_prefix}_r4_res" in st.session_state.calculated_ratios:
                    ratio_name = st.session_state.calculated_ratios.get(f"{key_prefix}_ratio_name", "不明な指標")
                    r4_res = st.session_state.calculated_ratios.get(f"{key_prefix}_r4_res")
                    change = st.session_state.calculated_ratios.get(f"{key_prefix}_change")
                    summary_line = f"- {ratio_name} (令和4年度): {r4_res:.2f}%"
                    if change is not None:
                        summary_line += f" (前年度比: {change:+.2f}pt)\n"
                    else:
                        summary_line += " (前年度の計算なし)\n"
                    calculated_ratios_summary += summary_line
                    any_ratio_calculated = True
            if not any_ratio_calculated:
                calculated_ratios_summary += "計算された財務指標はありませんでした。\n"

            # ★修正箇所: ファイルコンテンツの作成
            submission_file_content = f"""## 麺屋 匠 経営分析 課題取り組み内容

**提出日時:** {timestamp_str_for_text}
**学生ID:** {student_id_input if student_id_input else "未入力"}
**アプリ利用時間:** {elapsed_time_str}

---
### 記述問題の解答

**選択した収益性指標:** {selected_ratio}
**主な理由 (80字以内):**
{reason_text}

{calculated_ratios_summary}
"""
            # ★修正箇所: ダウンロードボタンの設置
            st.markdown("---")
            st.subheader("提出用ファイルのダウンロード")
            st.markdown("以下のボタンをクリックすると、解答内容が記述されたテキストファイルがダウンロードされます。")
            
            # ファイル名の生成（学生IDがあれば含める）
            student_id_for_filename = student_id_input if student_id_input else "unknown"
            download_filename = f"Kadai_{student_id_for_filename}_{timestamp_str_for_filename}.txt"

            st.download_button(
                label="提出用ファイルをダウンロード",
                data=submission_file_content.encode('utf-8'), # UTF-8でエンコード
                file_name=download_filename,
                mime='text/plain' # MIMEタイプをプレーンテキストに指定
            )
            st.info(f"ダウンロードされたファイル（{download_filename}）をdotCampusの指定された場所に提出してください。")


            st.markdown("---")
            # 自己評価のための考察ポイントは引き続き表示
            with st.expander("解答例と解説はこちら（クリックして展開）", expanded=False):
                st.markdown(f"""
                あなたが着目した指標は **{selected_ratio}** ですね。
                その理由について、以下の視点でさらに考察を深めてみましょう。

                この問題では、直近の経営状況で悪化したと考えられる収益性の財務指標とその主な理由を記述します。
                「麺屋 匠」の状況や計算した財務指標から、**複数の収益性指標の悪化**が考えられます。
                大切なのは、**どの指標に着目し、その悪化の根拠を企業の状況と関連付けて説明できるか**です。

                **考えられる指標と判断根拠の例：**

                * **売上高総利益率**（または **売上高原価率**）
                    * **着眼点:** 企業の状況説明文にある「こだわりの国産原材料の仕入れ価格が高騰しており、特にスープの主原料である豚骨や鶏ガラ、小麦粉の価格上昇が経営を圧迫している」という記述。
                    * **考え方:** これは売上原価の上昇を示唆します。「安易な食材の変更や値上げには慎重な姿勢」であるため売上高の大きな増加は見込みにくい中、売上原価が上昇すると、売上総利益（率）は低下し、売上高原価率は上昇（悪化）すると考えられます。
                    * **解答の方向性（例1）：** こだわりの国産原材料の仕入れ価格が高騰したが、食材の変更や値上げには慎重な姿勢を経営者が示しているため、売上原価の増加により売上総利益が圧迫されたため。
                    * **解答の方向性（例2）：** こだわりの国産原材料の仕入れ価格が高騰したが、食材の変更や値上げには慎重な姿勢を経営者が示しているため、売上原価が上昇したため。

                * **売上高営業利益率**（または **売上高販管費率**）
                    * **着眼点:** 上記の売上総利益の減少（または伸び悩み）に加え、「人件費や固定費の削減は考えておらず、むしろ従業員のモチベーション維持のため、待遇改善も視野に」という記述、そして「競争が激化」による客足の鈍化。
                    * **考え方:** 売上減少や売上総利益の伸び悩みがある中で、販売費及び一般管理費が削減されない（むしろ増加の可能性も）となると、営業利益はさらに圧迫されます。これにより売上高営業利益率が低下、または売上高販管費率が上昇（悪化）すると考えられます。
                    * **解答の方向性（例3）：** 国産原材料の仕入れ価格が高騰したが、経営者が食材の変更や値上げには慎重な姿勢を示すとともに人件費や固定費の削減を実施しないことで、本業の利益が減少したため。
                    * **解答の方向性（例4）：** 国産原材料の仕入れ価格が高騰したが、経営者が食材の変更や値上げには慎重な姿勢を示すとともに人件費や固定費の削減を実施しないことで、販管費の負担が増加したため。

                **＜あなたの解答と照らし合わせて＞**
                1.  **指標の選択の妥当性:** あなたが選んだ **{selected_ratio}** は、計算結果や企業の状況説明と照らし合わせて、悪化の根拠を具体的に説明できる指標でしたか？
                2.  **理由の具体性と網羅性:** 記述した理由は、**{selected_ratio}** が悪化した要因を的確に捉えられていますか？「麺屋 匠の状況」から読み取れる複数の要因（例：売上原価の変動、販売費及び一般管理費の変動など）を考慮し、最も主要なものを挙げられていますか？
                3.  **80字以内での表現力:** 情報を整理し、指定された文字数で簡潔かつ論理的にまとめることができましたか？

                **＜学習を深めるために＞** 
                * 「麺屋 匠」の店主は、この状況に対してどのような対策を検討しているでしょうか？その対策は、あなたが指摘した経営課題の解決に繋がりそうか、SWOT分析の結果も踏まえて考えてみましょう。
                """)