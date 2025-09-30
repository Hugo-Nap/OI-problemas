from pulp import *

#pedirle al usuario si quiere maximizar, presione tecla 1 o minimizar presoina tecla 2
min_max =int(input("Si quiere maximizar presione tecla 1 si quiere minimizar presione tecla 2"))

if(min_max == 1):
    problem = LpProblem("Metodo Simplex " , LpMaximize)
    else:
        LpMinimize("Metodo Simplex" , LpMinimize)

#variables automaticas
number_variables = int(input("Cuantas variables vas a ocupar: "))
variables = [LpVariable(f"x{i + 1}",lowBount = 0) for i in range(number_variables)]