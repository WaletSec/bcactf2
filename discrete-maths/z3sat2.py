from z3 import *

a = Int('a')
b = Int('b')
c = Int('c')

solve(a != 0, -b / (2*a) == 2, a * 2 * 2 + b * 2 + c == -2, b * b - 4 * a * c == 16)
