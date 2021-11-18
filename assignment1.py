import random

user_choice = input('Would you like to roll the dice?')

while user_choice=='yes':
    print(random.randint(1,6))
    repeat = input('Would you like to roll again?')
    if repeat=='yes':
        continue
    else:
        print('Thank you for playing!')
        break
