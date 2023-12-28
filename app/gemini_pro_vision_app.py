import streamlit as st

from controller import ChatManager, ImageManager

class GeminiProVisionAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Gemini Pro Vision", 
            page_icon="🖼️",
        )
        ChatManager.set_default_api_key()
    
    @staticmethod
    def display_main_page() -> None:
        
        st.markdown("# 🖼️ Gemini Pro Vision")
        with st.form(key="gemini_pro_vision_form"):
            uploaded_files = st.file_uploader(label="JPGファイル", accept_multiple_files=False)
            prompt = st.text_area(label="プロンプト")
            submit_button = st.form_submit_button(label="Submit", type="primary")

        if submit_button:
            st.image(ImageManager.display_input_image(uploaded_files))
            message = st.chat_message("assistant")
            for chunk in ChatManager.gemini_pro_vision_generate_content(image_path=uploaded_files, query=prompt, stream=True):
                message.markdown(chunk)

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.display_main_page()