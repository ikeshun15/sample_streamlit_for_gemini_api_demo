import streamlit as st
from streamlit_lottie import st_lottie_spinner

from controller import ChatManager
from model import LottieManager
from ..s_state import GeminiProFormSState, GeminiProChatSState


class GeminiProAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro", 
            page_icon="💬",
        )
    
    @staticmethod
    def init_session_state():
        GeminiProFormSState.init()
        GeminiProChatSState.init()

    @staticmethod
    def on_click():
        GeminiProFormSState.set(value=True)

    @classmethod
    def main_page(cls) -> None:
        st.header(body="💬 Gemini Pro Demo", divider='rainbow')
        prompt = st.chat_input(placeholder="Gemini Proに聞いてください...", on_submit=cls.on_click, disabled=GeminiProFormSState.get())
        chat_reset_button = st.sidebar.button(label="チャットリセット", type="primary", use_container_width=True)

        if chat_reset_button:
            GeminiProChatSState.reset()

        chat_entity = GeminiProChatSState.get()
        chat_history_list = chat_entity.get_chat_history_list()
        if chat_history_list:
            for message in chat_history_list:
                if message.role == "user":
                    with st.chat_message("user"):
                        st.markdown(message.parts[0].text)
                else:
                    with st.chat_message("assistant"):
                        st.markdown(message.parts[0].text)

        if prompt:
            user_message = st.chat_message("user")
            user_message.markdown(prompt)
            
            with st.chat_message("assistant"):
                gemini_message = st.empty()

            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                response = ChatManager.get_gemini_pro_chat_content(chat=chat_entity.chat, prompt=prompt, stream=True, history=GeminiProChatSState.get(), callback_func=gemini_message.markdown)
                GeminiProFormSState.set(value=False)
                st.rerun()

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.main_page()
