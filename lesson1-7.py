a = float(input("Введите первый результат в км: "))
b = float(input("Введите цель в км: "))
i = 1
while True:
    print(f'{i}-й день: {round(a,2)}')
    i += 1
    a *= 1.1
    if a > b:
        break
print(f'на {i} день спортсмен достиг результата -  не менее {b} км.')