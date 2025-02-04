from complex import ComplexNum
from rational import RationalNum
import unittest
import coverage
import math

cov = coverage.Coverage()
cov.start()


class TestComplex(unittest.TestCase):

    def test_init(self):
        c1 = ComplexNum(RationalNum(1, 1), RationalNum(2, 1))
        self.assertEqual(c1.get_real(), RationalNum(1, 1))
        self.assertEqual(c1.get_im(), RationalNum(2, 1))

        c2 = ComplexNum(RationalNum(3, 2), RationalNum(5, 2))
        self.assertEqual(c2.get_real(), RationalNum(3, 2))
        self.assertEqual(c2.get_im(), RationalNum(5, 2))

    def test_add(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        res = c1 + c2
        self.assertEqual(res.get_real(), RationalNum(5, 2))
        self.assertEqual(res.get_im(), RationalNum(3, 4))

    def test_sub(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        res = c1 - c2
        self.assertEqual(res.get_real(), RationalNum(-3, 2))
        self.assertEqual(res.get_im(), RationalNum(3, 4))

    def test_mul(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        res = c1 * c2
        self.assertEqual(res.get_real(), RationalNum(1, 1))
        self.assertEqual(res.get_im(), RationalNum(3, 2))

    def test_truediv(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        res = c1 / c2
        self.assertEqual(res.get_real(), RationalNum(1, 4))
        self.assertEqual(res.get_im(), RationalNum(3, 8))

    def test_truediv0(self): #деление на 0
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(0, 0)
        with self.assertRaises(ValueError):
            c1 / c2

    def test_eq(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c3 = ComplexNum(2, 0)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)

    def test_iadd(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        c1 += c2
        self.assertEqual(c1.get_real(), RationalNum(5, 2))
        self.assertEqual(c1.get_im(), RationalNum(3, 4))

    def test_isub(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        c1 -= c2
        self.assertEqual(c1.get_real(), RationalNum(-3, 2))
        self.assertEqual(c1.get_im(), RationalNum(3, 4))

    def test_imul(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        c1 *= c2
        self.assertEqual(c1.get_real(), RationalNum(1, 1))
        self.assertEqual(c1.get_im(), RationalNum(3, 2))

    def test_itruediv(self): 
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(2, 0)
        c1 /= c2
        self.assertEqual(c1.get_real(), RationalNum(1, 4))
        self.assertEqual(c1.get_im(), RationalNum(3, 8))
    
    def test_itruediv0(self): #деление на 0
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(0, 0)
        with self.assertRaises(ValueError):
            c1 /= c2

    def test_neg(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        result = -c1
        self.assertEqual(result.get_real(), RationalNum(-1, 2))
        self.assertEqual(result.get_im(), RationalNum(-3, 4))

    def test_abs(self):
        c1 = ComplexNum(RationalNum(3, 4), RationalNum(4, 5))
        self.assertAlmostEqual(abs(c1), ((3/4)**2 + (4/5)**2) ** 0.5)

    def test_abs0(self): #модуль 0
        c1 = ComplexNum(0, 0)
        result = abs(c1)
        self.assertEqual(result, 0)

    def test_arg(self):
        c1 = ComplexNum(RationalNum(1, 1), RationalNum(1, 1))
        self.assertAlmostEqual(c1.arg(), math.atan2(1, 1))

        c2 = ComplexNum(0, RationalNum(1, 1)) #real = 0
        self.assertAlmostEqual(c2.arg(), math.pi / 2)

        c3 = ComplexNum(RationalNum(1, 1), 0) #im = 0
        self.assertAlmostEqual(c3.arg(), 0)

        c4 = ComplexNum(RationalNum(0, 1), RationalNum(0, 1)) #число = 0
        self.assertEqual(c4.arg(), 0)    

    def test_pow(self):
        c1 = ComplexNum(0, 1)
        res1 = c1 ** 2
        self.assertEqual(res1.get_real(), RationalNum(-1, 1))
        self.assertEqual(res1.get_im(), RationalNum(0, 1))
        
        c2 = ComplexNum(RationalNum(1, 2), RationalNum(1, 2))
        res2 = c2 ** 2
        self.assertEqual(res2.get_real(), RationalNum(0, 1))
        self.assertEqual(res2.get_im(), RationalNum(0, 1))

    def test_pow0(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        res = c1 ** 0
        self.assertEqual(res.get_real(), RationalNum(1, 1))
        self.assertEqual(res.get_im(), RationalNum(0, 1))

    def test_pown(self): #целые числа
        c1 = ComplexNum(1, 2)
        with self.assertRaises(ValueError):
            c1 ** -1

    def test_pownn(self): #рациональные числа
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        with self.assertRaises(ValueError):
            c1 ** -1

    def test_repr(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        self.assertEqual(repr(c1), "1/2 + 3/4i")

    def test_reprn(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(-3, 4))
        self.assertEqual(repr(c1), "1/2 - 3/4i")    

    def test_get_real(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        self.assertEqual(c1.get_real(), RationalNum(1, 2))

    def test_get_im(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        self.assertEqual(c1.get_im(), RationalNum(3, 4))

    def test_set_real(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c1.set_real(RationalNum(2, 1))
        self.assertEqual(c1.get_real(), RationalNum(2, 1))

    def test_set_im(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c1.set_im(RationalNum(5, 4))
        self.assertEqual(c1.get_im(), RationalNum(5, 4))

    def test_large_nums(self):
        c1 = ComplexNum(RationalNum(10**100, 1), RationalNum(10**100, 1))
        c2 = ComplexNum(RationalNum(10**100, 1), RationalNum(10**100, 1))
        res = c1 * c2
        self.assertEqual(res.get_real(), RationalNum(0, 1))
        self.assertEqual(res.get_im(), RationalNum(2 * 10**200, 1))

    def test_small_nums(self):
        c1 = ComplexNum(RationalNum(1, 10**10), RationalNum(1, 10**10))
        c2 = ComplexNum(RationalNum(1, 10**10), RationalNum(1, 10**10))
        res = c1 + c2
        self.assertEqual(res.get_real(), RationalNum(2, 10**10))
        self.assertEqual(res.get_im(), RationalNum(2, 10**10))

    def test_real0(self):
        c1 = ComplexNum(0, RationalNum(3, 4))
        c2 = ComplexNum(0, RationalNum(1, 2))
        res1 = c1 + c2
        self.assertEqual(res1.get_real(), RationalNum(0, 1))
        self.assertEqual(res1.get_im(), RationalNum(5, 4))

    def test_im0(self):
        c1 = ComplexNum(RationalNum(1, 2), 0)
        c2 = ComplexNum(RationalNum(3, 4), 0)
        res = c1 + c2
        self.assertEqual(res.get_real(), RationalNum(5, 4))
        self.assertEqual(res.get_im(), RationalNum(0, 1))

    def test_operations(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(2, 1), RationalNum(1, 2))
        c3 = ComplexNum(RationalNum(1, 1), RationalNum(1, 1))
        res = c1 - c2 + c3
        self.assertEqual(res.get_real(), RationalNum(-1, 2))
        self.assertEqual(res.get_im(), RationalNum(10, 8))    

    def test_add_int_float(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        res1 = c1 + 2
        self.assertEqual(res1.get_real(), RationalNum(5, 2))
        self.assertEqual(res1.get_im(), RationalNum(3, 4))

        res2 = c1 + 2.5
        self.assertEqual(res2.get_real(), RationalNum(5, 2))
        self.assertEqual(res2.get_im(), RationalNum(3, 4))

    def test_sub_int_float(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        res1 = c1 - 2
        self.assertEqual(res1.get_real(), RationalNum(-3, 2))
        self.assertEqual(res1.get_im(), RationalNum(3, 4))

        res2 = c1 - 2.5
        self.assertEqual(res2.get_real(), RationalNum(-3, 2))
        self.assertEqual(res2.get_im(), RationalNum(3, 4))

    def test_mul_int_float(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        res1 = c1 * 2
        self.assertEqual(res1.get_real(), RationalNum(1, 1))
        self.assertEqual(res1.get_im(), RationalNum(3, 2))

        res2 = c1 * 2.5
        self.assertEqual(res2.get_real(), RationalNum(8, 8))
        self.assertEqual(res2.get_im(), RationalNum(12, 8))

    def test_truediv_int_float(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        res1 = c1 / 2
        self.assertEqual(res1.get_real(), RationalNum(1, 4))
        self.assertEqual(res1.get_im(), RationalNum(3, 8))

        c2 = ComplexNum(RationalNum(1, 1), RationalNum(1, 4))
        res2 = c2 / 1.5
        self.assertEqual(res2.get_real(), RationalNum(4, 4))
        self.assertEqual(res2.get_im(), RationalNum(1, 4))

    def test_truediv_real0_im0(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(0, 1), RationalNum(1, 1))
        res1 = c1 / c2
        self.assertEqual(res1.get_real(), RationalNum(6, 8))
        self.assertEqual(res1.get_im(), RationalNum(-4, 8))

        c3 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c4 = ComplexNum(RationalNum(1, 1), 0)
        res2 = c3 / c4
        self.assertEqual(res2.get_real(), RationalNum(4, 8))
        self.assertEqual(res2.get_im(), RationalNum(3, 4))   


suite = unittest.TestLoader().loadTestsFromTestCase(TestComplex)
unittest.TextTestRunner().run(suite)

cov.stop()
cov.save()
cov.report()