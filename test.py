import streamlit as st
import datetime
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🌱 습관 화분", layout="centered")

# 버튼 CSS: 연녹색 배경
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #a8e6a3;
        color: black;
        height: 3em;
        width: 100%;
        border-radius:10px;
        font-size:18px;
    }
    div.stButton > button:hover {
        background-color: #8ed68e;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 초기 상태 세팅
if "habits" not in st.session_state:
    st.session_state.habits = []
    st.session_state.growth = {}
    st.session_state.logs = {}

# 🌱 단계별 화분 + 식물 이모지
plant_stages = ["🪴", "🌱", "🌿", "🌳", "🌴"]

st.title("🌱 습관 화분 키우기")
st.write("습관을 3개 정해서 꾸준히 키워보세요! (💧 버튼 누르면 화분 속 식물이 자랍니다)")

# 습관 등록
if not st.session_state.habits:
    with st.form("habit_form"):
        habit1 = st.text_input("습관 1", "운동하기")
        habit2 = st.text_input("습관 2", "책 읽기")
        habit3 = st.text_input("습관 3", "일찍 자기")
        submitted = st.form_submit_button("등록하기🌱")

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

        col1, col2 = st.columns(2)

        # 💧 물주기 버튼 클릭 시 바로 growth 증가 + 레벨업 체크
        with col1:
            if st.button(f"💧 {habit} 물주기", key=f"water_{habit}"):
                if st.session_state.growth[habit] < len(plant_stages) - 1:
                    st.session_state.growth[habit] += 1
                    stage = st.session_state.growth[habit]
                    st.success(f"{habit} 화분이 자랐습니다! {plant_stages[stage]}")
                    
                    # 레벨업 효과
                    if stage == len(plant_stages) - 1:
                        st.balloons()
                        st.success(f"🎉 {habit} 화분이 최대 단계에 도달했습니다! 🌴 레벨업 완료!")
                else:
                    st.info(f"{habit} 화분은 이미 다 자랐습니다 🌴")
                
                # 오늘 날짜 로그 기록
                today = datetime.date.today()
                st.session_state.logs[habit].append(today)

        # 🔄 다시 시작 버튼 클릭 시 growth 초기화
        with col2:
            if st.button(f"🔄 {habit} 다시 시작", key=f"reset_{habit}"):
                st.session_state.growth[habit] = 0
                st.warning(f"{habit} 화분을 씨앗부터 다시 시작합니다 🌱")

        # 버튼 아래에서 바로 화분 상태 표시
        stage = st.session_state.growth[habit]
        st.markdown(f"<h2 style='text-align:center;font-size:50px'>{plant_stages[stage]}</h2>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("📊 주간 달성률 통계")

    today = datetime.date.today()
    last_week = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    last_week_str = [d.strftime("%m/%d") for d in last_week]

    # 습관별 차트
    for habit in st.session_state.habits:
        st.subheader(f"{habit} 주간 달성률")
        counts = [st.session_state.logs[habit].count(day) for day in last_week]

        df = pd.DataFrame({
            "날짜": last_week_str,
            "횟수": counts
        })

        fig = px.bar(
            df,
            x="날짜",
            y="횟수",
            text="횟수",
            labels={"횟수": "횟수", "날짜": "날짜"},
        )

        fig.update_traces(textposition='outside')
        fig.update_yaxes(dtick=1)  # y축 1씩 증가
        fig.update_xaxes(tickangle=0)  # x축 글자 수평
        st.plotly_chart(fig, use_container_width=True)
