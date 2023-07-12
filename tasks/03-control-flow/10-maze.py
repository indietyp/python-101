"""
This is an extra task, that is not required for the course.

You will be given a maze (as a `Maze` object) and a starting position (as a `Cell` object),
your goal is to find a path from the starting position to the exit of the maze.

`State` is an enumeration with the following values:
    - `State.WALL`: A wall, you cannot move here.
    - `State.EMPTY`: An empty cell, you can move here.
    - `State.VISITED`: A cell that has been visited, you can move here.
    - `State.MARKED`: A cell that has been marked, you can move here.

The `Position` object has the following attributes:
    - `x`: The x coordinate of the position.
    - `y`: The y coordinate of the position.

The `Cell` object additionally has the following methods:
    - `neighbors(state: State | None) -> list[Position]`:
        Returns a list of positions that are neighbors of the given position.
    - `distance(other: Position) -> int`:
        Returns the distance between the given position and the other position.
        (Manhattan distance)
    - `state() -> State`: Returns the state of the position.
    - `set_state(state: State) -> None`: Sets the state of the position to the given state

The maze object exposes the following methods:
    - `size() -> tuple[int, int]`:
        Returns the size of the maze as a tuple of two integers.
    - `cell(position: Position) -> State`: Returns the cell at the given position.
    - `cells(state: State | None) -> list[Cell]`:
        Returns a list of positions that satisfy the given state.
    - `random_cell(state: State | None) -> Cell`:
        Returns a random position of the specified state.
    - `deepest_cell(state: State | None) -> Cell`:
        Returns the deepest position of the specified state.
    - `shallowest_cell(state: State | None) -> Cell`:
        Returns the shallowest position of the specified state.
    - `newest_cell(state: State | None) -> Cell`:
        Returns the newest position of the specified state, time is measured by
        the modification time.
    - `oldest_cell(state: State | None) -> Cell`:
        Returns the oldest position of the specified state,
        time is measured by the modification time.
    - `neighbors(position: Cell, state: State | None) -> list[Cell]`:
        Returns a list of positions that are neighbors of the given position.
    - `start() -> Cell`: Returns the starting position.
    - `has_path() -> bool`:
        Returns `True` if there is a path from the starting position using `State.MARKED`
    - `assert_path(cell: Cell) -> None`: Raises an exception if the given position
        is not the exit of the maze.
    - `render_animations() -> str`: Exports the animation of the maze as an HTML file.
    - `render_state() -> str`: Exports the state of the maze as an HTML file.

There are a lot of viable solutions to this problem,
but the easiest one is to use a graph algorithm like BFS or DFS.
"""
from pathlib import Path

from maze import Maze, State, Position, Cell

# Feel free to change these values to test your code.
WIDTH = 16
HEIGHT = 16

maze = Maze(WIDTH, HEIGHT)

# Write your code below this line 👇

# Write your code above this line 👆

# This will raise an exception if the maze is not solved.
maze.assert_path()

# This will export the maze as an HTML file that you can open in your browser.
DIRECTORY = Path(__file__).parent.absolute()
OUTPUT = DIRECTORY / 'maze.html'

OUTPUT.write_text(maze.render_animation())
