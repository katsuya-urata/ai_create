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

import streamlit as st

# ログイン画面のタイトル
st.title('ログイン')

# ユーザ名とパスワードの入力フィールド
username = st.text_input('ユーザ名')
password = st.text_input('パスワード', type='password')

# ログインボタン
login_button = st.button('ログイン')

# ログインボタンがクリックされた場合の処理
if login_button:
    # ここでユーザ名とパスワードの認証を行う
    # 仮の認証処理: ユーザ名が"admin"で、パスワードが"password"の場合にのみログイン成功とする
    if username == 'admin' and password == 'password':
        st.success('ログインに成功しました！')
    else:
        st.error('ユーザ名またはパスワードが正しくありません。')



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
