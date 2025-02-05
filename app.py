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


if st.session_state.game.nPlayers != 0 and st.session_state.game.turn != 1:
    name(st.session_state.game.nPlayers)


if st.session_state.game.turn == 1:

    st.session_state.game.new_game()

    col = st.columns(len(st.session_state.game.Players), vertical_alignment="bottom", border=True)

    try:
        for i in range(len(st.session_state.game.Players)):
            if i == len(st.session_state.game.Players) // 2:
                col[i].text("Dealer:")
                dealer_uncovered_cards = st.session_state.game.dealer.hand.cards
                dealer_uncovered_cards.pop(len(dealer_uncovered_cards))
                last_card = st.session_state.game.dealer.hand.cards[len(st.session_state.game.dealer.hand.cards)]
                if len(st.session_state.game.dealer.hand.cards) > 2:
                    col[i].image([card.front])
                
            col[i].write(f"{st.session_state.game.Players[i].name}:")
            col[i].image([card.front_image for card in st.session_state.game.Players[i].hand.cards], width=st.session_state.game.card_width)
    except:
        pass

st.write(st.session_state)
st.write(st.session_state.game.Players)
st.write(st.session_state.game.dealer)