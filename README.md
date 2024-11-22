# 8-Puzzle Solver  

This repository contains a Python script to solve the **8-puzzle problem** using three search algorithms: **BFS (Breadth-First Search)**, **DFS (Depth-First Search)**, and **A* Search**. It provides a detailed comparison of their performance in terms of **iterations**, **runtime**, **solution path length**, and both **space and time complexity**.  

## Overview  

The **8-puzzle problem** involves rearranging tiles on a 3x3 grid to match a given goal state, moving one tile at a time into the blank space. This problem is widely used to explore search strategies, algorithms, and their performance characteristics.  

## Features  
- Solves the 8-puzzle using BFS, DFS, and A* search.  
- Outputs detailed performance metrics:  
  - **Iterations**  
  - **Runtime (seconds)**  
  - **Solution path length**  
- Allows users to test and compare all three algorithms on random puzzles.  

## Requirements  

- Python 3.x  
- No external libraries are required.  

## Usage  

Clone this repository:  
 ```bash  
 git clone https://github.com/lunzai/segi-btl3124-8puzzle.git  
 cd segi-btl3124-8puzzle
 ```  

Run the script:  
 ```bash  
 python 8puzzle.py -a a*,bfs,dfs
 ```  
The script will generate random puzzles, solve them using BFS, DFS, and A*, and display the results, including metrics for comparison.  

```plaintext
usage: 8puzzle.py [-h] -a ALGORITHMS [-i INITIAL] [-g GOAL] [-m MAX_ITERATIONS] [-c CHECK_ONLY]

8-Puzzle Solver

options:
  -h, --help            show this help message and exit
  -a ALGORITHMS, --algorithms ALGORITHMS
                        Comma-separated algorithms to use (bfs, dfs, a*, etc.)
  -i INITIAL, --initial INITIAL
                        Initial state as comma-separated values (e.g., 1,2,3,4,5,6,7,8,0)
  -g GOAL, --goal GOAL  Goal state as comma-separated values, default: 1,2,3,4,5,6,7,8,0
  -m MAX_ITERATIONS, --max_iterations MAX_ITERATIONS
                        Maximum number of iterations (0 for no limit)
  -c CHECK_ONLY, --check_only CHECK_ONLY
                        Only check solvability (1=True, 0=False)
```

## Example Output  

```plaintext  
Initial State:
+---+---+---+
| 2 |   | 8 |
+---+---+---+
| 7 | 3 | 4 |
+---+---+---+
| 6 | 1 | 5 |
+---+---+---+
Goal State:
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+
Number of inversions: 16, Puzzle is Solvable

Running algorithm: A*
Solved using A* in 18 iterations and 0.0008 seconds.
Solution path length: 17
Solution path: ['↓', '↓', '←', '↑', '→', '→', '↑', '←', '←', '↓', '→', '↓', '→', '↑', '←', '↓', '→']
----------------------------------------
Running algorithm: BFS
Solved using BFS in 13243 iterations and 0.0839 seconds.
Solution path length: 17
Solution path: ['↓', '↓', '←', '↑', '→', '→', '↑', '←', '←', '↓', '→', '↓', '→', '↑', '←', '↓', '→']
----------------------------------------
Running algorithm: DFS
Solved using DFS in 13919 iterations and 2.5816 seconds.
Solution path length: 13611
solution path: Path length > 500 not shown
----------------------------------------
```  

## Contribution  

Feel free to fork this repository, make improvements, or add new features. Pull requests are welcome!  

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  
