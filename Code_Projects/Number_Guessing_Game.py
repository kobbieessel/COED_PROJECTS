from random import randint
from emoji import emojize

#Variable declaration
number = randint(1,10) # Randomly generates a number between 1 and 10
attempt = 5  # Number of attempts the player has to guess the correct number
isPlay = True # Boolean flag to determine if the game should continue
score = 0; # Keeps track of the player's score

# Initial message to the player explaining the game
print(f"\nWelcome to the Guessing Game!\n\nI'm thinking of a number between 1 and 10.\nYou have {attempt} attempts to guess the correct number\nGood luck!\n")

# this function checks the user's guessed number
def user_guess(user):
  global attempt, isPlay, score, number

   # If the guessed number matches the target number
  if user == number:
    print(f"\n{emojize(":face_with_tears_of_joy:")} {emojize(":face_with_tears_of_joy:")} {emojize(":face_with_tears_of_joy:")} Congratulations! {emojize(":face_with_tears_of_joy:")} {emojize(":face_with_tears_of_joy:")} {emojize(":face_with_tears_of_joy:")}\nYou guessed it!\nThe number was {number}\n")
    score += 5 # Increases the player's score by 5
    
     # Ask if the player wants to play again
    ans = input("Do you want to play again (y/n): ")
    if ans == "y":
      number = randint(1,10) # Generates a new random number
      attempt = 5  # Resets attempts
      print("\n")
          
    else:
      isPlay = False # Ends the game if the player chooses not to play again
      print(f"You have {attempt} attempts left.\n")
      print(f"-------------------------------End Game--------------------------------")

  # Checks if the guessed number is lower than the target number
  elif (user < number):
    print(f"Too low!"  + emojize(":down_arrow:") + "\n")
    attempt -= 1 # Decrease the number of attempts left

  # Checks if the guessed number is higher than the target number
  elif (user > number):
    print(f"Too high!" + emojize(":up_arrow:") + "\n")
    attempt -= 1
  
# Game loop that continues as long as the player has attempts and chooses to keep playing
while isPlay:
  print("live:", emojize(":pizza:") * attempt) # Displays the number of lives left with pizza emoji
  print(f"score:", score, "\n") # Displays the player's current score
  try:
    user = int(input("Please enter your guess: ")) # Prompts the user for a guess
    user_guess(user) # Calls the user_guess function to evaluate the guess

    # If attempts run out, end the current game and ask to play again
    if attempt == 0:
      print(f"You have {attempt} attempts left.\n")
      print(f"-------------------------------Game Over!--------------------------------\nThe correct number was {number}.\nWould you like to play again? (y/n): ")
      play = input().lower()
      number = randint(1,10) # Generates a new random number
      print("\n")

      if play == "n" or play == "no":
        print("Game ended\n")
        break  # Exits the game loop

      else:
        attempt = 5 # Resets attempts if the player wants to play again
  
  # Handles non-numeric input errors
  except ValueError:
    print("\nCheck your input and try again.\nOnly enter numbers.\n")