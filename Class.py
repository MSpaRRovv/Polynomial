class Polynom:
    def __init__(self, *coefficients):
        if len(coefficients) == 1:
            if isinstance(coefficients[0], dict):
                self.coefficients = [0] * (max(coefficients[0].keys()) + 1) #прибавля
                for power, coef in coefficients[0].items():
                    self.coefficients[power] = coef
            elif isinstance(coefficients[0], Polynom):
                self.coefficients = coefficients[0].coefficients[:]
            else:
                self.coefficients = coefficients[0] #Значит список
        else:
            self.coefficients = list(coefficients)#считаем что аргументы являются списком

    def __repr__(self) -> str:
        return f"Polynom {self.coefficients[::-1]}"

    def __str__(self) ->str:
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

    def __eq__(self, other) -> bool:
        if isinstance(other, Polynom):
            return self.coefficients == other.coefficients
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
        elif isinstance(other, int):
            result = self.coefficients[:]
            result[0] += other
            return Polynom(result)
        else:
            raise ValueError("Не поддерживает сложение")

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
            term = coef
            for _ in range(d):
                term *= power
                power -= 1
            derived_coefficients.append(term)
        return Polynom(derived_coefficients)

    def degree(self):
        return len(self.coefficients) - 1

    def __mul__(self, other):
        if isinstance(other, Polynom):
            result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i, coef in enumerate(self.coefficients):
                for j, other_coef in enumerate(other.coefficients):
                    result[i + j] += coef * other_coef
            return Polynom(result)
        elif isinstance(other, int):
            return Polynom([coef * other for coef in self.coefficients])
        else:
            raise ValueError("Не поддерживает умножение")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter(enumerate(self.coefficients))

    def __next__(self):
        return next(iter(enumerate(self.coefficients)))

