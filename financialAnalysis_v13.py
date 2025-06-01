import streamlit as st
import pandas as pd
import datetime # タイムスタンプ用

# カフェ・なごみの状況に関するテキスト
nagomi_cafe_text = """
「カフェ・なごみ」は、閑静な住宅街の一角で15年間営業を続ける、地域密着型の個人経営カフェです。店主の山田さんが一人で切り盛りしており、木の温もりを感じられる落ち着いた店内にはカウンター席とテーブル席が合わせて18席あります。主な顧客層は近隣に住む主婦や高齢者で、リピーターが多く、顧客との会話を大切にする山田さんの人柄もあって、常連客にとっては憩いの場となっています。

看板メニューは、山田さんが厳選した豆を使い一杯ずつ丁寧に淹れるハンドドリップコーヒーと、手作りのケーキやスコーンです。特に、季節の果物を使った自家製ジャムを添えたスコーンセットは人気で、これを目当てに訪れる顧客も少なくありません。顧客の平均滞在時間は比較的長く、ゆったりとした時間を過ごしてもらうことを重視しているため、座席回転率は低いのが特徴です。客単価は平均1,000円程度です。

しかし、ここ数年、経営環境は厳しさを増しています。2年前に近隣の駅前に大手コーヒーチェーン店が出店したことに加え、最近ではデリバリーサービスに対応した新しいスタイルのカフェも周辺にオープンし、競争が激化しています。その影響で、特に週末の新規顧客の獲得が難しくなり、全体の売上は前年比で約10%減少しています。

さらに、コーヒー豆の国際価格の高騰や、包装資材、水道光熱費といった諸経費の上昇が続いており、利益を圧迫しています。山田さんは、長年の常連客への配慮から、これまでメニュー価格を据え置いてきました。数年前に、将来の顧客層拡大を見込んで、最新式の高価な業務用エスプレッソマシンと専用グラインダーを導入しましたが、期待したほど若年層の来店やエスプレッソベースの高単価メニューの注文が増えず、売上への貢献は限定的です。結果として、これらの新しい設備は十分に活用されないまま、店舗スペースのかなりの部分を占めています。また、売上の減少を見越せず、一部の賞味期限の短い焼き菓子用の材料や、季節限定メニュー用に仕入れた特殊な食材が、予測よりも売れ残ることが増え、廃棄ロスも散見されるようになりました。現在の店舗は築30年の建物を賃借しており、老朽化に伴う修繕費が突発的に発生することも懸念されています。

山田さんは、現状を打破するために、SNSでの情報発信を強化したり、テイクアウトメニューの種類を増やしたりといった施策を始めていますが、一人での運営のため、大きな変革には踏み出せていません。常連客を大切にしながらも、新たな収益源を確保し、コスト上昇分を吸収していくための方策が急務となっています。
"""

# カフェ・なごみ 貸借対照表データ (令和3年度末、令和4年度末、単位：千円)
# 固定資産回転率悪化を強調した版の数値を使用
data_bs_nagomi_r3 = {
    '資産の部': ['流動資産', ' 現金及び預金', ' 売掛金', ' 棚卸資産', '固定資産', ' 有形固定資産', '資産合計'],
    '金額': [1500, 1150, 50, 300, 3000, 3000, 4500]
}
df_bs_nagomi_r3_assets = pd.DataFrame(data_bs_nagomi_r3)

data_bs_nagomi_r3_liab_net = {
    '負債・純資産の部': ['流動負債', ' 買掛金', ' 短期借入金', ' 未払金等', '固定負債', ' 長期借入金', ' リース債務', '負債合計', '純資産の部', ' 資本金', ' 利益剰余金', '純資産合計', '負債純資産合計'],
    '金額': [310, 180, 0, 130, 1540, 1500, 40, 1850, '', 1000, 1650, 2650, 4500]
}
df_bs_nagomi_r3_liab_net = pd.DataFrame(data_bs_nagomi_r3_liab_net)

data_bs_nagomi_r4 = {
    '資産の部': ['流動資産', ' 現金及び預金', ' 売掛金', ' 棚卸資産', '固定資産', ' 有形固定資産', '資産合計'],
    '金額': [1997, 1637, 50, 310, 3100, 3100, 5097]
}
df_bs_nagomi_r4_assets = pd.DataFrame(data_bs_nagomi_r4)

