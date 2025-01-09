import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=105


# number_of_decks = st.number_input("Number of decks", min_value=1, max_value=1, value=1)

deck = Deck(1)


# st.markdown(f"## Deck created with {number_of_decks} deck/s")

# st.image([card.image for card in deck.cards], width=card_width)

if st.button("Shuffle"):
    deck.shuffle()
# st.image([card.image for card in deck.cards], width=card_width)

@st.dialog("Place a bet")
def bet():
    with st.form("Bet", clear_on_submit=True, enter_to_submit=False, border=False):

        bet = st.number_input("", min_value=1, max_value=500, value=1, key="bet")

        if st.form_submit_button("Invia"):
            st.rerun()


if st.button("Place a bet"):
    bet()


try:
    st.text(f"The player has bet: {st.session_state['bet']}")
except:
    pass


playerCards: list[Card] = []
botCards: list[Card] = []

for i in range(2):
    playerCards.append(deck.draw())
    botCards.append(deck.draw())

st.image([card.image for card in playerCards], width=50)
st.image([card.image for card in botCards], width=50)

st.write(st.session_state)
