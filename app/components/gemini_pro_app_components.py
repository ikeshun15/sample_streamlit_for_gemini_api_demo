import streamlit as st
from streamlit_lottie import st_lottie_spinner
from google.api_core.exceptions import InternalServerError

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
    def apply_button_disable():
        GeminiProFormSState.set(value=True)

    @staticmethod
    def apply_button_able():
        GeminiProFormSState.set(value=False)

    @classmethod
    def main_page(cls) -> None:
        st.header(body="💬 Gemini Pro Demo", divider='rainbow')
        prompt = st.chat_input(placeholder="Gemini Proに聞いてください...", on_submit=cls.apply_button_disable, disabled=GeminiProFormSState.get())
        chat_reset_button = st.sidebar.button(label="チャットリセット", type="primary", use_container_width=True, on_click=cls.apply_button_able)

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
                try:
                    gemini_message.write_stream(ChatManager.get_gemini_pro_chat_generator(chat=chat_entity.chat, prompt=prompt, stream=True))
                    cls.apply_button_able()
                    st.rerun()
                except InternalServerError as e:
                    st.error("AIに問い合わせ中にエラーが発生しました。チャットをリセットして再度送信してください。", icon="🤷")

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.main_page()
