import requests
from ascii_logo import logo
from rich import print as rprint
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.layout import Layout
from rich import box
from rich.text import Text
import time
import sys
console = Console()
layout = Layout()

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
    "white on dark_red",
    "bold yellow on black",
    "bright_white on dark_red",
    "green on black",
    "black on white",
]
centered_logo = Align.center(logo[3], vertical="middle", style=styles[0])

def rich_print_logo():
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
                if len(guess_integers_list) == 4 and all(0 <= num <= 7 for num in guess_integers_list):
                    return guess_integers_list
                else:
                    print("Only Numbers between 0 and 7, Try again!")
                    continue
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
        rprint("Sorry to see you go :loudly_crying_face:")
        return False

def display_game(attempts,board=[],feedbacks=[]):
    game_layout = Layout()

    game_charts = Table(title="Game Session",border_style="red",title_style="bold magenta", header_style="blue",show_header=True, box=box.ROUNDED,expand=True)


    # game_charts.add_column("Attempts",justify="center",ratio=1)
    game_charts.add_column("Board",justify="center",ratio=1)
    game_charts.add_column("Feedback Board",justify="center",ratio=1)

    for i in range(len(board)):
        game_charts.add_row(str(board[i]),str(feedbacks[i]))

    game_layout.split_column(
        Layout(
            Panel(
                renderable=centered_logo,
                title="Welcome to Mastermind",
                box=box.ROUNDED,
                border_style="red",
                title_align="center",
                expand=True,
                padding=(2,2),


            ),
            name="upper",
            ratio=3,
            minimum_size=15,


        ),
        Layout(name="Game Board",ratio=5)
    )

    attempts_text = Text(str(attempts), justify='center',style="dark_red")
    difficulty_text = Text("Hard",justify="center",style="orange_red1")
    hints_text = Text("3/3",justify="center",style="green3")
    game_layout["Game Board"].split_row(
        Layout(name="left",ratio=2),
        # Layout(Panel.fit(attempts_text,style="yellow",title="Attempts Left",width=25,highlight=True,height=5),name="left",ratio=2),
        Layout(game_charts, name="right",ratio=6)
    )
    game_layout["left"].split_column(
        Layout(Panel(attempts_text,style="yellow",title="Attempts Left"),name="left",ratio=3),
        Layout(Panel(hints_text,style="bright_black",title="Hints Left"),name="center",ratio=3),
        Layout(Panel(difficulty_text,style="deep_pink2",title="Difficulty Level"),name="lower",ratio=3)
    )






    rprint(game_layout)


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
    while attempts <= max_attempts:
        print(sequence)
        attempts_left = max_attempts - attempts
        display_game(attempts=attempts_left,board=board,feedbacks=feedbacks)
        guess = get_players_guess()
        attempts += 1
        feedback = evaluate_players_guess(guess,sequence)
        # display_game()
        board.append(guess)
        feedbacks.append(list(feedback.values()))
        if all(value == 0 for value in feedback.values()):
            print("All numbers are incorrect")
        elif feedback["correct_location"] == 4:
            print("Woohooo, you have won")
            break
        # print("Session Details      "+"     Board    "+"     Feedback     ")
        # for i in range(len(board)):
        #     print(f"                     {board[i]}     " +   f"  Correct Numbers: {feedbacks[i][0]}, Correct Location: {feedbacks[i][1]}")
        # print(f"Attempts left {attempts_left}")
    else:
        print("Sorry you have failed.Better luck next time")


if __name__== "__main__":
    # display_game()
    play_game()
