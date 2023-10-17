from functions import *

system_equation = [[1, 1, 0], [1, 2, -3], [0, 0, 0]]
displays_sys_equation(system_equation, 2 , 2)
coeff = returnCoeff(system_equation)   
resolve_sys_equation(system_equation, coeff)
