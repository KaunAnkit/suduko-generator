# Sudoku Generator

Generate and solve Sudoku puzzles with solution uniqueness verification.

## Requirements

- Python 3.x
- No external dependencies

## Usage

```python
from src.generator import board_gen
from src.sudoku_solver import board_filler
from src.solution_counter import solution_counter

# Generate a puzzle
puzzle = board_gen()

# Solve it
solution = board_filler(puzzle)

# Verify unique solution
num_solutions = solution_counter(puzzle)
```

## Features

- Puzzle generation with backtracking algorithm
- Sudoku solving with constraint validation
- Solution counting for uniqueness verification
