from enum import IntFlag, auto
from random import choice
from typing import Self


class State(IntFlag):
    WALL = auto()
    EMPTY = auto()
    START = auto()
    EXIT = auto()

    # These are not strictly necessary, but helpful for implementing different algorithms.
    VISITED = auto()
    MARKED = auto()


DENY = State.WALL | State.START | State.EXIT | State.EMPTY


class Time:
    t: int

    def __init__(self):
        self.t = 0

    def tick(self):
        self.t += 1


class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def manhattan_distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidean_distance(self, other: Self) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Cell:
    position: Position

    state: State
    depth: int
    modified: Time

    maze: 'Maze'

    def __init__(self, x: int, y: int, maze: 'Maze'):
        self.x = x
        self.y = y

        self.depth = 0

        self.maze = maze

    def neighbours(self, state: State | None = None) -> list['Cell']:
        neighbours = []

        if self.x > 0:
            neighbours.append(self.maze.cells[self.y][self.x - 1])
        if self.x < len(self.maze.cells[0]) - 1:
            neighbours.append(self.maze.cells[self.y][self.x + 1])
        if self.y > 0:
            neighbours.append(self.maze.cells[self.y - 1][self.x])
        if self.y < len(self.maze.cells) - 1:
            neighbours.append(self.maze.cells[self.y + 1][self.x])

        if state is not None:
            neighbours = [cell for cell in neighbours if cell.state in state]

        return neighbours

    def distance(self, other: Self) -> int:
        return self.position.manhattan_distance(other.position)

    def state(self) -> State:
        return self.state

    def set_state(self, state: State):
        if self.state == State.START:
            raise Exception('Cannot change the state of the start cell.')

        if self.state == State.EXIT:
            raise Exception('Cannot change the state of the exit cell.')

        if self.state == State.WALL and state != State.WALL:
            raise Exception('Cannot change the state of a wall cell.')

        self.state = state
        # noinspection PyProtectedMember
        self.modified = self.maze._tick()

    def is_wall(self) -> bool:
        return self.state == State.WALL

    def is_empty(self) -> bool:
        return self.state == State.EMPTY

    def is_start(self) -> bool:
        return self.state == State.START

    def is_exit(self) -> bool:
        return self.state == State.EXIT

    def is_visited(self) -> bool:
        return self.state == State.VISITED

    def is_marked(self) -> bool:
        return self.state == State.MARKED

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cell):
            return NotImplemented

        return self.position == other.position

    def __hash__(self) -> int:
        return self.position.__hash__()

    def __str__(self) -> str:
        return self.position.__str__()


class Maze:
    time: Time
    cells: list[list[Cell]]

    _start: Position
    _exit: Position

    _hardcore: bool

    def _tick(self) -> Time:
        self.time.tick()
        return self.time

    def size(self) -> (int, int):
        return len(self.cells[0]), len(self.cells)

    def cell(self, position: Position) -> Cell:
        return self.cells[position.y][position.x]

    def cells(self, state: State | None = None) -> list[Cell]:

        # we no longer allow the user to get all nodes, only a subset
        if self._hardcore:
            if state is None:
                state = ~DENY
            else:
                state = state & ~DENY

        return [cell for row in self.cells for cell in row if
                state is None or cell.state in state]

    def random_cell(self, state: State | None = None) -> Cell:
        return choice(self.cells(state))

    def deepest_cell(self, state: State | None = None) -> Cell:
        return max(self.cells(state), key=lambda cell: cell.depth)

    def shallowest_cell(self, state: State | None = None) -> Cell:
        return min(self.cells(state), key=lambda cell: cell.depth)

    def newest_cell(self, state: State | None = None) -> Cell:
        return max(self.cells(state), key=lambda cell: cell.modified.t)

    def oldest_cell(self, state: State | None = None) -> Cell:
        return min(self.cells(state), key=lambda cell: cell.modified.t)

    @staticmethod
    def neighbours(cell: Cell, state: State | None = None) -> list[Cell]:
        return cell.neighbours(state)

    def start(self) -> Cell:
        return self.cell(self._start)

    def has_path(self):
        """
        Assert that we have a path from the start to the exit with `State.MARKED` cells.
        """

        start = self.start()

        stack = [start]
        while stack:
            cell = stack.pop()

            for neighbour in self.neighbours(cell, State.MARKED):
                if neighbour.is_exit():
                    return True

                stack.append(neighbour)

        return False

    def assert_path(self):
        """
        Assert that we have a path from the start to the exit with `State.MARKED` cells.
        """

        if not self.has_path():
            raise Exception('No path from start to exit.')
