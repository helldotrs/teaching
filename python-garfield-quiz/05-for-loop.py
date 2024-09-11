#we're adding a bit of complexity here (a for-loop and a 2d list) but with result is code that is easier to use, as well as to add future functionality, for example, custom wordlists.

q_and_a_list = (
    ("what is garfields favorite food?", "lasagna")
    ("what day does garfield hate?", "monday")
)

score = 0

def ask_question(question, correct_answer):
    user_answer = input(question)
  
    if( user_answer.lower() == correct_answer):
        print("corret answer!")
        score += 1
    else:
        print("wrong answer :(")
      
    print("your current score is: " + str(score))

for sublist in q_and_a_list:
    ask_question(sublist[0], sublist[1]) #remember that the first item in a list is 0, this is due to legacy conventions


print("quiz complete!! your final score is: " + str(score))

"""not important for now: list of things to add:
empty
"""

#fixme: untested
