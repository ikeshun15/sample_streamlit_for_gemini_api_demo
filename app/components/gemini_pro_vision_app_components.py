import streamlit as st
from streamlit_lottie import st_lottie_spinner

from controller import ChatManager
from model import ImageManager, LottieManager
from ..s_state import GeminiProVisionFormSState, GeminiProVisionChatSState
from ..entity import GeminiProVisionChatEntity

class GeminiProVisionAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro Vision", 
            page_icon="🖼️",
        )

    @staticmethod
    def init_session_state():
        GeminiProVisionFormSState.init()
        GeminiProVisionChatSState.init()

    @staticmethod
    def on_click():
        GeminiProVisionFormSState.set(value=True)
    
    @classmethod
    def main_page(cls) -> None:
        st.header(body="🖼️ Gemini Pro Vision", divider='rainbow')
        with st.form(key="gemini_pro_vision_form", clear_on_submit=True):
            uploaded_files = st.file_uploader(label="画像をアップロード", type=["jpg", "jpeg", "png"], accept_multiple_files=False, disabled=GeminiProVisionFormSState.get())
            prompt = st.text_area(label="プロンプト", placeholder="Gemini Proに聞いてください...", disabled=GeminiProVisionFormSState.get())
            submit_button = st.form_submit_button(label="Submit", type="primary", on_click=cls.on_click, disabled=GeminiProVisionFormSState.get())

        if submit_button:
            user_message = st.chat_message("user")
            user_message.markdown(prompt)
            user_message.image(ImageManager.display_input_image(image_path=uploaded_files))

            with st.chat_message("assistant"):
                message = st.empty()
            
            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                response = ChatManager.gemini_pro_vision_generate_content(image_path=uploaded_files, prompt=prompt, stream=True, callback_func=message.markdown)
                GeminiProVisionChatSState.set(value=GeminiProVisionChatEntity(image_path=uploaded_files, prompt=prompt, response=response))
                GeminiProVisionFormSState.set(value=False)
                st.rerun()

        gemini_chat_instance = GeminiProVisionChatSState.get()

        if gemini_chat_instance.prompt != "" or gemini_chat_instance.image_path != "":
            user_message = st.chat_message("user")
            user_message.markdown(gemini_chat_instance.prompt)
            user_message.image(ImageManager.display_input_image(image_path=gemini_chat_instance.image_path))
        
        if gemini_chat_instance.response != "":
            gemini_message = st.chat_message("assistant")
            gemini_message.markdown(gemini_chat_instance.response)

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.main_page()