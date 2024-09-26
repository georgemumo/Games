def new_game():
    guesses = []
    correct_answers = 0
    question_number = 1

    for key in questions:
        print("---------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_answers += check_answer(questions.get(key),guess)
        question_number += 1
    display_score(correct_answers,guesses )
# ========================
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

# ========================
def display_score(correct_answers,guesses):
    print("--------------------------------")
    print("RESULTS")
    print("-------------------------------- ")
    print("Correct Answers:", end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Your answers:", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = correct_answers/len(questions)*100
    print("Your score is :" + str(score) + "%")

# ========================
def play_again():
    response = input("Would you like to play again? (Yes/No): ").upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "B"
}
options = [
           ["A. Guido van Rossu", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python ","D. SNL"],
           ["A. True","B. False","C. Sometimes","D. None"]
           ]
new_game()
while play_again():
    new_game()
print("Thank you for playing!")