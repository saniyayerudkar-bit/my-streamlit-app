
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import random

# Page Configuration
st.set_page_config(
    page_title="Welcome Dashboard",
    page_icon="🌸",
    layout="centered"
)

# Session State
if "visits" not in st.session_state:
    st.session_state.visits = 0

if "greeted" not in st.session_state:
    st.session_state.greeted = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "quote" not in st.session_state:
    st.session_state.quote = ""

# Motivational Quotes
quotes = [
    "Believe in yourself and make it happen! ✨",
    "Every day is a new opportunity. 🌷",
    "Dream big and work hard. 💜",
    "Small steps lead to big achievements. 🌈",
    "Your only limit is your mind. 🌟"
]

# Theme Selection
st.sidebar.title("🎨 Customize Your App")

theme = st.sidebar.selectbox(
    "Choose Your Theme",
    ["Lavender", "Pink", "Blue", "Mint Green"]
)

themes = {
    "Lavender": ("#f5f0ff", "#e8daef", "#6c3483"),
    "Pink": ("#fff0f5", "#fce4ec", "#ad1457"),
    "Blue": ("#eaf4ff", "#d6eaff", "#1565c0"),
    "Mint Green": ("#eafff5", "#d5f5e3", "#117864")
}

background, card, text_color = themes[theme]

# Custom CSS
css = """
<style>
.stApp {
    background-color: BACKGROUND;
}
h1 {
    color: TEXTCOLOR;
    text-align: center;
    font-size: 40px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: TEXTCOLOR;
}
.welcome {
    background-color: CARD;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    font-size: 25px;
    color: TEXTCOLOR;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.quote {
    background-color: CARD;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: TEXTCOLOR;
    font-size: 18px;
    margin-top: 20px;
}
.stButton > button {
    border-radius: 12px;
    height: 45px;
    font-weight: bold;
}
</style>
"""

css = css.replace("BACKGROUND", background)
css = css.replace("CARD", card)
css = css.replace("TEXTCOLOR", text_color)

st.markdown(css, unsafe_allow_html=True)

# Sidebar Information
st.sidebar.markdown("---")
st.sidebar.info(
    "🌸 A personalized welcome application built using Python and Streamlit."
)

st.sidebar.markdown("### Features")
st.sidebar.write("✅ Personalized Greeting")
st.sidebar.write("✅ Indian Clock")
st.sidebar.write("✅ Motivational Quotes")
st.sidebar.write("✅ Multiple Themes")

# Main Heading
st.title("🌸 Welcome Dashboard")

st.markdown(
    '<p class="subtitle">Your little space for positive vibes!</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# Date and Time
india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📅 Today's Date",
        india_time.strftime("%d-%m-%Y")
    )

with col2:
    st.metric(
        "🕒 Current Time",
        india_time.strftime("%I:%M:%S %p")
    )

st.markdown("---")

# Visit Counter
st.session_state.visits += 1

# Name Input
st.subheader("💜 Tell Us About Yourself")

name = st.text_input(
    "Enter your name:",
    value=st.session_state.name
)

if st.button("Generate Welcome"):
    if name.strip():
        st.session_state.name = name.strip()
        st.session_state.greeted = True
        st.session_state.quote = random.choice(quotes)
    else:
        st.warning("Please enter your name.")

# Personalized Greeting
if st.session_state.greeted:
    st.markdown(
        f'<div class="welcome">Welcome, {st.session_state.name}! 🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="quote">{st.session_state.quote}</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# Visit Counter Display
st.info(
    f"👀 App visits in this session: {st.session_state.visits}"
)

# Footer
st.caption("Made with Python and Streamlit 💜")
