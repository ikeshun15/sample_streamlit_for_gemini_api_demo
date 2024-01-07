import streamlit as st
from streamlit_lottie import st_lottie
from time import sleep

from model import LottieManager
from ..s_state import WakeupLottieSState

class HomeAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Home",
            page_icon="🏠",
        )

    @staticmethod
    def init_session_state():
        WakeupLottieSState.init()

    @staticmethod
    def display_wakeup_lottie() -> None:
        if not WakeupLottieSState.get():
            st_lottie(animation_source=LottieManager.WAKEUP_LOTTIE, key="WAKEUP_LOTTIE", speed=1.7, reverse=False, loop=False)
            sleep(1.5)
            WakeupLottieSState.set(value=True)
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
        cls.init_page()
        cls.init_session_state()
        cls.display_wakeup_lottie()
        cls.display_main_page()