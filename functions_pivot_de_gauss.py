from functions_system_equat_2_inconnues import *
import numpy as np



def displays_sys_pivot_de_gauss(list_xy, nbrEquation, nbrVar, initSize, inconnu):
    for i in range(nbrEquation):
        print("|", end=" ")
        for j in range(nbrVar):
            print(f' {list_xy[i][j]} {inconnu[j]}  + ', end=' ') if j < nbrVar - 1 else print(
                f' {list_xy[i][j]} {inconnu[j]}  = {list_xy[i][nbrVar]}')


def variable_eliminator(myMatrice, coeff, nbrVar):
    result = list()
    result.append(myMatrice[0])
    result.append(myMatrice[1])
    print("result : ", result)
   
    if isinstance(coeff, int) or isinstance(coeff, float):
        if myMatrice[0][0] % myMatrice[1][0] == 0 and myMatrice[1][0] <= myMatrice[0][0]:

            result[1] = [coeff * myMatrice[1][i] for i in range(len(myMatrice[0]))]


        elif myMatrice[1][0] % myMatrice[0][0] == 0 and myMatrice[1][0] >= myMatrice[0][0] or (
                myMatrice[1][0] <= myMatrice[0][0]):

            result[0] = [coeff * myMatrice[0][i] for i in range(len(myMatrice[1]))]


        else:
            print("error to isinstance -  int")

    elif type(coeff) == list:
        result[0] = [coeff[1] * myMatrice[0][i] for i in range(len(myMatrice[0]))]
        result[1] = [coeff[0] * myMatrice[1][i] for i in range(len(myMatrice[1]))]
    else:
        print("error")

    x = [result[0][i] + result[1][i] for i in range(nbrVar)]
    return x


def returnCoeff(operator):
    if  operator[0][0] != 0 and 0 != operator[1][0] :
        if operator[0][0] % operator[1][0] == 0 or 0 == operator[1][0] % operator[0][0]:

            coeff = coeff_dir_comp(operator, 0)
            print(coeff)  # , " <-- coefficient"
            return coeff
        else:

            coeff = coeff_dir_incomp(operator, 0)
            print(coeff)  # " <-- coefficient"
            return coeff


def setLines(myMatrice, pivot, index_pivot, index_line):
    operator = list()

    operator.append(pivot[index_pivot])
    operator.append(myMatrice[index_line])
    coeff = returnCoeff(operator)
    x = variable_eliminator(operator, coeff, len(pivot[0]))
    operator.clear()
    return x


def setSystem_transformation(myMatrice, initSize, inconnu, pivotRegistered):
    if len(myMatrice) == 1:
        return [myMatrice, pivotRegistered]
    else:
        pivot = list()
        turnExc = 1
        pivot.append(myMatrice[0])
        pivotRegistered.append(myMatrice[0])

        while turnExc < len(pivot[0]) - 1:
            pivot.append(setLines(myMatrice, pivot, 0, turnExc))
            turnExc += 1
        turnExc = 0
        displays_sys_pivot_de_gauss(pivot, len(pivot), len(pivot), initSize, inconnu)

        result = [x[1::] for k, x in enumerate(pivot) if x != pivot[0]]

        # result = [x if ]
        inconnu.pop(0)
        return setSystem_transformation(result, initSize, inconnu, pivotRegistered)


def getSolution(myMatrice):
    inconnu = ["x", "y", "z", "u", "t"]  ; inconnu = inconnu[:len(myMatrice[0]) - 1]
    solutions = {x : None for x in inconnu} 
    beginSize = len(myMatrice[0])
    pivotRegistered = []
    stateSystem = setSystem_transformation(myMatrice, beginSize, inconnu, pivotRegistered)
    print(stateSystem[0], "\n  all pivots : \n", stateSystem[1])
    listPivot = stateSystem[1]
    if len(myMatrice) == 3 :
        z = stateSystem[0][0][1] /stateSystem[0][0][0] 
        y = (listPivot[1][-1] - listPivot[1][-2]*z)/listPivot[1][0]
        x =  (listPivot[0][-1] - ( listPivot[0][-2]*z + listPivot[0][-3]*y))/ listPivot[0][0]
       
        print(f' x = {x} --> {(listPivot[0][-1] - ( listPivot[0][-2]*z + listPivot[0][-3]*y))} / {listPivot[0][0]} ,',end='')
        print(f' y = {y} --> {(listPivot[0][-1] - ( listPivot[0][-2]*z + listPivot[0][-3]*y))} / {listPivot[0][0]} ,' , end='')
        print(f'  z = {z} --> {stateSystem[0][0][1]} / {stateSystem[0][0][0]}' ,end='')
    elif len(myMatrice) == 4  : 
        u = stateSystem[0][0][1] /stateSystem[0][0][0]  
        z = (listPivot[2][-1] - listPivot[2][-2]*u)/listPivot[2][0] 
        y = (listPivot[1][-1] - ( listPivot[1][-2]*z + listPivot[1][-3]*u))/listPivot[1][0]
        x = (listPivot[0][-1] - (listPivot[0][-2]*y + listPivot[0][-2]*z + listPivot[0][-3]*u))/listPivot[0][0] 
        print(f'----->x= {x} == { (listPivot[0][-1] - (listPivot[0][-2]*y + listPivot[0][-2]*z + listPivot[0][-3]*u))} / {listPivot[0][0] }, ' , end=' ')
        print( f'y = {y}')
        print(f'z = {z}  ')
        print(f',  u = {u}')
        
    #elif len()
        
    
    
 
    
 
   
 
    
    
   


mySystem = np.random.randint(-3 , 5 ,size=(3,4)).tolist()

displays_sys_equation(mySystem, 3, 3)
getSolution(mySystem)