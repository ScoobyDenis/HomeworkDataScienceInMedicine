digit = int(input("Введите число: "))
large_digit = digit % 10
while digit > 0:
    digit //= 10
    n = digit % 10
    if n > large_digit:
        large_digit = n

print(large_digit)
