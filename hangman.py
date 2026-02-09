
import random
names=["vamsi","charan","cherry"]
lives=6

choose_name= random.choice(names)
print(choose_name)

placeholder= ""
wordlength=len(choose_name)
for postion in range(wordlength):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]
while not game_over:
    guess= input(" Guess a letter from names:").lower()
    display= ""
    for letter in choose_name:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in choose_name:
        lives-=1
        if lives==0:
            game_over=True
            print("you loose the game")
    if "_" not in display:
        game_over=True
        print("You won the Game")

