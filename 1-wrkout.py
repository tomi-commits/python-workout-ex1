

import random

#After taking a short stab at this I just did what was in the book
#the point was to read and see what the workouts are about. And see if I'll return to
#this tomorrow.


def guessing_game():
    answer = random.randint(0,100)

    while True:
            #using int inline, I wouldn't have done that on my own, would have
            #used another line to do that. less lines = better?.
            #I guess I should keep an eye on doing that in the future.
         user_guess = int(input('What is your guess?'))

         if user_guess == answer:
             print(f'Right! The answer is {user_guess}')
             break

         if user_guess < answer:
             print(f'Your guess of {user_guess} is too low!')
         else:
             print(f'Your guess of {user_guess} is too HIGH!')

guessing_game()
