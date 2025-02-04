class RationalNum:

    def __init__(self, numerator, denominator):
        try:
            numerator / denominator
        except:
            if denominator == 0:
                raise ValueError('Делить на 0 нельзя')
        
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other): #сложение
        up = self.numerator * other.denominator + other.numerator * self.denominator
        down = self.denominator * other.denominator

        return RationalNum(up, down)

    def __sub__(self, other): #вычитание
        up = self.numerator * other.denominator - other.numerator * self.denominator
        down = self.denominator * other.denominator

        return RationalNum(up, down)

    def __mul__(self, other): #умножение
        up = self.numerator * other.numerator
        down = self.denominator * other.denominator

        return RationalNum(up, down)

    def __truediv__(self, other): #деление
        if other.numerator == 0:
            raise ValueError('Делить на 0 нельзя')
        
        up = self.numerator * other.denominator
        down = self.denominator * other.numerator

        return RationalNum(up, down)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self): #унарный минус
        return RationalNum(-self.numerator, self.denominator)

    def __abs__(self):
        return RationalNum(abs(self.numerator), abs(self.denominator))

    def __pow__(self, n):
        if n == 0:
            return RationalNum(1, 1)
        
        if n < 0:
                raise ValueError('Степень числа должна быть натуральной')

        up = self.numerator ** n
        down = self.denominator ** n

        return RationalNum(up, down)
        
    def __repr__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        
        if self.numerator == 0:
            return 0
        
        return f"{self.numerator}/{self.denominator}"


    '''
    геттеры и сеттеры
    '''
    def get_up(self):
        return self.numerator

    def get_down(self):
        return self.denominator

    def set_up(self, value):
        self.numerator = value

    def set_down(self, value):
        if value == 0:
            raise ValueError('Делить на 0 нельзя')
        
        self.denominator = value

    def __lt__(self, other):
        '''
        это мне нужно было для вывода отрицательной мнимой части
        complex.py line 153
        '''

        return self.numerator * other.denominator < other.numerator * self.denominator