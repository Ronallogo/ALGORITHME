
system_equation = [ [-1 ,1,-1] , [2,1,1]  , [0,0,0] ]



def coeff_dir_comp(list  , coeff_x_y ):
    
    print("\n------------\n")
    # case where the  module of  x_1 and x_2 and x_1 and _2 is true donc x_1 = x_2 ou x_1 = -1 * x_2
    if (list[0][coeff_x_y] % list[1][coeff_x_y] == 0 and list[1][coeff_x_y] % list[0][coeff_x_y] == 0) :
        #le cas ou x_1 et x_2  > 0
        if (list[0][coeff_x_y] > 0 and list[1][coeff_x_y] >0) :
            # return -1 si x_1 == x_2
            return -1 * (list[0][coeff_x_y] *  1/list[0][coeff_x_y])  if  list[0][coeff_x_y] == list[1][coeff_x_y] else print("condition 1-1 not verify")
        #le cas ou x_1  > 0 et x_2  < 0
        
        elif (list[0][coeff_x_y] > 0 and list[1][coeff_x_y] < 0) :
            # return 1 si x_1 ==  -x_2
            
            return (list[0][coeff_x_y] /list[0][coeff_x_y]) if list[0][coeff_x_y] == (-1 * list[1][coeff_x_y]) else print("condition 1-2 not verify")
        #le cas ou x_1 < 0 et x_2  > 0
        
        elif (list[0][coeff_x_y] < 0 and list[1][coeff_x_y] > 0) :
            # return 1 si x_1 == -x_2
            
            return (list[0][coeff_x_y] /list[0][coeff_x_y]) if list[0][coeff_x_y]  == (-1 * list[1][coeff_x_y]) else  print("condition 1-3 not verify")
        #le cas ou x_1 et x_2  < 0
        
        elif (list[0][coeff_x_y] < 0 and list[1][coeff_x_y] < 0) :
            # return -1 si x_1 == x_2
            return -1 * (list[0][coeff_x_y] /list[0][coeff_x_y])  if list[0][coeff_x_y]  ==  list[1][coeff_x_y] else  print("condition 1-4 not verify") 
      
    # the case where x_1 is the mutiple of x_2
    elif list[0][coeff_x_y] % list[1][coeff_x_y] == 0  and ( list[0][coeff_x_y] > 0 and list[1][coeff_x_y] > 0) :
        
        for x in range(list[0][coeff_x_y] + 1 //2) :
            alpha = x
            if (list[0][coeff_x_y] == list[1][coeff_x_y] * x) :
                print("coeff_director is :")
                return  alpha * -1
            else :
                print("+")
    elif list[0][coeff_x_y] % list[1][coeff_x_y] == 0  and ( list[0][coeff_x_y] > 0 and list[1][coeff_x_y] < 0) :
          for x in range(list[0][coeff_x_y] + 1 //2) :
            alpha = x
            if (list[0][coeff_x_y] == list[1][coeff_x_y] * (x * -1)) :
                print("coeff_director is :")
                return  alpha 
            else :
                print("+")
        
    elif list[0][coeff_x_y] % list[1][coeff_x_y] == 0  and ( list[0][coeff_x_y] < 0 and list[1][coeff_x_y] > 0) :
        for x in range( (-1 * list[0][coeff_x_y] ) + 1 //2) :
            alpha = x
            if (list[0][coeff_x_y] == list[1][coeff_x_y] * (x * -1)) :
                print("coeff_director is :")
                return  alpha 
            else :
                print("+")
                
    elif  list[0][coeff_x_y] % list[1][coeff_x_y] == 0  and ( list[0][coeff_x_y] < 0 and list[1][coeff_x_y] < 0) : 
        for x in range( (-1 * list[0][coeff_x_y] ) + 1 //2) :
            alpha = x
            if (list[0][coeff_x_y] == list[1][coeff_x_y] * (x)) :
                print("coeff_director is :")
                return -1 *  alpha 
            else :
                print("+")
    
    # the case where x_2 is the mutiple of x_1
    
    elif  list[1][coeff_x_y] % list[0][coeff_x_y] == 0  and ( list[0][coeff_x_y] < 0 and list[1][coeff_x_y] < 0) :
        for x in range( (-1 * list[1][coeff_x_y] ) + 1 //2) :
            alpha = x
            if (list[1][coeff_x_y] == list[0][coeff_x_y] * (x)) :
                print("coeff_director is :")
                return -1 *  alpha 
            else :
                print("+") 
    
    elif  list[1][coeff_x_y] % list[0][coeff_x_y] == 0  and ( list[0][coeff_x_y] < 0 and list[1][coeff_x_y] > 0) :
        for x in range( list[1][coeff_x_y] + 1 //2) :
            alpha = x
            if (list[1][coeff_x_y] == list[0][coeff_x_y] * (-1 * x)) :
                print("coeff_director is :")
                return  alpha 
            else :
                print("+")        
    
    elif  list[1][coeff_x_y] % list[0][coeff_x_y] == 0  and ( list[0][coeff_x_y] > 0 and list[1][coeff_x_y] < 0) :
        for x in range( (-1 * list[1][coeff_x_y]) + 1 //2) :
            alpha = x
            if (list[1][coeff_x_y] == list[0][coeff_x_y] * (-1 * x)) :
                print("coeff_director is :")
                return  alpha 
            else :
                print("+")  
    
    elif  list[1][coeff_x_y] % list[0][coeff_x_y] == 0  and ( list[0][coeff_x_y] > 0 and list[1][coeff_x_y] > 0) :
        for x in range( (list[1][coeff_x_y]) + 1 //2) :
            alpha = x
            if (list[1][coeff_x_y] == list[0][coeff_x_y] * (x)) :
                print("coeff_director is :")
                return -1 *  alpha 
            else :
                print("+")      
    
    else  :
        print("process not finish yet")
  
def coeff_dir_incomp(list , coeff_x_y) : 
    result_coeff = []
    # x_1 % x_2 != 0 and {x_1 and x_2} > 0
  
    if (list[0][coeff_x_y] % list[1][coeff_x_y] != 0 and list[1][coeff_x_y] % list[0][coeff_x_y] != 0) and (list[0][coeff_x_y] > 0 and list[1][coeff_x_y] > 0) :
        # x_1 > x_2
       
        if list[0][coeff_x_y] > list[1][coeff_x_y] :
            
            result_coeff.append(list[0][coeff_x_y]) 
            result_coeff.append(-1 * list[1][coeff_x_y])
            print(result_coeff)
            return result_coeff
        else : 
            result_coeff.append(list[0][coeff_x_y] * -1 ) 
            result_coeff.append(list[1][coeff_x_y])
            return result_coeff 
    
    elif (list[0][coeff_x_y] % list[1][coeff_x_y] != 0 and list[1][coeff_x_y] % list[0][coeff_x_y] != 0) and (list[0][coeff_x_y] > 0 and list[1][coeff_x_y] < 0) :
        result_coeff.append(list[0][coeff_x_y]) 
        result_coeff.append(-1 * list[1][coeff_x_y])
        return result_coeff 
        
    elif (list[0][coeff_x_y] % list[1][coeff_x_y] != 0 and list[1][coeff_x_y] % list[0][coeff_x_y] != 0) and (list[0][coeff_x_y] < 0 and list[1][coeff_x_y] > 0) :
        result_coeff.append(list[0][coeff_x_y] * -1 ) 
        result_coeff.append(list[1][coeff_x_y])     
        return result_coeff 
    
    elif (list[0][coeff_x_y] % list[1][coeff_x_y] != 0 and list[1][coeff_x_y] % list[0][coeff_x_y] != 0) and (list[0][coeff_x_y] < 0 and list[1][coeff_x_y] < 0) :
        if list[0][coeff_x_y] > list[1][coeff_x_y] :
         
            result_coeff.append(list[0][coeff_x_y]) 
            result_coeff.append(-1 * list[1][coeff_x_y])
            print(result_coeff)
            return result_coeff 
        else :
          
            result_coeff.append(list[0][coeff_x_y] * -1 ) 
            result_coeff.append(list[1][coeff_x_y])
            print(result_coeff)
            return result_coeff 
    
    else : print("Error - it is  a incompatible situation with this function \n")
# result  = coeff_dir_comp(system_equation , 0)   
    
  
    
def resolve_sys_equation(list_xy , coeff_an ):
    print('coeff :' , coeff_an)
    if isinstance(coeff_an , int) :
        y =  (coeff_an * list_xy[0][2] + list_xy[1][2])/(coeff_an * list_xy[0][1] + list_xy[1][1])
        x = 1/list_xy[0][0] * (list_xy[0][2] - list_xy[0][1]*y)
        print("S : {"+ f'{x} ; {y} '+"}")
    elif type(coeff_an) == list :
        y = 1
        x = 1
        print("S : {"+ f'{x} ; {y} '+"}")
        
    else :
        print("Error")
        
    
    
 

def displays_sys_equation(list , nbrVar , list_var = None):
    inconnu =["x" , "y" , "z"]
    for i in range(nbrVar) :
        print(f'| {list[i][0]} {inconnu[0]}  +  {list[i][1]} {inconnu[1]}  = {list[i][2]}  \n')
        
       
        
    
    
 
displays_sys_equation(system_equation , 2 )
coeff = coeff_dir_comp(system_equation , 0) 
resolve_sys_equation(system_equation , coeff)
 
 