from z3 import *

x = Int('x')
y = Int('y')
z = Int('z')

solve(5*x - 6*y + 3*z == 153, 2*x + 5*y - 7*z == -163, 4*x + 8*y + 8*z == -28)
