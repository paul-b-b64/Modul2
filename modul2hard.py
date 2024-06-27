num_ = int(input('Введи число: '))
pass_ = ""
for i in range(1, num_//2 + 1):
    for j in range(1, 20):
        prom_zn = ""
        if num_ % (i + j) == 0 and i != j:
            prom_zn += str(i)
            prom_zn += str(j)
            if prom_zn not in pass_[::-1]:
                pass_ += prom_zn
            elif len(prom_zn) > 2:
                pass_ += prom_zn
            elif prom_zn not in pass_:
                pass_ += prom_zn
print(pass_)






# num_ = int(input('Введи число: '))
# pass_ = []
# prom_zn = []
# for i in range(1, num_//2 + 1):
#     for j in range(2, 20):
#         if num_ % (i + j) == 0 and i != j:
#             prom_zn.append(i)
#             prom_zn.append(j)
#


# b = a[::-1]
# print(pass_)

