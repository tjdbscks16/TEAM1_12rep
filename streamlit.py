import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="종합 대시보드 (Task 1~7)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("종합 대시보드")

# 탭으로 Task 구분
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Task 1: 기본 UI",
    "Task 2: 데이터 표시",
    "Task 3: 차트 그리기",
    "Task 4: CSV 분석",
    "Task 5: 인터랙티브 필터"
])


with tab1:
    st.header("Task 1: 기본 UI 컴포넌트")
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

with tab2:
    st.header("Task 2: 데이터 표시하기")
    st.subheader("CSV 업로드")
    uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state["uploaded_csv"] = df
        st.dataframe(df)
    else:
        st.info("CSV 파일을 업로드하면 데이터가 표시됩니다.")

with tab3:
    st.header("Task 3: 차트 그리기")
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
        st.info("먼저 위 탭에서 CSV 파일을 업로드 해주세요.")

with tab4:
    st.header("Task 4: 파일 업로드 - CSV 분석 (penguins.csv 사용)")
    if "uploaded_csv" not in st.session_state:
        st.warning("⚠ 먼저 'Task 2'에서 CSV 파일을 업로드하세요.")
        st.stop()

    df = st.session_state["uploaded_csv"]

    st.success("CSV 데이터 불러오기 완료!")
    st.write("### 데이터 미리보기")
    st.dataframe(df.head())

    with st.expander("기본 통계 보기"):
        st.write(df.describe())

    with st.expander("결측치 확인 및 데이터타입"):
        st.write("### 결측치")
        st.write(df.isnull().sum())
        st.write("### 데이터 타입")
        st.write(df.dtypes)

with tab5:
    st.header("Task 5: 인터랙티브 필터")
    if "uploaded_csv" not in st.session_state:
        st.warning("⚠ 먼저 'Task 2'에서 CSV 파일을 업로드하세요.")
        st.stop()

    df = st.session_state["uploaded_csv"]

    # 기준 컬럼 선택과 결과 분할을 컬럼으로 나눔 (심플한 레이아웃)
    filter_col, result_col = st.columns(2)

    with filter_col:
        filter_column = st.selectbox(
            "기준 컬럼 선택",
            ["species", "island", "sex", "bill_length_mm", "flipper_length_mm", "body_mass_g"]
        )
    with result_col:
        result = df.groupby(filter_column).size().reset_index(name="value")
        st.write("### 필터 결과")
        st.dataframe(result)

    # 차트는 전체 너비로 보여줌
    chart = (
        alt.Chart(result)
        .mark_bar()
        .encode(
            x=filter_column,
            y="value"
        )
    )
    st.altair_chart(chart, use_container_width=True)
