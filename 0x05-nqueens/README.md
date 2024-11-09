# N Queens Problem Solver

This project implements a solution for the **N Queens problem**, a classic combinatorial problem in computer science and mathematics. The goal is to place `N` queens on an `N×N` chessboard so that no two queens attack each other.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Algorithm](#algorithm)
- [Files](#files)
- [Author](#author)

## Description

The N Queens problem challenges us to place N queens on a chessboard of size N×N such that:
1. No two queens are on the same row.
2. No two queens are on the same column.
3. No two queens are on the same diagonal.

This project uses a **backtracking algorithm** to find all possible solutions for a given `N`.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3).
- Adheres to PEP 8 style (version 1.7.*).
- Only the `sys` module is imported.
- The script is executable.

## Usage

1. Clone this repository or copy the script.
2. Make the script executable:
   ```bash
   chmod +x 0-nqueens.py
   ```
3. Run the script with the size of the chessboard (`N`) as an argument:
   ```bash
   ./0-nqueens.py N
   ```

### Input Constraints
- `N` must be an integer greater than or equal to 4.
- If invalid input is provided, the program will:
  - Print an error message.
  - Exit with status code `1`.

## Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
...
```

### Error Cases

```bash
$ ./0-nqueens.py
Usage: nqueens N

$ ./0-nqueens.py 3
N must be at least 4

$ ./0-nqueens.py not_a_number
N must be a number
```

## Algorithm

This program uses a **backtracking approach**:
1. Start with an empty chessboard.
2. Place a queen in a row if it is safe.
3. Move to the next row.
4. If a solution is invalid, backtrack to the previous row and try a different position.
5. Continue until all solutions are found.

### Key Functions
- `get_input()`: Validates the program's input.
- `is_attacking(pos0, pos1)`: Checks if two queens attack each other.
- `build_solution(row, group)`: Recursively builds valid solutions using backtracking.
- `get_solutions()`: Initializes the board and finds all possible solutions.

## Files

- `0-nqueens.py`: Main script to solve the N Queens problem.

## Author

[Awe Caleb]  
**Email**: [calebawe0@gmail.com]  
**GitHub**: [www.github.com/Olu433]
