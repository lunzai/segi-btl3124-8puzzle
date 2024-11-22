import argparse
import random
import time
from queue import PriorityQueue, Queue
from collections import deque

# Helper function - Check if puzzle is solvable
def is_solvable(state):
    inversions = sum(
        1
        for i in range(len(state))
        for j in range(i + 1, len(state))
        if state[i] != 0 and state[j] != 0 and state[i] > state[j]
    )
    return inversions % 2 == 0, inversions

# Helper function - Format puzzle in table form
def format_puzzle(state):
    rows = []
    border = "+---+---+---+" 
    for i in range(0, len(state), 3):
        row = "| " + " | ".join(str(num) if num != 0 else " " for num in state[i:i + 3]) + " |"
        rows.append(border)
        rows.append(row)
    rows.append(border) 
    return "\n".join(rows)

# Generate random solvable puzzle state
def generate_solvable_state(goal_state):
    while True:
        state = goal_state[:]
        random.shuffle(state)
        if is_solvable(state)[0]:
            return state

# Algorithm: Breadth-first search (BFS)
def bfs(initial_state, goal_state, max_iterations):
    queue = Queue()
    queue.put((initial_state, []))
    visited = set()
    iterations = 0

    while not queue.empty():
        if max_iterations and iterations >= max_iterations:
            break
        current, path = queue.get()
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))
        if current == goal_state:
            return path, iterations
        next_states = generate_next_states(current)
        for state, move in next_states:
            queue.put((state, path + [move]))
        iterations += 1

    return None, iterations

# Algorithm: Depth-first search (DFS)
def dfs(initial_state, goal_state, max_iterations):
    stack = deque([(initial_state, [])]) 
    visited = set()
    iterations = 0

    while stack:
        if max_iterations and iterations >= max_iterations:
            print("Reached max iterations limit.")
            return None, iterations
        current, path = stack.pop()
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))

        if current == goal_state:
            return path, iterations

        next_states = generate_next_states(current)
        for state, move in next_states:
            if tuple(state) not in visited:
                stack.append((state, path + [move]))
        iterations += 1

    print("Goal not found within constraints.")
    return None, iterations

# Algorithm: A Star Search - with Manhatten distance
def a_star(initial_state, goal_state, max_iterations):
    def h(state):
        # Manhattan Distance
        distance = 0
        for i in range(1, 9):  # Exclude 0 (blank space)
            current_index = state.index(i)
            goal_index = goal_state.index(i)
            distance += abs(current_index // 3 - goal_index // 3) + abs(current_index % 3 - goal_index % 3)
        return distance

    open_set = PriorityQueue()
    open_set.put((0, initial_state, []))
    visited = set()
    iterations = 0

    while not open_set.empty():
        if max_iterations and iterations >= max_iterations:
            break
        f_n, current, path = open_set.get()
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))
        if current == goal_state:
            return path, iterations
        
        g_n = len(path)
        next_states = generate_next_states(current)
        for state, move in next_states:
            h_n = h(state)
            open_set.put((g_n + h_n, state, path + [move]))
        iterations += 1

    return None, iterations

# Generate next valid states by moving the blank space.
def generate_next_states(state):
    next_states = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)

    moves = {
        "↑": (-1, 0),
        "↓": (1, 0),
        "←": (0, -1),
        "→": (0, 1),
    }

    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            next_states.append((new_state, move))

    return next_states

# Command-line interface
def parse_args():
    parser = argparse.ArgumentParser(description="8-Puzzle Solver")
    parser.add_argument("-a", "--algorithms", required=True, help="Comma-separated algorithms to use (bfs, dfs, a*, etc.)")
    parser.add_argument("-i", "--initial", help="Initial state as comma-separated values (e.g., 1,2,3,4,5,6,7,8,0)")
    parser.add_argument("-g", "--goal", default="1,2,3,4,5,6,7,8,0", help="Goal state as comma-separated values, default: 1,2,3,4,5,6,7,8,0")
    parser.add_argument("-m", "--max_iterations", type=int, default=0, help="Maximum number of iterations (0 for no limit)")
    parser.add_argument("-c", "--check_only", type=int, default=0, help="Only check solvability (1=True, 0=False)")
    # parser.add_argument("-v", "--verbosity", action="count", default=0, help="Verbose output (-v, -vv, -vvv for levels)")
    return parser.parse_args()

def main():
    args = parse_args()
    algorithms = args.algorithms.split(",")
    goal_state = list(map(int, args.goal.split(",")))
    initial_state = list(map(int, args.initial.split(","))) if args.initial else generate_solvable_state(goal_state)
    solvable, inversions = is_solvable(initial_state)

    if args.check_only:
        print(f"Number of inversions: {inversions}, Puzzle is {'Solvable' if solvable else 'Not Solvable'}")
        return

    print("Initial State:\n" + format_puzzle(initial_state))
    print("Goal State:\n" + format_puzzle(goal_state))
    print(f"Number of inversions: {inversions}, Puzzle is {'Solvable' if solvable else 'Not Solvable'}\n")

    if not solvable:
        print("Puzzle is not solvable. Exiting.")
        return

    for alg in algorithms:
        print(f"Running algorithm: {alg.upper()}")
        start_time = time.time()
        if alg == "bfs":
            path, iterations = bfs(initial_state, goal_state, args.max_iterations)
        elif alg == "dfs":
            path, iterations = dfs(initial_state, goal_state, args.max_iterations)
        elif alg == "a*":
            path, iterations = a_star(initial_state, goal_state, args.max_iterations)
        else:
            print(f"Algorithm {alg} not implemented.")
            continue

        end_time = time.time()
        duration = end_time - start_time
        if path is None:
            print(f"Algorithm {alg.upper()} could not solve the puzzle within the given constraints.")
        else:
            print(f"Solved using {alg.upper()} in {iterations} iterations and {duration:.4f} seconds.")
            print("Solution path length:", len(path))
            if len(path) <= 500:
                print("Solution path:", path)
            else: 
                print("solution path: Path length > 500 not shown")
        print("-" * 40)

if __name__ == "__main__":
    main()
