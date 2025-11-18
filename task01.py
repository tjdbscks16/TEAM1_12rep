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
