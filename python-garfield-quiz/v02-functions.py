score = 0

def ask_question(question, correct_answer):
    user_answer = input(question)
  
    if( user_answer == correct_answer):
        print("corret answer!")
        score += 1
    else:
        print("wrong answer :(")
      
    print("your current score is: ")
    print(score)


ask_question("what is garfields favorite food?", "lasagna")
ask_question("what day does garfield hate?", "monday")

print("quiz complete!! your score is: ")
print(score)

"""not important for now: list of things to add:
str(score)
lower(input())
read questions and answers from a list (2d list / dict / tuple)
"""

#fixme: untested