data_bs_nagomi_r4_liab_net = {
    '負債・純資産の部': ['流動負債', ' 買掛金', ' 短期借入金', ' 未払金等', '固定負債', ' 長期借入金', ' リース債務', '負債合計', '純資産の部', ' 資本金', ' 利益剰余金', '純資産合計', '負債純資産合計'],
    '金額': [284, 160, 0, 124, 1610, 1570, 40, 1894, '', 1000, 2203, 3203, 5097]
}
df_bs_nagomi_r4_liab_net = pd.DataFrame(data_bs_nagomi_r4_liab_net)


# カフェ・なごみ 損益計算書データ (令和3年度、令和4年度、単位：千円)
data_pl_nagomi = {
    '項目': ['売上高', '売上原価', '売上総利益', '販売費及び一般管理費', '営業利益', '営業外収益', '営業外費用', '経常利益', '税引前当期純利益', '法人税等', '当期純利益'],
    '令和3年度': [6000, 1800, 4200, 2800, 1400, 15, 65, 1350, 1350, 270, 1080],
    '令和4年度': [5400, 1782, 3618, 2850, 768, 8, 60, 716, 716, 163, 553] # 利益剰余金整合のため調整
}
df_pl_nagomi = pd.DataFrame(data_pl_nagomi)

# Streamlit アプリケーション
st.set_page_config(layout="wide")

st.title('経営分析学習ツール')

# サイドバーのコンテンツ
st.sidebar.title("学習支援情報")
with st.sidebar.expander("⚙️ 効率性分析の基礎知識", expanded=False):
    st.markdown("""**効率性分析とは？**\n企業が保有する資産をどれだけ効率的に活用して売上を上げているかを評価する分析です。\n\n**代表的な効率性指標**\n* **固定資産回転率:** `売上高 ÷ 固定資産`\n 固定資産が売上獲得にどれだけ効率的に利用されたかを示します。高いほど効率が良い。\n* **棚卸資産回転率:** `売上原価 ÷ 棚卸資産`\n 棚卸資産（在庫）がどれだけ効率的に販売されたかを示します。高いほど在庫管理が効率的。\n* **総資本回転率:** `売上高 ÷ 総資本（総資産）`\n 投下された総資本がどれだけ効率的に売上を生み出したかを示します。高いほど効率が良い。""")
with st.sidebar.expander("📝 記述問題のポイント解説", expanded=False):
    st.markdown("""
    課題の記述問題に取り組む上での考え方のヒントです。

    1.  **着眼点を見つける**
        * カフェ・なごみのどの効率性指標が、過去（令和3年度と比較して令和4年度に）特に悪化したか？
        * 「カフェ・なごみの状況」の文章の中に、その悪化の原因や背景を示唆する記述はどこにあるか？
        * （例：高額なエスプレッソマシンの未活用、食材の廃棄ロス、売上の低迷など）
        * なぜそれが経営課題と言えるのか？ 将来にどのような影響があるか？

    2.  **論理的に説明する**
        * 「カフェ・なごみの【指標名】は令和3年度の【数値A】から令和4年度には【数値B】へと【良化/悪化】した。これは【企業の状況D】が影響し、【指標の構成要素E】が【変動した状態】であるため、【Fのような経営状態】を示している。その結果、将来の【Gという計画】の実行が困難になる、あるいは【Hという問題】が悪化する」
        * というように、具体的な数値、企業の状況、指標の意味、将来への影響を結びつけて説明しましょう。

    3.  **指定された形式・文字数でまとめる**
        * 指標を選択し、60字～90字程度で記述します。（設問の指示に従いましょう）
        * 指標について、最も重要な要因に絞り込み、簡潔に表現しましょう。
    """)

st.header('問題')
st.markdown("カフェ・なごみの状況と財務諸表（令和3年度・令和4年度）を踏まえ、カフェ・なごみの経営課題を最も適切に捉えている効率性に関する財務指標を１つ選択し、その理由について60字～90字程度で述べよ。")
st.markdown("---")

