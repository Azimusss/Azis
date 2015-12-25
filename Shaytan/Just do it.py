import random

print("*" * 20, 1, "*" * 20)
# Дана десятичная дробь. Вывести два ближайших целых числа

flt = 18.3

def mn_mx(flt):
    mn_flt = int(flt)
    mx_flt = mn_flt + 1
    return mn_flt, mx_flt

print(mn_mx(flt))

print("*" * 20, 2, "*" * 20)
# Заполнить список n-элементами в диапазоне от a до b (a, b - целые)

col_vo = 5
a = 3
b = 4
lst = []

for el in range(col_vo):
    lst.append(random.randint(a, b))

print(lst)

print("*" * 20, 3, "*" * 20)
# Дан список из произвольных целых чисел. Вывести три самые большие элемента списка.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_lst1 = []

print("lst = ", lst1)
for el in lst1:
    max_lst1.append(max(lst1))
    lst1.remove(max(lst1))
    if len(max_lst1) == 3:
        print("3 max:", max_lst1)
        break

print("*" * 20, 4, "*" * 20)
# Дано произвольное слово из русских букв. Каких букв в слове больше, гласных или согласных?

glasn=['а','е','и','о','у','ы','э','ю','я'];
glasn_col_vo = 0
soglas_col_vo = 0
slovo = "Трамвай"

i = 0
while i < len(slovo) - 1:
    i += 1
    if slovo[i] in glasn:
        glasn_col_vo = glasn_col_vo + 1
    else:
        soglas_col_vo = soglas_col_vo + 1

print(slovo)
if glasn_col_vo < soglas_col_vo:
    print("soglasnih bolshe")
elif glasn_col_vo > soglas_col_vo:
    print("glasnih bolshe")
elif glasn_col_vo == soglas_col_vo:
    print("ravnoye colichestvo")

print("*" * 20, 5, "*" * 20)
# Дано целое произвольное число. Вывести максимальное число, которое получится в результате умножения двух его цифр.

chislo = 80237
len_chislo = len(chislo)
lit_m = []

while i < len_chislo:
    i = 0
    i += 1