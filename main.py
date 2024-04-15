import requests
from ascii_logo import logo

URL = "https://www.random.org/integers/?"
PARAMS = {"num":4,"min":1,"max":6,"col":1,"base":10,"format":"plain","rnd":"new"}

def generate_random_sequence(url,params):
    response = requests.get(url,params)
    integer_list = [int(num) for num in response.text.strip().split()]
    return integer_list

def get_players_guess():
    while True:
        try:
            players_guess_input = input("Please guess a combination of four numbers from 0 - 7 (no spaces): ")
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
            except ValueError :
                print("Numbers only please: no extra spaces, or letters or special characters")
        except KeyboardInterrupt:
            print("\nQuitting the game.....")
            break
        except Exception as error:
            print(f"An Unexpected Error has Occured {error}")

def evaluate_players_guess(players_guess,generated_sequence):
    feedback = {"correct_number(s)": 0, "correct_location": 0}
    for i in range(len(generated_sequence)):
        if players_guess[i] == generated_sequence[i]:
            feedback["correct_location"] += 1
    for i in range(len(generated_sequence)):
        if players_guess[i] in generated_sequence:
            feedback["correct_number(s)"] += 1
    return feedback


