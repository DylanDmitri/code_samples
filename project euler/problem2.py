
a, b = 1, 2
total = 0

while b < 4e6:
    total += 0 if b%2 else b
    a, b = b, a+b

print(total)
