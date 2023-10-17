from functions import *

mySystem = [[1,2,3,1],[2,1,3,0],[1,4,-1,2],[1,-1,2,4]]

 
    
displays_sys_equation(mySystem , 4 ,4)


def setSystem(myMatrice):
    pivot = list()
    pivot.append(myMatrice[0])
    operator = list()
    operator.append(pivot[0])
    operator.append(myMatrice[1])
    coeff = returnCoeff(operator)
    
    
    
setSystem(mySystem)
    
    
    
    
    
    
        
            
     
    
    
    

