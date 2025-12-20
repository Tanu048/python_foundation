print("\n\t\t\t* WELCOME TO THE QUIZ *\n------------------------------------------------------------")

play=input("Do you wanna play?\n(Yes/No) ")
if play.lower()!="yes":
    quit()
else: 
    ans = ("mars","au","pacific ocean","rabindranath tagore","japan")
    question = ("01.Which planet is known as the 'Red Planet'?","02.What is the chemical symbol for gold?","03.Which is the largest ocean on Earth?","04.Who wrote the Indian national anthem?","05.Which country is known as the \"Land of the Rising Sun\"?")
    i=0
    score=0
    while i<len(question):
        print(question[i])
        answer=input(" Enter answer: ")
        if answer.lower()==ans[i]:
            score+=1
            print("\t\tcorrect answer!")
            
        else:
            print("\t\t wrong answer!")
            
        i+=1
    print(f"\n------------------------------------------------------------\n\n\tYour final score is: {score}\n")