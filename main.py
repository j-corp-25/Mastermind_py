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
    players_set = set()
    for i in range(len(generated_sequence)):
        if players_guess[i] == generated_sequence[i]:
            feedback["correct_location"] += 1
    for i in range(len(generated_sequence)):
        if players_guess[i] in generated_sequence and not players_guess[i] in players_set:
            feedback["correct_number(s)"] += 1
            players_set.add(players_guess[i])
    return feedback


def play_game():
    max_attempts = 10
    attempts = 0
    board = []
    feedbacks = []
    sequence = generate_random_sequence(url=URL,params=PARAMS)
    while attempts < max_attempts:
        print(f"Attempts Status: {attempts}/{max_attempts}")
        print(f"Remaining attempts: {max_attempts - attempts}")
        print("This is the sequence", sequence)
        guess = get_players_guess()
        feedback = evaluate_players_guess(guess,sequence)
        print("Feedback:",feedback)
        if all(value == 0 for value in feedback.values()):
            print("All numbers are incorrect")
        elif feedback["correct_location"] == 4:
            print("Woohooo, you have won")
            break
        board.append(guess)
        feedbacks.append(feedback.values())
        print("Feedbacks", feedbacks)
        print("This is your feedback Table")
        for single_feedback in feedbacks:
            print(single_feedback)




        print("This is the board game Table ")
        for single_guess in board:
            print(single_guess)
        attempts += 1
    else:
        print("Sorry you have failed.Better luck next time")






if __name__== "__main__":
    play_game()
