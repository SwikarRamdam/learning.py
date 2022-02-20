def newgame():
    guesses = []
    currect_guesses = 0
    questions_num = 1
    for keys in questions: #prints keys in a sequence as for is a loop
        print(keys)
        print("------------------------------------------------\n")
        for i in options[questions_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess) #key number is same here as well
        questions_num +=1
    display_score(correct_guesses,guess)

def check_answer(answer,guess):
    if answer==guess:
        print("Correct !")
        return 1
    else:
        print("Wrong !")
        return 0
    
#-------------------------------------------------

def display_score(correct_guesses,guess):
       print("------------------------------------------------\n")
       print("Results")
       print("------------------------------------------------\n")
       print("Answers :", end=" ")
       for i in questions:
           print(questions.get(i),end=" ")
       print("Guesses :")
       for i in guesses:
           print(i,end=" ")
    
       score = int((correct_guesses)/len(questions)*100)
       print("Your score : "+str(score)+ "%")

def play_again():
    play = input("Play Again? (yes,no)")
    if play=="yes":
        return True
    else:
        return False


questions = {       #dictionary
    "What is life ?" : "A",  #parameters before colon are called keys and those on the other side is known as value
    "Who is father of computer?" : "B",
    "Why is Nepal so beautiful?" : "C",
    "How are you?" : "D"
}

options =[ ["A.Don't know","B.You Know","C.Do you know?","D:Nobody knows"],
            ["A.Someone","B.Charles Babbage","C.Noone","D:Computer is a machine idiot"],
            ["A.Because it is","B.Swikar lives here","C.Natural Beauty","D:Haha"],
            ["A.Healthy","B.Young","C.Free","D:Good Enough"]
]
newgame()
while play_again():
    newgame()
print("Thank You")



# # -------------------------
# def new_game():

#     guesses = []
#     correct_guesses = 0
#     question_num = 1

#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)

#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1

#     display_score(correct_guesses, guesses)

# # -------------------------
# def check_answer(answer, guess):

#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0

# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")

#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()

#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()

#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")

# # -------------------------
# def play_again():

#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()

#     if response == "YES":
#         return True
#     else:
#         return False
# # -------------------------


# questions = {
#  "Who created Python?: ": "A",
#  "What year was Python created?: ": "B",
#  "Python is tributed to which comedy group?: ": "C",
#  "Is the Earth round?: ": "A"
# }

# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

# new_game()

# while play_again():
#     new_game()

# print("Byeeeeee!")