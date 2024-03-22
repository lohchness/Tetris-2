# COMP30024 Artificial Intelligence, Semester 1 2024
# Project Part A: Single Player Tetress

from .core import PlayerColor, Coord, PlaceAction, Direction
from .utils import render_board

import collections

DIRECTIONS = [Direction.Up, Direction.Down, Direction.Left, Direction.Right]

def search(
    board: dict[Coord, PlayerColor], 
    target: Coord
) -> list[PlaceAction] | None:
    """
    This is the entry point for your submission. You should modify this
    function to solve the search problem discussed in the Part A specification.
    See `core.py` for information on the types being used here.

    Parameters:
        `board`: a dictionary representing the initial board state, mapping
            coordinates to "player colours". The keys are `Coord` instances,
            and the values are `PlayerColor` instances.  
        `target`: the target BLUE coordinate to remove from the board.
    
    Returns:
        A list of "place actions" as PlaceAction instances, or `None` if no
        solution is possible.
    """

    # The render_board() function is handy for debugging. It will print out a
    # board state in a human-readable format. If your terminal supports ANSI
    # codes, set the `ansi` flag to True to print a colour-coded version!
    print(render_board(board, target, ansi=False))


    ########################################


    # bfs_queue = collections.deque()

    # # Add the initial state to the queue
    # for coord, val in board.items():
    #     if val == PlayerColor.RED:
    #         bfs_queue.append(coord)
    #         print(coord.r, coord.c)
    
    # # board_check(board)
            
    # while (bfs_queue):
    #     current_coord = bfs_queue.pop()

    #     for i in range(4):
    #         new_coord = current_coord.__add__(DIRECTIONS[i])
    #         if not is_in_board(new_coord, board):
    #             bfs_queue.append(new_coord)
    #             print(new_coord.r, new_coord.c)
    #             board_check(board)

    for key, val in board.items():
        if val == PlayerColor.RED:
            red = key

    actions = possible_actions(Coord(1, 4), board)
    result = []
    for c in actions:
        action = PlaceAction(c[0], c[1], c[2], c[3])
        result.append(action)
        

    print(render_board(board, target, ansi=False))

    return None

    ########################################
    

    # Here we're returning "hardcoded" actions as an example of the expected
    # output format. Of course, you should instead return the result of your
    # search algorithm. Remember: if no solution is possible for a given input,
    # return `None` instead of a list.
    return [
        PlaceAction(Coord(2, 5), Coord(2, 6), Coord(3, 6), Coord(3, 7)),
        PlaceAction(Coord(1, 8), Coord(2, 8), Coord(3, 8), Coord(4, 8)),
        PlaceAction(Coord(5, 8), Coord(6, 8), Coord(7, 8), Coord(8, 8)),
    ]


# Check if coordinate is in board
def is_in_board(coord: Coord, board: dict[Coord, PlayerColor]) -> bool:
    for key in board.keys():
        if key.r == coord.r and key.c == coord.c:
            return True
    return False

def board_check(board: dict[Coord, PlayerColor]):
    row_counts = collections.defaultdict(int)
    col_counts = collections.defaultdict(int)

    rows_to_remove = []
    cols_to_remove = []
    # Count the number of pieces in each row and column
    for coord in board.keys():
        row_counts[coord.r] += 1
        col_counts[coord.c] += 1
        # If a row or column has 11 pieces, keep track of the row/column number
        if row_counts[coord.r] == 11:
            rows_to_remove.append(coord.r)
        if col_counts[coord.c] == 11:
            cols_to_remove.append(coord.c)

    keys_to_remove = []
    # Remove the coords that match the row/column number that were kept track of
    for coord in board.keys():
        if coord.r in rows_to_remove:
            keys_to_remove.append(coord)
        if coord.c in cols_to_remove:
            keys_to_remove.append(coord)

    for key in keys_to_remove:
        if key in board:
            del board[key]


#Check all tetrominos that can be placed around start cell
def possible_actions( start: Coord, board:dict[Coord, PlayerColor]):
    
    result = dls(start, board, tetromino=[], actions = [])
    return result


def dls(start: Coord, 
        board: dict[Coord, PlayerColor], 
        shape, actions
)->list[list]:
    
    for c in [start.right(), start.left(), start.up(), start.down()]:
        if c not in board and c not in shape:
            shape.append(c)
            """
            possible solution for T shape
            if len(shape) == 3:
                mid = shape[1]
                for i in [mid.right(), mid.left(), mid.up(), mid.down()]:
                    if i not in board and i not in shape:
                        shape.append(i)
                        actions.append(shape.copy())
                        shape.pop()
            """
            if len(shape) == 4:
                actions.append(shape.copy())
                shape.pop()
            else:
                dls(c, board, shape, actions)
        
        # Pop a coordinate from shape after all its successors
        # has been explored
        if c == start.down() and shape:
                shape.pop()

    return actions



# Assumes piece is one coordinate for now
def heuristic(board: dict[Coord, PlayerColor], piece: Coord, target: Coord) -> int:
    """
    Heuristic function: distance from piece to target's horizontal or vertical
    """




    return 0