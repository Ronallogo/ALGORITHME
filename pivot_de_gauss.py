from functions import *

mySystem = [[2,2,3,1],[4,1,3,0],[1,4,-1,2],[1,-1,2,4]]

 
    
displays_sys_equation(mySystem , 4 ,4)


def setSystem(myMatrice):
    pivot = list()
    pivot.append(myMatrice[0])
    operator = list()
    operator.append(pivot[0])
    operator.append(myMatrice[1])
    coeff = returnCoeff(operator)
    
    if isinstance(coeff , int) or isinstance( coeff , float) :
        if coeff == (operator[0][0] * -1) :
            operator[0] = [coeff * operator[0][i]  for i in range(len(operator[0]))]
            print(operator[0] , "  1")
        elif coeff == (operator[1][0] * -1) :
            operator[1] = [coeff * operator[1][i]  for i in range(len(operator[1]))]
            print(operator[1] , " 2")
    elif type(coeff) == list :
        operator[0] = [coeff[1] * operator[0][i]  for i in range(len(operator[0]))]
        operator[1] = [coeff[0] * operator[1][i]  for i in range(len(operator[1]))]
        
        print(operator)
         
        

    
               
                
   
        
    
    
    
setSystem(mySystem)
    
    
    
    
    
    
        
            
     
    
    
    

