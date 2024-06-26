# numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num_ = int(input('Введи число: '))
deliteli_ = []
for i in range(1, num_ + 1): # цикл нахождения делителей введенного числа
   if (num_ % i) == 0 and i > 2:
       deliteli_.append((i))
print(deliteli_)

# for i in range(len(deliteli_)): # на каждый делитель ищем пары сумм
#     num_ = deliteli_[i]
#     pass_ = []
#     if num_ % 2 != 0:
#         for i in range (1, num_//2 + 1):
#             a = num_ - i
#             pass_.append(i)
#             pass_.append(a)
#         print(pass_)
#     else:
#         for i in range (1, num_//2):
#             a = num_ - i
#             pass_.append(i)
#             pass_.append(a)
#         print(pass_)
