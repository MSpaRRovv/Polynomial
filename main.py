from Class import Polynom

p1 = Polynom([1, 2, 3])
p2 = Polynom({0: -3, 2: 1, 5: 4})
p3 = Polynom(p2)
p4 = Polynom(0, 2, 0, 5)
p5 = Polynom(1, 2, 3, 8, 9, 10, 5, 11, 0)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p1 == p2)
print(p2 == p3)
print(p3 + p2)
print(p1 - p2)
print(p1 + 10)
print(-p1)
print(p1 - 10)
print(p1(2))
print(p1.der())
print(p1.degree())
print(p1 * p2)
print(p1 * 10)
print(p3.der())

for power, coef in p1:
    print(power, coef)





