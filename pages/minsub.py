import streamlit as st  # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('2023학년도 홍익대 전자전기공학부 입시 결과')

# 텍스트 출력
st.write('# 1. 수시')

import numpy as np   # numpy 라이브러리 임포트
import pandas as pd
data = {
    '전형 유형': ['학생부교과', '학생부종합', '농어촌전형', '학교생활우수자'],
    '평균 등급': [1.85, 2.49, 1.78, 2.49]
}
df = pd.DataFrame(data)
df.set_index('전형 유형', inplace=True)
st.title('수시 입결')
st.bar_chart(df)

st.write('# 2. 정시')
import streamlit as st
import pandas as pd
import numpy as np

# 데이터 설정
subjects = np.array(['국어', '영어', '수학', '탐구', '평균'])
scores = np.array([85, 1.91, 92, 84.5, 87.17])
df = pd.DataFrame({
    '과목': subjects,
    '점수': scores
})
df.set_index('과목', inplace=True)
st.title('정시 입결')
st.bar_chart(df)
