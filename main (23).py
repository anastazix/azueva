c= int(input("Введите количество сантиметров: "))
d = int(input("Введите количество дециметров: "))
m = int(input("Введите количество миллиметров: "))
met = c / 100 + d / 10 + m / 1000
print(f"Количество метров: {met}")
