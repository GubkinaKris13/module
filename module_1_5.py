immutable_var = (1, 2, 3, "Точка", False)
print(immutable_var)
#immutable_var[4] = True кортеж не потддерживает обращение по элементам
#immutable_var.append('добавить') только через конкатенацию
mutable_list = [1, 2, 3, 'Точка', False]
mutable_list[4] = True
mutable_list.append('добавить')
print(mutable_list)