import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=105


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=1, value=1)

deck = Deck(number_of_decks)


st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)

player_money: float = 2000

bet = st.number_input("Bet", min_value=1, max_value=500, value=1)

playerCards: list[Card] = []
botCards: list[Card] = []

for i in range(2):
    playerCards = deck.draw()
    botCards = deck.draw()

st.image([card.image for card in playerCards], width=50)
st.image([card.image for card in botCards], width=50)
