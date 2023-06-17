import streamlit as st

def calculate_remaining_time():
    try:
        current_age = int(st.session_state['entry_age'])
        average_age = int(st.session_state['entry_average_age'])
        meetings_per_month = st.session_state['entry_meetings']
        hours_per_meeting = st.session_state['entry_hours']

        if average_age <= current_age:
            st.error("平均壽命要大於目前年齡。")
            return

        months_remaining = (average_age - current_age) * 12

        total_hours = months_remaining * meetings_per_month * hours_per_meeting

        remaining_years = total_hours // (365 * 24)
        remaining_months = (total_hours % (365 * 24)) // (30 * 24)
        remaining_days = (total_hours % (30 * 24)) // 24
        remaining_hours = total_hours % 24

        result = "您還有"

        if remaining_years > 0:
            result += f"{remaining_years}年"

        if remaining_months > 0:
            result += f"{remaining_months}個月"

        if remaining_days > 0:
            result += f"{remaining_days}天"

        if remaining_hours > 0:
            result += f"{remaining_hours}個小時"

        result += "的時間<br>可以和對方相處"

        font_size = 18

        # 使用字符串格式化将变量应用于 HTML 标签中
        styled_text = "<font size='{}'>{}</font>".format(font_size, result)
        st.markdown(styled_text, unsafe_allow_html=True)


        

        

    except ValueError:
        st.error("請輸入有效的數字。")

st.title("相處時間計算器")

st.session_state['entry_average_age'] = st.number_input("平均壽命：", value=80)
st.markdown("""
台灣「110年簡易生命表」，國人的平均壽命為80.86歲，男性77.67歲、女性84.25歲\n

2022年大马预期寿命数据，平均寿命预计为73.4岁，男性71.3岁。女性75.8岁。
""")

        
st.session_state['entry_age'] = int(st.number_input("對方的現在年齡：", value=0, step=1))



meetings_options = list(range(31))
st.session_state['entry_meetings'] = st.selectbox("每個月碰面次數：", meetings_options)

hours_options = list(range(1, 25))
st.session_state['entry_hours'] = st.selectbox("每次碰面時間（小時）：", hours_options)

button_calculate = st.button("計算")
if button_calculate:
    calculate_remaining_time()
    
image_url_family = f"https://source.unsplash.com/1440x1280/?grandparents family"
st.image(image_url_family, use_column_width=True)
