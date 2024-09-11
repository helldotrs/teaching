#By converting the score from int (positive whole number) to string (text) we can now combine it in the same print statement without mixing types. 
#Notice that in programming*, 7 written as such is a number while "7" written as such is a text. hence 7+7 --> 14, "7"+"7" --> "77"
#*any exceptions to this are in garbage programming languages that should for the better part be disregarded

score = 0

def ask_question(question, correct_answer):
    user_answer = input(question)
  
    if( user_answer == correct_answer):
        print("corret answer!")
        score += 1
    else:
        print("wrong answer :(")
      
    print("your current score is: " + str(score))


ask_question("what is garfields favorite food?", "lasagna")
ask_question("what day does garfield hate?", "monday")

print("quiz complete!! your final score is: " str(score))

"""not important for now: list of things to add:
lower(input())
read questions and answers from a list (2d list / dict / tuple)
"""

#fixme: untested
