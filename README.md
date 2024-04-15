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
__***These are the instructions as of `4/14/2024`. I will keep updating these instructions and my thought process throughout this awesome challenge.__


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

For this challenge I was going to initially use `JavaScript`, but after planning an initial blueprint of the logic of the game I decided to instead use `Python`. My primary language for doing leetcode and solving DS&A problems is python. It is a very flexible language and easier to understand so I figured I should use python instead since heavy logic could be implemented with this particular game. I havent implemented any games before using python but I didnt want that to stop me from trying it out this challenge. I found the prompt very exitement and Ideas started flying through my head.

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

### Bugs

- After careful testing and tracking the return of the players feedback I found a bug in the logic that increases the counter for the correct number incorrectly. The correct location is working as expected but in a scenario where the user inputs the same number repeatedly, the `correct_number` is not working as expected.
- Below is an image showing this
![BugInDictionary](/assets/bug.PNG)
- If you look at the feedback carefully, the `correct_number` value is not accurate. Base on the users input and given the sequence=`[4,6,1,6]` it should be `{'correct_number(s)': 2, 'correct_location': 2} `
