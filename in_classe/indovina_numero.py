import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
#print(random_number)

# Insert your guess

N = 6

vinto = False
for i in range(N):
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess == random_number:
        print("Congratulations! You guessed the number.")
        vinto = True
        break
    elif guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
if not vinto:
    print("Game over! The number was:", random_number)
