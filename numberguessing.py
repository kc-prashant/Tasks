import random

attempts =5 # limit of attempt

random_num= random.randint(1,100) # to initialize random number form 1 to 100


for i in range(attempts): # start to check
    guess =int(input("Guess a number(1-100): "))

    if guess ==random_num :
     print( "Good you guessed it right!")
     break

    elif guess <random_num -10:
     print("Too low")

    elif guess >random_num +10:
        print("Too  High")

    elif guess <random_num :
        print(" close but low")

    elif guess >random_num :
        print("close but  High")

    if i== attempts -1:
        print("Game Over!")




