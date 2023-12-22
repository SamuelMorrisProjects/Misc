from random import randint
guess=int(input("Guess the number I am thinking of its somewhere between 1-10: "))
x = randint(1,10)
while guess != x:
    print("Try again\n")
    guess=int(input("Guess the number I am thinking of its somewhere between 1-10: "))
print('You got it')
