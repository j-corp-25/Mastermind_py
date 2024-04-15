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
