import streamlit as st
import datetime
import pandas as pd

st.set_page_config(page_title="🪴 습관 화분", layout="centered")

# 초기 상태 세팅
if "habits" not in st.session_state:
    st.session_state.habits = []  # 습관 이름 리스트
    st.session_state.growth = {}  # 습관별 성장 단계
    st.session_state.logs = {}    # 습관별 날짜별 달성 기록

# 🌱 성장 단계 (화분 + 식물 이모지 조합)
plant_stages = [
    "🌱",                # 빈 화분
    "🌿",              # 씨앗 싹틈
    "🌳",              # 새싹 성장
    "🌴",              # 작은 나무
    "🪴"               # 큰 나무
]

st.title("🌱 습관 화분 키우기")
st.write("습관을 3개 정해서 꾸준히 키워보세요! (물주기 💧 하면 화분 속 식물이 자랍니다)")

# 습관 등록 단계
if not st.session_state.habits:
    with st.form("habit_form"):
        habit1 = st.text_input("습관 1", "운동하기")
        habit2 = st.text_input("습관 2", "책 읽기")
        habit3 = st.text_input("습관 3", "일찍 자기")
        submitted = st.form_submit_button("등록하기 🌱")

        if submitted:
            st.session_state.habits = [habit1, habit2, habit3]
            for h in st.session_state.habits:
                st.session_state.growth[h] = 0
                st.session_state.logs[h] = []
            st.success("습관이 등록되었습니다!")
else:
    # 습관별 화분 표시
    for habit in st.session_state.habits:
        st.subheader(f"🌸 {habit}")
        stage = st.session_state.growth[habit]
        st.markdown(f"<h2 style='text-align:center;'>{plant_stages[stage]}</h2>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # 물주기 버튼
        with col1:
            if st.button(f"💧 {habit} 물주기", key=f"water_{habit}"):
                if st.session_state.growth[habit] < len(plant_stages) - 1:
                    st.session_state.growth[habit] += 1
                    st.success(f"{habit} 화분이 자랐습니다! {plant_stages[st.session_state.growth[habit]]}")
                else:
                    st.info(f"{habit} 화분은 이미 다 자랐습니다 🌴")

                # 오늘 날짜 기록
                today = datetime.date.today()
                st.session_state.logs[habit].append(today)

        # 다시 시작 버튼
        with col2:
            if st.button(f"🔄 {habit} 다시 시작", key=f"reset_{habit}"):
                st.session_state.growth[habit] = 0
                st.warning(f"{habit} 화분을 씨앗부터 다시 시작합니다 🪴")

    st.markdown("---")
    st.header("📊 주간 달성률 통계")

    # 최근 7일 기준 데이터 집계
    today = datetime.date.today()
    last_week = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]

    chart_data = {}
    for habit in st.session_state.habits:
        counts = []
        for day in last_week:
            counts.append(st.session_state.logs[habit].count(day))
        chart_data[habit] = counts

    df = pd.DataFrame(chart_data, index=[d.strftime("%m/%d") for d in last_week])
    st.bar_chart(df)

