import requests
from ascii_logo import logo
from rich import print as rprint
from rich.console import Console
from rich.prompt import Prompt
import time
import sys
from rich.align import Align
console = Console()

URL = "https://www.random.org/integers/?"
PARAMS = {
    "num": 4,
    "min": 1,
    "max": 6,
    "col": 1,
    "base": 10,
    "format": "plain",
    "rnd": "new",
}

styles = [
    "white on blue",
    "bold yellow on black",
    "bright_white on dark_red",
    "green on black",
    "black on white",
]
def rich_print_logo():
    centered_logo = Align.center(logo, vertical="middle", style=styles[2])
    rprint(centered_logo)

def generate_random_sequence(url, params):
    response = requests.get(url, params)
    integer_list = [int(num) for num in response.text.strip().split()]
    return integer_list


def get_players_guess():
    while True:
        try:
            players_guess_input = input(
                "Please guess a combination of four numbers from 0 - 7 (no spaces): "
            )
            if len(players_guess_input) == 0:
                print("Input cannot be empty, You must crack the code!")
                continue
            elif len(players_guess_input) > 4:
                print("That is too many numbers, please input exactly Four numbers")
                continue
            elif len(players_guess_input) < 4:
                print("That is not enough numbers, please input exactly Four numbers")
                continue
            try:
                guess_integers_list = [int(num) for num in players_guess_input.strip()]
                if len(guess_integers_list) == 4 and all(
                    0 <= num <= 7 for num in guess_integers_list
                ):
                    return guess_integers_list
            except ValueError:
                print(
                    "Numbers only please: no extra spaces, or letters or special characters"
                )
        except KeyboardInterrupt:
            print("\nQuitting the game.....")
            break
        except Exception as error:
            rprint(f"An Unexpected Error has happened {error}")


def evaluate_players_guess(players_guess, generated_sequence):
    feedback = {"correct_numbers": 0, "correct_location": 0}
    players_set = set()
    for i in range(len(generated_sequence)):
        if players_guess[i] == generated_sequence[i]:
            feedback["correct_location"] += 1
    for i in range(len(generated_sequence)):
        if (
            players_guess[i] in generated_sequence
            and not players_guess[i] in players_set
        ):
            feedback["correct_numbers"] += 1
            players_set.add(players_guess[i])
    return feedback


def test_game():
    sequence = [0,1,3,5]
    players_guesses = [[2,2,4,6],[0,2,4,6],[2,2,1,1],[0,1,5,6]]
    for guess in players_guesses:
        feedback = evaluate_players_guess(guess,sequence)
        if all(value == 0 for value in feedback.values()):
            print("all incorrect")
        else:
            print(f"{feedback["correct_numbers"]}correct number"+"and" + f"{feedback["correct_location"]}correct location" )


def introduce_game():
    def slow_output(string, speed=0.01):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)

    intro_messages = [
        "Hi Welcome, to Mastermind!\n",
        "# Instructions\n",
        "1. Your task is to guess a 4 number combination\n",
        "2. You will get Feedback whether your numbers are correct and/or the location is correct\n",
        "3. You have a total of 10 Attempts\n",
        "4. Good luck and have fun\n",
    ]

    for message in intro_messages:
        slow_output(message)

    start_game = Prompt.ask("Would you like to start?", choices=["y", "n"], default="y")

    if start_game == "y":
        name = input("Awesome, What is your name? ")
        print(f"{name} is playing")
        return name
    else:
        rprint("[b]Sorry to see you go :loudly_crying_face:")
        return False


def play_game():
    rich_print_logo()
    players_name = introduce_game()
    if players_name is False:
        return
    sequence = generate_random_sequence(url=URL,params=PARAMS)
    max_attempts = 10
    attempts = 0
    board = []
    feedbacks = []
    while attempts < max_attempts:
        print(sequence)
        # print(f"Attempts Status: [{attempts}/{max_attempts}]")
        # print("This is the sequence", sequence)
        print(f"[       Attempts left: {max_attempts - attempts}     ]")
        guess = get_players_guess()
        feedback = evaluate_players_guess(guess,sequence)
        if all(value == 0 for value in feedback.values()):
            print("All numbers are incorrect")
        elif feedback["correct_location"] == 4:
            print("Woohooo, you have won")
            break
        board.append(guess)
        feedbacks.append(list(feedback.values()))
        print("Session Details      "+"     Board    "+"     Feedback     ")
        for i in range(len(board)):
            print(f"                     {board[i]}     " +   f"    {[feedbacks[i][0] ,feedbacks[i][1]]}")
        attempts += 1
    else:
        print("Sorry you have failed.Better luck next time")


if __name__== "__main__":
    play_game()
