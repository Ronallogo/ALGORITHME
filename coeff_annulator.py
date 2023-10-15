system_equation = [[-1, 2, -2], [6, 1, 5], [0, 0, 0]]


def coeff_dir_comp(list_xy, coeff_x_y):
    print("\n------------\n")
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

        for x in range(list_xy[0][coeff_x_y] + 1 // 2):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * x:
                print("coeff_director is :")
                return alpha * -1
            else:
                print("+")
    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 > list_xy[1][coeff_x_y]):
        for x in range(list_xy[0][coeff_x_y] + 1 // 2):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x * -1):
                print("coeff_director is :")
                return alpha
            else:
                print("+")

    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]):
        for x in range((-1 * list_xy[0][coeff_x_y]) + 1 // 2):
            alpha = x
            if list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x * -1):
                print("coeff_director is :")
                return alpha
            else:
                print("+")


    elif list_xy[0][coeff_x_y] % list_xy[1][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0):
        for x in range((-1 * list_xy[0][coeff_x_y]) + 1 // 2):
            alpha = x
            if (list_xy[0][coeff_x_y] == list_xy[1][coeff_x_y] * (x)):
                print("coeff_director is :")
                return -1 * alpha
            else:
                print("+")

    # the case where x_2 is the mutiple of x_1

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 and list_xy[1][coeff_x_y] < 0):
        for x in range((-1 * list_xy[1][coeff_x_y]) + 1 // 2):
            alpha = x
            if (list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (x)):
                print("coeff_director is :")
                return -1 * alpha
            else:
                print("+")

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] < 0 < list_xy[1][coeff_x_y]):
        for x in range(list_xy[1][coeff_x_y] + 1 // 2):
            alpha = x
            if list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (-1 * x):
                print("coeff_director is :")
                return alpha
            else:
                print("+")

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 > list_xy[1][coeff_x_y]):
        for x in range((-1 * list_xy[1][coeff_x_y]) + 1 // 2):
            alpha = x
            if list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (-1 * x):
                print("coeff_director is :")
                return alpha
            else:
                print("+")

    elif list_xy[1][coeff_x_y] % list_xy[0][coeff_x_y] == 0 and (
            list_xy[0][coeff_x_y] > 0 and list_xy[1][coeff_x_y] > 0):
        for x in range((list_xy[1][coeff_x_y]) + 1 // 2):
            alpha = x
            if (list_xy[1][coeff_x_y] == list_xy[0][coeff_x_y] * (x)):
                print("coeff_director is :")
                return -1 * alpha
            else:
                print("+")

    else:
        print("process not finish yet")


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
        print("Error - it is  a incompatible situation with this function \n")


# result  = coeff_dir_comp(system_equation , 0)


def resolve_sys_equation(list_xy, coeff_an):
    print('coeff :', coeff_an)
    if isinstance(coeff_an, float) or isinstance(coeff_an, int):
        y = (coeff_an * list_xy[0][2] + list_xy[1][2]) / (coeff_an * list_xy[0][1] + list_xy[1][1])
        x = 1 / list_xy[0][0] * (list_xy[0][2] - list_xy[0][1] * y)
        print("S : {" + f'{x} ; {y} ' + "}")
    elif type(coeff_an) == list:
        y = 1
        x = 1
        print("S : {" + f'{x} ; {y} ' + "}")

    else:
        print("Error")


def displays_sys_equation(list_xy, nbrVar, list_var=None):
    inconnu = ["x", "y", "z"]
    for i in range(nbrVar):
        print(f'| {list_xy[i][0]} {inconnu[0]}  +  {list_xy[i][1]} {inconnu[1]}  = {list_xy[i][2]}  \n')


displays_sys_equation(system_equation, 2)
if system_equation[0][0] % system_equation[1][0] == 0 == system_equation[1][0] % system_equation[0][0]:
    coeff = coeff_dir_comp(system_equation, 0)
else:
    coeff = coeff_dir_incomp(system_equation, 0)
resolve_sys_equation(system_equation, coeff)
