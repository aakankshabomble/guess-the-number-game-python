#  import library
import random

# welcome
print("welcome to number guessing game ... !")
# number
number = random.randint(1, 9)

print("choose the number between 1 to 9: ")


# type casting


# 3 chance
chance = 3
score = 0
while chance > 0:
    print(chance, "chance remaining . try your luck")

    # hint
    num = int(input())
    if num < number:
        # input form user(if else)
        print("number is too small")
        score = 0
    elif num > number:
        print("number is to big")
        score = 0
    elif num == number:
        score = 1
        break
    chance -= 1

# won or lose
if score == 0:
    print("better luck next time..")
    print("the number was ", number)
else:
    print("you won...!")












#TODOfinish
