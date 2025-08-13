import streamlit as st
import random

# 음식 이모지 리스트
food_emojis = [
    "🍕", "🍔", "🍟", "🌭", "🍣", "🍜", "🍰", "🍩", "🍇", "🍉",
    "🥗", "🍤", "🍫", "🍦", "🍞", "🥪", "🥩", "🧀", "🥟", "🍿"
]

st.title("🍽️ 랜덤 음식 추천기")
st.write("버튼을 눌러서 오늘의 음식을 추천받아보세요!")

if st.button("🍽️ 추천 받기"):
    recommended = random.choice(food_emojis)
    st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{recommended}</h1>", unsafe_allow_html=True)
