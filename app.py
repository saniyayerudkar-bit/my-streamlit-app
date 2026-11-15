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

# Initialize Session State
if "visits" not in st.session_state:
    st.session_state.visits = 0

if "greeted" not in st.session_state:
    st.session_state.greeted = False

if "name" not in st.session_state:
    st.session_state.name = ""

# Indian Time
india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

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
    "Lavender": ["#f5f0ff", "#e8daef", "#6c3483"],
    "Pink": ["#fff0f5", "#fce4ec", "#ad1457"],
    "Blue": ["#eaf4ff", "#d6eaff", "#1565c0"],
    "Mint Green": ["#eafff5", "#d5f5e3", "#117864"]
}

background, card, text_color = themes[theme]

# Custom CSS
st.markdown(f"""
<style>
.stApp {{
    background-color: {background};
}}

h1 {{
    color: {text_color};
    text-align: center;
    font-size: 40px;
}}

.subtitle {{
    text-align: center;
    font-size: 18px;
    color: {text_color};
}}

.welcome {{
    background-color: {card};
    padding: 30
