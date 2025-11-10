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
NEG_TEN = -10
NEG_NINE = -9
NEG_EIGHT = -8
NEG_SEVEN = -7
NEG_SIX = -6
NEG_FIVE = -5
NEG_FOUR = -4
NEG_THREE = -3
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
HUNDRED = 100
THOUSAND = 1000

CONSTANTS = {
    'NEG_TEN': -10, 'NEG_NINE': -9, 'NEG_EIGHT': -8,
    'NEG_SEVEN': -7, 'NEG_SIX': -6, 'NEG_FIVE': -5,
    'NEG_FOUR': -4, 'NEG_THREE': -3, 'NEG_TWO': -2, 
    'NEG_ONE': -1, 'ZERO': 0, 'ONE': 1, 'TWO': 2, 
    'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6,
    'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10,
    'HUNDRED': 100, 'THOUSAND': 1000,
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

# Scale constants for scale_[tf]
SM2 = 2
SM3 = 3
SD2 = -2
SD3 = -3
S4_NAMES = {
    'SM2': 2, 'SM3': 3, 'SD2': -2, 'SD3': -3,
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

# Type ranges for mutation generation
INT_TYPE_RANGES = {
    'F_': F_NAMES,
    'FL': FL_NAMES,
    'L_': L_NAMES,
    'R_': R_NAMES,
    'R4': R4_NAMES,
    'R8': R8_NAMES,
    'A4': A4_NAMES,
    'A8': A8_NAMES,
    'C_': COLORS,
    'Integer': CONSTANTS,
}

PAIR_TYPE_RANGES = {
    'IJ': PAIR_GENERIC_CONSTANTS,
}

# Type overlap compatibility map
# Each old hint maps to the set of hints it's compatible with
# Based on type definitions in arc_types.py
HINT_OVERLAPS = {
    # Base container types - now exclusively tuple-based
    'Tuple': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'Container': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'ContainerContainer': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'Callable': {'Callable'},
    
    # Numeric types - range/rank indices
    # NOTE: Boolean = bool is a subtype of int in Python (True=1, False=0)
    # Therefore Boolean is compatible with all Integer and range types
    'Boolean': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_'},
    'Integer': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_'},
    'Numerical': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_', 'IJ'},
    
    # Integer ranges - all compatible with each other and Integer/Numerical
    'F_': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'R_', 'R4', 'R8', 'C_'},
    'FL': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_'},
    'L_': {'Boolean', 'Integer', 'Numerical', 'L_', 'FL'},
    'R_': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'R4': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'R8': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'A4': {'Boolean', 'Integer', 'Numerical', 'A4', 'A8'},
    'A8': {'Boolean', 'Integer', 'Numerical', 'A4', 'A8'},
    'C_': {'Boolean', 'Integer', 'Numerical', 'C_', 'F_', 'R_', 'R4', 'R8'},
    'I_': {'Boolean', 'Integer', 'Numerical'},
    'J_': {'Boolean', 'Integer', 'Numerical'},
    'IJ': {'Numerical', 'IJ'},
    
    # Specific tuple types - consolidated from frozenset variants
    'Indices': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Object': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Objects': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Grid': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'Samples': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'TupleTuple': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'TTT_iii': {'TupleTuple', 'Tuple', 'Container', 'ContainerContainer'},
    'Colors': {'Tuple', 'Container', 'ContainerContainer'},
    'Cell': {'Cell', 'Tuple', 'Container'},
    
    # Generic catch-all types
    'Any': {'Any', 'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_', 'IJ', 'Tuple', 'Container', 'ContainerContainer', 'Callable', 'Grid', 'Samples', 'TTT_iii', 'Cell', 'Colors', 'Object', 'Objects', 'Indices', 'TupleTuple'},
}

GENERIC_CONSTANTS = INT_GENERIC_CONSTANTS | PAIR_GENERIC_CONSTANTS
GENERIC_CONSTANT_NAMES = [*GENERIC_CONSTANTS]
ALL_CONSTANTS = B_NAMES | FL_NAMES | R_NAMES | COLORS | GENERIC_CONSTANTS
ALL_CONSTANT_NAMES = [*ALL_CONSTANTS]