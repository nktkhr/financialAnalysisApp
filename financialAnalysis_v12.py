import streamlit as st
import pandas as pd
import datetime # タイムスタンプ用

# 鶴亀温泉の状況に関するテキスト
tsurukame_onsen_text = """
鶴亀温泉は、古くから地元で親しまれてきた温泉街に位置する、創業80年を超える老舗銭湯である。泉質の良さには定評があるが、建物や設備の老朽化が深刻で、特に耐震性や基本的なバリアフリー対応の遅れが喫緊の課題となっていた。周辺には新しいコンセプトの温浴施設やリニューアルされた宿泊施設が増え、鶴亀温泉も時代の変化に対応する必要に迫られていた。

そこで鶴亀温泉の経営陣は、事業の持続可能性を高めるため、X1年度に大規模リニューアル計画を実行した（X2年4月リニューアルオープン）。総事業費は1億円にのぼり、主に本館の耐震補強、基本的なバリアフリー化対応、そして老朽化したボイラーシステムの更新といった、施設の維持と安全性向上を中心とした投資を行った。しかしながら、若年層を積極的に呼び込むためのデザイン性の高いモダンな休憩スペースやサウナ施設、体験型コンテンツといった魅力向上策については、資金的な制約から今回のリニューアルでは見送らざるを得なかった。これらは今後の重要な追加投資案件として計画されている。

リニューアルの資金調達にあたっては、自己資金30百万円を充当しましたが、残りの70百万円は外部からの調達が必要であった。メインバンクである地方銀行と粘り強く交渉し、長期の設備資金融資として60百万円を確保。不足する10百万円は、返済期間が比較的短い地域振興目的の公的融資制度で賄うことになった。

経営者は、今回のリニューアルで一定の成果はあったものの、若者層の取り込みという点で課題が残っており、先に計画しているモダンな設備への追加投資（推定50百万円規模）の必要性を強く感じている。しかし、現状の財務状況、特に同業のB社と比較した場合の資本構成を鑑みると、この追加投資の実現には大きな困難が伴うことが考えられる。日々の資金繰りは何とか最低限維持できているものの、この構造的な財務課題の解決なくしては、鶴亀温泉の持続的な成長は難しいと認識し、財務戦略の再構築を急務と考えています。
"""

# 貸借対照表データ (X6年3月期末時点、単位：百万円)
data_bs_tsurukame = {
    '資産の部': ['流動資産', ' 現預金', ' その他流動資産', '固定資産', ' 建物・設備（純額）', ' 土地', '資産合計'],
    '金額': [25, 18, 7, 150, 140, 10, 175]
}
df_bs_tsurukame_assets = pd.DataFrame(data_bs_tsurukame)

data_bs_tsurukame_liab_net = {
    '負債・純資産の部': ['流動負債', ' 買掛金', ' 短期借入金', ' 1年以内返済予定の長期借入金', '固定負債', ' 長期借入金', '負債合計', '純資産の部', ' 資本金', ' 利益剰余金', '純資産合計', '負債純資産合計'],
    '金額': [27, 10, 8, 9, 65, 65, 92, '', 10, 73, 83, 175]
}
df_bs_tsurukame_liab_net = pd.DataFrame(data_bs_tsurukame_liab_net)

data_bs_b_sha = {
    '資産の部': ['流動資産', ' 現預金', ' その他流動資産', '固定資産', ' 建物・設備（純額）', ' 土地', '資産合計'],
    '金額': [35, 20, 15, 145, 135, 10, 180]
}
df_bs_b_sha_assets = pd.DataFrame(data_bs_b_sha)

data_bs_b_sha_liab_net = {
    '負債・純資産の部': ['流動負債', ' 買掛金', ' 短期借入金', ' 1年以内返済予定の長期借入金', '固定負債', ' 長期借入金', '負債合計', '純資産の部', ' 資本金', ' 利益剰余金', '純資産合計', '負債純資産合計'],
    '金額': [24, 10, 7, 7, 66, 66, 90, '', 10, 80, 90, 180]
}
df_bs_b_sha_liab_net = pd.DataFrame(data_bs_b_sha_liab_net)


# Streamlit アプリケーション
st.set_page_config(layout="wide")

st.title('経営分析学習支援ツール: 鶴亀温泉')

