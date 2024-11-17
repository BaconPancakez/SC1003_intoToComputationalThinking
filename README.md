# Introduction to Computational Thinking and Programming

This repository contains Python implementations of various exercises and mini-projects designed to develop computational thinking skills, including decomposition, pattern recognition, and algorithm design.

## Contents

1. Battleship Placement  
   A small segment for a Battleship game, involving ship placement and handling user inputs for attack coordinates.

2. Random Number Generation and Guessing Game  
   A simple program to generate a random number, take user input, and provide feedback in a "Bulls and Cows" game format.

3. To-Do List Application  
   A practical exercise to build a console-based task management application.

4. Pattern Recognition - Cellular Automata  
   A simulator for Elementary Cellular Automata based on user-defined rules.

5. Merge Sort Implementation  
   A customized merge sort algorithm for sorting a list of dictionaries by a specific key.

---

1. Battleship Placement

---

Overview
A simplified implementation of the Battleship game, focusing on ship placement and attack coordinate validation.

Features

- Allows users to define starting positions for ships.
- Validates user inputs and places ships on a game board.
- Handles attack coordinates with boundary validation.

---

2. Random Number Generation and Guessing Game

---

Overview
This program generates a 4-digit random number and allows the user to guess it. The game provides feedback in the form of "Bulls" (correct digits in the correct place) and "Cows" (correct digits in the wrong place).

Features

- Random number generation using the random.shuffle method.
- Input validation to ensure the user enters exactly four digits.
- Comparison of user guesses with the target number to provide feedback.

---

3. To-Do List Application

---

Overview
A console-based task management application for adding, viewing, editing, deleting, and filtering tasks.

Features

- Add tasks with a title and optional description.
- Mark tasks as completed or pending.
- Save tasks to a file and load them back later.

---

4. Pattern Recognition - Cellular Automata

---

Overview
A simulator for Elementary Cellular Automata, which evolves a grid of cells based on user-defined rules (0-255) and an initial state.

Features

- Implements logic for rule-based cell state updates.
- Generates patterns for a specified number of generations.

---

5. Merge Sort Implementation

---

Overview
An implementation of the merge sort algorithm for sorting a list of dictionaries by a specified key.

Features

- Accepts a list of dictionaries with attributes like name and age.
- Sorts the list based on the provided key using a recursive merge sort approach.

---

## Setup and Usage

Prerequisites

- Python 3.x
- Jupyter Notebook (for exercises documented in notebooks)

Installation

1. Clone this repository:
   git clone https://github.com/BaconPancakez/SC1003_intoToComputationalThinking
   cd SC1003_intoToComputationalThinking

2. Run the exercises using Python or Jupyter Notebook.

Running a Program
To execute a specific script, run:
python script_name.py

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
