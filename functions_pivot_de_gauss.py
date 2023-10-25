from functions_system_equat_2_inconnues import *


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
    print("<-------------------------->")
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
    inconnu = ["x", "y", "z", "u", "t"]
    beginSize = len(myMatrice[0])
    z = 0
    pivotRegistered = []
    # while  z == 0 :
    stateSystem = setSystem_transformation(myMatrice, beginSize, inconnu, pivotRegistered)
    print(stateSystem[0], "\n  all pivots : \n", stateSystem[1])


mySystem = [[1, -2, 5, 1], [2, -5, -9, 0], [1, 7, -3, 1], [1, -1, 2, 1]]

displays_sys_equation(mySystem, 4, 3)
getSolution(mySystem)
