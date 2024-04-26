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
        print("\nplayer hand:")
        time.sleep(1)
        player_hand.append(hand_tuple)
        joined_player_hand = ' '.join(player_hand)
        player = player + card_value
        print(player,"\n")
        print(joined_player_hand)
    elif dealer_start == True:
        print("\n dealer hand:")
        time.sleep(1)
        dealer_hand.append(hand_tuple)
        joined_dealer_hand = ' '.join(dealer_hand)
        dealer = dealer + card_value
        print(dealer,"")
        print(joined_dealer_hand)

    if turn == "player":
        print("\nplayer hand:")
        player_hand.append(hand_tuple)
        joined_player_hand = ' '.join(player_hand)
        player = player + card_value
        print(player,"\n")
        print(joined_player_hand)
    elif turn == "dealer":
        print("\n dealer hand:")
        dealer_hand.append(hand_tuple)
        joined_dealer_hand = ' '.join(dealer_hand)
        dealer = dealer + card_value
        print(dealer,"\n")
        print(joined_dealer_hand)

dealer_start = True
dealer_hand.append("???\n")
card()
dealer_start = False

player_start = True
time.sleep(1)
card()
time.sleep(1)
card()
time.sleep(1)
player_start = False

ans = input("type 1 to hit, 0 to stand or 3 to double down")
while stand == False and player <= 21:
    turn = "player"
    time.sleep(1)
    if ans == "1":
        card()
        ans = input("type 1 to hit, 0 to stand")
    elif ans == "0":
        stand = True
    elif ans == "3":
        card()
        stand = True
    else:
        print("fel input")
    time.sleep(1)
if player > 21:
    print("Bust")
else:
    loose = False
    win = False
    time.sleep(1)
    print("dealer turn")
    while loose == False and win == False:
        turn = "dealer"
        dealer_start = True
        dealer_hand.remove("???\n")
        time.sleep(1)
        card()
        time.sleep(1)
        dealer_start = False
        card()
        time.sleep(1)
        if dealer > player and dealer <= 21:
            win = True
            print("Dealer win")
        if dealer > 21:
            loose = True
            print("You win")