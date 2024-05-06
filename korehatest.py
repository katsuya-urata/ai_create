import streamlit as st

# タイトルを設定
st.title('Streamlit アプリ')

# テキストを表示
st.write('これはStreamlitアプリのテストです。')

# データ入力と処理
# 例: ユーザから数値を入力し、2倍した値を表示する
user_input = st.number_input('数値を入力してください', value=0)
result = user_input * 2
st.write('入力された数値の2倍は:', result)

import matplotlib.pyplot as plt

# データフレームの表示
import pandas as pd

df = pd.DataFrame({
    '名前': ['Alice', 'Bob', 'Charlie'],
    '年齢': [25, 30, 35]
})

st.write('データフレームの表示:')
st.write(df)

# チェックボックスと条件付き表示
if st.checkbox('詳細を表示する'):
    st.write('ここに詳細な情報が表示されます。')

# サイドバーへのウィジェットの追加
st.sidebar.header('サイドバーウィジェット')
st.sidebar.write('ここにサイドバーのウィジェットを追加します。')

# おしまい
st.write('これでStreamlitアプリの構文の基本を理解できました。')