# session_stateの初期化
if 'calculated_efficiency_ratios_nagomi_ts' not in st.session_state: # キー名を変更して衝突を避ける
    st.session_state.calculated_efficiency_ratios_nagomi_ts = {}
if 'start_time_nagomi_ts' not in st.session_state: # キー名を変更
    st.session_state.start_time_nagomi_ts = datetime.datetime.now()


tab1, tab2, tab3 = st.tabs(["企業の状況と財務諸表", "財務指標の計算", "課題への取り組み"])

with tab1:
    st.header('カフェ・なごみの状況')
    st.markdown(nagomi_cafe_text)
    st.markdown("---")
    st.header('財務諸表（単位：千円）')

    st.subheader('カフェ・なごみ')
    col_nagomi_bs, col_nagomi_pl = st.columns(2)
    with col_nagomi_bs:
        st.markdown("##### 貸借対照表（令和3年度末・令和4年度末）")
        col_nagomi_bs_r3, col_nagomi_bs_r4 = st.columns(2)
        with col_nagomi_bs_r3:
            st.markdown("###### 令和3年度末")
            st.dataframe(df_bs_nagomi_r3_assets.set_index('資産の部'), height=285)
            st.dataframe(df_bs_nagomi_r3_liab_net.set_index('負債・純資産の部'), height=425)
        with col_nagomi_bs_r4:
            st.markdown("###### 令和4年度末")
            st.dataframe(df_bs_nagomi_r4_assets.set_index('資産の部'), height=285)
            st.dataframe(df_bs_nagomi_r4_liab_net.set_index('負債・純資産の部'), height=425)
            
    with col_nagomi_pl:
        st.markdown("##### 損益計算書（令和3年度・令和4年度）")
        st.dataframe(df_pl_nagomi.set_index('項目'))

    st.info("上記のテキストと財務諸表をよく読んで、カフェ・なごみの経営状況（特に効率性）を把握しましょう。過去の状況との比較が重要です。")

