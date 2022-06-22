import random
no = random.randint(1, 30)

name = input("Hello, Enter your name?")
no_of_guesses = 0
print('Hello '+ name+ ' Comp is Guessing a number between 1 - 30:')

while no_of_guesses < 3:
    guess = int(input())
    no_of_guesses += 1
    if guess < no:
        print('Guessed no is low')
    if guess > no:
        print('Guessed no is high')
    if guess == no:
        break
if guess == no:
    print('You guessed the number in ' + str(no_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(no))
