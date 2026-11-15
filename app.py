import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="My Welcome App",
    page_icon="🌸",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f5f0ff;
}
h1 {
    color: #6c3483;
    text-align: center;
}
.welcome {
    background-color: #e8daef;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    color: #512e5f;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌸 About App")
st.sidebar.write("Welcome to My Streamlit Application!")
st.sidebar.info("This application generates personalized greetings.")

# Main Heading
st.title("🌸 Welcome App")
st.write("### Enter your name to get a personalized greeting!")

# Name Input
name = st.text_input("Enter Your Name 👇", placeholder="Your name here")

# Buttons
col1, col2 = st.columns(2)

with col1:
    submit = st.button("Submit 🎉", use_container_width=True)

with col2:
    clear = st.button("Clear ❌", use_container_width=True)

# Greeting Logic
if submit:
    if name.strip():
        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning"
        elif hour < 17:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        st.balloons()

        st.markdown(
            f'<div class="welcome">✨ {greeting}, {name}! ✨<br>'
            'Welcome to My App!</div>',
            unsafe_allow_html=True
        )

        st.success("Your greeting was generated successfully!")

        st.write("📅 Date:", datetime.now().strftime("%d-%m-%Y"))
        st.write("⏰ Time:", datetime.now().strftime("%I:%M:%S %p"))

    else:
        st.warning("Please enter your name first!")

if clear:
    st.rerun()

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Python and Streamlit")
