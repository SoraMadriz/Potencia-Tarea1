import sympy
def newton_raphson(f,x,x0,error):
#Lista de valores que se pasarán al excel
    iterations_list  =[]
    value_ant_list=[]
    error_list=[]
#declaración de variables
    df=sympy.diff(f,x)
    x_ant = x0
    iteration=0
#Algoritmo solicitado
    while True:
        x_act = x_ant - (f.subs(x,x_ant).evalf() / df.subs(x,x_ant).evalf())
        iteration += 1

        #Se añaden los nuevo valores a la salida
        iterations_list.append(iteration)
        value_ant_list.append(round(x_ant,4))
        error_list.append(abs(round(x_act - x_ant,4)))

        #Se verifica la condición
        if abs(x_act-x_ant) < error or iteration > 100:
            break
        else:
            x_ant = x_act

    return value_ant_list, iterations_list, error_list

