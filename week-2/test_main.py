# Alexander Holmes
# CIS-226
# 9/9/22

from main import add

# Import our add function (that isn't written yet)


# Create a test function (any function that starts with test)
def test_add():
    # Use an assert statement
    # We expect 1 + 3 to equal 4
    assert add(1, 3) == 4

def test_add_swapped():
    """You can add a docstring to explain the test
    Check same results when arguments swapped
    """
    # We expect 3 + 1 to equal 1 + 3 and to equal 4
    assert add(3, 1) == add(1, 3) == 4

def test_add_multiple():
    """You can assert multiple things in the same function"""
    assert add(1, 1) == 2
    assert add(-1, -1) == -2
    assert add(1, 0) == 1


def create_board(board):
    board = [
        ['X', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'X', 'O'],
    ]
    return board

def test_create_board_not_replaced():
    original = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]
    original_row1 = original[0]
    original_row2 = original[1]
    original_row3 = original[2]
    new = create_board(original)
    # Check like normal:
    assert new == EXPECTED
    # Now check original was updated
    assert original == EXPECTED
    # And check the rows were not replaced, but updated also
    assert original_row1 == EXPECTED[0]
    assert original_row2 == EXPECTED[1]
    assert original_row3 == EXPECTED[2]


EXPECTED = [
    ['X', 'O', 'O'],
    ['O', 'X', 'X'],
    ['X', 'X', 'O'],
]


def test_create_board():
    board = [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*'],
    ]
    board = create_board(board)
    assert board == EXPECTED