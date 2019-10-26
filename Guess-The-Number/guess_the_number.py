import random
print("Guess The Number!")
print("Rule 1: Guess until you can correctly guess the number!")
print("Rule 2: Guessed number must be in range of 1-10" )
print("Rule 3: FOLLOW RULE 1, 2 AND 3")
# print (random.randint(1,10))
a = random.randint(1,10)
b = int(input())
if a == b:
    print("You guessed the number!")
else :
    print("You lost! Try again")
if b > a:
    print("Your number is more than the actual number")
else:
    print("Your number is less than the actual number")
