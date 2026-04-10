import streamlit as st
from game_logic import generate_cards

def init_state():
    """Streamlit의 session_state를 초기화하여 게임 상태를 관리합니다."""
    if "cards" not in st.session_state:
        st.session_state.cards = generate_cards()      # 16장의 섞인 카드 리스트
    if "flipped_indices" not in st.session_state:
        st.session_state.flipped_indices = []          # 현재 뒤집힌 카드의 인덱스 (최대 2개 저장)
    if "matched_indices" not in st.session_state:
        st.session_state.matched_indices = []          # 짝이 맞춰진 카드의 인덱스들 모음

def reset_game():
    """게임 상태를 초기 상태로 되돌리고 카드를 다시 섞습니다."""
    st.session_state.cards = generate_cards()
    st.session_state.flipped_indices = []
    st.session_state.matched_indices = []
