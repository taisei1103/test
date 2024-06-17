import streamlit as st  # streamlit 라이브러리 임포트


# 타이틀 텍스트 출력
st.title('오민근의🪫모교 홍익대학교 전자전기공학부🔌')


# 텍스트 출력
st.write('# 1. 학과 소개')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    # 전자전기 공학부
    - **전자전기공학부**는 전자, 전기공학 전반에 걸친 기초 및 응용학문을 종합적으로 교육한다. 본 학부는 21세기 정보화 시대를 선도하고 고도 산업 사회를 끌고 갈 고급인력 양성을 목표로하며, 다양한 분야에 걸친 학과목을 고르게 개설하고 심도있는 강의를 통하여 높은 수준의 교육체계를 유지하고 있다. 
    
    - *연구실* 분야
        - 반도체 및 정보소자 분야
        - 마이크로파 및 광파 분야
        - 통신, 신호처리 및 인공지능 분야
        - 전력분야
        - 제어시스템 및 정보처리 분야
        
    - 홍익대학교 전자전기공학부 공식홈페이지
        - [홍익대학교 전자전기공학부](https://ee.hongik.ac.kr/dept/index.html)

    '''
    )

# DataFrame 출력
import pandas as pd  # pandas 라이브러리 임포트

st.write('# 2. 교육시설')  # 텍스트 출력
st.markdown(
    '''
    **전자전기 공학부 시설 정보**
    *홍익대학교 제2공학관의 시설정보*
    최고수준의 실습기기를 통하여 이론을 바탕으로 한 실습환경 제공
    '''
    )
df = pd.DataFrame({  # DataFrame 생성
    '강의실명': ['전기기재 실험실', '전자기재실', '전자공학 실험준비실', '실험준비실', '기초전기전자 실험실-1', '기초전기전자 실험실-2', '기초전기전자 실험실-3', '기초전기전자 실험실-4', '기초전자실험실-1', '기초전자실험실-2', '기초전자실험실-3'],
    '면적(A)': [72.05, 25.56, 29.16, 38.48, 106.11, 106.11, 106.11, 106.11, 87.48, 87.48, 87.48]
})

st.dataframe(df)  # DataFrame 출력

# 그래프 출력
import numpy as np   # numpy 라이브러리 임포트

st.write('# 3. 그래프 표시하기')  # 텍스트 출력
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) # DataFrame 생성

st.bar_chart(chart_data)  # 바 차트 출력

# 이미지 출력
from PIL import Image     # 이미지 처리를 위한 PIL 라이브러리 임포트

st.write('# 4. 이미지 표시하기')   # 텍스트 출력
img = Image.open('league of legends.jpeg')    # 이미지 파일 열기
st.image(img, width=300)          # 이미지 출력
