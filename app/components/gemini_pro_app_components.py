import streamlit as st
from streamlit_lottie import st_lottie_spinner

from controller import ChatManager
from model import LottieManager
from ..s_state import GeminiProFormSState, GeminiProChatSState, GeminiProChatConvSState
from ..entity import GeminiProChatEntity

class GeminiProAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro", 
            page_icon="💬",
        )
        ChatManager.set_default_api_key()
    
    @staticmethod
    def init_session_state():
        GeminiProFormSState.init()
        GeminiProChatSState.init()
        GeminiProChatConvSState.init()

    @staticmethod
    def on_click():
        GeminiProFormSState.set(value=True)

    @staticmethod
    def header():
        st.header(body="💬 Gemini Pro Demo", divider='rainbow')

    @classmethod
    def generate_content_page(cls) -> None:
        prompt = st.chat_input(placeholder="Gemini Proに聞いてください...", on_submit=cls.on_click, disabled=GeminiProFormSState.get())
        
        if prompt:
            user_message = st.chat_message("user")
            user_message.markdown(prompt)
            
            with st.chat_message("assistant"):
                gemini_message = st.empty()

            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                response = ChatManager.gemini_pro_generate_content(prompt=prompt, stream=True, callback_func=gemini_message.markdown)
                GeminiProChatSState.set(value=GeminiProChatEntity(prompt=prompt, response=response))
                GeminiProFormSState.set(value=False)
                st.rerun()
        
        gemini_chat_instance = GeminiProChatSState.get()

        if gemini_chat_instance.prompt != "":
            user_message = st.chat_message("user")
            user_message.markdown(gemini_chat_instance.prompt)
        
        if gemini_chat_instance.response != "":
            gemini_message = st.chat_message("assistant")
            gemini_message.markdown(gemini_chat_instance.response)

    @classmethod
    def multi_conv_page(cls) -> None:
        prompt = st.chat_input(placeholder="Gemini Proに聞いてください...", on_submit=cls.on_click, disabled=GeminiProFormSState.get())

        gemini_chat_conv_list = GeminiProChatConvSState.get()

        if gemini_chat_conv_list:
            for message in gemini_chat_conv_list:
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
                history = ChatManager.gemini_pro_chat_content(prompt=prompt, stream=True, history=GeminiProChatConvSState.get(), callback_func=gemini_message.markdown)
                GeminiProChatConvSState.set(value=history)
                GeminiProFormSState.set(value=False)
                st.rerun()

    @classmethod
    def select_page(cls) -> None:
        st.header(body="💬 Gemini Pro Demo", divider='rainbow')
        mode_select = st.toggle(label="会話モード(連続やり取り)", value=True)
        if mode_select:
            cls.multi_conv_page()
        else:
            cls.generate_content_page()

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.select_page()