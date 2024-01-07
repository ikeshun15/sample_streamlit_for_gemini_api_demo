import streamlit as st
from streamlit_lottie import st_lottie
from time import sleep

from controller import LottieManager

class HomeAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Home",
            page_icon="🏠",
        )

    @staticmethod
    def display_wakeup_lottie() -> None:
        if not "wakeup_lottie" in st.session_state:
            st.session_state["wakeup_lottie"] = True

        if st.session_state["wakeup_lottie"]:
            st_lottie(animation_source=LottieManager.WAKEUP_LOGO, key="STREAMLIT_LOGO_LOTTIE", speed=1.7, reverse=False, loop=False)
            sleep(1.5)
            st.session_state["wakeup_lottie"] = False
            st.rerun()
    
    @staticmethod
    def display_main_page() -> None:
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
    def set_page(cls) -> None:
        cls.display_wakeup_lottie()
        cls.init_page()
        cls.display_main_page()