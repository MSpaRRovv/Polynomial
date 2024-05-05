import unittest
from Class import Polynom


class TestPolynom(unittest.TestCase):
    def test_init(self):
        p1 = Polynom(5)
        self.assertEqual(p1.coefficients, [5])

        p2 = Polynom([1, 2, 3])
        self.assertEqual(p2.coefficients, [1, 2, 3])

        p3 = Polynom([])
        self.assertEqual(p3.coefficients, [])

        p4 = Polynom({0: -3, 2: 1, 5: 4})
        self.assertEqual(p4.coefficients, [-3, 0, 1, 0, 0, 4])

        p5 = Polynom(p1)
        self.assertEqual(p5.coefficients, [5])

        p6 = Polynom(0, 2, 0, 5)
        self.assertEqual(p6.coefficients, [0, 2, 0, 5])

        p7 = Polynom(1, 2, 3, 8, 9, 10, 5, 11, 0)
        self.assertEqual(p7.coefficients, [1, 2, 3, 8, 9, 10, 5, 11, 0])

        p8 = Polynom(1)
        self.assertEqual(p8.coefficients, [1])

        p9 = Polynom({0: 0})
        self.assertEqual(p9.coefficients, [0])

        p10 = Polynom([0])
        self.assertEqual(p10.coefficients, [0])

        p11 = Polynom({})
        self.assertEqual(p11.coefficients, [])

    def test_add(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([1, 2, 3])
        expected = Polynom([2, 4, 6])
        assert p1 + p2 == expected

        p3 = Polynom(5)
        p4 = Polynom([1, 2, 3])
        expected1 = Polynom([6, 2, 3])
        assert p3 + p4 == expected1

        p5 = Polynom({0: -3, 2: 1, 5: 4})
        p6 = Polynom({0: -3, 2: 1, 5: 4})
        expected2 = Polynom({0: -6, 2: 2, 5: 8})
        assert p5 + p6 == expected2

        p7 = Polynom(0, 2, 0, 5)
        p8 = Polynom(1, 2, 3, 8, 9, 10, 5, 11, 0)
        expected3 = Polynom(1, 4, 3, 13, 9, 10, 5, 11, 0)
        assert p7 + p8 == expected3

        p9 = Polynom()
        p10 = Polynom()
        expected4 = Polynom()
        assert p9 + p10 == expected4

        p11 = Polynom(0)
        p12 = Polynom(0)
        expected5 = Polynom(0)
        assert p11 + p12 == expected5

        p13 = Polynom()
        p14 = Polynom([0, 0, 0])
        expected6 = Polynom([0, 0, 0])
        assert p13 + p14 == expected6

        p15 = Polynom([0, 0, 0])
        p16 = Polynom(1)
        expected7 = Polynom([1, 0, 0])
        assert p15 + p16 == expected7

    def test_radd(self):
        p1 = Polynom([1, 2, 3])
        i1 = 5
        expected = Polynom([6, 2, 3])
        assert i1 + p1 == expected

        p2 = Polynom({0: -3, 2: 1, 5: 4})
        i2 = 3
        expected1 = Polynom([0, 0, 1, 0, 0, 4])
        assert i2 + p2 == expected1

        p3 = Polynom(0, 2, 0, 5)
        i3 = 1
        expected2 = Polynom(1, 2, 0, 5)
        assert i3 + p3 == expected2

    def test_call(self):
        p1 = Polynom([1, 2, 3])
        assert p1(0) == 1
        assert p1(1) == 6
        assert p1(2) == 17
        assert p1(3) == 34
        assert p1(4) == 57
        assert p1(5) == 86

        p2 = Polynom({0: -3, 2: 1, 5: 4})
        assert p2(0) == -3
        assert p2(1) == 2
        assert p2(2) == 129
        assert p2(3) == 978

        p3 = Polynom(0)
        assert p3(0) == 0
        assert p3(1) == 0
        assert p3(111) == 0

        p4 = Polynom(1)
        assert p4(0) == 1
        assert p4(1) == 1
        assert p4(111) == 1

        p5 = Polynom([])
        assert p5(0) == 0
        assert p5(1) == 0
        assert p5(111) == 0

        p6 = Polynom({})
        assert p6(0) == 0
        assert p6(1) == 0
        assert p6(111) == 0

        p7 = Polynom([0, 0, 0])
        assert p7(0) == 0
        assert p7(1) == 0
        assert p7(111) == 0

    def test_neg(self):
        p1 = Polynom([1, 2, 3])
        expected = Polynom([-1, -2, -3])
        assert -p1 == expected

        p2 = Polynom({0: -3, 2: 1, 5: 4})
        expected1 = Polynom({0: 3, 2: -1, 5: -4})
        assert -p2 == expected1

        p3 = Polynom(0, 2, 0, 5)
        expected2 = Polynom(0, -2, 0, -5)
        assert -p3 == expected2

        p4 = Polynom(1)
        expected3 = Polynom(-1)
        assert -p4 == expected3

        p5 = Polynom([])
        expected4 = Polynom([])
        assert -p5 == expected4

    def test_eq(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([1, 2, 3])
        assert p1 == p2

        p3 = Polynom({0: -3, 2: 1, 5: 4})
        p4 = Polynom({0: -3, 2: 1, 5: 4})
        assert p3 == p4

        p5 = Polynom(0, 2, 0, 5)
        p6 = Polynom(0, 2, 0, 5)
        assert p5 == p6

        p7 = Polynom(1)
        p8 = Polynom(1)
        assert p7 == p8

        p9 = Polynom([])
        p10 = Polynom([])
        assert p9 == p10

        p11 = Polynom(0)
        p12 = Polynom([1, 2, 3])
        assert p11 != p12

        p13 = Polynom([0])
        p14 = Polynom(0)
        assert p13 == p14

        p15 = Polynom({})
        p16 = Polynom([])
        assert p15 == p16

    def test_sub(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([1, 2, 3])
        expected = Polynom([0, 0, 0])
        assert p1 - p2 == expected

        p3 = Polynom(5)
        p4 = Polynom([1, 2, 3])
        expected1 = Polynom([4, -2, -3])
        assert p3 - p4 == expected1
        expected2 = Polynom([-4, 2, 3])
        assert p4 - p3 == expected2

        p5 = Polynom({0: -3, 2: 1, 5: 4})
        p6 = Polynom({0: -3, 2: 1, 5: 4})
        expected3 = Polynom({0: 0, 2: 0, 5: 0})
        assert p5 - p6 == expected3

        p7 = Polynom(0, 2, 0, 5)
        p8 = Polynom(1, 2, 3, 8, 9, 10, 5, 11, 0)
        expected4 = Polynom(-1, 0, -3, -3, -9, -10, -5, -11, 0)
        assert p7 - p8 == expected4

    def test_rsub(self):
        p1 = Polynom([1, 2, 3])
        i1 = 5
        expected = Polynom([4, -2, -3])
        assert i1 - p1 == expected

        p2 = Polynom({0: -3, 2: 1, 5: 4})
        i2 = 3
        expected1 = Polynom([6, 0, -1, 0, 0, -4])
        assert i2 - p2 == expected1

        p3 = Polynom([1, 2, 3])
        i3 = 0
        expected2 = Polynom([1, 2, 3])
        assert p3 - i3 == expected2
        expected3 = Polynom([-1, -2, -3])
        assert i3 - p3 == expected3

    def test_der(self):
        p1 = Polynom([1, 2, 3])
        expected = Polynom([0, 2, 6])
        assert p1.der() == expected

        p2 = Polynom()
        expected1 = Polynom()
        assert p2.der() == expected1

        p3 = Polynom(1)
        expected2 = Polynom(0)
        assert p3.der() == expected2

        p4 = Polynom({})
        expected3 = Polynom()
        assert p4.der() == expected3

        p5 = Polynom(1, 2, 3, 4, 5, 6)
        expected4 = Polynom([0, 2, 6, 12, 20, 30])
        assert p5.der() == expected4

        p6 = Polynom({0: -3, 2: 1, 5: 4})
        expected5 = Polynom([0, 0, 2, 0, 0, 20])
        assert p6.der() == expected5

    def test_degree(self):
        p1 = Polynom([1, 2, 3])
        assert p1.degree() == 2

        p2 = Polynom([0])
        assert p2.degree() == "Нулевой полином Степень не определяется"

        p3 = Polynom()
        assert p3.degree() == "Нулевой полином Степень не определяется"

        p4 = Polynom({0: 0})
        assert p4.degree() == "Нулевой полином Степень не определяется"

        p5 = Polynom(1)
        assert p5.degree() == 0

    def test_mul(self):
        p1 = Polynom(1, 2, 3)
        p2 = Polynom(4, 5, 6)
        expected = Polynom([4, 13, 28, 27, 18])
        assert p1 * p2 == expected

        p3 = Polynom([0, 0, 0])
        p4 = Polynom([0, 0, 0])
        expected1 = Polynom([0, 0, 0, 0, 0])
        assert p3 * p4 == expected1

        p5 = Polynom(0)
        p6 = Polynom(0)
        expected2 = Polynom(0)
        assert p5 * p6 == expected2

        p7 = Polynom({})
        p8 = Polynom([0])
        expected3 = Polynom([])
        assert p7 * p8 == expected3

    def test_round(self):
        p1 = Polynom(1, 2, 3)
        i = 3
        expected = Polynom([3, 6, 9])
        assert p1 * i == expected
        assert i * p1 == expected

        p2 = Polynom([0, 0, 0])
        i2 = 3
        expected1 = Polynom([0, 0, 0])
        assert p2 * i2 == expected1
        assert i2 * p2 == expected1

        i3 = 0
        expected2 = Polynom([0, 0, 0])
        assert p1 * i3 == expected2
        assert i3 * p1 == expected2

        i4 = -1
        expected3 = Polynom([-1, -2, -3])
        assert p1 * i4 == expected3
        assert i4 * p1 == expected3

        assert p2 * i4 == expected2
        assert i4 * p2 == expected2

    def test_iter(self):
        p = Polynom(1, 2, 3, 4, 5)
        expected = [1, 2, 3, 4, 5, 6]
        for power, coef in p:
            assert coef == expected[power]

        p1 = Polynom(0)
        expected1 = [0]
        for power, coef in p1:
            assert coef == expected1[power]

        p2 = Polynom([])
        expected2 = []
        for power, coef in p2:
            assert coef == expected2[power]

    def test_next(self):
        p1 = Polynom([1, 2, 3])
        it = iter(p1)
        self.assertEqual(next(it), (0, 1))
        self.assertEqual(next(it), (1, 2))
        self.assertEqual(next(it), (2, 3))
        p2 = Polynom([])
        it = iter(p2)
        with self.assertRaises(StopIteration):
            next(it)

