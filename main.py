import requests
from logos import logo,win_logo,lose_logo
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
console = Console()

URL = "https://www.random.org/integers/?"
PARAMS = {
    "num": 4,
    "min": 0,
    "max": 7,
    "col": 1,
    "base": 10,
    "format": "plain",
    "rnd": "new",
}

centered_intro_logo = Align.center(logo, vertical="middle", style='white on dark_red')
centered_win_logo = Align.center(win_logo, vertical="middle", style='white on green')
centered_lose_logo = Align.center(lose_logo, vertical="middle", style='bold yellow on black')


def generate_random_sequence(url, params):
    response = requests.get(url, params)
    integer_list = [int(num) for num in response.text.strip().split()]
    return integer_list


def get_players_guess(difficulty_level,current_hint,max_hints,previous_hints,give_hint,sequence):
    while True:
        try:
            players_guess_input = input(
                f"Please guess a combination of four numbers from 0 - {difficulty_level} (no spaces): "
            )

            if players_guess_input.lower() == 'hint':
                if max_hints > 0:
                    hint = give_hint(sequence,previous_hints)
                    if hint is not None:
                        previous_hints.append(hint)
                        current_hint = f"There is a {str(hint)} in the sequence somewhere"
                        print(current_hint)
                        max_hints -= 1
                else:
                    print("No hints left")
                continue
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
                    0 <= num <= difficulty_level for num in guess_integers_list
                ):
                    return guess_integers_list, current_hint, max_hints
                else:
                    print(f"Only Numbers between 0 and {difficulty_level}, Try again!")
                    continue
            except ValueError:
                print(
                    "Numbers only please: no extra spaces, or letters or special characters"
                )
        except KeyboardInterrupt:
            print("\nQuitting the game.....")
            break
        except Exception as error:
            print(f"An Unexpected Error has happened {error}")


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

def introduce_game():
    def slow_output(string, speed=0.01):
        for char in string:
            console.print(char, end="", highlight=True)
            time.sleep(speed)

    intro_messages = [
        "Hi Welcome, to Mastermind!\n",
        "# Instructions\n",
        "1. Your task is to guess a 4 number combination\n",
        "2. You will get feedback on your correct numbers and if the locations are correct\n",
        "3. You have a total of 10 Attempts\n",
        "4. The secret sequence can have duplicate numbers\n"
        "5. The higher the difficulty the higher number range you need to guess *(Easy is from 0 to 7 for a single number)\n"
        "6. You can use 'HINT' or 'hint', to print out a hint. But you only get 2 hints.\n"
        "Good luck and have fun\n",
    ]

    for message in intro_messages:
        slow_output(message)

    start_game = Prompt.ask("Would you like to start?", choices=["y", "n"], default="y")

    if start_game == "y":
        name = input("Awesome, What is your name? ")
        return name
    else:
        rprint("Sorry to see you go :loudly_crying_face:")
        return False

def display_game(hint_info,players_name, difficulty, attempts, board, feedbacks):
    game_master_layout = Layout()
    hint, remaining_hints = hint_info
    attempts_text = Text(str(attempts), justify="center", style="dark_red")
    name_text = Text(players_name, justify="center", style="deep_pink4")
    hints_text = Text(hint, justify="center", style="green3")
    subtitle_text = Text(f"Hints left: {str(remaining_hints)} ",justify="center",style="blue_violet")

    def convertDifficulty():
        if difficulty == 7:
            return "Easy", "Range: 0 to 7"
        elif difficulty == 8:
            return "Medium", "Range: 0 to 8"
        elif difficulty == 9:
            return "Hard", "Range: 0 to 9"

    level, level_range = convertDifficulty()
    difficulty_text = Text(level, justify="center", style="orange_red1")

    game_session_chart = Table(
        title="Game Session",
        border_style="red",
        title_style="bold magenta",
        header_style="blue",
        show_header=True,
        box=box.ROUNDED,
        expand=True,
    )
    game_session_chart.add_column("Combination Board", justify="center", ratio=1,width=10)
    game_session_chart.add_column("Feedback", justify="center", ratio=1, no_wrap=True)

    for i in range(len(board)):
        game_session_chart.add_row(str(board[i]), (feedbacks[i]))

    game_master_layout.split_column(
        Layout(
            Panel(
                renderable=centered_intro_logo,
                title="Welcome to Mastermind",
                box=box.ROUNDED,
                border_style="red",
                title_align="center",
                expand=True,
                padding=(2, 2),
            ),
            name="upper",
            ratio=3,
            minimum_size=15,
        ),
        Layout(name="Game Board", ratio=5),
    )

    game_master_layout["Game Board"].split_row(
        Layout(name="left", ratio=2), Layout(game_session_chart, name="right", ratio=6)
    )
    game_master_layout["left"].split_column(
        Layout(
            Panel(attempts_text, style="yellow", title="Attempts Left"),
            name="left",
            ratio=3,
            minimum_size=1
        ),
        Layout(
            Panel(hints_text, style="bright_black",title="Hints",subtitle=subtitle_text,),
            name="center",
            ratio=3,
            minimum_size=1,

        ),
        Layout(
            Panel(name_text, style="royal_blue1", title="Player"),
            name="center",
            ratio=3,
            minimum_size=1
        ),
        Layout(
            Panel(
                difficulty_text,
                style="deep_pink2",
                title="Difficulty Level",
                subtitle=level_range,
            ),
            name="lower",
            ratio=3,
            minimum_size=1
        ),
    )
    console.print(game_master_layout)

def select_difficulty(players_name):
    difficulty = Prompt.ask(
        "What difficulty do you want?",
        choices=["easy", "medium", "hard"],
        default="easy",
    )
    if difficulty == "easy":
        rprint(f"Wise Choice {players_name}")
        time.sleep(1)
        return 7
    elif difficulty == "medium":
        rprint(f"I wish you the best of luck {players_name}")
        time.sleep(1)
        return 8
    elif difficulty == "hard":
        rprint(f"You're insane {players_name} for choosing this option!!")
        time.sleep(1)
        return 9

def give_hint(sequence,previous_hints):

    for digit in sequence:
        if digit not in previous_hints:
            return digit
    return None

def play_game():
    rprint(centered_intro_logo)
    new_params = PARAMS.copy()
    players_name = introduce_game()
    if players_name is False:
        return
    max_diff_level = select_difficulty(players_name)
    new_params["max"] = max_diff_level
    sequence = generate_random_sequence(URL,new_params)
    max_attempts = 10
    attempts = 0
    board = []
    feedbacks = []
    previous_hints= []
    max_hints = 2
    current_hint = ""
    while attempts < max_attempts:
        attempts_left = max_attempts - attempts
        display_game(hint_info=[current_hint, max_hints],
                     players_name=players_name,
                     difficulty=max_diff_level,
                     attempts=attempts_left,
                     board=board,
                     feedbacks=feedbacks)
        guess, current_hint, max_hints = get_players_guess(max_diff_level, current_hint, max_hints, previous_hints, give_hint,sequence)
        board.append(guess)
        feedback = evaluate_players_guess(guess,sequence)
        if all(value == 0 for value in feedback.values()):
            feedback_string = "All Incorrect"
        else:
            feedback_string = f"Correct number(s): {feedback["correct_numbers"]}\tCorrect location: {feedback['correct_location']}"
        feedbacks.append(feedback_string)
        if feedback["correct_location"] == 4:
            rprint(centered_win_logo)
            break
        attempts += 1
    else:
        rprint(centered_lose_logo)
        console.print(f"The sequence was {sequence}. Better luck next time!",justify="center",style="red")

if __name__== "__main__":
    play_game()
