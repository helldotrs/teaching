#note that until version 04, the answers are case sensitive, so "Lasagna" wont match with "lasagna" 

score = 0

if( input("what is garfields favorite food?") == "lasagna"):
    score += 1
    print("correct!")
else:
    print("wrong :(")

if( input("what day does garfield hate?") == "monday"):
    score += 1
    print("correct!")
else:
    print("wrong :(")

print("quiz complete!! your score is: ")
print(score)

"""not important for now: list of things to add:
ask question function
str(score)
lower(input())
read questions and answers from a list (2d list / dict / tuple)
"""

#fixme: untested
#mvp --> minimal viable product
