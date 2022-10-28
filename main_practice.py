import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
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

#　表を表示させる
# df = pd.DataFrame({
#     '1列目' : [1,2,3,4],
#     '2列目' : [10,20,30,40]
# })

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
# 折れ線ブラフで表示
st.line_chart(df)
# 棒グラフで表示
st.bar_chart(df)

# 地図上にプロットする
map_df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69 , 139.70],
    columns=['lat','lon']
)
st.map(map_df)

# チェックBOXで動的な処理
if st.checkbox('show Image'):

    # 画像を表示させる
    img = Image.open('sample.jpg')
    st.image(img, caption='Naoto Maeda', use_column_width=True)

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


