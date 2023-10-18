from functions_system_equat_2_inconnues import *


def variable_eliminator(myMatrice , coeff):
    result = list()
    result = myMatrice.copy()
    if isinstance(coeff , int) or isinstance( coeff , float) :
        if coeff == (myMatrice[0][0] * -1) :
            result[0] = [coeff * myMatrice[0][i]  for i in range(len(myMatrice[0]))]
        elif coeff == (myMatrice[1][0] * -1) :
         result[1] = [coeff * myMatrice[1][i]  for i in range(len(myMatrice[1]))]

    elif type(coeff) == list :
        result[0] = [coeff[1] * myMatrice[0][i]  for i in range(len(myMatrice[0]))]
        result[1] = [coeff[0] * myMatrice[1][i]  for i in range(len(myMatrice[1]))]                                                                                                                                                                             
    else : 
        print("error")
    result.append([])
    result[2] = [myMatrice[0][i] + myMatrice[1][i] for i in range(len(myMatrice[0]))]
    return result[2]
 
 

    

def setSystem(myMatrice):
    pivot = list()
    turnExc = 0
    operator = list()
    pivot.append(myMatrice[0])
     
    operator.append(pivot[0])
    operator.append(myMatrice[2])
    if operator[0][0] % operator[1][0] == 0 or 0 == operator[1][0] % operator[0][0]:
        print("compatible")
        coeff = coeff_dir_comp(operator, 0)
    else:
        print("incompatible")
        coeff = coeff_dir_incomp(operator, 0)
    print(coeff , " <-- coefficient")
    x = variable_eliminator(operator  , coeff)
    print(x) 
    pivot.append(x)
    

 
mySystem = [[2,2,3,1 , -1],[4,1,3,0 , 1],[1,4,-1,2 , 0],[1,-1,2,4 , -2]]
   
displays_sys_equation(mySystem , 4 ,4)  
setSystem(mySystem)
    