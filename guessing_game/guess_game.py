import random as rd

print("\t\tTHE GUESSING GAME !!!")                             #\t is the same for a tab space

upper_bond=int(input("Enter a number:"))

if upper_bond>=0:                                        
    random_number=rd.randint(0,upper_bond)
else:
    print("Type an integer greater than 0 next time!")
    quit()                                                            # ends that program 

while True:
    user_input=input("make a guess: ")
    if user_input.isdigit():
        user_input=int(user_input)
        if user_input>=0:
            if user_input==random_number:
                print("You guessed it right, you win!!")
                break
            else:
                print("Not a match, make a choice again.")
                continue
    else:
        print("Type an integer greater than 0 next time!")   
