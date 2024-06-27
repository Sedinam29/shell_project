# %%
# Define a func that allows users to choose characters to play as
#     Display a message asking the user to enter their choice
#     While True:
#         Get the user's input and convert it to lowercase
#         If the user's input is in ['rock', 'paper', 'scissors', 'quit']:
#             Return the user's input
#         Else:
#             Display a message saying the input is invalid

# Define a function take_computer_choice:
#     Return a random choice from ['rock', 'paper', 'scissors']

# Define a function who_wins:
#     If the user's choice is the same as the computer's choice:
#         Return "It's a tie!"
#     Else If the user's choice beats the computer's choice:
#         Return "You win!"
#     Else:
#         Return "You lose!"

# Define a function play_round:
#     Call the function get_user_choice and store the result in user
#     If user is 'quit':
#         Return None
#     Call the function get_computer_choice and store the result in computer
#     Call the function who_wins with user and computer as arguments and store the result in result
#     Return a string that includes the user's choice, the computer's choice, and the result

# Define a function rps_game:
#     While True:
#         Call the function play_round and store the result in result
#         If result is None:
#             Break the loop
#         Print the result

# Call the function rps_game


# %%
import random

def take_character():
    """Let the user choose a character."""
    characters = {
        'rocky': {'favorite': 'rock', 'bonus': 0.1},
        'paperino': {'favorite': 'paper', 'bonus': 0.1},
        'scissorsly': {'favorite': 'scissors', 'bonus': 0.1}
    }
    print("\nChoose your character: Rocky, Paperino, or Scissorsly.")
    while True:
        character = input().lower()
        if character in characters:
            return f"Alright {character.capitalize()}! Let's go!", characters[character]
        else:
            print("Invalid character. Please choose Rocky, Paperino, or Scissorsly.")

def take_user_choice(character):
    """Get the user's choice."""
    print("\nEnter your choice (rock, paper, scissors) or 'quit' to stop.")
    while True:
        user = input().lower()
        if user in ['rock', 'paper', 'scissors', 'quit']:
            return user
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def take_computer_choice():
    """Get the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def who_wins(user, computer, character):
    """Determine the winner of a round."""
    if user == computer:
        return "It's a tie!"
    elif (user == character['favorite'] and computer != character['favorite'] and random.random() < character['bonus']) or \
         (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_round(character):
    """Play a round of rock, paper, scissors!"""
    user = take_user_choice(character)
    if user == 'quit':
        return None
    computer = take_computer_choice()
    result = who_wins(user, computer, character)
    return f"You chose {user}, and the computer chose {computer}. {result}"

def rps_game():
    """Play a game of rock, paper, scissors."""
    character = take_character()
    print(character[0])  # print the message for the chosen character
    while True:
        result = play_round(character[1])  # pass the character attributes to play_round
        if result is None:
            break
        print(result)

if __name__ == "__main__":
    rps_game()



# %%



