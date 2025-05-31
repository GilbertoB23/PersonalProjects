import random

# Loop
  # Ask: roll the dice?
  # if user enters y
  #   Ask user how many dice they want to roll
  #   print them
  # if user enters n
  #   print thank you message
  #   terminate
  # else
  #   print invalid choice

total_dice_rolled = 0

while True:
  choice = input("Roll the dice? (y/n): ").lower()
  if choice == 'y':
    dice_amount = int(input("How many dice do you want to roll? "))
    total_dice_rolled += dice_amount
    for i in range(dice_amount):
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      print(f"({die1}, {die2},)")
  elif choice == 'n':
    print("Thank you for playing!")
    print(f"You rolled a total of {total_dice_rolled} dice")
    break
  else:
    print("Invalid Choice. Try again!")