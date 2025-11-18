import streamlit as st
import pandas as pd
import altair as alt


# ================================
# Task 1: 기본 UI 컴포넌트
# ================================
st.title("Task1: 기본 UI 컴포넌트")

name = st.text_input("이름을 입력하세요", "")
age = st.slider("나이를 선택하세요", 0, 100, 22)
option = st.selectbox('좋아하는 색', ["빨강", "주황", "보라", "파랑", "노랑", "검정", "핑크"])
checked = st.checkbox("이용 약관에 동의합니다.")
btn = st.button("확인")

if btn:
    st.success(f"""
    ✔ 이름: {name}  
    ✔ 나이: {age}  
    ✔ 좋아하는 색: {option}  
    ✔ 이용 약관 동의: {checked}
    """)
#st.area_chart(data=None, x=10, y=10, x_label='testX', y_label='testY', color=None, stack=None, width="stretch", height="content", use_container_width=None)




# ================================
# Task 2: 데이터표시하기
# ================================
st.set_page_config(
    page_title = "Streamlit Tutorial",
    page_icon = ":shark",
    layout = "wide",
    initial_sidebar_state = "auto"
)
st.header("Task 2: 데이터 표시하기")

st.subheader("CSV 업로드")
uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["uploaded_csv"] = df   # 세션에 저장
    st.dataframe(df)
else:
    st.write("CSV 파일을 업로드하면 데이터가 표시됩니다.")


msg = st.chat_input("메시지를 입력하세요")

# ================================
# Task 3: 차트그리기 
# ================================
from numpy.random import default_rng as rng

if "uploaded_csv" in st.session_state:
    df = st.session_state["uploaded_csv"]

   
    st.line_chart(df["bill_length_mm"]) 
    st.write("부리 길이 분포")

    mass_df = df.groupby("species")["body_mass_g"].mean()
    st.bar_chart(mass_df)
    st.write("종별 평균 몸무게")

    st.area_chart(df["body_mass_g"])
    st.write("샘플별 체중")
    
else:
    st.info("먼저 위에서 CSV 파일을 업로드 해주세요.")


# ================================
# Task 4: CSV 업로드
# ================================
st.title("Task 4: 파일 업로드 - CSV 파일 분석 (penguins.csv 사용)")

# Task 2에서 업로드한 데이터 확인
if "uploaded_csv" not in st.session_state:
    st.warning("⚠ 먼저 Task 2에서 CSV 파일을 업로드하세요.")
    st.stop()

df = st.session_state["uploaded_csv"]

st.success("CSV 데이터 불러오기 완료!")
st.write("### 🔍 데이터 미리보기")
st.dataframe(df.head())

st.write("### 📏 기본 통계")
st.write(df.describe())

st.write("### ⚠️ 결측치 확인")
st.write(df.isnull().sum())

st.write("### 🔤 데이터 타입")
st.write(df.dtypes)
# ================================
# Task 5: 인터랙티브 필터
# ================================
st.title("Task 5: 인터랙티브 필터")

if "uploaded_csv" not in st.session_state:
    st.warning("⚠ 먼저 Task 2에서 CSV 파일을 업로드하세요.")
    st.stop()

df = st.session_state["uploaded_csv"]

# 필터 선택
filter_column = st.selectbox(
    "기준 컬럼 선택",
    ["species", "island", "sex", "bill_length_mm", "flipper_length_mm", "body_mass_g"]
)

# 그룹화
result = df.groupby(filter_column).size().reset_index(name="value")

st.write("### 필터 결과")
st.dataframe(result)

# 차트 표시
chart = (
    alt.Chart(result)
    .mark_bar()
    .encode(
        x=filter_column,
        y="value"
    )
)

st.altair_chart(chart, use_container_width=True)