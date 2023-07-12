import abc
from copy import deepcopy
from dataclasses import dataclass
from enum import IntFlag, auto
from random import choice, randrange, shuffle
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


@dataclass(frozen=True, slots=True, match_args=True, order=True, init=True, repr=True)
class Position:
    x: int
    y: int

    def manhattan_distance(self, other: Self) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidean_distance(self, other: Self) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def components(self) -> tuple[int, int]:
        return self.x, self.y


class Cell:
    position: Position

    _state: State
    depth: int
    modified: Time

    maze: 'Maze'

    def __init__(self, position: Position, maze: 'Maze'):
        self.position = position

        self.depth = 0
        self._state = State.EMPTY

        self.maze = maze

    # noinspection PyProtectedMember
    def neighbours(self, state: State | None = None) -> list['Cell']:
        neighbours = []

        x, y = self.position.components()

        if x > 0:
            neighbours.append(self.maze._cells[y][x - 1])
        if x < len(self.maze._cells[0]) - 1:
            neighbours.append(self.maze._cells[y][x + 1])
        if y > 0:
            neighbours.append(self.maze._cells[y - 1][x])
        if y < len(self.maze._cells) - 1:
            neighbours.append(self.maze._cells[y + 1][x])

        if state is not None:
            neighbours = [cell for cell in neighbours if cell._state in state]

        return neighbours

    def distance(self, other: Self) -> int:
        return self.position.manhattan_distance(other.position)

    def state(self) -> State:
        return self._state

    def set_state(self, state: State):
        if self._state == State.START:
            raise Exception('Cannot change the state of the start cell.')

        if self._state == State.EXIT:
            raise Exception('Cannot change the state of the exit cell.')

        if self._state == State.WALL and state != State.WALL:
            raise Exception('Cannot change the state of a wall cell.')

        self.maze.snapshots.append(deepcopy(self))

        self._state = state
        # noinspection PyProtectedMember
        self.modified = self.maze._tick()

    def _copy(self) -> Self:
        copy = Cell(self.position, self.maze)
        copy._state = self._state
        copy.depth = self.depth

        return copy

    def is_wall(self) -> bool:
        return self._state == State.WALL

    def is_empty(self) -> bool:
        return self._state == State.EMPTY

    def is_start(self) -> bool:
        return self._state == State.START

    def is_exit(self) -> bool:
        return self._state == State.EXIT

    def is_visited(self) -> bool:
        return self._state == State.VISITED

    def is_marked(self) -> bool:
        return self._state == State.MARKED

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
    _cells: list[list[Cell]]

    snapshots: list[Cell]

    _start: Position
    _exit: Position

    _hardcore: bool

    # noinspection PyProtectedMember
    def generate(self, width: int, height: int):
        generator = Prims(height, width)
        grid = generator.generate()
        start, end = generator.entrances(grid)

        self._cells = [[Cell(Position(x, y), self) for x in range(width)] for y in
                       range(height)]

        # not using setter to not increase time
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if (x, y) == start:
                    self._cells[y][x]._state = State.START

                elif (x, y) == end:
                    self._cells[y][x]._state = State.EXIT

                if cell == 1:
                    self._cells[y][x]._state = State.WALL

        self._start = Position(*start)
        self._exit = Position(*end)

    def __init__(self, width: int, height: int):
        self.time = Time()

        self.generate(width, height)

        self.snapshots = []

        self._hardcore = False

    def _tick(self) -> Time:
        self.time.tick()
        return self.time

    def enable_hardcore(self):
        self._hardcore = True

    def _apply_snapshot(self, snapshot: Cell):
        self._cells[snapshot.position.y][snapshot.position.x] = snapshot

    def size(self) -> (int, int):
        return len(self._cells[0]), len(self._cells)

    def cell(self, position: Position) -> Cell:
        return self._cells[position.y][position.x]

    def cells(self, state: State | None = None) -> list[Cell]:
        # we no longer allow the user to get all nodes, only a subset
        if self._hardcore:
            if state is None:
                state = ~DENY
            else:
                state = state & ~DENY

        return [cell for row in self._cells for cell in row if
                state is None or cell.state() in state]

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
        visited = {start.position}

        while stack:
            cell = stack.pop()

            for neighbour in self.neighbours(cell, State.MARKED):
                if neighbour.position in visited:
                    continue

                if neighbour.is_exit():
                    return True

                stack.append(neighbour)
                visited.add(neighbour.position)

        return False

    def assert_path(self):
        """
        Assert that we have a path from the start to the exit with `State.MARKED` cells.
        """

        if not self.has_path():
            raise Exception('No path from start to exit.')

    def export(self):
        ...


