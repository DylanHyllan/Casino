import random
dealer = 0
player = 0
stand = False
turn = None
dealer_hand = []
player_hand = []

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
    
    if turn == "player":
        hand = ("You got", card_name, "of", group_name)
        player_hand.append(hand)
        ' '.join(player_hand)
        player = player + card_value
        print(player)
    elif turn == "dealer":
        hand = ("Dealer got", card_name, "of", group_name)
        dealer_hand(hand)
        ' '.join(dealer_hand)
        dealer = dealer + card_value
        print(dealer)

while stand == False and player <= 21:
    turn = "player"
    ans = input("type 1 to hit or 0 to stand")
    if ans == "1":
        card()
    elif ans == "0":
        stand = True
if player > 21:
    print("You lost")
elif player == 21:
    print("you win")
else:
    loose = False
    win = False
    print("dealer turn")
    while loose == False and win == False:
        turn = "dealer"
        card()
        if dealer > player and dealer <= 21:
            win = True
            print("You lost")
        if dealer > 21:
            loose = True