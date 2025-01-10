import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=105


# st.session_state["iniziato"] = False
# st.session_state["deck"] = Deck(1)

if "iniziato" not in st.session_state:
    st.session_state["iniziato"] = False

if "deck" not in st.session_state:
    st.session_state["deck"] = Deck(1)

@st.dialog("Place a bet")
def bet():
    with st.form("Bet", clear_on_submit=True, enter_to_submit=False, border=False):

        bet = st.number_input("", min_value=1, max_value=500, value=1, key='bet')

        if st.form_submit_button("Invia"):
            st.session_state["iniziato"] = True
            st.session_state["deck"].shuffle()
            st.rerun()

if st.session_state["iniziato"] == False:
    if st.button("Place a bet"):
        bet()


if st.session_state["iniziato"] == True:
    
    try:
        st.text(f"The player has bet: {st.session_state['bet']}")
    except:
        pass


    playerCards: list[Card] = []
    botCards: list[Card] = []

    for i in range(2):
        playerCards.append(st.session_state["deck"].draw())
        botCards.append(st.session_state["deck"].draw())

    st.image([card.image for card in playerCards], width=card_width)
    st.image([card.image for card in botCards], width=card_width)

st.write(st.session_state)
