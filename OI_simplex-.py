from pulp import *

#pedirle al usuario si quiere maximizar, presione tecla 1 o minimizar presoina tecla 2
min_max =int(input("Si quiere maximizar presione tecla 1 si quiere minimizar presione tecla 2"))

if(min_max == 1):
    problem = LpProblem("Metodo Simplex " , LpMaximize)
    else if(min_max == 2):
        problem = LpProblem("Metodo Simplex" , LpMinimize)
    else: 
        print ("Dato invalido, intentelo de nuevo..")

#variables automaticas
number_variables = int(input("Cuantas variables vas a ocupar: "))
variables = [LpVariable(f"x{i + 1}",lowBount = 0) for i in range(number_variables)]
funtion_objective = 0

# ingreso de la funcion onjetivo
for i in range(number_variables):
    z_coefficients = float(input("ingrese el coeficiente de la variable x {i + 1}"))
    # mostrar variables con su coeficiente
    print(f"Coeficiente de x1: {i + 1} : {z_coefficients}")
    funtion_objective += z_coefficients * variables[i]
problem = funtion_objective + problem

#restricciones
number_restriction = int(input("cuantas restricciones va a ingresarse "))
for i in range(int (number_restriction))
    coefficients = []#lista vacia llamada coeficientes
    for j in range(int (number_variables))
    coeff = float(input("ingrese el coeficiente de la variable x {j + 1} en la restriccion {i + 1}"))
    print(f"coeficiente de x {j + 1} en la restriccion {i + 1} : {coeff}") 
    coefficients.append(coeff)#agrega el valor al final de la lista
restrition = sum(coefficients[j] *  variable[j] for j in range (int(number_variables)))
lim = float(input("ingresa el valor limite de la restriccion {i + 1}"))
problem = (restriccion <= lim)#acomodar los ejercicios de acuerdo al ejercicio

#resolver problema
    