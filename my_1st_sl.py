import streamlit as st  # streamlit 라이브러리 임포트


# 타이틀 텍스트 출력
st.title('😊오민근의 관심 분야👍 ')

# 텍스트 출력
st.write('# 1. Computer Game')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    # League Of Legend
    - 온라인 게임 **국내 피시방 점유율 1위 게임**
    
    - LCK *'리그오브레전드 챔피언스 코리아'* 팀목록
        - SKT T1
        - DWG KIA
        - Gen.G
    ## 게임사 공식홈페이지
    - [라이엇 게임즈](https://www.riotgames.com/ko)
    - [리그오브레전드](https://www.leagueoflegends.com/ko-kr/)

    )

# DataFrame 출력
import pandas as pd  # pandas 라이브러리 임포트

st.write('# 2. Watching YouTube')  # 텍스트 출력
df = pd.DataFrame({  # DataFrame 생성
    '구독중': ['PAKA', '랄로', 'ITSUB잇섭'],
    '구독자': [75만명, 125만명, 255만명]
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
img = Image.open('python.png')    # 이미지 파일 열기
st.image(img, width=300)          # 이미지 출력

