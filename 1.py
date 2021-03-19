print("Введи число ")
n = int(input())
f = 1
for i in range(1,n+1,):
    f *= i
print("Твой ответ ")
print(f)