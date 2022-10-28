import streamlit as st
import time

# 文字を表示させる
st.title('Streamlit 超入門')
st.write('DataFrame')

# プログレスバーの表示
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i + 1}')
    bar.progress(i+1)
    time.sleep(0.1)


# セレクトBOXで動的な処理
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
    )
'あなたの好きな数字は',option,'です'

# 2カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# サイドバーで表示
# テキストBOXで動的な処理    
text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味',text

# スライダーで動的な処理
condition = st.sidebar.slider('あなたの今の調子はどうですか？',0,100,50)
'コンディション:',condition

# expander
expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')


