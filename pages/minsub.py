import streamlit as st  # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('2023학년도 홍익대 전자전기공학부 입시 결과')

# 텍스트 출력
st.write('# 1. 수시')

import numpy as np   # numpy 라이브러리 임포트
import pandas as pd

# 데이터 설정
data = {
    '전형 유형': ['학생부교과', '학생부종합', '농어촌전형', '학교생활우수자'],
    '평균 등급': [1.85, 2.49, 1.78, 2.49]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 전형 유형을 인덱스로 설정
df.set_index('전형 유형', inplace=True)

# Streamlit 제목 설정
st.title('전자전기공학부 2023학년도 입시 결과')

# 바 차트 생성 및 표시
st.bar_chart(df)
