from pulp import *

#pedirle al usuario si quiere maximizar, presione tecla 1 o minimizar presoina tecla 2
min_max =int(input("Si quiere maximizar presione tecla 1 si quiere minimizar presione tecla 2"))

if(min_max == 1):
    problem = LpProblem("Metodo Simplex " , LpMaximize)
elif(min_max == 2):
    problem = LpProblem("Metodo Simplex" , LpMinimize)
else: 
    print ("Dato invalido, intentelo de nuevo..")

#variables automaticas
number_variables = int(input("Cuantas variables vas a ocupar: "))
variables = [LpVariable(f"x{i + 1}",lowBound = 0) for i in range(number_variables)]
funtion_objective = 0

# ingreso de la funcion objetivo
for i in range(number_variables):
    z_coefficients = float(input(f"ingrese el coeficiente de la variable x {i + 1}"))
    # mostrar variables con su coeficiente
    print(f"Coeficiente de x1: {i + 1} : {z_coefficients}")
    funtion_objective += z_coefficients * variables[i]
problem = funtion_objective + problem

#restricciones
number_restriction = int(input("cuantas restricciones va a ingresarse "))
for i in range(int (number_restriction))
    coefficients = []#lista vacia llamada coeficientes
    for j in range(int (number_variables))
    coeff = float(input(f"ingrese el coeficiente de la variable x {j + 1} en la restriccion {i + 1}: "))
    print(f"coeficiente de x {j + 1} en la restriccion {i + 1} : {coeff}") 
    coefficients.append(coeff)#agrega el valor al final de la lista
restrition = sum(coefficients[j] *  variables[j] for j in range (int(number_variables)))
lim = float(input(f"ingresa el valor limite de la restriccion {i + 1}": ))
problem = (restrition <= lim)#acomodar las resticciones de acuerdo al ejercicio

#resolver problema
problem.solve()
print("Estado: ", LpStatus[problem.status])
print("Valor de la funcion objetivo: ", value(problem.objective))
print("Valores de las variables: ")
for v in problem.variables():
    print(f"{v.name} = {v.varValue}")