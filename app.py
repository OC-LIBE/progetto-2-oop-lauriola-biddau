import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player

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


@st.dialog("Number of players")
def players():
    with st.form("Players", clear_on_submit=True, enter_to_submit=False, border=False):
        nPlayers = st.number_input("Numero giocatori", min_value=1, max_value=7, value=1, label_visibility="hidden")

        if st.form_submit_button("Invia"):
            st.session_state["nPlayers"] = nPlayers
            st.session_state["deck"].shuffle()
            st.rerun()

if "nPlayers" not in st.session_state:
    if st.button("start"):
        players()


@st.dialog("Player place a bet")
def bet(numPlrs):
    with st.form(f"Bet", clear_on_submit=True, enter_to_submit=False, border=False):

        for i in range(numPlrs):

            bet = st.number_input(f"Player {i+1}:", min_value=1, max_value=500, value=10)
            st.session_state["PLAYERS"][i].bet = bet

        if st.form_submit_button("Invia"):
            st.session_state["iniziato"] = True
            st.rerun()

if "PLAYERS" not in st.session_state:
    st.session_state["PLAYERS"] = []

if st.session_state["iniziato"] == False and "nPlayers" in st.session_state:

    for i in range(st.session_state["nPlayers"]):
        plr = Player()
        st.session_state["PLAYERS"].append(plr)

    if st.session_state["PLAYERS"][0].bet == 0:  # first player is always okay to check
        bet(len(st.session_state["PLAYERS"]))


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
