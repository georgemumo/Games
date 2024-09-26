def check_score():
    correct_answer = 0
    my_answers=[]
    question_num= 1
    for key in quest:
        print("---------------------------------")
        print(key)
        for u in option[question_num-1]:
            print(u)
        guess = input("Enter either : A, B,C or D: ").upper()
        my_answers.append(guess)
        correct_answer += check_answer(quest.get(key),guess)
        question_num += 1
    display_score(correct_answer,my_answers)
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def display_score(correct_answer,my_answers):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")
    print("Correct Answer:", end=" ")
    for k in quest:
        print(quest.get(k),end=" ")

    print()
    print("Your answers:", end="")
    for u in my_answers:
        print(u, end=" ")
    print()

    score =int(correct_answer/len(quest)*100)

    print("Your average score is:" + str(score) + "%" )

def play_again():
    response = input("Would you like to play again? (Yes/No): ").upper()
    if response == "YES":
        return True
    else:
        return False

quest= {
    "What is the capital city of kenya": "C",
    "Who is the first president of kenya:? ": "B",
    "Who were the first people to invent an aeroplane:?": "A",

}

option = [
    ["A. Machackos", "B. Kisumu", "C. Nairobi", "D. Naivasha"],
    ["A. Daniel Moi", "B. Jomo Kenyatta","C.Pombe Magufuli","D. William Ruto"],
    ["A. The right brothers", "B. Elon Musk","C. Zack Zuckerbug","D. Alicia Kanini"]
]

check_score()
while play_again():
    check_score()
print("Thanks for playing!")

