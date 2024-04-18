# Instructions to Start up the game

For this project, ensure you have Python `3.12.0` installed. You can download this version from here [Python Docs](https://www.python.org/downloads/)

### 1.  Clone the repo

```bash
git clone https://github.com/j-corp-25/Mastermind_py
```

### 2. Navigate to project directory

```bash
cd Mastermind_py
```

### 3. Setting up the environment
- If you don't have `pipenv` installed already, you'll need to install it. Run the following command to install `pipenv`:
- (Note: `pip` is included with Python installations from version `3.4` onwards, so you should already have it if your Python version is up-to-date. )

```bash
pip install pipenv
```
- After installing `pipenv` then you can run:

```bash
pipenv install
```

- This will set up the virtual environment based on the libraries I have installed in the `Pipfile` and make sure all the correct versions of dependencies are used.

- To activate environment run the below command:

```bash
pipenv shell
```

### 4. Running the project
- To run the script

  ```bash
  python main.py
  ```

***
__***These are the instructions as of `4/17/2024`. I will keep updating these instructions and my thought process throughout this awesome challenge.__


## Mastermind Game Overview

Mastermind Game is a player against the `computer`. The player's goal is to guess a combination of 4 numbers. After each turn where the player guesses, the computer will provide the following feedback:
- The number(s) are guessed correctly but are in the wrong place.
- The number(s) are guessed correctly and are in the right place.
- Notifies the player if all numbers were incorrect.

The player will need to use these hints to eventually ‘crack the code` that the computer initializes with. The player has 10 attempts.


## Barebone Requirements:
The player needs to interact with the game:
- The player can provide input.
- The player can see the history of guesses/attempts and feedback from previous attempts.
- The player can see the number of attempts remaining.

After these initial requirements, anything else can be up to the limits of my imagination.


## Thought process and Game Plan

For this challenge I was going to initially use `JavaScript`, but after planning an initial blueprint of the logic of the game I decided to instead use `Python`. My primary language for doing leetcode and solving DS&A problems is python. It is a very flexible language and easier to understand so I figured I should use python instead since heavy logic could be implemented with this particular game. I havent implemented any games before using python but I didnt want that to stop me from trying it out this challenge. I found the prompt very exiting and Ideas started flying through my head.

For my initial plan, I needed to figure out if im going to classes or a pure functional approach. Using classes would be a more scalable solution bringing in the ability for more features to be added easily and easier control of the state. However, Im going to set up the game with functional components and once I have that down I will possibly expand to classes. My goal is to have the base requirements first and then expand. Whether that is on the UI side or not I want the core logic of the game to function properly.

I made an initial skeleton of what I want to show in the command line. This is just the start, I want to leverage other libraries like `rich` and `tabulate` to enhance the UI when I get to that point.

Here is my initial mock up of a design

```

 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌     ▐░▌     ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌
 ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀

# Hey! Welcome player to Mastermind.The best codebreaker game out there.

Instructions:
Guess the 4 number combination in as little attempts as possible.
- I will provide feedback if any of the numbers are correct and if they are in the correct place.
- I will also let you know if all your numbers are incorrect as well. Good Luck and Break on!
- Only enter numbers please!


Please input your guess:


```
After the player has input their guess this is how I plan it to look.

```

  Game Session Details         Game Board(Table)                        FeedBack Board(Table)
  [Attempts Left].....        [ 1  2   3   4  ]                  [Correct Number(s) | Correct Location ]
  [      8      ]             [ 2  4   6   7  ]                  [       1                   2         ]
        ...                          ...                                           ...
  [...]                       [...]                              [...]
```

##### Above is how I want the UI to be eventually, I'm hoping leveraging libraries like `rich` can help me achieve this without too much configuration
### Breaking down the logic of the game into smaller steps:



### Breaking down the logic of the game into smaller steps:


#### 1. Game setup


  - **Game State** I need to initialize the game state with certain variables being tracked. These include the number of attempts remaining, the actual board state, and the feedback board. This will end up being my main function that runs the game, but I can set up individual functions inside.
    - For the board state, I can set up an empty list and as the player guesses, I can append that guess to the list, thereby "building" up the board like a stack. In the future, I could implement a possible redo or undo feature so players can replay.
  - **Generate the Secret code** For this action, I can set up constant variables at the top of the file with the parameters as well. Generating the code is a straightforward process. I can set up a function that uses requests to fetch the numbers and convert them into a list. I need to keep the parameters modular because I'm thinking of using the max parameter to increase the difficulty in the future. I can use `num=7` as a base difficulty, then `num=8` as a medium difficulty, and finally `num=9` as hard.
  - **Generating Feedback** This is one of the actions that will require more complex logic. I need to create an algorithm that can determine how many numbers are correct and in the right location, and how many numbers are correct but in the wrong location.
    - For exact matches, I can compare the indices of both the `players_guess` and the `generated_sequence`. I can use regular variables as counters or I can use a dictionary with specific keys. I also need to account for when all the numbers are wrong. This would mean that at the same index where `players_guess[i]` is compared to `generated_sequence[i]`, the values are not equal, and at the same time, no `players_guess[i]` is in the `generated_sequence` array.

### Bugs and setbacks

- After careful testing and tracking the return of the players feedback I found a bug in the logic that increases the counter for the correct number incorrectly. The correct location is working as expected but in a scenario where the user inputs the same number repeatedly, the `correct_number` is not working as expected.
- Below is an image showing this
![BugInDictionary](/assets/bug.PNG)
- If you look at the feedback carefully, the `correct_number` value is not accurate. Base on the users input and given the sequence=`[4,6,1,6]` it should be `{'correct_number(s)': 1, 'correct_location': 2} `
- After two or so hours I figured out the trick. I was dealing with a problem where I would exclude duplicates. This was just like the LeetCode problem that checks if there are duplicates. But I just needed to add a little twist.
- I initially had the below structure:
  ```py
  def evaluate_players_guess(players_guess,generated_sequence):
      feedback = {"correct_number(s)": 0, "correct_location": 0}
      for i in range(len(generated_sequence)):
          if players_guess[i] == generated_sequence[i]:
              feedback["correct_location"] += 1
      for i in range(len(generated_sequence)):
          if players_guess[i] in generated_sequence:
              feedback["correct_number(s)"] += 1
      return feedback
  ```
- The function would fail every time the player would input the same number for the entire combination.
- **However, after using a `set` I cracked it!** and got this. Logic has been conquered!
  ```py
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
  ```
- On Tuesday I ran into a setback where I couldn't understand what "renderable" objects were in rich documentation. I would pass down the function and try to display the output on the terminal but I would get an attribute error `AttributeError: 'int' object has no attribute 'translate'`. I ended finding out after a lot fo trial and error that it needed to be string or another `rich` created object.
- My first intention was to just turn everything into a string as it came into the `display_game` function and everything will be fine, but the `feedback` was in a dictionary so I needed to figure out how to display it properly.
- What I ended up doing was implementing a check to determine the type of feedback contained in the dictionary. If every value in the feedback dictionary was 0, indicating that all numbers and their locations were incorrect, I set the feedback string to "All numbers and locations are incorrect." If the feedback contained any correct numbers or locations, I formatted the feedback string to include these details, showing both the count of correct numbers and their correct locations, thereby making it clear and informative to the player.

## Work Timeline

### Monday

- Spent the weekend deciding on a programming language, which delayed concrete planning but helped in developing a detailed blueprint for the game structure.
- Set a goal to finalize core features and ensure the logic was correct from the start of the week regardless of UI.
- Planned to outline the game's features, functions, and user interface. Also considered whether to use the `rich` library to avoid potential restructuring of the code later.

### Tuesday

- Dedicated the day to researching the rich library to understand how it could be used to implement the game’s visual mock-ups.
- Invested over 10 hours in studying documentation, experimenting with examples, and adjusting variables to extract useful elements for the project.
- Achieved a breakthrough at 7:33 PM, mastering the use of rich.layout, rich.table, and rich.console. It was an incredible moment!
- I actually had a moment of Eureka at 7:33 pm. After spending so much time trying to understanding `rich.layout` , `rich.table` and understanding how the `rich.console` operates. I finally knew how to manipulate these methods.

### Wednesday

- Spent some time polishing functions and running the black formatter to keep the code clean.
- My goal was to add a game timer and some hints. The timer turned out to be a real headache because threading in Python was way trickier than I expected, eating into the time I had planned to work on the hints.
- I kicked off with the timer and, looking back, I wish I hadn't. I got sucked into a threading rabbit hole for about four to five hours and still couldn't get it to work the way I needed.
- I figured out that the timer had to run alongside/parallel the game's main function, but cracking that code just wasn't happening.
- Because of all the time I spent struggling with the timer, I only managed to set up a basic placeholder for the hints and not completely functional.
- The reason I wanted to leave the the hints feature for later was because from the start I didn't want to focus on features that required more creativity.
- Because a feature that requires more creativity means more trial and error to get it "right" vs a timer that is sole purpose is to tick down or up while playing.

### Thursday

- My goal for today is to get hints working, its a harder feature to implement than I thought because theres multiple ways to it.
- Aside from working on the hints I also want to start refactoring my code to be more readable since theres only one day left.
- If I get hints working, I'll see if I can work on setting up some kind of score.
- If get hints, and score working without using too much time. I'll comeback to research how to make a timer run while the person is playing.
- Regarding the score feature. The initial plan is to integrate a function that calculates the score based on the number of hints used and the attempts left before winning. Achieving maximum points should be possible only if no hints are used and the number of attempts is minimized.
- This way you can only achieve the maximum amount of points if you dont use hints and have as little attempts as possible.


### Friday
TBD
