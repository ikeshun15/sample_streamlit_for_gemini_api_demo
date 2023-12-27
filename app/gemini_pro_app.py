import streamlit as st

from controller import ChatManager

class GeminiProAppComponents:
    @staticmethod
    def init_page():
        ChatManager.set_default_api_key()
        st.set_page_config(
            page_title="Gemini Pro", 
            page_icon="💬",
        )
    
    @staticmethod
    def display_main_page():
        
        st.markdown("# 💬 Gemini Pro")
        with st.form(key="gemini_pro_form"):
            prompt = st.text_input(label="プロンプト")
            submit_button = st.form_submit_button(label="Submit", type="primary")

        if submit_button:
            message = st.chat_message("assistant")
            message.markdown(ChatManager.gemini_pro_generate_content(query=prompt, stream=False))

    @classmethod
    def set_page(cls):
        cls.init_page()
        cls.display_main_page()