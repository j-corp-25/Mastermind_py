from main import evaluate_players_guess


def test_example_run():
    sequence = [0,1,3,5]
    players_guesses = [[2,2,4,6],[0,2,4,6],[2,2,1,1],[0,1,5,6]]
    for guess in players_guesses:
        feedback = evaluate_players_guess(guess,sequence)
        if all(value == 0 for value in feedback.values()):
            print("all incorrect")
        else:
            print(f"{feedback["correct_numbers"]} correct number"+" and " + f"{feedback["correct_location"]} correct location" )


if __name__ == "__main__":
    test_example_run()
