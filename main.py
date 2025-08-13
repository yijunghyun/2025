import streamlit as st
import random
import datetime

# 🎨 귀여운 음식 데이터 (카테고리별)
foods = {
    "한식": [
        ("🍚", "비빔밥"), ("🍲", "김치찌개"), ("🍜", "칼국수"), ("🍗", "치킨"),
        ("🥟", "만두"), ("🍠", "군고구마"), ("🥬", "쌈밥"), ("🍙", "주먹밥"),
        ("🥢", "떡볶이"), ("🥩", "불고기")
    ],
    "양식": [
        ("🍕", "피자"), ("🍔", "햄버거"), ("🍝", "파스타"), ("🥩", "스테이크"),
        ("🥪", "샌드위치"), ("🥗", "샐러드"), ("🍟", "감자튀김"), ("🌭", "핫도그"),
        ("🍳", "오믈렛"), ("🫕", "치즈퐁듀")
    ],
    "일식": [
        ("🍣", "초밥"), ("🍤", "새우튀김"), ("🍛", "카레라이스"), ("🍜", "라멘"),
        ("🍙", "삼각김밥"), ("🥟", "교자만두"), ("🥢", "우동"), ("🍡", "당고"),
        ("🥚", "타마고야키"), ("🦪", "굴튀김")
    ],
    "디저트": [
        ("🍰", "케이크"), ("🍩", "도넛"), ("🍫", "초콜릿"), ("🍦", "아이스크림"),
        ("🍪", "쿠키"), ("🧁", "컵케이크"), ("🍯", "허니토스트"), ("🍧", "빙수"),
        ("🍮", "푸딩"), ("🍬", "사탕")
    ],
    "음료": [
        ("☕", "커피"), ("🍵", "말차"), ("🧋", "버블티"), ("🍹", "과일 칵테일"),
        ("🥤", "탄산음료"), ("🍶", "사케"), ("🥛", "우유"), ("🍊", "오렌지주스"),
        ("🫖", "홍차"), ("🍷", "와인")
    ]
}

# 🌈 앱 제목
st.markdown("<h1 style='text-align: center; color: pink;'>🍽️ 랜덤 음식 추천기 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>귀여운 음식 이모지로 오늘의 메뉴를 골라드려요!</p>", unsafe_allow_html=True)

# 📅 오늘 날짜 기반 추천
today = datetime.date.today()
random.seed(today.toordinal())
all_foods = sum(foods.values(), [])
today_food = random.choice(all_foods)

with st.expander("📅 오늘의 추천 음식 보기"):
    st.markdown(f"<h1 style='text-align: center; font-size: 120px;'>{today_food[0]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>오늘은 <b>{today_food[1]}</b> 어때요? 😋</h3>", unsafe_allow_html=True)

# 🍴 카테고리 선택
st.subheader("🍴 카테고리별 추천 받기")
category = st.selectbox("메뉴 카테고리를 골라주세요", list(foods.keys()))

# 🎁 추천 버튼
if st.button("✨ 랜덤 추천 받기 ✨"):
    emoji, name = random.choice(foods[category])
    st.markdown(f"<h1 style='text-align: center; font-size: 120px;'>{emoji}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>오늘은 <b>{name}</b> 먹는 건 어때요? 🥰</h3>", unsafe_allow_html=True)

    # 👍 / 👎 평가
    st.write("이 추천이 마음에 드시나요?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 좋아요"):
            st.success("좋아요! 🍀 행복한 식사 되세요!")
    with col2:
        if st.button("👎 별로에요"):
            st.warning("다음엔 더 맛있는 걸 추천할게요! 🐣")

# 🌟 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>© 2025 귀여운 음식 추천기 🍒</p>", unsafe_allow_html=True)
