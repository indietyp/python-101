"""
This is an extra task, that is not required for the course.

You will be given a maze (as a `Maze` object) and a starting position (as a `Position` object),
your goal is to find a path from the starting position to the exit of the maze.

`State` is an enumeration with the following values:
    - `State.WALL`: A wall, you cannot move here.
    - `State.EMPTY`: An empty cell, you can move here.
    - `State.START`: The starting position, you can move here.
    - `State.EXIT`: The exit of the maze, you can move here.
    - `State.VISITED`: A cell that has been visited, you can move here.
    - `State.MARKED`: A cell that has been marked, you can move here.

The `Position` object has the following attributes:
    - `x`: The x coordinate of the position.
    - `y`: The y coordinate of the position.
    - `depth`: The depth of the position, this is used to determine the order in which
        the positions are visited.

The `Position` object additionally has the following methods:
    - `neighbors() -> list[Position]`: Returns a list of positions that
        are neighbors of the given position.
    - `neighbors_with_state(state: State) -> list[Position]`:
        Returns a list of positions that are neighbors of the given position
        and have the given state.
    - `distance(other: Position) -> int`:
        Returns the distance between the given position and the other position.
        (Manhattan distance)
    - `state() -> State`: Returns the state of the position.
    - `set_state(state: State) -> None`: Sets the state of the position to the given state

The maze object exposes the following methods:
    - `size() -> tuple[int, int]`:
        Returns the size of the maze as a tuple of two integers.
    - `cell(position: Position) -> State`: Returns the cell at the given position.
    - `cells(state: State | None) -> list[Position]`:
        Returns a list of positions that satisfy the given state.
    - `random_cell(state: State | None) -> Position`:
        Returns a random position of the specified state.
    - `deepest_cell(state: State | None) -> Position`:
        Returns the deepest position of the specified state.
    - `shallowest_cell(state: State | None) -> Position`:
        Returns the shallowest position of the specified state.
    - `newest_cell(state: State | None) -> Position`:
        Returns the newest position of the specified state, time is measured by
        the modification time.
    - `oldest_cell(state: State | None) -> Position`:
        Returns the oldest position of the specified state,
        time is measured by the modification time.
    - `neighbors(position: Position) -> list[Position]`: Returns a list of positions that
        are neighbors of the given position.
    - `neighbors_with_state(position: Position, state: State) -> list[Position]`:
        Returns a list of positions that are neighbors of the given position and
        have the given state.
    - `get_start() -> Position`: Returns the starting position.
    - `assert_exit(position: Position) -> None`: Raises an exception if the given position
        is not the exit of the maze.
    - `export(filename: str) -> None`: Exports the maze to the given filename as a GIF
        image.

There are a lot of viable solutions to this problem,
but the easiest one is to use a graph algorithm like BFS or DFS.
"""
