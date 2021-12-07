

N = int(input())
a = input().split()
if len(a) == N:
    flag = True
    for i in range(0, len(a)):
        a[i] = int(a[i])
        if a[i] < -99999 or a[i] > 99999:
            flag = False
    if flag:
        max_number = max(a)
        min_number = min(a)
        s = max_number + min_number
        print(s)

print("Конец")