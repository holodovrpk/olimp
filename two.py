s = input().split()

n = int(s[0])
m = int(s[1])



if n<10**22 and m < 10**22:
    l = list(str(n + m))
    summa = 0
    for i in l:
        summa += int(i)
    print(summa)
else:
    print("нет")

print("Конец")
