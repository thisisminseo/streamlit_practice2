import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

#페이지 기본설정 
st.set_page_config(   
    page_icon = "📜",
    page_title = "김민서",
    layout = "wide",
)

#페이지 헤더 , 서브헤더 ,제목설정
st.header('최보은바보')
st.subheader('토요일에 비옴 우산챙기셈')

#페이지 칼럼 분할(예: 부트스트랩 컬럼 ,  그리드)
cols = st.columns((1,1,2))
cols[0].metric("1/13", "10℃","2 ℃")
cols[0].metric("1/14", "7℃","-3 ℃")
cols[0].metric("1/15", "2℃","-5 ℃")
cols[1].metric("1/16", "0℃","-2 ℃")
cols[1].metric("1/17", "1℃","+1 ℃")
cols[1].metric("1/118", "3℃","+2 ℃")

#라인 그래프 데이터 생성(with pandas)
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c'])

#칼럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)
