# DinoGame

Welcome to DinoGame, a fun and exciting game where you control a dinosaur to avoid obstacles and score points!

## Prerequisites

Before you start playing the game, make sure you have Python installed on your computer. You can download and install Python from [the official Python website](https://www.python.org/).

## Installation

Follow these steps to set up the game on your local machine:

### 1. Clone or Download the Repository

Clone the repository to your local machine or download the game files as a ZIP archive and extract them to a directory of your choice.

### 2. Create a Virtual Environment (Optional)

Navigate to the game directory using your command prompt or terminal, and create a virtual environment:

```sh
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```sh
  .\venv\Scripts\activate
  ```

- On MacOS/Linux:
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages:

```sh
pip install pygame PythonTurtle
```

## Running the Game

Once you have installed the dependencies, you can start playing the game:

1. Navigate to the game directory if you are not already there.
2. Run the game using Python:
   ```sh
   python main.py
   ```

Follow the on-screen instructions to play the game. Enjoy!

## How To Play

### Controls

- Use the arrow keys to move the dinosaur.
- Press the spacebar to make the dinosaur jump.
- After colliding with an obstacle, enter your name
- Press "Play Again" or view high scores

### Saving Scores

- After you collide with an obstacle, the game will freeze, and you will be prompted to enter your name
- This name will be associated with your score in the High Scores window
- High scores will be temporarily saved as long as you are running the game
- Individual scores can be removed

## Deactivating the Virtual Environment (Optional)

When you’re done playing, you can deactivate the virtual environment:

```sh
deactivate
```
