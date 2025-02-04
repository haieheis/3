'''
1)def __sub__(self, other): #вычитание
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))
        self.real = self.real - other.real
        self.im = self.im - other.im

        return self

2)def __sub__(self, other): #вычитание
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        return ComplexNum(self.real - other.real, self.im - other.im)

я не понимаю почему при первом варианте код выводит неправильный ответ, а во втором варианте все нормально =(
'''


from rational import RationalNum
import math


class ComplexNum:

    def __init__(self, real, im):
        '''
        хранение в виде рациональных чисел и неявное преобразование
        '''
        
        if isinstance(real, (int, float)) and isinstance(im, (int, float)):
            self.real = RationalNum(real, 1)
            self.im = RationalNum(im, 1)

        else:
            self.real = real
            self.im = im


    '''
    перегрузка операторов
    '''
    def __add__(self, other): #сложение
        if isinstance(other, (int, float)): #преобразовываем число типа int, float в комплексное
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        return ComplexNum(self.real + other.real, self.im + other.im)

    def __sub__(self, other): #вычитание
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        return ComplexNum(self.real - other.real, self.im - other.im)

    def __mul__(self, other): #умножение
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        real = self.real * other.real - self.im * other.im
        im = self.real * other.im + self.im * other.real

        return ComplexNum(real, im)

    def __truediv__(self, other): #деление
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        denominator = other.real * other.real + other.im * other.im

        if denominator == RationalNum(0, 1):
            raise ValueError('Делить на 0 нельзя')

        real = (self.real * other.real + self.im * other.im) / denominator
        im = (other.real * self.im - self.real * other.im) / denominator

        return ComplexNum(real, im)

    def __eq__(self, other): #равенство
        return self.real == other.real and self.im == other.im

    def __ne__(self, other): #неравенство
        return not self.__eq__(other)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))
        
        self.real += other.real
        self.im += other.im

        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        self.real -= other.real
        self.im -= other.im

        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        self.real = self.real * other.real - self.im * other.im
        self.im = self.real * other.im + self.im * other.real
        
        return self

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(int(other), 1), RationalNum(0, 1))

        denominator = (other.real ** 2) + (other.im ** 2)

        if denominator == RationalNum(0, 1):
            raise ValueError('Делить на 0 нельзя')

        self.real = (self.real * other.real + self.im * other.im) / denominator
        self.im = (other.real * self.im - self.real * other.im) / denominator
        
        return self

    def __neg__(self): #унарный минус
        return ComplexNum(-self.real, -self.im)

    def __abs__(self): #модуль
        real = self.real.numerator / self.real.denominator
        im = self.im.numerator / self.im.denominator

        return (real**2 + im**2)**0.5

    def arg(self):  #аргумент (угол)
        return math.atan2(self.im.numerator / self.im.denominator, self.real.numerator / self.real.denominator)
    
    def __pow__(self, n): #степень
        if n < 0:
            raise ValueError('Степень должна быть натуральным числом')
        
        elif n == 0:
            return ComplexNum(RationalNum(1, 1), RationalNum(0, 1))

        else:
            r = self.__abs__()
            f = self.arg()

            real = r**n * math.cos(n * f)
            im = r**n * math.sin(n * f)

            return ComplexNum(RationalNum(int(real), 1), RationalNum(int(im), 1))

    def __repr__(self): #вывод
        if self.im < RationalNum(0, 1):
            return f"{self.real} - {-self.im}i"
        
        elif self.real == 0:
            return f"{self.im}"
        
        elif self.im == 0:
            return f"{self.real}"
        
        else:
            return f"{self.real} + {self.im}i"

    '''
    геттеры и сеттеры
    '''
    def get_real(self):
        return self.real

    def get_im(self):
        return self.im

    def set_real(self, value):
        self.real = value

    def set_im(self, value):
        self.im = value