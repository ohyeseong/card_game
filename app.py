import streamlit as st
import time
from state import init_state, reset_game
from game_logic import check_match

# 페이지 기본 설정
st.set_page_config(page_title="카드 뒤집기 🃏", layout="centered")

# 상태 초기화
init_state()

st.title("🃏 카드 뒤집기 기억력 게임")
st.write("같은 그림의 카드를 찾아서 맞춰보세요!")

# 두 카드가 뒤집힌 상태라면 짝을 확인
if len(st.session_state.flipped_indices) == 2:
    idx1, idx2 = st.session_state.flipped_indices
    card1 = st.session_state.cards[idx1]
    card2 = st.session_state.cards[idx2]
    
    if check_match(card1, card2):
        # 짝이 맞으면 matched 리스트에 추가
        st.session_state.matched_indices.extend([idx1, idx2])
    
    # 사용자가 확인할 수 있도록 1초 대기 후 리셋 (동기 방식)
    time.sleep(1)
    st.session_state.flipped_indices = []
    st.rerun()

# 4x4 그리드 생성
cols = st.columns(4)
for i in range(16):
    col = cols[i % 4]
    
    with col:
        # 이 카드가 이미 맞춰졌거나, 현재 뒤집힌 상태인지 확인
        is_matched = i in st.session_state.matched_indices
        is_flipped = i in st.session_state.flipped_indices
        
        if is_matched or is_flipped:
            # 카드의 진짜 이모지 표시, 더 이상 클릭 안되게 disabled 처리
            st.button(st.session_state.cards[i], key=f"card_{i}", disabled=True)
        else:
            # 뒷면 ❓ 아이콘 표시 및 클릭 기능 활성화
            if st.button("❓", key=f"btn_{i}"):
                if len(st.session_state.flipped_indices) < 2:
                    st.session_state.flipped_indices.append(i)
                    st.rerun()

# 종료 조건: 모든 카드를 맞췄을 때
if len(st.session_state.matched_indices) == 16:
    st.success("🎉 축하합니다! 모든 카드를 맞혔습니다! 🎉")
    if st.button("다시 하기"):
        reset_game()
        st.rerun()
