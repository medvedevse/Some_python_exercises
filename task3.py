a = list(map(int, input('Введите числа (через пробел):',).split()))

for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] > 0:
        print(a[i], end=" ")

