from functions_system_equat_2_inconnues import *


def variable_eliminator(myMatrice , coeff , nbrVar):
    result = list()
    result.append(myMatrice[0])
    result.append(myMatrice[1])
    print("result : "  , result)
    if isinstance(coeff , int) or isinstance( coeff , float) :
        if myMatrice[0][0] % myMatrice[1][0]  == 0 and  myMatrice[1][0] <= myMatrice[0][0]:
            print("inside 1")
            result[1] = [coeff * myMatrice[1][i]  for i in range(len(myMatrice[0]))]
            print(result)
           
        elif  myMatrice[1][0] % myMatrice[0][0]  == 0 and myMatrice[1][0] >= myMatrice[0][0] :
            print("inside 2")
            result[0] = [coeff * myMatrice[0][i]  for i in range(len(myMatrice[1]))]
            print(result)
          
        else : 
            print("error to isinstance -  int")

    elif type(coeff) == list :
        result[0] = [coeff[1] * myMatrice[0][i]  for i in range(len(myMatrice[0]))]
        result[1] = [coeff[0] * myMatrice[1][i]  for i in range(len(myMatrice[1]))]                                                                                                                                                                             
    else : 
        print("error")
   
    x = [result[0][i] + result[1][i] for i in range(nbrVar)]
    return x
 
 
 
 
 
def setSystem(myMatrice):
    pivot = list()
    turnExc = 0
    operator = list()
    pivot.append(myMatrice[0])
     
    operator.append(pivot[0])
    operator.append(myMatrice[1])
    if operator[0][0] % operator[1][0] == 0 or 0 == operator[1][0] % operator[0][0]:
        print("compatible")
        coeff = coeff_dir_comp(operator, 0)
    else:
        print("incompatible")
        coeff = coeff_dir_incomp(operator, 0)
    print(coeff , " <-- coefficient")
    x = variable_eliminator(operator  , coeff , len(pivot[0]))
    pivot.append(x)
   
  
    
    

 
mySystem = [[2,2,3,1 ,-1],[4,1,3,0 ,1],[1,4,-1,2 ,0],[1,-1,2,4 ,-2]]
   
displays_sys_equation(mySystem , 4 ,4)  
setSystem(mySystem)
    
    
    
    
    
    
 