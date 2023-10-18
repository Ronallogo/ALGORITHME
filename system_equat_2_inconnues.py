from functions_system_equat_2_inconnues import *


 
##############################################


system_equation = [[6, 1, 0], [1, 2, -3], [0, 0, 0]]
displays_sys_equation(system_equation, 2 , 2)
if system_equation[0][0] % system_equation[1][0] == 0 or 0 == system_equation[1][0] % system_equation[0][0]:
    print("compatible")
    coeff = coeff_dir_comp(system_equation, 0)
else:
    print("incompatible")
    coeff = coeff_dir_incomp(system_equation, 0)
resolve_sys_equation(system_equation, coeff)   


 
 