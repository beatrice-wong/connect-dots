# Pipeline
1. Create a solver core (terminal based)
2. turn the thingys into actual UI for user to interact with
3. PROFIT!

# Solver Core

Input: size of the board, number of endpoints, locations of endpoints
## Represent the board

|Game   |Representation|DataType|
|-------|--------------|--------|
|Square |Coordinates|Array|
|Colored Pair|Endpoint Cells|Class (Point 1, Point 2, Coord 1, Coord 2)|

- paths occupy cells and cannot overlap

## Backtracking Solver
- Find possible simple paths between a color’s endpoints, avoiding cells already used by other paths.
- Try one path, then recursively solve the remaining pairs.
- Backtrack when a pair has no valid path.
- Accept a solution only if every cell is used exactly once.

```
solve(remainingPairs, usedCells):
    if no pairs remain:
        succeed only if every board cell is used

    choose a pair with few possible paths
    for each possible path:
        mark its cells used
        if solve(other pairs, used cells):
            return solution
        undo the path

    return no solution
```
## Additional Consideration
- Some of the complicated ones require the longest route and additional rules
- add pruning such as choosing the pair with the fewest available paths first