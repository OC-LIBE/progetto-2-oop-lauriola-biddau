import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import HumanPlayer, Dealer

st.set_page_config(
   layout="wide",
)


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
    with st.form(f"Name and Bet", clear_on_submit=True, enter_to_submit=False, border=False):

        for i in range(numPlrs):
            name = st.text_input(f"Player{i+1} Name:")
            bet = st.number_input(f"Player{i+1} Bet:", min_value=1, max_value=500, value=50, step=50)

            st.session_state["PLAYERS"][i].name = name
            st.session_state["PLAYERS"][i].bet = bet

        if st.form_submit_button("Invia"):
            st.session_state["iniziato"] = True
            st.rerun()

if "PLAYERS" not in st.session_state:
    st.session_state["PLAYERS"] = []


if st.session_state["iniziato"] == False and "nPlayers" in st.session_state:

    for i in range(st.session_state["nPlayers"]):

        plr = HumanPlayer()
        st.session_state["PLAYERS"].append(plr)

    if st.session_state["PLAYERS"][0].bet == 0:  # first player is always okay to check because it always exists at this point
        bet(len(st.session_state["PLAYERS"]))


if "dealer" not in st.session_state:
    st.session_state["dealer"] = Dealer()


if st.session_state["iniziato"] == True:

    for i in range(2):
        for p in st.session_state["PLAYERS"]:
            p.hand.addCard(st.session_state["deck"].draw())
        st.session_state["dealer"].hand.addCard(st.session_state["deck"].draw())

    col = st.columns(len(st.session_state["PLAYERS"]), vertical_alignment="bottom", border=False)

    card_width = round(-35/36 * (len(st.session_state["PLAYERS"]) -1) **2 + 105)

    try:
        for i in range(len(st.session_state["PLAYERS"])):
            if i == len(st.session_state["PLAYERS"]) // 2:
                col[i].text("Dealer:")
                col[i].image([card.front_image for card in st.session_state["dealer"].hand.cards], width=card_width)

            col[i].write(st.session_state["PLAYERS"][i].name)
            col[i].image([card.front_image for card in st.session_state["PLAYERS"][i].hand.cards], width=card_width)
    except:
        pass

st.write(st.session_state)
