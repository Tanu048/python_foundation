import random as rd 

def get_choice():
    player_choice= input("Enter your choice: ")
    choices=["rock", 'paper', 'sissors']
    # made a list here so that there is sumn to choose from 
    computer_choice= rd.choice(choices)
    options={"player":player_choice, "computer":computer_choice}
    # added a dictonary called options as python does not return multiple values and we want to return two values 
    return options 

def who_wins(player,computer):
    print(f"You choose: {player}, computer chooses: {computer}")
    if player==computer:
        print("It is a tie!!!")
        return 
    elif player=='rock':
        if computer=='paper':
            print('You loose!')
            return 
        elif computer=='sissors':
            print('You win!')
            return
    elif player=='paper':
        if computer=='rock':
            print('You win!')
            return
        elif computer=='sissors':
            print('You loose!')
            return
    elif player=='sissors':
        if computer=='rock':
            print('You loose!')
            return
        elif computer=='paper':
            print('You win!')
            return
        
choice=get_choice()
result=who_wins(choice["player"],choice["computer"])