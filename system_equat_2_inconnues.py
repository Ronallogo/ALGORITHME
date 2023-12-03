from functions_system_equat_2_inconnues import *


 
##############################################

#creation d 'un systeme
system_equation = [[3, -1, 0], [5, 2, 22], [0, 0, 0]]
#afficher le systeme
displays_sys_equation(system_equation, 2 , 2)
# verification pour determiner si les premiers termes des deux equations
#sont multiples de l'un ou de l'autre
coeff = coeff_dir_incomp(system_equation, 0)
solutions(resolve_sys_equation(system_equation, coeff))   


 
 