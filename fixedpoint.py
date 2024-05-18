import sympy
def fixed_point(f,x,x0,error):
# Lista de los elementos que se verán en el excel
    iterations_list  =[]
    value_ant_list=[]
    error_list=[]
#Declaración de variables 
    x_ant = x0
    iteration = 0
#Algoritmo solicitado
    while True:
        x_act = f.subs(x,x_ant).evalf()
        iteration+=1

        #Se añaden los nuevo valores a la salida
        iterations_list.append(iteration)
        value_ant_list.append(round(x_ant,4))
        error_list.append(round(abs(x_act - x_ant),4))

        #Se verifica la condición
        if abs(x_act - x_ant)<error or iteration>50:
            break
        else:
            x_ant = x_act

    
    return value_ant_list, iterations_list, error_list




