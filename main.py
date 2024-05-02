from Class import Polynom

poly1 = Polynom([1, 2, 3])
poly2 = Polynom({0: -3, 2: 1, 5: 4})
poly3 = Polynom(poly2)
poly4 = Polynom(0, 2, 0, 5)
poly5 = Polynom(1, 2, 3, 8, 9, 10, 5, 11, 0)

print(poly1)
print(poly2)
print(poly3)
print(poly4)
print(poly5)
print(poly1 == poly2)
print(poly2 == poly3)
print(poly3 + poly2)
print(poly1 - poly2)
print(poly1 + 10)
print(-poly1)
print(poly1 - 10)
print(poly1(2))
print(poly1.der())
print(poly1.degree())
print(poly1 * poly2)
print(poly1 * 10)
print(poly3.der())
poly6 = Polynom()
print(poly6)

for power, coef in poly1:
    print(power, coef)

print(poly1.__repr__())