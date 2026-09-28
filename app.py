import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="EduGenie - AI Study Assistant", layout="wide")

st.title("🎓 EduGenie: AI Powered Study Assistant")
st.write("SkillWallet Generative AI Project - Ask doubts or get study summaries!")

# API Key Setup
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # User Input
    user_topic = st.text_area("Enter your topic, question, or study notes:")

    task = st.selectbox(
        "Choose an action:",
        ["Explain in Simple Terms", "Summarize Key Points", "Generate 5 Quiz Questions"]
    )

    if st.button("Generate with AI"):
        if user_topic:
            with st.spinner("AI is thinking..."):
                prompt = f"You are an expert tutor. Please {task} for the following content:\n\n{user_topic}"
                response = model.generate_content(prompt)
                st.subheader("EduGenie Response:")
                st.write(response.text)
        else:
            st.warning("Please enter a question or topic first!")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start!")