# Taken from https://github.com/john-science/mazelib/tree/main
class GenerationAlgorithm(abc.ABC):
    def __init__(self, h, w):
        """Maze Generator Algorithm constructor

        Attributes:
            h (int): height of maze, in number of hallways
            w (int): width of maze, in number of hallways
            H (int): height of maze, in number of hallways + walls
            W (int): width of maze, in number of hallways + walls
        """
        assert w >= 3 and h >= 3, "Mazes cannot be smaller than 3x3."
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1

    @abc.abstractmethod
    def generate(self) -> list[list[int]]:
        raise NotImplementedError

    """ All of the methods below this are helper methods,
    common to many maze-generating algorithms.
    """

    def _find_neighbors(self, row: int, col: int, grid: list[list[int]], is_wall=False):
        """Find all the grid neighbors of the current position; visited, or not.

        :param row: row of cell of interest
        :param col: column of cell of interest
        :param grid: 2D maze grid
        :param is_wall: Are we looking for neighbors that are walls, or open cells?
        :return: all neighboring cells that match our request
        """
        ns = []

        if row > 1 and grid[row - 2][col] == is_wall:
            ns.append((row - 2, col))
        if row < self.H - 2 and grid[row + 2][col] == is_wall:
            ns.append((row + 2, col))
        if col > 1 and grid[row][col - 2] == is_wall:
            ns.append((row, col - 2))
        if col < self.W - 2 and grid[row][col + 2] == is_wall:
            ns.append((row, col + 2))

        shuffle(ns)
        return ns


class Prims(GenerationAlgorithm):
    """
    The Algorithm

    1. Choose an arbitrary cell from the grid, and add it to some
        (initially empty) set visited nodes (V).
    2. Randomly select a wall from the grid that connects a cell in
        V with another cell not in V.
    3. Add that wall to the Minimal Spanning Tree (MST), and the edge's other cell to V.
    4. Repeat steps 2 and 3 until V includes every cell in G.
    """

    def generate(self) -> list[list[int]]:
        """
        highest-level method that implements the maze-generating algorithm
        """

        # create empty grid
        grid = [deepcopy([1] * self.W) for _ in range(self.H)]

        # choose a random starting position
        row = randrange(1, self.H, 2)
        col = randrange(1, self.W, 2)
        grid[row][col] = 0

        # created a weighted list of all vertices connected in the graph
        neighbors = self._find_neighbors(row, col, grid, True)

        # loop over all current neighbors, until empty
        visited = 1

        while visited < self.h * self.w:
            # find neighbor with lowest weight, make it current
            nn = randrange(len(neighbors))
            row, col = neighbors[nn]

            visited += 1
            grid[row][col] = 0

            neighbors = neighbors[:nn] + neighbors[nn + 1:]
            # connect that neighbor to a random neighbor with grid[posi] == 0
            nearest_n0, nearest_n1 = self._find_neighbors(
                row, col, grid
            )[0]
            grid[(row + nearest_n0) // 2][(col + nearest_n1) // 2] = 0

            # find all unvisited neighbors of current, add them to neighbors
            unvisited = self._find_neighbors(row, col, grid, True)
            neighbors = list(set(neighbors + unvisited))

        return grid

    def entrances(self, grid: list[list[int]], depth: int = 0):
        """Generate maze entrances, along the outer walls.

        Returns: None
        """

        start_side = randrange(4)

        # maze entrances will be on opposite sides of the maze.
        if start_side == 0:
            start = (0, randrange(1, self.W, 2))  # North
            # check that one down from start is not a wall
            if grid[1][start[1]] == 1:
                return self.entrances(grid, depth=depth + 1)

            end = (self.H - 1, randrange(1, self.W, 2))
            if grid[self.H - 2][end[1]] == 1:
                return self.entrances(grid, depth=depth + 1)

        elif start_side == 1:
            start = (self.H - 1, randrange(1, self.W, 2))  # South
            if grid[self.H - 2][start[1]] == 1:
                return self.entrances(grid, depth=depth + 1)

            end = (0, randrange(1, self.W, 2))
            if grid[1][end[1]] == 1:
                return self.entrances(grid, depth=depth + 1)
        elif start_side == 2:
            start = (randrange(1, self.H, 2), 0)  # West
            if grid[start[0]][1] == 1:
                return self.entrances(grid, depth=depth + 1)

            end = (randrange(1, self.H, 2), self.W - 1)
            if grid[end[0]][self.W - 2] == 1:
                return self.entrances(grid, depth=depth + 1)
        else:
            start = (randrange(1, self.H, 2), self.W - 1)  # East
            if grid[start[0]][self.W - 2] == 1:
                return self.entrances(grid, depth=depth + 1)

            end = (randrange(1, self.H, 2), 0)
            if grid[end[0]][1] == 1:
                return self.entrances(grid, depth=depth + 1)

        # ensure that the start and end are not placed in a boring spot
        if abs(start[0] - end[0]) + abs(start[1] - end[1]) < 2:
            # if we've tried enough times, just give up and
            # return the boring start and end
            if depth > 32:
                return start, end

            self.entrances(grid, depth=depth + 1)

        return start, end


def print_grid(grid: list[list[int]], start: tuple[int, int] = None,
               end: tuple[int, int] = None):
    def char(state: int, row: int, col: int):
        if (row, col) == start:
            return 'S'

        if (row, col) == end:
            return 'E'

        if state == 1:
            return '█'

        return ' '

    for y, row in enumerate(grid):
        print(''.join([char(state, y, x) for x, state in enumerate(row)]))

#
# if __name__ == '__main__':
#     generator = Prims(10, 10)
#     grid = generator.generate()
#     start, end = generator.entrances(grid)
#
#     print_grid(grid, start, end)
