import streamlit as st
from streamlit_lottie import st_lottie_spinner

from controller import ChatManager
from model import LottieManager

class GeminiProAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro", 
            page_icon="💬",
        )
        ChatManager.set_default_api_key()
    
    @staticmethod
    def display_main_page() -> None:
        st.markdown("# 💬 Gemini Pro")
        with st.form(key="gemini_pro_form"):
            prompt = st.text_area(label="プロンプト")
            submit_button = st.form_submit_button(label="Submit", type="primary")

        if submit_button:
            with st.chat_message("assistant"):
                message = st.empty()

            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                response = ChatManager.gemini_pro_generate_content(query=prompt, stream=True, callback_func=message.markdown)
                message.markdown(response)

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.display_main_page()