with tab2:
    st.header('効率性分析 - 各種指標の計算')
    st.markdown("以下の各効率性指標について、カフェ・なごみ（令和3年度・令和4年度）の財務諸表から適切な数値を入力してください。数値（千円単位）を入力すると、自動的に比率（回転数）が計算されます。")

    def get_value(df_assets, df_liab_net, df_pl, item_name, part='資産', period_pl=None):
        try:
            item_name_stripped = item_name.strip()
            if part == '資産':
                return int(df_assets[df_assets['資産の部'].str.strip() == item_name_stripped]['金額'].iloc[0])
            elif part == '負債純資産':
                return int(df_liab_net[df_liab_net['負債・純資産の部'].str.strip() == item_name_stripped]['金額'].iloc[0])
            elif part == '純資産合計':
                 return int(df_liab_net[df_liab_net['負債・純資産の部'].str.strip() == '純資産合計']['金額'].iloc[0])
            elif part == '資産合計':
                 return int(df_assets[df_assets['資産の部'].str.strip() == '資産合計']['金額'].iloc[0])
            elif part == '損益計算書項目':
                if df_pl is None or period_pl is None: return None
                if period_pl in df_pl.columns: # 時系列データの場合
                    return int(df_pl[df_pl['項目'].str.strip() == item_name_stripped][period_pl].iloc[0])
                else: # 単年度データの場合（今回は使用しないが念のため）
                     return int(df_pl[df_pl['項目'].str.strip() == item_name_stripped]['金額'].iloc[0])
            return None
        except (IndexError, ValueError, TypeError, KeyError):
            return None
            
    def show_efficiency_ratio_calculation(ratio_name_jp, ratio_key_en, formula_text,
                                          items_needed, 
                                          calculation_func,
                                          unit="回"):
        st.subheader(ratio_name_jp)
        st.markdown(f"**計算式:** `{formula_text}`")
        
        results = {}
        
        company_data_map = {
            'nagomi_r3': ('カフェ・なごみ (令和3年度)', df_bs_nagomi_r3_assets, df_bs_nagomi_r3_liab_net, df_pl_nagomi, '令和3年度'),
            'nagomi_r4': ('カフェ・なごみ (令和4年度)', df_bs_nagomi_r4_assets, df_bs_nagomi_r4_liab_net, df_pl_nagomi, '令和4年度')
        }

        for company_key, (company_name_display, df_assets, df_liab_net, df_pl, period_pl) in company_data_map.items():
            st.markdown(f"##### {company_name_display}")
            item_values_for_calc = {}
            valid_inputs = True
            cols = st.columns(len(items_needed))
            for i, (item_key, (display_name, part, actual_item_name)) in enumerate(items_needed.items()):
                actual_val = get_value(df_assets, df_liab_net, df_pl, actual_item_name, part, period_pl)
                user_input = cols[i].number_input(f"{display_name}", 
                                              key=f"{ratio_key_en}_{company_key}_{item_key}", 
                                              value=None, 
                                              placeholder=f"例: {actual_val if actual_val is not None else '数値'}", 
                                              format="%d", step=1,
                                              help=f"{company_name_display}の財務諸表から「{actual_item_name}」を入力")
                if user_input is None:
                    valid_inputs = False
                item_values_for_calc[item_key] = user_input
            
            if valid_inputs:
                try:
                    result_val = calculation_func(item_values_for_calc)
                    if result_val is not None:
                        st.metric(label=f"{ratio_name_jp} ({company_name_display})", value=f"{result_val:.2f} {unit}")
                        results[company_key] = result_val
                        st.session_state.calculated_efficiency_ratios_nagomi_ts[f"{ratio_key_en}_{company_key}_res"] = result_val
                        st.session_state.calculated_efficiency_ratios_nagomi_ts[f"{ratio_key_en}_ratio_name_jp"] = ratio_name_jp
                    else:
                        st.warning("計算不能 (入力値を確認してください)")
                except ZeroDivisionError:
                    st.warning("計算不能 (分母が0です)")
                except Exception as e:
                    st.error(f"計算エラー: {e}")
            else:
                st.info("必要な数値をすべて入力してください。")
            st.markdown("---")
        
        if 'nagomi_r3' in results and 'nagomi_r4' in results:
            nagomi_r3_res = results['nagomi_r3']
            nagomi_r4_res = results['nagomi_r4']
            comparison_text_nagomi = f"カフェ・なごみ: 令和3年度 {nagomi_r3_res:.2f}{unit} → 令和4年度 {nagomi_r4_res:.2f}{unit}"
            st.markdown(f"**なごみ 時系列比較:** {comparison_text_nagomi}")

    # 固定資産回転率
    show_efficiency_ratio_calculation(
        "固定資産回転率", "fixed_asset_turnover", "売上高 ÷ 有形固定資産",
        {'uriage': ('売上高', '損益計算書項目', '売上高'), 'kotei_shisan': ('有形固定資産', '資産', '有形固定資産')},
        lambda v: v['uriage'] / v['kotei_shisan'] if v['uriage'] is not None and v['kotei_shisan'] is not None and v['kotei_shisan'] != 0 else None
    )
    # 棚卸資産回転率
    show_efficiency_ratio_calculation(
        "棚卸資産回転率", "inventory_turnover", "売上原価 ÷ 棚卸資産",
        {'uriage_genka': ('売上原価', '損益計算書項目', '売上原価'), 'tanaoroshi': ('棚卸資産', '資産', '棚卸資産')},
        lambda v: v['uriage_genka'] / v['tanaoroshi'] if v['uriage_genka'] is not None and v['tanaoroshi'] is not None and v['tanaoroshi'] != 0 else None
    )
    # 総資本回転率
    show_efficiency_ratio_calculation(
        "総資本回転率", "total_asset_turnover", "売上高 ÷ 総資本（資産合計）",
        {'uriage': ('売上高', '損益計算書項目', '売上高'), 'soushisan': ('総資本(資産合計)', '資産合計', '資産合計')},
        lambda v: v['uriage'] / v['soushisan'] if v['uriage'] is not None and v['soushisan'] is not None and v['soushisan'] != 0 else None
    )
    
    st.info("**考察のポイント：**\n* カフェ・なごみの各効率性指標は、令和3年度から令和4年度にかけてどのように変化しましたか？\n* テキストで述べられているカフェ・なごみの状況や経営者の懸念は、どの指標に表れていますか？")

