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
        nPlayers = st.number_input("Numero giocatori", min_value=1, max_value=50, value=1, label_visibility="hidden")

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
            for j in range(len(Names)):
                if Names[j] == "":
                    Names[j] = f"player{j+1}"
                st.session_state.game.addPlayer(Names[j])
            st.session_state.game.new_game()
            st.rerun()


if st.session_state.game.nPlayers != 0 and st.session_state.game.namesGiven == False:
    name(st.session_state.game.nPlayers)


@st.dialog("Bet")
def bet(player):
    with st.form(f"Bet", clear_on_submit=True, enter_to_submit=False, border=False):
        
        bettedAmount = st.number_input(f"Puntata {player.name}:", min_value=1, max_value=1000, value=50, step=50)

        if st.form_submit_button("Invia"):
            st.session_state.game.playerBet(player, bettedAmount)
            st.rerun()

try:
    col = st.columns(len(st.session_state.game.Players), vertical_alignment="bottom", border=True)


    for i in range(len(st.session_state.game.Players)):

        if i == len(st.session_state.game.Players) // 2:
            col[i].text("Dealer:")

            try:
                dealer_cards = []
                for j in st.session_state.game.dealer.hand.cards:
                    dealer_cards.append(j)

                last_card = dealer_cards.pop()
                last_card_image = None
                if st.session_state.game.playersDone == False:
                    last_card_image = last_card.back_image

                else:
                    last_card_image = last_card.front_image
                
                
                dealer_cards_images = [card.front_image for card in dealer_cards]
                dealer_cards_images.append(last_card_image)
                col[i].image(dealer_cards_images, width=st.session_state.game.card_width)
            except:
                pass
                
        col[i].write(f"{st.session_state.game.Players[i].name}:")
        try:
            col[i].image([card.front_image for card in st.session_state.game.Players[i].hand.cards], width=st.session_state.game.card_width)
        except:
            pass

        if st.session_state.game.Players[i].bet != 0:
            col[i].text(f"{st.session_state.game.Players[i].name} ha puntato: {st.session_state.game.Players[i].bet}")

        if st.session_state.game.Players[i].busted() == True:
            col[i].text(f"{st.session_state.game.Players[i].name} BUSTED")
        
        if st.session_state.game.Players[i].stood == True:
            col[i].text(f"{st.session_state.game.Players[i].name} STOOD")
except:
    pass


if st.session_state.game.bettingTime == True:
    for i in range(len(st.session_state.game.Players)):

        if st.session_state.game.Players[i].bet == 0:
            with col[i]:
                if st.button("Punta", key=f"betButton{i}"):
                    bet(st.session_state.game.Players[i])


elif st.session_state.game.bettingTime == False and st.session_state.game.namesGiven == True and st.session_state.game.playersDone == False:
    for i in range(len(st.session_state.game.Players)):
        
        if st.session_state.game.Players[i].busted() == False and st.session_state.game.Players[i].stood == False:
            with col[i]:
                if st.button("Hit", key=f"HitButton{i}"):
                    st.session_state.game.playerHit(st.session_state.game.Players[i])
                    st.rerun()
            
            with col[i]:
                if st.button("Stand", key=f"StandButton{i}"):
                    st.session_state.game.playerStand(st.session_state.game.Players[i])
                    st.rerun()


    playingPlayers = 0
    for i in range(len(st.session_state.game.Players)):
        if st.session_state.game.Players[i].stood == False and st.session_state.game.Players[i].busted() == False:
            playingPlayers += 1

    if playingPlayers == 0:
        st.session_state.game.dealerTurn()
        st.rerun()



st.write(st.session_state)
st.write(st.session_state.game.Players)
st.write(st.session_state.game.dealer)