# サイドバーのコンテンツ
st.sidebar.title("学習支援情報")
with st.sidebar.expander("🛡️ 安全性分析の基礎知識", expanded=False):
    st.markdown("""**安全性分析とは？**\n企業の支払い能力や財務構造の安定性を評価する分析です。短期的な支払い能力と長期的な財務安定性の両面から見ます。\n\n**代表的な安全性指標**\n* **自己資本比率:** `(自己資本 ÷ 総資産) × 100`\n 総資本に占める自己資本の割合。高いほど財務が安定。\n* **流動比率:** `(流動資産 ÷ 流動負債) × 100`\n 短期的な支払い能力を示します。200%以上が理想、100%以下は注意。\n* **固定長期適合率:** `(固定資産 ÷ (自己資本 + 固定負債)) × 100`\n 固定資産が長期の安定資金でどれだけ賄われているかを示します。100%以下が望ましい。\n* **負債比率:** `((流動負債 + 固定負債) ÷ 自己資本) × 100`\n 自己資本に対する負債の割合。低いほど財務リスクが低い。""") # 固定比率の記述をサイドバーからも削除
with st.sidebar.expander("📝 記述問題のポイント解説", expanded=False):
    st.markdown("""
    課題の記述問題に取り組む上での考え方のヒントです。

    1.  **着眼点を見つける**
        * 鶴亀温泉のどの安全性指標が、B社と比較して特に悪いか？
        * 「鶴亀温泉の状況」の文章の中に、その悪化の原因や背景を示唆する記述はどこにあるか？
        * （例：大規模リニューアル、資金調達の内訳、自己資本の増加の遅れ、将来の追加投資計画など）
        * なぜそれが「長期的な安全性および資本構成」に関する課題と言えるのか？

    2.  **論理的に説明する**
        * 「鶴亀温泉の【指標名】は【数値A】であり、B社の【数値B】と比較して【良い/悪い】。これは【企業の状況C】が影響し、【指標の構成要素D】が【変動した状態】であるため、【Eのような財務状態】を示している。その結果、将来の【Fという計画】の実行が困難になる」
        * というように、具体的な数値、企業の状況、指標の意味、将来への影響を結びつけて説明しましょう。

    3.  **指定された形式・文字数でまとめる**
        * 指標を選択し、それぞれについて60字～90字程度で記述します。（設問の指示に従いましょう）
        * 指標について、最も重要な要因に絞り込み、簡潔に表現しましょう。
    """)

st.header('問題')
st.markdown("鶴亀温泉の状況と貸借対照表を踏まえて、同業他社と比較したときに鶴亀温泉の経営課題として考えられる安全性に関する財務指標を１つ選択し、その理由について60字～90字程度で述べよ。")
st.markdown("---")

# session_stateの初期化
if 'calculated_safety_ratios' not in st.session_state:
    st.session_state.calculated_safety_ratios = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()


tab1, tab2, tab3 = st.tabs(["企業の状況と財務諸表", "財務指標の計算", "課題への取り組み"]) # SWOTタブを削除

with tab1:
    st.header('鶴亀温泉の状況')
    st.markdown(tsurukame_onsen_text)
    st.markdown("---")
    st.header('貸借対照表（X6年3月期末時点、単位：百万円）')

    col_bs_tsurukame, col_bs_b_sha = st.columns(2)
    with col_bs_tsurukame:
        st.subheader('鶴亀温泉')
        col_bs_tsurukame_assets, col_bs_tsurukame_liab_net = st.columns(2)
        with col_bs_tsurukame_assets:
            st.markdown("##### 資産の部")
            st.dataframe(df_bs_tsurukame_assets.set_index('資産の部'))
        with col_bs_tsurukame_liab_net:
            st.markdown("##### 負債・純資産の部")
            st.dataframe(df_bs_tsurukame_liab_net.set_index('負債・純資産の部'))
    
    with col_bs_b_sha:
        st.subheader('同業他社B')
        col_bs_b_sha_assets, col_bs_b_sha_liab_net = st.columns(2)
        with col_bs_b_sha_assets:
            st.markdown("##### 資産の部")
            st.dataframe(df_bs_b_sha_assets.set_index('資産の部'))
        with col_bs_b_sha_liab_net:
            st.markdown("##### 負債・純資産の部")
            st.dataframe(df_bs_b_sha_liab_net.set_index('負債・純資産の部'))

    st.info("上記のテキストと財務諸表をよく読んで、鶴亀温泉の経営状況と同業他社との違いを把握しましょう。")

