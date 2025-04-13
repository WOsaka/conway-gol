# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Controls](#controls)

## Introduction

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. This project simulates the game using Python and Pygame.

## Features

- Interactive grid to toggle cell states.
- Predefined patterns for quick setup.
- Step-by-step or continuous simulation.
- Adjustable grid size and speed.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WOsaka/conway-gol.git
   cd conway-gol
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install requirements.txt
   ```

5. Run the game:

   ```bash
   python main.py
   ```

## Controls

- **Left Click**: Toggle cell state (alive/dead).
- **Right Click**: Set current pattern.
- **Space**: Start/stop the simulation.
- **q**: Quit the game.
- left/right arrow: Change pattern.
