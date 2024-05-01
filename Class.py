class Polynom:
    def __init__(self, *coefficients):
        if len(coefficients) == 1:
            if isinstance(coefficients[0], dict):
                self.coefficients = [0] * (max(coefficients[0].keys()) + 1)
                for power, coef in coefficients[0].items():
                    self.coefficients[power] = coef
            elif isinstance(coefficients[0], Polynom):
                self.coefficients = coefficients[0].coefficients[:]
            else:
                self.coefficients = coefficients[0]
        else:
            self.coefficients = list(coefficients)

    def __repr__(self):
        return f"Polynom {self.coefficients}"

    def __str__(self):
        terms = []
        for power, coef in reversed(list(enumerate(self.coefficients))):
            if coef != 0:
                term = ""
                if power > 0:
                    if coef == 1:
                        term += "x"
                    elif coef == -1:
                        term += "-x"
                    elif coef > 0:
                        term += f"{coef}x"
                    else:
                        term += f"{coef}x"
                    if power > 1:
                        term += f"^{power}"
                else:
                    term += str(coef)
                terms.append(term)
        if not terms:
            return "0"
        return " + ".join(terms)

    def __eq__(self, other):
        if isinstance(other, Polynom):
            return self.coefficients == other.coefficients
        elif isinstance(other, float):
            return len(self.coefficients) == 1 and self.coefficients[0] == other
        else:
            False

    def __add__(self, other):
        if isinstance(other, Polynom):
            max_degree = max(len(self.coefficients), len(other.coefficients))
            result = [0] * max_degree
            for i in range(max_degree):
                if i < len(self.coefficients):
                    result[i] += self.coefficients[i]
                if i < len(other.coefficients):
                    result[i] += other.coefficients[i]
            return Polynom(result)
        elif isinstance(other, (int, float)):
            result = self.coefficients[:]
            result[0] += other
            return Polynom(result)
        else:
            raise ValueError("Unsupported operand type(s) for +")

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Polynom([-coef for coef in self.coefficients])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __call__(self, x):
        result = 0
        for power, coef in enumerate(self.coefficients):
            result += coef * (x ** power)
        return result

    def der(self, d=1):
        derived_coefficients = []
        for power, coef in enumerate(self.coefficients):
            if power >= d:
                term = coef
                for _ in range(d):
                    term *= power
                    power -= 1
                derived_coefficients.append(term)
        return Polynom(derived_coefficients)


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
print(poly1.der(1))
