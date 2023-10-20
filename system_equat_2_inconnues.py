from functions_system_equat_2_inconnues import *


 
##############################################

#creation d 'un systeme
system_equation = [[6, 1, 0], [1, 2, -3], [0, 0, 0]]
#afficher le systeme
displays_sys_equation(system_equation, 2 , 2)
# verification pour determiner si les premiers termes des deux equations
#sont multiples de l'un ou de l'autre

if system_equation[0][0] % system_equation[1][0] == 0 or 0 == system_equation[1][0] % system_equation[0][0]:
    print("compatible")
    #retourne un coefficient correspondant --> voir dns le fichiers_des_fonctions de cet exercices
    coeff = coeff_dir_comp(system_equation, 0)
else:
    #dans le cas contraire
    print("incompatible")
        #retourne les coefficients correspondants --> voir dns le fichiers_des_fonctions de cet exercices

    coeff = coeff_dir_incomp(system_equation, 0)
solutions(resolve_sys_equation(system_equation, coeff))   


 
 