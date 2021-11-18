import random

number = random.randint(1,100)

play = input('Would you like to guess a number between 1 and 100? ')

while play=='yes':
    try:
        user_choice = int(input('Guess a number between 1 and 100: '))
        if user_choice > number:
            print('The number is lower than your guess')
            again = input('Would you like to guess again?')
            if again=='yes':
                continue
            else:
                break
        elif user_choice<number:
            print('The number is higher than your guess')
            again = input('Would you like to guess again?')
            if again=='yes':
                continue
            else:
                break
        else:
            print("Congratulations, that's the correct number!")
            break
    except:
        print('You must enter an integer number!')
        continue

print('Thanks for playing!')