#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define s = Character("Simona", color="#f44")

default found = False


# Il gioco comincia qui.

label start:

    # Mostra uno sfondo. Al momento mostra una sagoma generica, ma puoi
    # aggiungere un file (chiamato "bg room.png" oppure "bg room.jpg")
    # alla directory 'images' per cambiarla.


    scene bg room

    # Mostra lo sprite di un personaggio.
    # Al momento mostra una sagoma generica, ma puoi aggiungere un file
    # (chiamato "eileen_happy.png") alla directory 'images' per cambiarla.

    show miho summertime smile:
        xalign 0.5
        yalign 5

    # Questo mostra linee di dialogo.

    s "Oggi è un giorno speciale"

    "E per questo stanno per arrivare due regali molto speciali!"

    "Sei pronto?"

    menu:

        "Sì":
            jump continue

        "No":
            jump end


label continue:

    "Evviva!"

    "Rullo di tamburi"

    s "Però il primo te lo dovrai guadagnare! Muovi il mouse per cercare la spada misteriosa!"

    call screen swordScreen

label yeah:

    s "Ce l'hai fatta! Ora puoi combattere!"

    "Grazie per aver giocato!"

    return

label end:

    s "Oh, che peccato! Alla prossima!"

    return
