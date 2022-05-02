class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        if self.a != 0:
            if self.b > 0:
                if self.b != 1:
                    return f'{self.a}+{self.b}i'
                else:
                    return f'{self.a}+i'
            elif self.b == 0:
                return f'{self.a}'
            else:
                return f'{self.a}{self.b}i'
        else:
            if self.b == 0:
                return f'0'
            else:
                return f'{self.b}i'


complex_num1 = ComplexNumber(10, -2)
complex_num2 = ComplexNumber(6, 3)
sum_complex = complex_num1 + complex_num2
print(sum_complex)
mult_complex = complex_num1 * complex_num2
print(mult_complex)