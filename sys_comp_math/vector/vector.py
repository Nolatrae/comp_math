import math


def length_of_scalar(vector):
    check_vec(vector)
    sum = 0
    for i in range(0, len(vector)):
        sum = sum + vector[i]**2
    sum = math.sqrt(sum)
    return sum


def scalar_product_of_vectors(vec1, vec2):
    check_vectors(vec1, vec2)
    temp = 0
    for i in range(len(vec1)):
        temp += vec1[i] * vec2[i]
    return temp



def equal_vectors(vec1, vec2, delta=0):
    check_vectors(vec1, vec2)
    for i in range(len(vec1)):
        if abs(vec1[i] - vec2[i]) > delta:
            return False
    return True


def addition_of_vectors(vec1, vec2):
    res = []
    for i in range(0, len(vec1)):
        res.append((vec1[i] + vec2[i]))
    return res


def subtracting_vectors(vec1, vec2):
    res = []
    for i in range(0, len(vec1)):
        res.append((vec1[i] - vec2[i]))
    return res


def div(vec1, vec2, delta=3):
    if check_vectors(vec1, vec2):
        return [(vec1[i] / vec2[i]) for i in range(len(vec1))]
    else:
        v, num = vec_num(vec1, vec2)
        return [v[i] / num for i in range(len(v))]


def mul(vec1, vec2):
    if check_vectors(vec1, vec2):
        return [(int(vec1[i] * vec2[i] *100) / 100) for i in range(len(vec1))]
    else:
        v, num = vec_num(vec1, vec2)
        return [v[i] * num for i in range(len(v))]


def normirovka(vector):
    lenght = length_of_scalar(vector)
    res = []
    for i in range(0, len(vector)):
        res.append(vector[i] / lenght)
    return res

def cos(vec1, vec2):
    check_vectors(vec1, vec2)
    multiply = scalar_product_of_vectors(vec1, vec2)
    lena = length_of_scalar(vec1)
    lenb = length_of_scalar(vec2)
    cos = (multiply / (lena * lenb))
    return cos


def colleniarity(vec1, vec2):
    check_vectors(vec1, vec2)
    return abs(cos(vec1, vec2)) == 1.0


def one_direction(vec1, vec2):
    check_vectors(vec1, vec2)
    return cos(vec1, vec2) == 1.0


def protiv(vec1, vec2):
    cosinus = cos(vec1, vec2)
    return cosinus == -1


def orthogonal_vectors(vec1, vec2, delta=5):
    cosinus = cos(vec1, vec2)
    return cosinus == 0


def angular(vec1, vec2, delta=5):
    check_vectors(vec1, vec2)
    coss = cos(vec1, vec2, delta)
    rad = math.acos(coss)
    return round(rad / math.pi * 180, 3)


def proect(first_vector, second_vector):
    multiply = scalar_product_of_vectors(first_vector, second_vector)
    lenb = length_of_scalar(second_vector)
    return (multiply / lenb)


def alt_change(vector):
    res = []
    for i in range(0, len(vector)):
        res.append(vector[i]*(-1))
    return res


def check_vectors(v1, v2):
    if type(v1) != list or type(v2) != list:
        return False
    if check_vec(v1):
        if check_vec(v2):
            check_size(v1, v2)
            return True
        else:
            mess = f"Vector must be list, not {type(v2)} with int or flaut elements"
            raise TypeError(mess)
    else:
        mess = f"Vector must be list, not {type(v1)} with int or flaut elements"
        raise TypeError(mess)


def check_vec(v):
    if type(v) != list:
        return False
    for item in v:
        if type(item) == list:
            return False
        if type(item) not in (int, float):
            mess = f"Vector must contanin only int or float coordinates, {item} is {type(item)}"
            raise TypeError(mess)
    return True


def check_size(v1, v2):
    if len(v1) != len(v2):
        mess = f"first vector len - {len(v1)}, second vector len - {len(v2)}, lens are not similar"
        raise ValueError(mess)
    return True


def vec_num(v, num):
    if type(v) == list:
        if check_vec(v) and type(num) in (int, float):
            return v, num
        else:
            mess = f"{num} must be list, int or float type, not {type(num)}"
            raise TypeError(mess)
    elif type(num) == list:
        if check_vec(num) and type(v) in (int, float):
            return num, v
        else:
            mess = f"{v} must be list, int or float type, not {type(v)}"
            raise TypeError(mess)
    else:
        raise TypeError(
            "Arguments don't contain vector, vector must be list type")