with tab3:
    st.header('記述問題への取り組み')
    st.subheader("解答入力欄")
    
    efficiency_ratios_options = ["固定資産回転率", "棚卸資産回転率", "総資本回転率", "その他"] 
    
    st.markdown("##### 注目する指標")
    selected_ratio = st.selectbox("注目すべき効率性指標を1つ選択してください:", options=efficiency_ratios_options, index=None, placeholder="指標を選択...", key="tab3_selected_ratio_nagomi_ts")
    reason_text = st.text_area("その指標が課題である理由 (60字～90字程度):", height=100, max_chars=90, key="tab3_reason_input_nagomi_ts")

    student_id_input_tab3 = st.text_input("学生ID（または識別番号）を入力してください（任意）:", key="student_id_input_tab3_nagomi_ts")

    if st.button("提出用テキストファイルを自動生成", key="generate_submission_file_button_nagomi_ts"):
        if not selected_ratio:
            st.warning("注目する財務指標を1つ選択してください。")
        elif not reason_text:
            st.warning("指標の理由を記述してください。")
        else:
            submission_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            timestamp_str_for_text = submission_time.strftime("%Y-%m-%d %H:%M:%S JST")
            timestamp_str_for_filename = submission_time.strftime("%Y%m%d_%H%M%S")

            elapsed_time_delta = submission_time.replace(tzinfo=None) - st.session_state.start_time_nagomi_ts # 正しいキー名を使用
            total_seconds = int(elapsed_time_delta.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_time_str = ""
            if hours > 0: elapsed_time_str += f"{hours}時間"
            if minutes > 0 or hours > 0: elapsed_time_str += f"{minutes}分"
            elapsed_time_str += f"{seconds}秒"
            if not elapsed_time_str: elapsed_time_str = "0秒"
            
            calculated_ratios_summary = "【計算した財務指標（「財務指標の計算」タブより）】\n"
            any_ratio_calculated = False
            ratio_keys_en = ["fixed_asset_turnover", "inventory_turnover", "total_asset_turnover"] 
            
            for r_key in ratio_keys_en:
                ratio_name_jp = st.session_state.calculated_efficiency_ratios_nagomi_ts.get(f"{r_key}_ratio_name_jp", "不明な指標")
                nagomi_r3_val = st.session_state.calculated_efficiency_ratios_nagomi_ts.get(f"{r_key}_nagomi_r3_res")
                nagomi_r4_val = st.session_state.calculated_efficiency_ratios_nagomi_ts.get(f"{r_key}_nagomi_r4_res")

                if nagomi_r3_val is not None or nagomi_r4_val is not None:
                    calculated_ratios_summary += f"- {ratio_name_jp}:\n"
                    if nagomi_r3_val is not None:
                        calculated_ratios_summary += f"  カフェ・なごみ (R3): {nagomi_r3_val:.2f}回\n"
                    if nagomi_r4_val is not None:
                        calculated_ratios_summary += f"  カフェ・なごみ (R4): {nagomi_r4_val:.2f}回\n"
                    any_ratio_calculated = True
            if not any_ratio_calculated:
                calculated_ratios_summary += "計算された財務指標はありませんでした。\n"
            
            submission_file_content = f"""## カフェ・なごみ 経営分析 課題取り組み内容

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
"""
            st.markdown("---")
            st.subheader("提出用ファイルのダウンロード")
            st.markdown("以下のボタンをクリックすると、解答内容が記述されたテキストファイルがダウンロードされます。")
            
            student_id_for_filename = student_id_input_tab3 if student_id_input_tab3 else "unknown"
            download_filename = f"CafeNagomi_Kadai_TimeSeries_{student_id_for_filename}_{timestamp_str_for_filename}.txt"

            st.download_button(
                label="提出用ファイルをダウンロード",
                data=submission_file_content.encode('utf-8'),
                file_name=download_filename,
                mime='text/plain'
            )
            st.info(f"ダウンロードされたファイル（{download_filename}）を指示された方法で提出してください。")

