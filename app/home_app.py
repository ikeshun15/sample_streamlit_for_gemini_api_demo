import streamlit as st

class HomeAppComponents:
    @staticmethod
    def init_page():
        st.set_page_config(
            page_title="Home",
            page_icon="🏠",
        )
    
    @staticmethod
    def display_main_page():
        st.write("# Gemini API Demoへようこそ 😊")

        st.markdown(
            """
            ### このデモアプリで使えるモデル
            - Gemini Pro
            - Gemini Pro Vision
            
            This streamlit was made by Shunichi Ikezu🍓
            """
        )

    @classmethod
    def set_page(cls):
        cls.init_page()
        cls.display_main_page()