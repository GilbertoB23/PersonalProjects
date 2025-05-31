import random

# Generate a random number
# Loop
  # Ask the user to make a guess between 1 and 100
  # if not a valid number
  #   print an error
  # if guess > number
  #   print too high
  # if guess < number
  #   print too low
  # else
  #  print guess was correct

random_number = random.randint(1, 100)

while True:
  try:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > random_number:
      print("Too High!")
    elif guess < random_number:
      print("Too Low!")
    else:
      print("Congratulations! You guessed the number.")
      break
  except ValueError:
    print("Please enter a valid number")
