F = False
T = True

B_NAMES = {
    'F': False, 'T': True,
}

# Ranks from first
F0 = 0
F1 = 1
F2 = 2
F3 = 3
F4 = 4
F5 = 5
F6 = 6
F7 = 7
F8 = 8
F9 = 9
F_NAMES = {
    'F0': 0, 'F1': 1, 'F2': 2, 'F3': 3, 'F4': 4,
    'F5': 5, 'F6': 6, 'F7': 7, 'F8': 8, 'F9': 9,
}

# Ranks from last
L1 = -1
L2 = -2
L3 = -3
L4 = -4
L5 = -5
L6 = -6
L7 = -7
L8 = -8
L9 = -9
L10 = -10
L_NAMES = {
    'L1': -1, 'L2': -2, 'L3': -3, 'L4': -4, 'L5': -5,
    'L6': -6, 'L7': -7, 'L8': -8, 'L9': -9, 'L10': -10,
}
FL_NAMES = {
    'F0': 0, 'F1': 1, 'F2': 2, 'F3': 3, 'F4': 4,
    'F5': 5, 'F6': 6, 'F7': 7, 'F8': 8, 'F9': 9,
    'L1': -1, 'L2': -2, 'L3': -3, 'L4': -4, 'L5': -5,
    'L6': -6, 'L7': -7, 'L8': -8, 'L9': -9, 'L10': -10,
}

# Randomized symbols, such as colors
R0 = 0
R1 = 1
R2 = 2
R3 = 3
R4 = 4
R5 = 5
R6 = 6
R7 = 7
R8 = 8
R9 = 9
R4_NAMES = {
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3,
}

R8_NAMES = {
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3,
    'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
}

R_NAMES = {
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
    'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
}

# Generic int constants
NEG_TWO = -2
NEG_ONE = -1
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10

CONSTANTS = {
    'NEG_TWO': -2, 'NEG_ONE': -1, 'ZERO': 0, 'ONE': 1,
    'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6,
    'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10,
}

INT_GENERIC_CONSTANTS = CONSTANTS

# Specific color constants
BLACK = 0
BLUE = 1
RED = 2
GREEN = 3
YELLOW = 4
GRAY = 5
MAGENTA = 6
ORANGE = 7
CYAN = 8
BURGUNDY = 9

# Generic and specific color constant dict
COLORS = {
    'BLACK': 0, 'BLUE': 1, 'RED': 2, 'GREEN': 3, 'YELLOW': 4, 
    'GRAY': 5, 'MAGENTA': 6, 'ORANGE': 7, 'CYAN': 8, 'BURGUNDY': 9,
}

# Angle-like constants for mir_rot_[tf]
A0 = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
A5 = 5
A6 = 6
A7 = 7
A8 = 8
A9 = 9
A4_NAMES = {
    'A0': 0, 'A1': 1, 'A2': 2, 'A3': 3,
}

A8_NAMES = {
    'A0': 0, 'A1': 1, 'A2': 2, 'A3': 3,
    'A4': 4, 'A5': 5, 'A6': 6, 'A7': 7,
}

# Generic pair constants
DOWN = (1, 0)
RIGHT = (0, 1)
UP = (-1, 0)
LEFT = (0, -1)

ORIGIN = (0, 0)
UNITY = (1, 1)
NEG_UNITY = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)

ZERO_BY_TWO = (0, 2)
TWO_BY_ZERO = (2, 0)
TWO_BY_TWO = (2, 2)
THREE_BY_THREE = (3, 3)

PAIR_GENERIC_CONSTANTS = {
    'DOWN': (1, 0), 'RIGHT': (0, 1), 'UP': (-1, 0), 'LEFT': (0, -1),

    'ORIGIN': (0, 0), 'UNITY': (1, 1), 'NEG_UNITY': (-1, -1),
    'UP_RIGHT': (-1, 1), 'DOWN_LEFT': (1, -1),

    'ZERO_BY_TWO': (0, 2), 'TWO_BY_ZERO': (2, 0),
    'TWO_BY_TWO': (2, 2), 'THREE_BY_THREE': (3, 3),
}

GENERIC_CONSTANTS = INT_GENERIC_CONSTANTS | PAIR_GENERIC_CONSTANTS
ALL_CONSTANTS = B_NAMES | FL_NAMES | R_NAMES | COLORS | GENERIC_CONSTANTS
ALL_CONSTANT_NAMES = [*ALL_CONSTANTS]