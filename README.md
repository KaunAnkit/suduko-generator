# Sudoku Generator

A Python-based Sudoku puzzle generator and solver with solution uniqueness verification.

## Project Overview

This project generates valid Sudoku puzzles and includes tools for solving them and verifying that each puzzle has a unique solution.

## Project Structure

```
suduko_generator/
├── src/
│   ├── generator.py          # Main puzzle generation logic
│   ├── sudoku_solver.py      # Core solving algorithm and board utilities
│   └── solution_counter.py   # Solution uniqueness verification
├── README.md                 # This file
```

## Files Description

### `src/generator.py`
- **empty_box_generator()**: Creates an empty 9x9 Sudoku board (cells initialized to -1)
- **random_list_generator()**: Generates a randomly shuffled list of numbers 1-9
- **board_gen()**: Main generator function that orchestrates puzzle creation

### `src/sudoku_solver.py`
- **position_finder()**: Finds the next empty cell in the board
- **number_placer()**: Validates if a number can be placed at a given position (checks row, column, and 3x3 box constraints)
- **board_filler()**: Solves a Sudoku puzzle using backtracking algorithm

### `src/solution_counter.py`
- **solution_counter()**: Counts the number of solutions for a given puzzle board to verify uniqueness

## Key Features

- **Sudoku Validation**: Implements standard Sudoku rules (no duplicates in rows, columns, or 3x3 boxes)
- **Backtracking Solver**: Uses recursive backtracking to efficiently solve puzzles
- **Solution Verification**: Checks if puzzles have a unique solution
- **Board Generation**: Creates valid empty Sudoku boards

## Getting Started

1. Navigate to the `src/` directory
2. Import the modules:
   ```python
   from generator import board_gen, empty_box_generator
   from sudoku_solver import board_filler, position_finder, number_placer
   from solution_counter import solution_counter
   ```

## Requirements

- Python 3.x
- Standard library (no external dependencies required)

---

**Note**: Code files have been organized in the `src/` folder for better project structure.
