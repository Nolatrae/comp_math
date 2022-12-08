import vector as v



first_vector = [0, 3, 5]
second_vector = [2, 4, 7]
scalar = 2




print("Сложение векторов")
print((v.addition_of_vectors(first_vector, second_vector)))

print("Вычитание векторов")
print(v.subtracting_vectors(first_vector, second_vector))

print("Умножение вектора на скаляр")
print(v.multiplication_by_scalar(first_vector, scalar))

print("Деление вектора на скаляр")
print(v.division_by_scalar(first_vector, scalar))

print("Скалярное произведение векторов")
print(v.scalar_product_of_vectors(first_vector, second_vector))

print("Проверка на коллинеарность")
print(v.collinearity_of_vectors(first_vector, second_vector))

print("Длина вектора")
print(v.length_of_scalar(first_vector))

print("Косинус между векторами")
print(v.cos(first_vector, second_vector))

print("Сонаправленность векторов")
print(v.directed_vectors(first_vector, second_vector))

print('Равенство векторов')
print(v.equal_vectors(first_vector, second_vector))

print('Угол между векторами')
v.angle_between_Vectors(first_vector, second_vector)

print('Ортогальные векторы')
print(v.orthogonal_vectors(first_vector, second_vector))

print('Нормировка вектора')
print(v.normirovka(first_vector))

print('изменить противоположное')
print(v.alt_change(first_vector))

print('Проекция вектора на вектор')
print(v.proect(first_vector, second_vector))

print('Противопожные')
print(v.protiv(first_vector, second_vector))
