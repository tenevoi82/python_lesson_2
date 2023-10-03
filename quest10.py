countM = int(input("Введите общее количесто монеток: "))

countO = 0 #количство орлов

for i in range(countM):
    j = int(input(f"{i}/{countM} Введите 0-орёл, или 1 для решко: "))
    if j == 0:
        countO +=1
countR = countM - countO #количство решко

#print ("Орлов",countO,"Решек",countR ) #для отладки
print("Нужно перевернуть ",end='')
if countR > countO:
    print(countO,end='')
else:
    print(countR,end='')
print(' монеток')