with tab2:
    st.header('安全性分析 - 各種指標の計算')
    st.markdown("以下の各安全性指標について、鶴亀温泉と同業他社Bの財務諸表から適切な数値を入力してください。数値（百万円単位）を入力すると、自動的に比率が計算されます。")

    def get_bs_value(df_assets, df_liab_net, item_name, part='資産'):
        try:
            if part == '資産':
                value = df_assets[df_assets['資産の部'].str.strip() == item_name.strip()]['金額'].iloc[0]
            elif part == '負債純資産':
                value = df_liab_net[df_liab_net['負債・純資産の部'].str.strip() == item_name.strip()]['金額'].iloc[0]
            elif part == '純資産合計':
                value = df_liab_net[df_liab_net['負債・純資産の部'].str.strip() == '純資産合計']['金額'].iloc[0]
            elif part == '負債合計':
                value = df_liab_net[df_liab_net['負債・純資産の部'].str.strip() == '負債合計']['金額'].iloc[0]
            return int(value)
        except (IndexError, ValueError, TypeError):
            return None
            
    def show_safety_ratio_calculation(ratio_name_jp, ratio_key_en, formula_text,
                                      items_needed, 
                                      calculation_func):
        st.subheader(ratio_name_jp)
        st.markdown(f"**計算式:** `{formula_text}`")
        
        results = {}
        input_values = {'鶴亀温泉': {}, '同業他社B': {}}

        for company_key, company_name, df_assets, df_liab_net in [
            ('tsurukame', '鶴亀温泉', df_bs_tsurukame_assets, df_bs_tsurukame_liab_net),
            ('b_sha', '同業他社B', df_bs_b_sha_assets, df_bs_b_sha_liab_net)
        ]:
            st.markdown(f"##### {company_name}")
            item_values_for_calc = {}
            valid_inputs = True
            cols = st.columns(len(items_needed))
            for i, (item_key, (display_name, part, actual_item_name)) in enumerate(items_needed.items()):
                actual_val = get_bs_value(df_assets, df_liab_net, actual_item_name, part)
                user_input = cols[i].number_input(f"{display_name}", 
                                              key=f"{ratio_key_en}_{company_key}_{item_key}", 
                                              value=None, 
                                              placeholder=f"例: {actual_val if actual_val is not None else '数値'}", 
                                              format="%d", step=1,
                                              help=f"{company_name}の貸借対照表から「{actual_item_name}」を入力")
                if user_input is None:
                    valid_inputs = False
                item_values_for_calc[item_key] = user_input
                # The following line was causing an error and is not strictly necessary for the calculation display logic here.
                # It was trying to assign to input_values[company_name] which might not have been initialized correctly for '同業他社B'
                # if company_name was not '鶴亀温泉'. Safely removed or refactored if this data is needed elsewhere.
                # For current logic, item_values_for_calc is sufficient.
                # input_values[company_name][display_name] = user_input 
            
            if valid_inputs:
                try:
                    result_val = calculation_func(item_values_for_calc)
                    if result_val is not None:
                        st.metric(label=f"{ratio_name_jp} ({company_name})", value=f"{result_val:.2f} %")
                        results[company_name] = result_val
                        st.session_state.calculated_safety_ratios[f"{ratio_key_en}_{company_key}_res"] = result_val
                        st.session_state.calculated_safety_ratios[f"{ratio_key_en}_ratio_name_jp"] = ratio_name_jp
                    else:
                        st.warning("計算不能 (入力値を確認してください)")
                except ZeroDivisionError:
                    st.warning("計算不能 (分母が0です)")
                except Exception as e:
                    st.error(f"計算エラー: {e}")
            else:
                st.info("必要な数値をすべて入力してください。")
            st.markdown("---")
        
        if '鶴亀温泉' in results and '同業他社B' in results:
            tsurukame_res = results['鶴亀温泉']
            b_sha_res = results['同業他社B']
            comparison_text = f"鶴亀温泉: {tsurukame_res:.2f}%, 同業他社B: {b_sha_res:.2f}%"
            st.markdown(f"**両社比較:** {comparison_text}")

    # 自己資本比率
    show_safety_ratio_calculation(
        "自己資本比率", "equity_ratio", "(自己資本 ÷ 総資産) × 100",
        {'jikoshihon': ('自己資本(純資産合計)', '純資産合計', '純資産合計'), 'soushisan': ('総資産(資産合計)', '資産', '資産合計')},
        lambda v: (v['jikoshihon'] / v['soushisan']) * 100 if v['jikoshihon'] is not None and v['soushisan'] is not None and v['soushisan'] != 0 else None
    )
    # 流動比率
    show_safety_ratio_calculation(
        "流動比率", "current_ratio", "(流動資産 ÷ 流動負債) × 100",
        {'ryudo_shisan': ('流動資産', '資産', '流動資産'), 'ryudo_fusai': ('流動負債', '負債純資産', '流動負債')},
        lambda v: (v['ryudo_shisan'] / v['ryudo_fusai']) * 100 if v['ryudo_shisan'] is not None and v['ryudo_fusai'] is not None and v['ryudo_fusai'] != 0 else None
    )
    # 固定長期適合率
    show_safety_ratio_calculation(
        "固定長期適合率", "fixed_long_term_ratio", "(固定資産 ÷ (自己資本 + 固定負債)) × 100",
        {'kotei_shisan': ('固定資産', '資産', '固定資産'), 'jikoshihon': ('自己資本(純資産合計)', '純資産合計', '純資産合計'), 'kotei_fusai': ('固定負債', '負債純資産', '固定負債')},
        lambda v: (v['kotei_shisan'] / (v['jikoshihon'] + v['kotei_fusai'])) * 100 if v['kotei_shisan'] is not None and v['jikoshihon'] is not None and v['kotei_fusai'] is not None and (v['jikoshihon'] + v['kotei_fusai']) != 0 else None
    )
    # 負債比率
    show_safety_ratio_calculation(
        "負債比率", "debt_to_equity_ratio", "((流動負債 + 固定負債) ÷ 自己資本) × 100",
        {'ryudo_fusai': ('流動負債', '負債純資産', '流動負債'), 'kotei_fusai': ('固定負債', '負債純資産', '固定負債'), 'jikoshihon': ('自己資本(純資産合計)', '純資産合計', '純資産合計')},
        lambda v: ((v['ryudo_fusai'] + v['kotei_fusai']) / v['jikoshihon']) * 100 if v['ryudo_fusai'] is not None and v['kotei_fusai'] is not None and v['jikoshihon'] is not None and v['jikoshihon'] != 0 else None
    )
    # 固定比率の計算を削除
    st.info("**考察のポイント：**\n* 鶴亀温泉の各安全性指標は、B社と比較してどのような状況ですか？\n* テキストで述べられている鶴亀温泉の状況や経営者の懸念は、どの指標に表れていますか？")

