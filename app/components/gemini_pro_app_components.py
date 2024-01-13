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

    @classmethod
    def generate_content_page(cls) -> None:
        with st.form(key="gemini_pro_form", clear_on_submit=True):
            prompt = st.text_area(label="プロンプト", placeholder="Gemini Proに聞いてください...", disabled=GeminiProFormSState.get())
            submit_button = st.form_submit_button(label="Submit", type="primary", on_click=cls.on_click, disabled=GeminiProFormSState.get())

        if submit_button:
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
    def multi_conv_page(cls):
        with st.form(key="gemini_pro_form", clear_on_submit=True):
            prompt = st.text_area(label="プロンプト", placeholder="Gemini Proに聞いてください...", disabled=GeminiProFormSState.get())
            submit_button = st.form_submit_button(label="Submit", type="primary", on_click=cls.on_click, disabled=GeminiProFormSState.get())

        if submit_button:
            user_message = st.chat_message("user")
            user_message.markdown(prompt)
            
            with st.chat_message("assistant"):
                gemini_message = st.empty()

            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                history = ChatManager.gemini_pro_chat_content(prompt=prompt, stream=True, history=GeminiProChatConvSState.get(), callback_func=gemini_message.markdown)
                GeminiProChatConvSState.set(value=history)
                GeminiProFormSState.set(value=False)
                st.rerun()
        
        gemini_chat_conv_list = GeminiProChatConvSState.get()
        print(gemini_chat_conv_list)
        if gemini_chat_conv_list:
            user_message = st.chat_message("user")
            gemini_message = st.chat_message("assistant")
            for message in gemini_chat_conv_list:
                if message.role == "user":
                    user_message.markdown(message.parts[0].text)
                else:
                    gemini_message.markdown(message.parts[0].text)

    @classmethod
    def select_page(cls):
        st.header(body="💬 Gemini Pro", divider='rainbow')
        mode_select =  st.radio(label="モードセレクト", options=["**会話(複数やり取り)**", "**生成**"], horizontal=True)
        if mode_select == "**会話(複数やり取り)**":
            cls.multi_conv_page()
        else:
            cls.generate_content_page()


    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        # cls.generate_content_page()
        cls.select_page()