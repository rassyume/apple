from click.termui import style
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('タイトル')
st.write('プログレスバーの表示')
'Start!!'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'
left_column, right_column=st.columns(2)
button=left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')
expander= st.expander('問い合わせ')
expander.write('内容')
#if st.checkbox('Show Image'):
    #img=Image.open('download.jpg')
    #st.image(img,caption='dog',use_column_width=True)

#option =st.selectbox(
    #'あなたが好きな数字を教えてください',
    #list(range(1,11))
#)
#'あなたの好きな数字は,',option

#st.write('Interactive Widgets')
#text=st.text_input('あなたの趣味を教えてください')
#'あなたの趣味:',text

#condition=st.slider('あなたの今の調子は?',0,100,50)
#'コンディション:',condition
#df=pd.DataFrame(
    #np.random.rand(100,2)/[50,50]+[35.69,139.70],
    #columns=['lat','lon']
#)
#st.table(df.style.highlight_max(axis=0))
#st.map(df)



