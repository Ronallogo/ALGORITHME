

def coeff_dir_comp(list_xy, coeff_x_y):
    print("\n------------\n")
    coeff_x_y = int(coeff_x_y)
    # case where the  module of  x_1 and x_2 and x_1 and _2 is true donc x_1 = x_2 ou x_1 = -1 * x_2
    if list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0:
        # le cas ou x_1 et x_2  > 0
        if list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] > 0:
            # return -1 si x_1 == x_2
            return -1 * (list_xy[0][coeff_x_y] * 1 / list_xy[0][coeff_x_y]) if list_xy[0][coeff_x_y] == list_xy[1][
                coeff_x_y] else print("condition 1-1 not verify")
        # le cas ou x_1  > 0 et x_2  < 0

        elif list_xy[0][coeff_x_y] > 0 > list_xy[1][coeff_x_y]:
            # return 1 si x_1 ==  -x_2

            return (list_xy[0][coeff_x_y] / list_xy[0][coeff_x_y]) if list_xy[0][coeff_x_y] == (
                    -1 * list_xy[1][coeff_x_y]) else print("condition 1-2 not verify")
        # le cas ou x_1 < 0 et x_2  > 0

        elif list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]:
            # return 1 si x_1 == -x_2

            return (list_xy[0][coeff_x_y] / list_xy[0][coeff_x_y]) if list_xy[0][coeff_x_y] == (
                    -1 * list_xy[1][coeff_x_y]) else print("condition 1-3 not verify")
        # le cas ou x_1 et x_2  < 0

        elif list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0:
            # return -1 si x_1 == x_2
            return -1 * (list_xy[0][coeff_x_y] / list_xy[0][coeff_x_y]) if list_xy[0][coeff_x_y] == list_xy[1][
                coeff_x_y] else print("condition 1-4 not verify")

            # the case where x_1 is the mutiple of x_2
    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] > 0):

        for x in range(list_xy[0][coeff_x_y] + 1 ):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * x:
                print("coeff_director is :")
                return alpha * -1
            
    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 > list_xy[1][coeff_x_y]):
        for x in range(list_xy[0][coeff_x_y] + 1 ):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x * -1):
                print("coeff_director is :")
                return alpha
           

    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]):
        for x in range((-1 * list_xy[0][coeff_x_y]) + 1 ):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x * -1):
                print("coeff_director is :")
                return alpha
            


    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0):
        for x in range((-1 * list_xy[0][coeff_x_y]) + 1):
            alpha = x
            if (list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x)):
                print("coeff_director is :")
                return -1 * alpha
          

    # the case where x_2 is the mutiple of x_1

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0):
        for x in range((-1 * list_xy[1][coeff_x_y]) + 1 ):
            alpha = x
            if (list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (x)):
                print("coeff_director is :")
                
                return -1 * alpha
          

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]):
        print("inside123")
        for x in range(list_xy[1][coeff_x_y] + 1 ):
            alpha = x
            if list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (-1 * x):
                print("coeff_director is :")
                print(alpha)
                return alpha
        
            

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 > list_xy[1][coeff_x_y]):
        list_xy[1][coeff_x_y] = int(list_xy[1][coeff_x_y])
        for x in range((-1 * list_xy[1][coeff_x_y]) + 1 +1):
            alpha = x
            if list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (-1 * x):
                print("coeff_director is :")
                return alpha
          

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] > 0):
        for x in range((list_xy[1][coeff_x_y]) + 1 +1):
            alpha = x
            if (list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (x)):
                print("coeff_director is :")
                return -1 * alpha
            

    else:
        print("Error - it is  a incompatible situation with this function-1 \n")

def coeff_dir_incomp(list_xy, coeff_x_y):
    result_coeff = []
    # x_1 % x_2 != 0 and {x_1 and x_2} > 0

    if (list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] != 0 and list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] != 0) and (
            list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] > 0):
        # x_1 > x_2

        if list_xy[0][coeff_x_y] > list_xy[1][coeff_x_y]:

            result_coeff.append(list_xy[0][coeff_x_y])
            result_coeff.append(-1 * list_xy[1][coeff_x_y])
            print(result_coeff)
            return result_coeff
        else:
            result_coeff.append(list_xy[0][coeff_x_y] * -1)
            result_coeff.append(list_xy[1][coeff_x_y])
            return result_coeff

    elif (list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] != 0 and list_xy[1][coeff_x_y] % list_xy[0][
        coeff_x_y] != 0) and (list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] < 0):
        result_coeff.append(list_xy[0][coeff_x_y])
        result_coeff.append(-1 * list_xy[1][coeff_x_y])
        return result_coeff

    elif (list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] != 0 and list_xy[1][coeff_x_y] % list_xy[0][
        coeff_x_y] != 0) and (list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]):
        result_coeff.append(list_xy[0][coeff_x_y] * -1)
        result_coeff.append(list_xy[1][coeff_x_y])
        return result_coeff

    elif (list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] != 0 and list_xy[1][coeff_x_y] % list_xy[0][
        coeff_x_y] != 0) and (list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0):
        if list_xy[0][coeff_x_y] > list_xy[1][coeff_x_y]:

            result_coeff.append(list_xy[0][coeff_x_y])
            result_coeff.append(-1 * list_xy[1][coeff_x_y])
            print(result_coeff)
            return result_coeff
        else:

            result_coeff.append(list_xy[0][coeff_x_y] * -1)
            result_coeff.append(list_xy[1][coeff_x_y])
            print(result_coeff)
            return result_coeff

    else:
        print("Error - it is  a incompatible situation with this function-2 \n")

def resolve_sys_equation(list_xy, coeff_an):
    print('coeff :', coeff_an)
    
    if isinstance(coeff_an, float) or isinstance(coeff_an, int):
       if list_xy[0][0] >= list_xy[1][0]:
            y = (coeff_an * list_xy[0][2] + list_xy[1][2]) / (coeff_an * list_xy[0][1] + list_xy[1][1])
            x = 1 / list_xy[0][0] * (list_xy[0][2] - list_xy[0][1] * y)
            return [x , y]
       else :
            y = ( list_xy[0][2] + coeff_an *list_xy[1][2]) / ( list_xy[0][1] + coeff_an *list_xy[1][1])
            x = 1 / list_xy[0][0] * (list_xy[0][2] - list_xy[0][1] * y)
            return [x , y]
    elif type(coeff_an) == list:
        y = (coeff_an[1]*list_xy[0][2] + list_xy[1][2]*coeff_an[0]) /((coeff_an[1]*list_xy[0][1] + list_xy[1][1]*coeff_an[0]) )
        x =   x = 1 / list_xy[0][0] * (list_xy[0][2] - list_xy[0][1] * y)
        return [x , y]

    else:
        print("Error")

def displays_sys_equation(list_xy, nbrEquation, nbrVar):
    inconnu = ["x", "y", "z","u", "t"]
    
    
    for i in range(nbrEquation):
        print("|" , end=" ")
        for j in range(nbrVar) :
            print(f' {list_xy[i][j]} {inconnu[j]}  + ' , end=' ') if j < nbrVar - 1 else   print(f' {list_xy[i][j]} {inconnu[j]}  = {list_xy[i][nbrVar]}')
             

def solutions(solutions) :
    print("S : {" + f'{solutions[0]} ; {solutions[1]} ' + "}")
             
                    


    
    
    
    
    
    
 
   
      
    
    
  

    
    
        
        
        
     
        