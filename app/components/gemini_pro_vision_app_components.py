import streamlit as st
from streamlit_lottie import st_lottie_spinner

from controller import ChatManager
from model import ImageManager, LottieManager

class GeminiProVisionAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro Vision", 
            page_icon="🖼️",
        )
        ChatManager.set_default_api_key()
    
    @staticmethod
    def main_page() -> None:
        st.header(body="🖼️ Gemini Pro Vision", divider='rainbow')
        with st.form(key="gemini_pro_vision_form", clear_on_submit=True):
            uploaded_files = st.file_uploader(label="画像をアップロード", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
            prompt = st.text_area(label="プロンプト", placeholder="Gemini Proに聞いてください...")
            submit_button = st.form_submit_button(label="Submit", type="primary")

        if submit_button:
            user_message = st.chat_message("user")
            user_message.markdown(prompt)
            user_message.image(ImageManager.display_input_image(uploaded_files))

            with st.chat_message("assistant"):
                message = st.empty()
            
            with st_lottie_spinner(animation_source=LottieManager.PROCESSING_LOTTIE, key="PROCESSING_LOTTIE", width=50):
                response = ChatManager.gemini_pro_vision_generate_content(image_path=uploaded_files, query=prompt, stream=True, callback_func=message.markdown)
                message.markdown(response)


    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.main_page()