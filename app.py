import streamlit as st

# st.title("いろはにほへと")
# st.write("今日は晴れです")
# name = st.text_input("お名前は")
# greeting = name + "さん、こんにちは"

# if name:
#     st.write(greeting)


#課題３
# st.title("BMI計算するよ")
# height = st.text_input("身長(m)を入力")
# weight = st.text_input("体重(kg)を入力")

# if height and weight:
#     height = float(height)
#     weight = float(weight)
#     bmi = weight / height ** 2
#     st.write("あなたのBMIは" + str(bmi) + "です。")


#課題２
# st.header("課題２：挨拶メッセージ")

# name = st.text_input("お名前を入力してください")
# age_str = st.text_input("年齢を入力してください")

# if name and age_str:
#     age = int(age_str)
#     st.write("こんにちは、" + name + "さん！あなたは" + str(age) + "歳ですよ？")


#課題１
# st.title("かんたん計算機")
# n1 = st.text_input("数字１を入力してください")
# n2 = st.text_input("数字２を入力してください")

# if n1 and n2:
#     n1 = float(n1)
#     n2 = float(n2)
#     wa = n1 + n2
#     sa = n1 - n2
#     seki = n1 * n2
#     shou = n1 / n2
#     st.write("和は" + str(wa) + "です。")
#     st.write("差は" + str(sa) + "です。")
#     st.write("積は" + str(seki) + "です。")
#     st.write("商は" + str(shou) + "です。")


#第4回
#課題１　持ち物チェックリスト
# items = ["PC", "充電器", "ノート", "教科書"]

# for item in items:
#     st.checkbox(item)

#課題２
# weather = st.selectbox(options=["晴れ", "雨", "雪"], label="今日の天気は？")
# temperature = st.slider(min_value=0, max_value=40, label="今日の気温は？")

# if st.button("コーデを提案する"):
#     st.subheader("おすすめコーデは")
#     if weather == "晴れ":
#         if temperature < 15:
#             st.write("上着が必要です")
#         else:
#             st.write("上着は必要ありません")
#     elif weather == "雨":
#         st.write("傘が必要です")
#     else:
#         st.write("雪なので外に出ないほうがいいでしょう")





# items = ["PC", "ノート"]

# new_item = st.text_input("新しいアイテムを入力してください")

# #リストに要素を追加
# if new_item:
#     items.append(new_item)

# st.subheader("必須アイテム：")

# for item in items:
#     st.checkbox(item)



#演習１：動的持ち物リスト

# if "items" not in st.session_state:
#     st.session_state["items"] = ["PC", "ノート"]

# new_item = st.text_input("新しいアイテムを入力")

# if st.button("追加"):
#     if new_item:
#         st.session_state["items"].append(new_item)

# st.subheader("持ち物リスト")
# for item in st.session_state["items"]:
#     st.checkbox(item)


# st.header("1.復習")
# st.write("こんにちは")

# st.header("2.今日の内容")
# st.write("今日の学習は様々な入力ウィジェットです")

# st.button("クリックしてね")
# st.checkbox("チェック事項１")

# fav_color = st.selectbox(
#     label = "好きな色は",
#     options = ["赤","青","緑"],
#     help = "以下から選んでください"
# )

# if fav_color == "赤":
#     st.write("あなたは情熱的な人ですね")
# elif fav_color == "青":
#     st.write("海は好きですか？")
# else:
#     st.write("自然は好きですか？")
#st.write("あなたの好きな色は" + fav_color)


# countries = st.multiselect(
#     label = "旅行で行きたい国は",
#     options = ["スイス","ドイツ","イタリア"],
#     help = "国を複数選んでね"
# )

# for country in countries:
#     st.write(country + "に行けるといいですね")

# st.slider(
#     label = "年齢を入力してください",
#     min_value = 20,
#     max_value = 70,
#     value = (20,40),        #最初に入力されている値
#     step = 10
# )

# from datetime import datetime, time

# st.date_input(
#     label = "あなたの誕生日は",
#     value = datetime(2026, 1, 1)
# )

# st.time_input(
#     label = "１限目の開始時間は",
#     value = time(9,0),
#     step = 60*30
# )


# st.write("メイン画像")

# st.header("自己紹介")
# st.write("名前：イマイ")

# with st.expander("詳細"):
#     st.write("生年月日：2005年7月5日")

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.header("Cat")
#         st.image("https://static.streamlit.io/examples/cat.jpg")
#     with col2:
#         st.header("Dog")
#         st.image("https://static.streamlit.io/examples/dog.jpg")
#     with col3:
#         st.header("Owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg")


# st.sidebar.write("サイドバー")
# houhou = st.sidebar.selectbox("連絡方法を選択してください",("メール","電話","LINE"))
# st.sidebar.write("連絡方法は" + houhou + "です")


# #演習
# import streamlit as st

# st.title("第7回 Streamlit レイアウト演習 - テンプレート")
# st.caption("st.sidebar, st.columns, st.expander を使ってみましょう。")

# st.markdown("---")
# st.subheader("演習1: サイドバー (st.sidebar)")
# st.write("**課題**: サイドバーに自分の名前と学籍番号を表示するテキスト入力を配置。")

# # ここに演習1のコードを記述してください
# # ヒント: st.sidebar.text_input() を使います

# name = st.sidebar.text_input("名前")
# id = st.sidebar.text_input("学籍番号")

# if name and id:
#     st.sidebar.write("名前は" + name + "です")
#     st.sidebar.write("学籍番号は" + id +"です")

# st.markdown("---")
# st.subheader("演習2: カラムレイアウト (st.columns)")
# st.write("**課題**: メインエリアを2列に分け、左列に好きなものの画像、右列にその説明文を表示。")

# # ここに演習2のコードを記述してください
# # ヒント: st.columns(2), st.image() を使います

# col1, col2 = st.columns(2)

# with col1:
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.write("猫派")
#     with st.expander("詳細"):
#         st.write("ミヌエットが世界で一番かわいい異論は認めない")

# st.markdown("---")
# st.subheader("演習3: エキスパンダー (st.expander)")
# st.write("**課題**: 説明文の下にエキスパンダーを設け、さらに詳細な情報を隠して表示できるようにする。")

# # ここに演習3のコードを記述してください
# # ヒント: with st.expander("タイトル"): を使います




# st.markdown("---")
# st.info("💡 コメントアウトされたコードを参考に、各演習課題を完成させてください。") 




# if "count" not in st.session_state:
#     st.session_state["count"]= 1

# if st.button("カウンター"):
#     st.session_state["count"] = st.session_state["count"] + 1

# st.write(st.session_state["count"] )


if "kibun_history" not in st.session_state:
    st.session_state["kibun_history"] = []

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("😊 嬉しい"):
        st.session_state["kibun_history"].append("😊 嬉しい")

with col2:
    if st.button("😢 悲しい"):
        st.session_state["kibun_history"].append("😢 悲しい")

with col3:
    if st.button("😴 眠い"):
        st.session_state["kibun_history"].append("😴 眠い")

with col4:
    if st.button("🍕 お腹すいた"):
        st.session_state["kibun_history"].append("🍕 お腹すいた")

for kibun in st.session_state["kibun_history"]:
    st.write(kibun)