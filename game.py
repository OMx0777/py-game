import random
import sys
import time
import string
def play_number_guessing_game():
    print("\n--- Starting Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts. 🎉")
                guessed_correctly = True
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\n--- Number Guessing Game Over ---\n")

def play_hangman():
    words = ["PYTHON", "PROGRAMMING", "DEVELOPER", "COMPUTER", "CHALLENGE", "GEMINI", "CODING", "ALGORITHM"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 7

    print("\n--- Starting Hangman Game ---")
    print("Welcome to Hangman!")
    print("Try to guess the secret word letter by letter.")

    def display_word_state():
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word_state()}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not 'A' <= guess <= 'Z':
            print("Invalid input. Please enter a single letter from A-Z.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        elif guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)
            incorrect_guesses += 1

        if "_" not in display_word_state():
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word} 🎉")
            break
    else:
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {secret_word}")

    print("\n--- Hangman Game Over ---\n")

def play_tic_tac_toe():
    print("\n--- Starting Tic-Tac-Toe ---")
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False

    def print_board():
        print(f"\n {board[0]} | {board[1]} | {board[2]}")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]}")

    def check_win(player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for condition in win_conditions:
            if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
                return True
        return False

    def check_draw():
        return ' ' not in board

    while not game_over:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = current_player
                if check_win(current_player):
                    print_board()
                    print(f"\n🎉 Player {current_player} wins! Congratulations! 🎉")
                    game_over = True
                elif check_draw():
                    print_board()
                    print("\nIt's a draw! Good game. 🤝")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Please choose an empty spot between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\n--- Tic-Tac-Toe Over ---\n")

def play_rock_paper_scissors():
    print("\n--- Starting Rock, Paper, Scissors ---")
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    rounds = 3

    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        player_choice = ""
        while player_choice not in choices:
            player_choice = input("Choose rock, paper, or scissors: ").lower()
            if player_choice not in choices:
                print("Invalid choice. Please choose rock, paper, or scissors.")

        computer_choice = random.choice(choices)
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round! 🤖")
            computer_score += 1

    print("\n--- Final Score ---")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print("Overall Winner: You! Congratulations! 🥳")
    elif computer_score > player_score:
        print("Overall Winner: Computer! Better luck next time. 😅")
    else:
        print("It's an overall tie! �")
    print("\n--- Rock, Paper, Scissors Over ---\n")

def play_dice_rolling_simulator():
    print("\n--- Starting Dice Rolling Simulator ---")
    while True:
        roll = input("Roll the dice? (yes/no): ").lower()
        if roll == 'yes':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"You rolled: {dice1} and {dice2}. Total: {dice1 + dice2} 🎲")
            time.sleep(0.5)
        elif roll == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print("\n--- Dice Rolling Simulator Over ---\n")

def play_coin_flip_simulator():
    print("\n--- Starting Coin Flip Simulator ---")
    while True:
        flip = input("Flip the coin? (yes/no): ").lower()
        if flip == 'yes':
            result = random.choice(['Heads', 'Tails'])
            print(f"The coin landed on: {result}! 🪙")
            time.sleep(0.5)
        elif flip == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print("\n--- Coin Flip Simulator Over ---\n")