# tab3が課題への取り組みになる (旧tab4)
with tab3:
    st.header('記述問題への取り組み')
    st.subheader("解答入力欄")
    # 固定比率を削除し、その他も維持
    safety_ratios_options = ["自己資本比率", "流動比率", "固定長期適合率", "負債比率", "その他"] 
    
    st.markdown("##### 注目する指標")
    selected_ratio = st.selectbox("注目すべき指標を1つ選択してください:", options=safety_ratios_options, index=None, placeholder="指標を選択...", key="tab3_selected_ratio")
    reason_text = st.text_area("その指標が課題である理由 (60字～90字程度):", height=100, max_chars=90, key="tab3_reason_input")

    student_id_input_tab3 = st.text_input("学生ID（または識別番号）を入力してください（任意）:", key="student_id_input_tab3")

    if st.button("提出用テキストファイルを自動生成", key="generate_submission_file_button_tsurukame_single"):
        if not selected_ratio:
            st.warning("注目する財務指標を1つ選択してください。")
        elif not reason_text:
            st.warning("指標の理由を記述してください。")
        else:
            submission_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            timestamp_str_for_text = submission_time.strftime("%Y-%m-%d %H:%M:%S JST")
            timestamp_str_for_filename = submission_time.strftime("%Y%m%d_%H%M%S")

            elapsed_time_delta = submission_time.replace(tzinfo=None) - st.session_state.start_time
            total_seconds = int(elapsed_time_delta.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_time_str = ""
            if hours > 0: elapsed_time_str += f"{hours}時間"
            if minutes > 0 or hours > 0: elapsed_time_str += f"{minutes}分"
            elapsed_time_str += f"{seconds}秒"
            if not elapsed_time_str: elapsed_time_str = "0秒"

            # SWOT関連のセッションステート取得を削除
            
            calculated_ratios_summary = "【計算した財務指標（「財務指標の計算」タブより）】\n"
            any_ratio_calculated = False
            # ratio_keys_enから "fixed_assets_to_equity_ratio" を削除
            ratio_keys_en = ["equity_ratio", "current_ratio", "fixed_long_term_ratio", "debt_to_equity_ratio"] 
            
            for r_key in ratio_keys_en:
                ratio_name_jp = st.session_state.calculated_safety_ratios.get(f"{r_key}_ratio_name_jp", "不明な指標")
                tsurukame_val = st.session_state.calculated_safety_ratios.get(f"{r_key}_tsurukame_res")
                b_sha_val = st.session_state.calculated_safety_ratios.get(f"{r_key}_b_sha_res")
                if tsurukame_val is not None or b_sha_val is not None:
                    calculated_ratios_summary += f"- {ratio_name_jp}:\n"
                    if tsurukame_val is not None:
                        calculated_ratios_summary += f"  鶴亀温泉: {tsurukame_val:.2f}%\n"
                    if b_sha_val is not None:
                        calculated_ratios_summary += f"  同業他社B: {b_sha_val:.2f}%\n"
                    any_ratio_calculated = True
            if not any_ratio_calculated:
                calculated_ratios_summary += "計算された財務指標はありませんでした。\n"
            
            submission_file_content = f"""## 鶴亀温泉 経営分析 課題取り組み内容

**提出日時:** {timestamp_str_for_text}
**学生ID:** {student_id_input_tab3 if student_id_input_tab3 else "未入力"}
**アプリ利用時間:** {elapsed_time_str}

---
### 記述問題の解答

**注目した指標:** {selected_ratio}
**その理由 (60字～90字程度):**
{reason_text}

---
**参考情報（学習過程の記録）**

{calculated_ratios_summary}
---
""" # SWOT分析の出力を削除

            st.markdown("---")
            st.subheader("提出用ファイルのダウンロード")
            st.markdown("以下のボタンをクリックすると、解答内容が記述されたテキストファイルがダウンロードされます。")
            
            student_id_for_filename = student_id_input_tab3 if student_id_input_tab3 else "unknown"
            download_filename = f"TsurukameOnsen_Kadai_{student_id_for_filename}_{timestamp_str_for_filename}.txt"

            st.download_button(
                label="提出用ファイルをダウンロード",
                data=submission_file_content.encode('utf-8'),
                file_name=download_filename,
                mime='text/plain'
            )
            st.info(f"ダウンロードされたファイル（{download_filename}）を指示された方法で提出してください。")

            st.markdown("---")
            with st.expander("模範解答例と解説はこちら（クリックして展開）", expanded=False):
                st.markdown(f"""
                **あなたが注目した指標：** **{selected_ratio}**
                その理由について、以下の模範解答例と比較し、考察を深めてみましょう。
                （問題文では2つの指標を挙げるよう指示されていますが、ここではあなたが選択した1つの指標について考えます。）

                ---
                **【模範解答例】**

                **1. 指標名：** 負債比率
                **課題と理由：**
                鶴亀温泉は110.8%とB社(100.0%)より高く、自己資本に対し負債が多い。財務リスクが高く返済負担も重いため、追加投資のための新規借入のハードルが上がり、財務の柔軟性が低下しているため経営課題である。（90字）

                **2. 指標名：** 固定長期適合率
                **課題と理由：**
                鶴亀温泉は101.4%と100%を超えB社(93.0%)より悪い。固定資産が長期安定資金で十分に賄われておらず、資本構成に問題がある。このため将来の設備更新や計画中の追加投資への財務的制約が大きい。（89字）

                ---
                **【解説】**

                本問題は、提示された情報から鶴亀温泉の財務上の課題を読み取り、それが将来の設備投資計画にどのような影響を与えるかを考察させることを目的としています。特に「長期的な安全性および資本構成」という観点から、適切な財務指標を用いて説明する能力を測ります。

                **1. 負債比率について**
                * **指標の意味と鶴亀温泉の状況：**
                    負債比率（総負債 ÷ 自己資本）は、自己資本に対してどれだけ負債を抱えているかを示し、企業の財務リスクの度合いを測る指標です。低いほど財務の安定性が高いとされます。
                    鶴亀温泉の負債比率は110.84%であり、同業他社B（100.00%）と比較して高い水準です。これは、自己資本（83百万円）に対して総負債（92百万円）の割合が高いことを示しています。
                * **テキストとの関連：**
                    テキスト中で経営者が「現状の財務状況、特に同業のB社と比較した場合の資本構成を鑑みると、この追加投資の実現には大きな困難が伴う」と懸念している点や、「構造的な財務課題の解決なくしては、鶴亀温泉の持続的な成長は難しい」と認識している状況は、この高い負債比率に表れています。また、「返済期間が比較的短い」公的融資（10百万円）を含む70百万円の外部資金でリニューアル費用を調達した経緯も、短期的な返済圧力への注意を促します。
                * **将来投資への影響（経営課題としての理由）：**
                    負債比率が高いということは、既に借入への依存度が高い状態であり、財務的な柔軟性が低いことを意味します。金利の変動リスクを受けやすく、また支払利息や元本返済の負担が経営を圧迫します。これにより、金融機関は追加融資に対して慎重になる可能性が高く、計画中のモダン設備への追加投資（推定50百万円規模）に必要な資金調達が困難になる、あるいはできたとしても不利な条件になる可能性があり、経営上の大きな課題となります。

                **2. 固定長期適合率について**
                * **指標の意味と鶴亀温泉の状況：**
                    固定長期適合率（固定資産 ÷ (自己資本 + 固定負債)）は、企業の固定資産が、返済義務のない自己資本と長期の安定した負債（固定負債）でどの程度賄われているかを示す指標です。100%以下が望ましいとされます。
                    鶴亀温泉の固定長期適合率は101.35%と100%を超過しており、同業他社B（92.95%）と比較しても悪い水準です。これは、リニューアルで増加した固定資産（150百万円）を、自己資本（83百万円）と固定負債（65百万円）の合計（148百万円）だけでは賄いきれていないことを意味し、資本構成のアンバランスを示しています。
                * **テキストとの関連：**
                    テキストでは、総事業費1億円の大規模リニューアル（主に施設の維持と安全性向上）が行われた結果、固定資産が増加したことが示唆されます。このリニューアル資金のうち自己資金は30百万円で、残る70百万円は外部調達（うち10百万円は「返済期間が比較的短い」公的融資）に依存しています。経営者が「現状の財務状況、特に同業のB社と比較した場合の資本構成を鑑みると、この追加投資の実現には大きな困難が伴う」と述べている通り、増加した固定資産を安定的に支えるための自己資本や長期負債のバランスに課題があり、この固定長期適合率の悪化がその問題を示唆しています。
                * **将来投資への影響（経営課題としての理由）：**
                    固定長期適合率が高い状態は、既に固定資産への投資が長期安定資金の許容量を超えている可能性を示唆し、財務の安定性が低いことを意味します。そのため、さらなる大規模な設備投資（若者向けモダン設備、推定50百万円規模）を行うための長期資金（特に借入）の追加調達が難しくなるか、できたとしても非常に厳しい条件になる可能性が高いです。これは、将来の成長戦略の実現にとって大きな制約となります。

                **他の指標について（流動比率など）：**
                鶴亀温泉の流動比率（92.59%）は100%を下回り、B社（145.83%）と比較しても低い水準です。これは短期的な支払い能力に懸念があることを示しています。しかし、テキストには「日々の資金繰りは何とか最低限維持できているものの、この構造的な財務課題の解決なくしては、鶴亀温泉の持続的な成長は難しい」とあり、直ちに経営破綻に繋がる危機的状況とまでは描写されていません。
                問題文が「長期的な安全性および資本構成を示す財務指標」に焦点を当てていること、またテキストで経営者が「資本構成」や「構造的な財務課題」について懸念を示し、「財務戦略の再構築を急務」と考えていることから、本解説ではより構造的で中長期的な影響が大きい負債比率と固定長期適合率を主要な課題として取り上げました。流動性の問題も重要な経営課題の一つですが、問題の意図を汲み取り、より適切な指標を選択することが求められます。

                """)