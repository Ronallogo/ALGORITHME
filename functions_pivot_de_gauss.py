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
 
def returnCoeff(operator) :
    if operator[0][0] % operator[1][0] == 0 or 0 == operator[1][0] % operator[0][0]:
        print("compatible")
        coeff = coeff_dir_comp(operator, 0)
        print(coeff , " <-- coefficient") 
        return coeff
    else :
        print("incompatible")
        coeff = coeff_dir_incomp(operator, 0)
        print(coeff , " <-- coefficient") 
        return coeff
 
 
 
def setLines(myMatrice , pivot , index_pivot , index_line):
   
    operator = list()
  
    operator.append(pivot[index_pivot])
    operator.append(myMatrice[index_line])
    coeff = returnCoeff(operator)
    x = variable_eliminator(operator  , coeff , len(pivot[0]))
    operator.clear()
    return x
 

def setSystem_transformation(myMatrice):
    if len(myMatrice) == 1 :
        exit()
    
    pivot = list()
    turnExc = 1
    pivot.append(myMatrice[0])
    while turnExc < len(pivot[0]) - 1:
        pivot.append( setLines(myMatrice , pivot , 0 ,turnExc))
        turnExc += 1
    displays_sys_equation(pivot, 4 ,4) 
    
    result = [x[1::]  for k ,  x in enumerate( pivot) if x != pivot[0]]
    #result = [x if ]
    print(result)
    return result
    

    
   
  
    
    

 
mySystem = [[2,2,3,1 ,-1],[4,1,3,0 ,1],[1,4,-1,2 ,0],[1,-1,2,4 ,-2]]
   
displays_sys_equation(mySystem , 4 ,4)  
setSystem_transformation(mySystem)
    
    
    
    
    
    
 