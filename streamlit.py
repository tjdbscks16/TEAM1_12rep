import streamlit as st

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


import pandas as pd
import altair as alt

# ================================
# Task 3: 차트그리기
# ================================
from numpy.random import default_rng as rng
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.area_chart(df, x_label='areaX', y_label='areaY')
st.line_chart(df, x_label='lineX', y_label='lineY')
st.bar_chart(df, x_label='barX', y_label='barY')
# ================================
# Task 4: CSV 업로드
# ================================
st.title("Task 4: 파일 업로드 - CSV 파일 분석 (penguins.csv 사용)")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 🔥 session_state에 저장
    st.session_state["penguins"] = df

    st.success("CSV 파일 업로드 완료!")
    st.write("### 🔍 데이터 미리보기")
    st.dataframe(df.head())

    st.write("### 📏 기본 통계")
    st.write(df.describe())

    st.write("### ⚠️ 결측치 확인")
    st.write(df.isnull().sum())

    st.write("### 🔤 컬럼별 데이터 타입")
    st.write(df.dtypes)

st.write("---")

# ================================
# Task 5: 인터랙티브 필터
# ================================
st.title("Task 5: 인터랙티브 필터")

if "penguins" not in st.session_state:
    st.warning("⚠ 먼저 Task 5에서 penguins.csv 파일을 업로드하세요.")
    st.stop()

df = st.session_state["penguins"]

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



