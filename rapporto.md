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
<br>

## 22.01.2025:
### aggiunte:
> Aggiunte le classi `HumanPlayer` e `Dealer` ereditarie di `Player` e la classe `Hand` incapsulata in `Player`.<br>
`HumanPlayer` contiene le informazioni sui giocatori come nome, soldi e la mano. La classe `Hand` permette di calcolare velocemente il valore della mano con la proprietà `score()` e di aggiungere una carta alla mano con `addCard()`.<br>
La classe `Dealer` eredita e possiede solamente `Hand`.

> Nel dialogo `bet()` si chiede anche il nome del giocatore oltre alla puntata.<br>

> Adesso viene visualizzato il nome di ogni giocatore, seguito dalle sue carte. Per primo c'è il dealer.<br>
Le carte vengono assegnate con un ciclo in `app.py` ai giocatori e al dealer.

> In st.session_state vengono salvati i giocatori con anche il loro nome, soldi, carte, che vengono visualizzate usando `short_rank` e `short_suit`, i due possibili valori della mano e la loro puntata.

### obiettivi:
> Trovare un migliore layout per la visualizzazione delle carte.

> Programmare le possibili azioni di gioco per i giocatori e per il dealer.
<br>

## 25.01.2025:
### aggiunte:
> Vengono create tante colonne quanti giocatori. Ogni colonna contiene il nome e le carte di uno dei giocatori.<br>
Le carte del Dealer vengono visualizzate in alto, dentro alla colonna in mezzo, che è calcolata con `len(st.session_state["PLAYERS"]) // 2`.

> Per garantire un buon layout, la variabile `card_width` non è più fissa a 105, ma dipende da una funzione di secondo grado:<br>
`-35/36 * x**2 + 105`<br>
dove il parametro x corrisponde al numero di giocatori (`len(st.session_state["PLAYERS"])`).

### obiettivi:
> Programmare le possibili azioni di gioco per i giocatori e per il dealer.
<br>

## 29.01.2025:
### aggiunte:
> Scaricata l'immagine per il retro della carta da <https://upload.wikimedia.org/wikipedia/commons/8/86/Carta_Francese_retro_Blu.jpg">
<br> e aggiornata la proprietà della classe Card "back_image", in modo da restituire l'immagine del retro.

> Aggiunto l'oggetto Game per coordinare tutti gli altri oggetti e comunicare con app.py per l'interfaccia grafica.

### note:
> Dato il cambiamento di struttura dovuto all'introduzione di Game, bisogna sistemare ancora molte cose, come la distribuzione delle carte.
<br>

## 05.02.2025:
### aggiunte:
> Metodo `new_game(self)` di `Game`, controlla la partita e chiama le funzionalità necessarie.

> La seconda carta del dealer viene visualizzata coperta.

### obiettivi:
> Programmare le possibili azioni di gioco per i giocatori e per il dealer.<br>
In particolare:<br>
- richiedere la puntata
- altre azioni (hit, stand, dubble down, split, insurance, surrender)

### dubbi:
> Come richiedere la puntata e l'azione a ciascun giocatore?<br>
Possibilità:<br>
- fare una grande form dove ognuno inserisce la propria puntata
- bottoni per indicare l'azione
- richiedere con un dialog a un giocatore alla volta cosa preferisce fare (opzione che sembra migliore per ora)
<br>

## 19.02.2025 (08:36):
### aggiunte:
> Metodo `playerBet(self, player, bettedAmount)` di `Game` che gestisce le puntate dei giocatori.<br>
Questo metodo viene chiamato da `app.py`, più precisamente dal dialog, la cui funzione è quella di visualizzare una form in cui si richiede al giocatore la puntata. Questo dialogo viene attivato dopo che un giocatore preme il proprio bottone `Puntata`.<br>
Questi bottoni sono visualizzabili da quando in `new_game(self)` avviene `self.bettingTime = True`.

> Con `app.py`, se un giocatore ha puntato, viene visualizzata la puntata sotto le proprie carte.

> in `playerBet(self, player, bettedAmount)`, `player.money -= bettedAmount` sottrae la puntata ai soldi del giocatore.

### obiettivi:
> Programmare le possibili azioni di gioco per i giocatori e per il dealer.<br>
In particolare:<br>
- hit, stand, dubble down, split, insurance, surrender
<br>

## 19.02.2025 (09:35):
### aggiunte:
> Adesso i giocatori possono fare `Hit` per mezzo di un bottone, che dà una carta al giocatore che lo preme.

> Una proprietà di HumanPlayer `busted` controlla se il giocatore ha superato 21. In quel caso, i bottoni delle azioni non vengono più visualizzati e si scrive `f"{player.nome} BUSTED"` nella colonna di tale giocatore.

### obiettivi:
> Programmare le funzionalità di `Stand`.

> Programmare le funzionalità del `Dealer`.

> Consegnare la vincita al giocatore vincente.

> Programmare la vittoria automatica del giocatore in caso di Blackjack.

> Programmare le altre possibili azioni di gioco per i giocaori.<br>
In particolare:
- dubble down
- split
- insurance
- surrender
<br>

## 26.02.2025 e 27.02.2025:
### aggiunte:
> Se un giocatore fornisce un nome vuoto, gli viene assegnato il nome di `f"player{j}"`, con j = numero del giocatore.

> Adesso i giocatori possono usare il bottone `Stand` quando non vogliono più pescare.

> Lo stato `playersDone` permette di capire quando mostrare la seconda carta del dealer.

> Il dealer pesca delle carte se la propria mano è inferiore a 17.

### obiettivi:
> Programmare il sistema per capire chi ha vinto e chi no e consegnare la vincita ai giocatori vincenti

> Cosa fare nel caso in cui un giocatore o il dealer ricevono due assi? --> aggiustare casi pesca per il dealer

> Programmare le altre possibili azioni di gioco per i giocaori.<br>
In particolare:
- dubble down
- split
- insurance
- surrender
<br>