import pandas as pd
import sympy as sp
import numpy as np
from fixedpoint import fixed_point
from newton import newton_raphson
import matplotlib.pyplot as plt

def run():
    x = sp.symbols('x')
    g = sp.sympify(9/x)
    f = sp.sympify(sp.tanh(x**2-9))
    value_fp, iteration_fp, error_fp= fixed_point(g,x,2.85,10**-4)
    value_nr, iteration_nr, error_nr = newton_raphson(f,x,2.85,10**-4)

#Escritura de los valores obtenidos por iteraciones de punto fijo
    df_fp = pd.DataFrame({"Iteraciones":iteration_fp,"Xn":value_fp,"Error":error_fp})
    df_nr= pd.DataFrame({"Iteraciones":iteration_nr,"Xn":value_nr,"Error":error_nr})
#Escritura de los valores obtenidos por iteraciones de punto fijo 
    with pd.ExcelWriter('salida.xlsx') as writer:
        df_fp.to_excel(writer, sheet_name="Fixed Point", index=False)
        df_nr.to_excel(writer, sheet_name="Newton-Raphson", index=False)

if __name__=="__main__":
    run()
