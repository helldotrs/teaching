#by converting userinput to lower we make sure the answers match. otherwise "Lasanga" wont match with "lasanga"

score = 0

def ask_question(question, correct_answer):
    user_answer = input(question)
  
    if( user_answer.lower() == correct_answer):
        print("corret answer!")
        score += 1
    else:
        print("wrong answer :(")
      
    print("your current score is: " + str(score))


ask_question("what is garfields favorite food?", "lasagna")
ask_question("what day does garfield hate?", "monday")

print("quiz complete!! your final score is: " str(score))

"""not important for now: list of things to add:
read questions and answers from a list (2d list / dict / tuple)
"""

#fixme: untested
