import PySimpleGUI as sg
import random
import time

dealer = 0
player = 0
stand = False
turn = None
dealer_hand = []
player_hand = []
double_down = False
player_start = False
dealer_start = False

def card():
    global dealer
    global player
    global turn
    global dealer_hand
    global player_hand
    group = 0
    amount = 0
    card_value = 0
    card_name = None
    group_name = None
    group = random.randint(1,4)
    amount = random.randint(1,13)
    if group == 1:
        group_name = "Clubs"
    elif group == 2:
        group_name = "Diamonds"
    elif group == 3:
        group_name = "Hearts"
    elif group == 4:
        group_name = "Spades"
    
    if amount == 1:
        card_name = "Ace"
        if player + 11 > 21:
            card_value = 1
        elif player + 11 <= 21:
            card_value = 11
    elif amount == 2:
        card_name = "2"
        card_value = 2

    elif amount == 3:
        card_name = "3"
        card_value = 3
    elif amount == 4:
        card_name = "5"
        card_value = 5
    elif amount == 5:
        card_name = "5"
        card_value = 5
    elif amount == 6:
        card_name = "6"
        card_value = 6
    elif amount == 7:
        card_name = "7"
        card_value = 7
    elif amount == 8:
        card_name = "8"
        card_value = 8
    elif amount == 9:
        card_name = "9"
        card_value = 9
    elif amount == 10:
        card_name = "10"
        card_value = 10
    elif amount == 11:
        card_name = "Jack"
        card_value = 10
    elif amount == 12:
        card_name = "Queen"
        card_value = 10
    elif amount == 13:
        card_name = "King"
        card_value = 10

    hand = (card_name, "of", group_name,"\n")
    hand_tuple = ' '.join(str(item) for item in hand)

    if player_start == True:
        joined_player_hand = ' '.join(hand_tuple)
        player_hand.append(joined_player_hand)
        player = player + card_value
      
    elif dealer_start == True:
        dealer_hand.append(hand_tuple)
        joined_dealer_hand = ' '.join(dealer_hand)
        dealer_hand.append(joined_dealer_hand)
        dealer = dealer + card_value

    if turn == "player":
        player = player + card_value
        player_hand.append(hand_tuple)

dealer_start = True
dealer_hand.append("???")
card()
d_show = ' '.join(dealer_hand)
dealer_start = False

player_start = True
card()
card()
p_start = ' '.join(player_hand)
player_start = False



def blackjack_window():
    sg.theme("neonyellow1")
    layout = [
        [sg.Text(
            "...",
            justification  = "right",
            expand_y = True,
            font="franklin 20",
            key="-D_SCORE-")
        ],
        [sg.Text(
            "...",
            # pad=((10, 350), (100, 10)),
            font="franklin 30",
            expand_x = True,
            key="-D_TEXT-")
        ],
        [sg.Text(
            "...",
            justification  = "right",
            expand_y = True,
            font="franklin 20",
            key="-SCORE-")
        ],
        [sg.Text(
            p_start,
            # pad=((10, 350), (100, 10)),
            font="franklin 30",
            expand_x = True,
            key="-TEXT-")
        ],
        [sg.Button("Hit", size=(12,2)), sg.Button("Stand", size=(12,2)), sg.Button("Double", size=(12,2))],
    ]
    return sg.Window("blackjack", layout, size=(500,400), element_justification='c')

window = blackjack_window()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Hit":
        turn = "player"
        card()
        show_player_hand = ' '.join(player_hand)
        window["-TEXT-"].update(show_player_hand)
        window["-SCORE-"].update(player)
        print(show_player_hand)
        print(show_player_hand)
    
    if event == "Stand":
        turn = "dealer"
window.close()

