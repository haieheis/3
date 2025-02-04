import unittest
import coverage
from rational import RationalNum


cov = coverage.Coverage()
cov.start()


class TestRational(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            RationalNum(1, 0)

    def test_down1(self):
        r1 = RationalNum(3, 1)
        r2 = RationalNum(2, 1)
        res = r1 + r2
        self.assertEqual(res.get_up(), 5)
        self.assertEqual(res.get_down(), 1)

    def test_one(self):
        r = RationalNum(1, 1)
        self.assertEqual(r.get_up(), 1)
        self.assertEqual(r.get_down(), 1)

    def test_add(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, 4)
        res = r1 + r2
        self.assertEqual(res.get_up(), 10)
        self.assertEqual(res.get_down(), 8)

    def test_addm(self):
        r1 = RationalNum(-1, 2)
        r2 = RationalNum(3, -4)
        res = r1 + r2
        self.assertEqual(res.get_up(), 10)
        self.assertEqual(res.get_down(), -8)

    def test_sub(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, 4)
        res = r1 - r2
        self.assertEqual(res.get_up(), -2)
        self.assertEqual(res.get_down(), 8)

    def test_mul(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, 4)
        res = r1 * r2
        self.assertEqual(res.get_up(), 3)
        self.assertEqual(res.get_down(), 8)
    
    def test_mul0(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(0, 2)
        self.assertEqual(r1 * r2, 0)

    def test_mulm(self):
        r1 = RationalNum(-1, 2)
        r2 = RationalNum(3, -4)
        res = r1 * r2
        self.assertEqual(res.get_up(), -3)
        self.assertEqual(res.get_down(), -8)

    def test_truediv(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, 4)
        res = r1 / r2
        self.assertEqual(res.get_up(), 4)
        self.assertEqual(res.get_down(), 6)
    
    def test_truedivm(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, -4)
        res = r1 / r2
        self.assertEqual(res.get_up(), -4)
        self.assertEqual(res.get_down(), 6)

    def test_truedivmm(self):
        r1 = RationalNum(-1, 2)
        r2 = RationalNum(3, -4)
        res = r1 / r2
        self.assertEqual(res.get_up(), 4)
        self.assertEqual(res.get_down(), 6)

    def test_truediv00(self):
        r3 = RationalNum(1, 2)
        r4 = RationalNum(0, 1)
        with self.assertRaises(ValueError):
            r3 / r4

    def test_eq(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(2, 4)
        r3 = RationalNum(3, 4)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_eqm(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(-1, 2)
        self.assertFalse(r1 == r2)
        self.assertTrue(r1 != r2)

    def test_ne(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(3, 4)
        self.assertTrue(r1 != r2)

    def test_neg(self):
        r = RationalNum(1, 2)
        self.assertEqual(-r, -RationalNum(1, 2))

    def test_abs(self):
        r1 = RationalNum(1, 2)
        self.assertEqual(abs(r1), RationalNum(1, 2))

        r2 = RationalNum(0, 1)
        self.assertEqual(abs(r2), RationalNum(0, 1))


    def test_pow(self):
        r = RationalNum(2, 3)
        self.assertEqual(r**2, RationalNum(4, 9))

        res = r ** 0
        self.assertEqual(res.get_up(), 1)
        self.assertEqual(res.get_down(), 1)

    def test_powm(self):
        r = RationalNum(1, 2)
        with self.assertRaises(ValueError):
            r ** -1

    def test_powmm(self):
        r = RationalNum(-2, 3)
        res = r ** 2
        self.assertEqual(res.get_up(), 4)
        self.assertEqual(res.get_down(), 9)

    def test_repr(self):
        r = RationalNum(1, 2)
        self.assertEqual(repr(r), '1/2')
    
    def test_reprm(self):
        r = RationalNum(-1, 2)
        self.assertEqual(repr(r), "-1/2")

    def test_get_up(self):
        r = RationalNum(1, 2)
        self.assertEqual(r.get_up(), 1)

    def test_get_down(self):
        r = RationalNum(1, 2)
        self.assertEqual(r.get_down(), 2)

    def test_set_up(self):
        r = RationalNum(1, 2)
        r.set_up(3)
        self.assertEqual(r.get_up(), 3)

    def test_set_down(self):
        r = RationalNum(1, 2)
        r.set_down(4)
        self.assertEqual(r.get_down(), 4)

    def test_set_down0(self):
        r = RationalNum(1, 2)
        with self.assertRaises(ValueError):
            r.set_down(0) 

    def test_large_nums(self):
        r1 = RationalNum(10**100, 1)
        r2 = RationalNum(10**100, 1)
        res = r1 * r2
        self.assertEqual(res.get_up(), 10**200)
        self.assertEqual(res.get_down(), 1)

    def test_small_nums(self):
        r1 = RationalNum(1, 10**100)
        r2 = RationalNum(1, 10**100)
        res = r1 * r2
        self.assertEqual(res.get_up(), 1)
        self.assertEqual(res.get_down(), 10**200)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRational)
unittest.TextTestRunner().run(suite)

cov.stop()
cov.save()
cov.report()