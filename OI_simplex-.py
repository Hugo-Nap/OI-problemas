from pulp import *

#variables automaticas
number_variables = int(input("Cuantas variables vas a ocupar: "))
variables = [LpVariable(f"x{i + 1}",lowBount = 0) for i in range(number_variables)]