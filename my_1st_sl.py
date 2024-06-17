import streamlit as st  # streamlit 라이브러리 임포트


# 타이틀 텍스트 출력
st.title('오민근의🪫모교 홍익대학교 전자전기공학부🔌')

st.write('# 홍익대학교 로고')   # 텍스트 출력
img = Image.open('hongik.png')    # 이미지 파일 열기
st.image(img, width=300)          # 이미지 출력

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
    '강의실명': ['전기기재 실험실', '전자기재실', '전자공학 실험준비실', '실험준비실', '기초전기전자 실험실-1', '기초전기전자 실험실-2', '기초전기전자 실험실-3', '기초전기전자 실험실-4', '기초전자실험실-1', '기초전자실험실-2', '기초전자실험실-3']
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



st.write('# 이것은 제목입니다. : st.write()')
st.title('이것은 제목입니다. : st.title()')
st.header('이것은 헤더입니다. : st.header()')
st.subheader('이것은 서브헤더입니다. : st.subheader()')
st.text('## 이것은 텍스트입니다. : st.text()')
st.markdown('## 이것은 마크다운입니다. : st.markdown()')

# 사이드바
st.header('🤖 사이드바')
st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

# 레이아웃: 컬럼
st.header('🤖 컬럼 레이아웃')
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])  # 동일한 라디오 버튼을 생성할 수 없음
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

# 레이아웃: 탭
st.header('🤖 탭 레이아웃')
tab_1, tab_2, tab_3 = st.tabs(['탭A', '탭B', '탭C'])  # 탭 인스턴스 생성. 3개의 탭을 생성

with tab_1:
    st.write('## 탭A')
    st.write('이것은 탭A의 내용입니다.')

with tab_2:
    st.write('## 탭B')
    st.write('이것은 탭B의 내용입니다.')

tab_3.write('## 탭C')
tab_3.write('이것은 탭C의 내용입니다.')

# 사용자 입력
st.header('🤖 사용자 입력')

text = st.text_input('여기에 텍스트를 입력하세요') # 텍스트 입력은 입력된 값을 반환
st.write(f'입력된 텍스트: {text}')

number = st.number_input('여기에 숫자를 입력하세요') # 숫자 입력은 입력된 값을 반환
st.write(f'입력된 숫자: {number}')

check = st.checkbox('여기를 체크하세요') # 체크박스는 True/False 값을 반환
if check:
    st.write('체크되었습니다.')

radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 라디오 버튼은 선택된 값을 반환
st.write(radio+'가 선택되었습니다.')

select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 셀렉트박스는 선택된 값을 반환
st.write(select+'가 선택되었습니다.')

slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50) # 슬라이더는 선택된 값을 반환
st.write(f'현재의 값은 {slider} 입니다.')

multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3']) # 멀티셀렉트박스는 선택된 값을 리스트로 반환
st.write(f'{type(multi) = }, {multi}가 선택되었습니다.')

button = st.button('여기를 클릭하세요') # 버튼은 클릭 여부를 반환
if button:
    st.write('버튼이 클릭되었습니다.(일반 텍스트: st.write()')
    st.success('버튼이 클릭되었습니다.(메시지: st.success())')  # 성공 메시지 출력
    st.balloons() # 풍선 애니메이션 출력

# 캐싱
st.header('🤖 캐싱 적용')

import time

@st.cache_data
def long_running_function(param1):
    time.sleep(5)
    return param1*param1

start = time.time()
num_1 = st.number_input('입력한 숫자의 제곱을 계산합니다.') # 숫자 입력은 입력된 값을 반환
st.write(f'{num_1}의 제곱은 {long_running_function(num_1)} 입니다. 계산시간은 {time.time()-start:.2f}초 소요')


# 세션 상태
st.header('🤖 세션 상태')

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("session_state를 사용하지 않은 경우")
color1 = st.color_picker("Color1", "#FF0000")
st.divider() # 구분선
st.scatter_chart(df, x="x", y="y", color=color1)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("session_state를 사용한 경우")
color2 = st.color_picker("Color2", "#FF0000")
st.divider() # 구분선
st.scatter_chart(st.session_state.df, x="x", y="y", color=color2)
