num_ = int(input('Введи число: '))
deliteli_ = []
for i in range(1, num_ + 1):
    # цикл нахождения делителей введенного числа
    if (num_ % i) == 0 and i > 2:
        deliteli_.append((i))
#for i in range(len(deliteli_)): # на каждый делитель ищем пары сумм
    num_ = deliteli_[i]
    pass_ = []
    if num_ % 2 != 0:  # для нечетных делителей так
        for j in range (1, num_//2 + 1):
            a = num_ - j
            pass_.append(j)
            pass_.append(a)
    else:
        for j in range (1, num_//2): # для четных делителей
            a = num_ - j
            pass_.append(j)
            pass_.append(a)
print(pass_)




# for i in range(len(deliteli_)): # на каждый делитель ищем пары сумм
#     num_ = deliteli_[i]
#     pass_ = []
#     if num_ % 2 != 0:  # для нечетных делителей так
#         for j in range (1, num_//2 + 1):
#             a = num_ - j
#             pass_.append(j)
#             pass_.append(a)
#         print(pass_)
#     else:
#         for j in range (1, num_//2): # для четных делителей
#             a = num_ - j
#             pass_.append(j)
#             pass_.append(a)
#         print(pass_)
