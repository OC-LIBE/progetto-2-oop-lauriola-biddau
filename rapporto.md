# Rapporto

## 08.01.2025:
>Blackjack

>importate le immagini delle carte

>creata la variabile dei soldi del giocatore
>creato l'input per scegliere la puntata
    
>stampate le carte pescare per giocatore e bot
<br>

## 09.01.2025:
### aggiunte:
>Puntata:<br>
un bottone chiamato "place a bet" apre un @st.dialog con una st.form che richiede una puntata usando st.numer_input() e st.form_submit_button. La puntata viene salvata in st.session_state sotto la chiave "bet", che viene utilizzata per stampare la puntata, processo per il quale viene usato un blocco try perché all'inizio la chiave "bet" non è ancora stata creata e cercandola in st.session_state si crea un errore.

### debug:
>playerCards è una lista quindi si usa append<br>
`playerCards.append(deck.draw())`

>tolta la variabile dei soldi del giocatore perché inutile per ora
<br>

## 10.01.2025:
### aggiunte:
> usato st.session_state per memorizzare se la partita è iniziata o no con la chiave 'iniziato' e il mazzo con la chiave 'deck'. Il motivo è quello di poter controllare cosa viene riaggiornato e cosa no ogni volta che avviene un'interazione e quindi una rerun. In questo modo il mazzo non viene rimescolato ogni volta. Per accedere al mazzo corrente conviene quindi fare: <br> `st.session_state["deck"]`<br>e continuare da lì.

> Adesso è possibile iniziare la partita subito piazzando una puntata. Questa, una volta fatta, viene memorizzata (lo scopo e quello di aggiungerla o di toglierla ai soldi del giocatore più avanti) e vengono pescate due carte.

>Per ora vengono mostrate anche le carte del bot, più avanti questo non dovrà essere il caso. Le carte assegnate ai giocatori vengono salvate sotto `playerCards`, rispettivamente, `botCards`.

### note:
> i commenti<br>`# st.session_state["iniziato"] = False`<br>`# st.session_state["deck"] = Deck(1)`<br>
servono per rapidamente resettare il session_state. Più avanti bisognerà automatizzare questo processo.
<br>

## 15.01.2025:
### aggiunte:
> Aggiunto il modulo `player.py` con la classe `Player`. un oggetto `Player` ha come attributi i propri soldi, la propria puntata e le proprie carte.

> Un bottone "Start" apre un `st.dialog` con una `st.form` che chiede il numero di giocatori (min 1, max 7).<br>
Da questa `st.form` si salva il numero di giocatori e si mescola il mazzo.

> Si creano gli oggetti `Player`, che verranno salvati con i loro attributi in `st.session_state["PLAYERS"]` e si apre un st.dialog con una st.form in cui vanno inserite le puntate dei giocatori, salvate in `st.session_state["PLAYERS"]` sotto i rispettivi giocatori.
