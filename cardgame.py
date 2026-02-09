import random
def deck_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare

user_card=[]
computer_card=[]
computer_score=-1
user_score=-1
game_over=False

for _ in range(2):
    user_card.append(deck_cards())
    computer_card.append(deck_cards())
while not game_over:
    user_score=calculate_score(user_card)
    computer_score= calculate_score(computer_card)
    print(f"your cards: {user_card} , currentscore: {user_score}")
    print(f"computer first cards: {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score>21:
        game_over= True
    else:
        user_choice=input("type 'y' to get another card, type 'n' to pass:")
        if user_choice=="y":
            user_card.append(deck_cards())
        else:
            game_over= True
while computer_score!=0 and computer_score<17:
    computer_card.append(deck_cards())
    computer_score=calculate_score(computer_card)
    