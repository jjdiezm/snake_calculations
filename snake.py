# Snake calculations for Python 3+
# Usage python snake.py

# Problem constraits
MAX_COLS = 10
MAX_ROWS = 10


def test_board(board):
    """ Test whether a board is according requierements or not

    :param board: must be an array of integers [rows, cols] according problem constraints
    :return: Boolean
    """
    if isinstance(board, list):
        if len(board) == 2:
            if board[0] <= MAX_COLS and board[1] <= MAX_ROWS:
                return True
    return False


def test_snake(snake):
    """ Test whether a snake is well-formed or not (adjacent coordinates with no intersections)

    :param snake: array of arrays with the snake shape
    :return: Boolean
    """
    passed_snake = list()
    if isinstance(snake, list):
        for element in snake:
            if isinstance(element, list):
                if len(element) == 2:
                    if isinstance(element[0], int) and isinstance(element[1], int):
                        if element[0] >= 0 and element[1] >= 0:
                            if len(passed_snake) > 0:
                                if passed_snake[-1][0] != element[0] and passed_snake[-1][1] != element[1]:
                                    # Error. Snake is not adjacent
                                    return False
                                else:
                                    if element in passed_snake:
                                        return False
                                    else:
                                        passed_snake.append(element)
                            else:
                                passed_snake.append(element)
                        else:
                            # Error. Not valid coordinates on Snake definition - negative values
                            return False
                    else:
                        # Error. Not valid coordinates on Snake definition - not int values
                        return False
                else:
                    # Error. Not valid coordinates on Snake definition - not 2d coordinates
                    return False
            else:
                # Error. Not valid Snake definition - not list of coordinates
                return False
    else:
        # Error. Not valid Snake definition not list of coordinates
        return False
    return True


def test_inbounds(coordinate, board):
    """ Function to Calculate if a coordinate is inside the board

    :param coordinate: list of row, col
    :param board: must be an array of integers [rows, cols]
    :return: Boolean
    """
    if 0 <= coordinate[0] <= board[0]-1:
        if 0 <= coordinate[1] <= board[1]-1:
            return True
    return False


def move_snake(snake, direction):
    """ Function that returns the snake moved

    :param snake: array of arrays with the snake shape
    :param direction: right, left, up or down
    :return: snake moved
    """
    head = snake[0]
    new_snake = list()
    if direction == "right":
        new_snake.append([head[0]+1, head[1]])
    elif direction == "left":
        new_snake.append([head[0]-1, head[1]])
    elif direction == "up":
        new_snake.append([head[0], head[1]+1])
    elif direction == "down":
        new_snake.append([head[0], head[1]-1])
    new_snake.extend(snake)
    return new_snake


def run_path(board, snake, depth, snake_list):
    """ Recursive function to find the valid paths

    :param board: must be an array of integers [rows, cols] according problem constraints
    :param snake: array of arrays with the snake shape (adjacent coordinates with no intersections)
    :param depth: number of movements to be done
    :param snake_list: list of valid paths
    :return: list of valid paths
    """
    head = snake[0]
    if test_inbounds(head, board) and test_snake(snake):
        if depth > 0:
            snake_list = run_path(board, move_snake(snake, "right"), depth-1, snake_list)
            snake_list = run_path(board, move_snake(snake, "left"), depth-1, snake_list)
            snake_list = run_path(board, move_snake(snake, "up"), depth-1, snake_list)
            snake_list = run_path(board, move_snake(snake, "down"), depth-1, snake_list)
        else:
            snake_list.append(snake)
    return snake_list


def available_paths(board, snake, depth):
    """ Function to Calculate the number of paths available on a Snake board

    :param board: must be an array of integers [rows, cols] according problem constraints
    :param snake: array of arrays with the snake shape (adjacent coordinates with no intersections)
    :param depth: number of movements to be done
    :return: Number of available paths
    """
    if test_board(board):
        if test_snake(snake):
            if isinstance(depth, int):
                if 1 <= depth <= 20:
                    list_result = run_path(board, snake, depth, [])
                else:
                    return "Depth must be an integer between 1 and 20"
            else:
                return "Depth must be an integer between 1 and 20"
        else:
            return "Error on snake definition not according requisites"
    else:
        return "Error on board definition not according requisites"
    return len(list_result)


board_used = [4, 3]
snake_used = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
paths = available_paths(board_used, snake_used, 3)
print(paths)


board_used = [2, 3]
snake_used = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
paths = available_paths(board_used, snake_used, 10)
print(paths)

board_used = [10, 10]
snake_used = [[5, 5], [5, 4], [4, 4], [4, 5]]
paths = available_paths(board_used, snake_used, 4)
print(paths)
