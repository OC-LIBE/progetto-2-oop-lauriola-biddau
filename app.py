import streamlit as st
from modules.game import Game

st.set_page_config(
   layout="wide",
)
if "game" not in st.session_state:
    st.session_state.game = Game()


@st.dialog("Number of players")
def players():
    with st.form("Players", clear_on_submit=True, enter_to_submit=False, border=False):
        nPlayers = st.number_input("Numero giocatori", min_value=1, max_value=7, value=1, label_visibility="hidden")

        if st.form_submit_button("Invia"):

            st.session_state.game.nPlayers = nPlayers
            st.session_state.game.deck.shuffle()
            st.rerun()

if st.session_state.game.nPlayers == 0:
    if st.button("start"):
        players()


@st.dialog("Players' name")
def name(numPlrs):
    with st.form(f"Name", clear_on_submit=True, enter_to_submit=False, border=False):

        Names = []
        for i in range(numPlrs):
            name = st.text_input(f"Player{i+1} Name:")
            Names.append(name)

        if st.form_submit_button("Invia"):
            for n in Names:
                st.session_state.game.addPlayer(n)
            st.session_state.game.turn = 1
            st.rerun()


if st.session_state.game.nPlayers != 0:
    name(st.session_state.game.nPlayers)


if st.session_state.game.turn == 1:

    for i in range(2):
        for p in st.session_state["PLAYERS"]:
            p.hand.addCard(st.session_state["deck"].draw())
        st.session_state["dealer"].hand.addCard(st.session_state["deck"].draw())

    col = st.columns(len(st.session_state["PLAYERS"]), vertical_alignment="bottom", border=True)

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
