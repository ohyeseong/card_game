import random

def generate_cards():
    """8쌍의 과일 이모지 카드를 생성하고 무작위로 섞어서 반환합니다."""
    emojis = ['🍎', '🍌', '🍉', '🍇', '🍓', '🍒', '🍍', '🥝']
    cards = emojis * 2  # 각 과일 이모지를 2개씩 만듦 (총 16개)
    random.shuffle(cards)
    return cards

def check_match(card1, card2):
    """선택한 두 카드가 같은지 비교하여 결과를 반환합니다."""
    return card1 == card2