def play_mad_libs():
    print("\n--- Starting Mad Libs ---")
    print("Let's create a silly story!")

    noun1 = input("Enter a noun (person, place, thing): ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    noun_plural = input("Enter a plural noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")

    story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}.
    Every day, they would go to the park and {verb_ing} with {noun_plural}.
    One day, a wild {color} {animal} appeared and joined the fun!
    It was the most unexpected adventure ever.
    """
    print(story)
    print("\n--- Mad Libs Over ---\n")

def play_simple_quiz_game():
    print("\n--- Starting Simple Quiz Game ---")
    questions = [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Rome"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter"], "answer": "B"},
        {"question": "What is 2 + 2?", "options": ["A. 3", "B. 4", "C. 5"], "answer": "B"}
    ]
    score = 0

    for i, q_data in enumerate(questions):
        print(f"\nQuestion {i+1}: {q_data['question']}")
        for option in q_data['options']:
            print(option)
        
        user_answer = input("Your answer (A, B, or C): ").upper()
        if user_answer == q_data['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Incorrect. ❌ The correct answer was {q_data['answer']}.")

    print("\n--- Quiz Results ---")
    print(f"You got {score} out of {len(questions)} questions correct! 🎉")
    print("\n--- Simple Quiz Game Over ---\n")

def play_higher_lower():
    print("\n--- Starting Higher or Lower ---")
    print("Guess if the next card will be higher or lower than the current one.")
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    rank_values = {rank: i for i, rank in enumerate(ranks)}

    current_card_rank = random.choice(ranks)
    current_card_suit = random.choice(suits)
    current_card_value = rank_values[current_card_rank]

    player_score = 0
    num_rounds = 3

    for _ in range(num_rounds):
        print(f"\nCurrent Card: {current_card_rank} of {current_card_suit}")
        guess = ""
        while guess not in ['higher', 'lower']:
            guess = input("Will the next card be 'higher' or 'lower'? ").lower()
            if guess not in ['higher', 'lower']:
                print("Invalid input. Please type 'higher' or 'lower'.")

        next_card_rank = random.choice(ranks)
        next_card_suit = random.choice(suits)
        next_card_value = rank_values[next_card_rank]

        print(f"Next Card: {next_card_rank} of {next_card_suit}")

        if guess == 'higher':
            if next_card_value > current_card_value:
                print("Correct! 🎉")
                player_score += 1
            elif next_card_value == current_card_value:
                print("It's a tie! No score change.")
            else:
                print("Incorrect. 😔")
        elif guess == 'lower':
            if next_card_value < current_card_value:
                print("Correct! 🎉")
                player_score += 1
            elif next_card_value == current_card_value:
                print("It's a tie! No score change.")
            else:
                print("Incorrect. 😔")
        
        current_card_rank = next_card_rank
        current_card_suit = next_card_suit
        current_card_value = rank_values[current_card_rank]

    print(f"\n--- Game Over! Final Score: {player_score} out of {num_rounds} ---")
    print("\n--- Higher or Lower Over ---\n")

def play_guess_the_word():
    print("\n--- Starting Guess the Word ---")
    words = ["APPLE", "BANANA", "CHERRY", "DATE", "GRAPE"]
    secret_word = random.choice(words)
    attempts = 0
    max_attempts = 5

    print(f"I'm thinking of a fruit. It has {len(secret_word)} letters.")
    print(f"You have {max_attempts} attempts to guess the whole word.")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Guess the word: ").upper()
        attempts += 1

        if guess == secret_word:
            print(f"🎉 Congratulations! You guessed the word '{secret_word}' in {attempts} attempts. 🎉")
            break
        else:
            print("That's not it. Keep trying!")
    else:
        print(f"Game Over! You ran out of attempts. The word was '{secret_word}'. 😔")
    print("\n--- Guess the Word Over ---\n")

def generate_password():
    print("\n--- Starting Password Generator ---")
    
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 6:
            print("Password should be at least 6 characters long for security.")
            length = 6
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        
        if not characters:
            print("You must select at least one character type. Using all by default.")
            characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))
        print(f"Your generated password: {password}")
    except ValueError:
        print("Invalid length. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("\n--- Password Generator Over ---\n")


def play_text_adventure():
    print("\n--- Starting Text Adventure ---")
    print("You are in a dark forest. There are two paths: left and right.")
    
    current_location = "forest_start"
    inventory = []

    while True:
        if current_location == "forest_start":
            print("\nYou are at the start of a dark forest. Which way do you go?")
            choice = input("Type 'left', 'right', or 'look' (or 'quit'): ").lower()
            if choice == 'quit':
                break
            elif choice == 'left':
                current_location = "dark_cave"
            elif choice == 'right':
                current_location = "sunny_meadow"
            elif choice == 'look':
                print("You see tall, ancient trees and hear the distant sound of water.")
            else:
                print("Invalid choice. Try again.")
        
        elif current_location == "dark_cave":
            print("\nYou entered a dark cave. It smells damp and earthy. There's a faint glimmer deeper inside.")
            choice = input("Type 'go deeper', 'go back', or 'look' (or 'quit'): ").lower()
            if choice == 'quit':
                break
            elif choice == 'go deeper':
                print("You carefully walk deeper into the cave...")
                if "torch" in inventory:
                    print("With your torch, you see a sparkling treasure chest! You found the treasure! 💰")
                    print("--- You Win! ---")
                    break
                else:
                    print("It's too dark to see anything! You stumble and hit your head. Ouch! You must go back.")
                    current_location = "dark_cave"
            elif choice == 'go back':
                current_location = "forest_start"
            elif choice == 'look':
                print("The cave walls are rough. You wish you had a light source.")
            else:
                print("Invalid choice. Try again.")

        elif current_location == "sunny_meadow":
            print("\nYou arrive in a sunny meadow. Birds are singing, and there's a small stream.")
            if "torch" not in inventory:
                print("Near the stream, you see a discarded but still functional torch. You pick it up.")
                inventory.append("torch")
                print("Torch added to your inventory!")
            print("What do you do?")
            choice = input("Type 'cross stream', 'go back', or 'look' (or 'quit'): ").lower()
            if choice == 'quit':
                break
            elif choice == 'cross stream':
                print("You safely cross the stream. On the other side, you see nothing but more forest.")
                print("Maybe you should head back to the start and explore the cave with your new torch?")
            elif choice == 'go back':
                current_location = "forest_start"
            elif choice == 'look':
                print("The meadow is peaceful. You feel a gentle breeze.")
                if "torch" in inventory:
                    print("You have a torch in your hand.")
            else:
                print("Invalid choice. Try again.")
        
    print("\n--- Text Adventure Over ---\n")


def main_game_selector():
    games = {
        '1': ("Number Guessing Game", play_number_guessing_game),
        '2': ("Hangman", play_hangman),
        '3': ("Tic-Tac-Toe", play_tic_tac_toe),
        '4': ("Rock, Paper, Scissors", play_rock_paper_scissors),
        '5': ("Dice Rolling Simulator", play_dice_rolling_simulator),
        '6': ("Coin Flip Simulator", play_coin_flip_simulator),
        '7': ("Mad Libs", play_mad_libs),
        '8': ("Simple Quiz Game", play_simple_quiz_game),
        '9': ("Higher or Lower", play_higher_lower),
        '10': ("Guess the Word", play_guess_the_word),
        '11': ("Password Generator", generate_password),
        '12': ("Text Adventure", play_text_adventure)
    }

    while True:
        print("\n" + "="*40)
        print("🎮 Welcome to the Expanded Game Hub! 🎮")
        print("="*40)
        print("Please choose a game to play:")
        
        for key, value in games.items():
            print(f"{key}. {value[0]}")
        
        print("13. Exit")
        print("="*40)

        choice = input("Enter your choice (1-13): ")

        if choice in games:
            game_function = games[choice][1]
            game_function()
        elif choice == '13':
            print("\nThanks for playing! Goodbye! 👋")
            sys.exit()
        else:
            print("\nInvalid choice. Please enter a number from the list.")
        
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main_game_selector()
