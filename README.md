# Rush Hour Puzzle Solver
## A program that solves puzzles in the game [Rush Hour](https://www.cokogames.com/rush-hour/play/) using Uniform Cost Search, Greedy Best-First Search and the A* Search Algorithm.

This project is an example of using search algorithms to solve a practical problem.

### Game Setup

The following is an example of a 36 character sample input string representing a 6x6 game board: **BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.**

or more easily recognizable in the format:

![image](https://user-images.githubusercontent.com/67298240/211711155-f79e8f9e-8a91-4cd4-a176-22292d12aab5.png)

The objective of the game is to reorganize the board so car AA is at the exit (the rightmost position in the game board).
A car's movement is constrained by its orientation. In the above example, car BB can only move horizontally and car JJ vertically.


### Input Files

An input file contains a list of puzzles to be solved, invalid puzzles are rejected. The text following a # character is ignored and can be used to add comments to an input file.

**Example input file:**

![image](https://user-images.githubusercontent.com/67298240/211937907-c844408e-0a45-4a76-a6a4-7d4e6b7f9238.png)

### Heuristics

The program uses 4 heuristics to improve search efficiency.

1. The number of blocking vehicles between car AA and the exit.
2. The number of blocked positions between car AA and the exit.
3. The number of blocking vehicles between car AA and the exit * 5.
4. The number of blocking vehicles between car AA and the exit, and for each blocking verticle vehicle with no available moves (trapped) + 1.

### Output Files

When the program terminates it produces a search and solution file for each solved puzzle. Runtime statistics for all solved puzzles are also compiled into a single Excel file.

The search file displays the order in which the states were visited to reach the goal state.

**Example search file:**

![image](https://user-images.githubusercontent.com/67298240/211710871-ad0045da-84e5-46cd-9798-596d2ab6582f.png)

The solution file displays the solution path to the goal state and various runtime information.

**Example solution file:**

![image](https://user-images.githubusercontent.com/67298240/211711014-3d8aec9e-6249-43d0-bf0c-770074f1648c.png)

The Excel file compiles the solution length, search length, and excution time into a tabular format for each solved puzzles.

**Example Excel file:**

![image](https://user-images.githubusercontent.com/67298240/211935837-1f55f44f-8e94-4c75-963e-f6b5292d345a.png)


