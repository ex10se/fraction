from decimal import Decimal


# сокращалка дробей
# allows to reduce a simple fraction
def fraction_reduction(num, denom):
    if not num:  # если числитель равен нулю, результат ноль
        return 0
    elif denom == 1 and isinstance(num, float):  # если в числителе десятичная дробь,
        return get_num_denom(num)  # применяем рекурсию, предварительно превратив дробь в обыкновенную
    elif denom == 1 and isinstance(num, int):  # если целое число, возвращаем только его
        return num
    if num * denom > 0:  # исправляем знаки (перемещаем минус в числитель)
        num, denom = abs(num), abs(denom)
    else:
        num, denom = -abs(num), abs(denom)
    for i in reversed(range(1, denom + 1)):  # идём по целым числам от знаменателя и вниз в поисках наибольшего делителя
        if not num % i and not denom % i:
            if denom // i == 1:  # если в знаменателе единица в результате сокращения
                return num // i
            return num // i, denom // i


# получаем обыкновенную дробь из десятичной
# allows to get a simple fraction from a decimal
def get_num_denom(number: float):
    num = Decimal(str(number)).as_integer_ratio()[0]
    denom = Decimal(str(number)).as_integer_ratio()[1]
    return fraction_reduction(num, denom)  # сокращаем


class Fraction:
    """
    Класс для работы с числами.
    Поддерживается ввод обыкновенных и десятичных дробей, целых и отрицательных чисел.
    Для ввода десятичных дробей и целых чисел знаменатель следут принимать за единицу.

    Class that allows to calculate.
    It supports input of simple fractions, decimals, integers and negative numbers.
    If you want to calculate decimal or integer, you have to take denominator as one.
    """

    def __init__(self, num, denom=1):
        if denom == 0:
            exit('Знаменатель не может быть равен нулю')
        if (isinstance(num, float) or isinstance(denom, float)) and denom != 1:  # если дробь десятичная в обыкновенной
            exit('Ввод десятичной дроби как части обыкновенной дроби не поддерживается')
        reduced_fraction = fraction_reduction(num, denom)
        if not isinstance(reduced_fraction, tuple):  # если вернулся только числитель
            self.a = reduced_fraction
            self.b = denom
        else:
            self.a = reduced_fraction[0]
            self.b = reduced_fraction[1]

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        return f'{self.a}/{self.b}'

    def __add__(self, other):
        new_numerator = self.a * other.b + self.b * other.a
        new_denominator = self.b * other.b
        reduced_fraction = fraction_reduction(new_numerator, new_denominator)
        if not isinstance(reduced_fraction, tuple):
            return str(reduced_fraction)
        return f'{reduced_fraction[0]}/{reduced_fraction[1]}'

    def __sub__(self, other):
        new_numerator = self.a * other.b - self.b * other.a
        new_denominator = self.b * other.b
        reduced_fraction = fraction_reduction(new_numerator, new_denominator)
        if not isinstance(reduced_fraction, tuple):
            return str(reduced_fraction)
        return f'{reduced_fraction[0]}/{reduced_fraction[1]}'

    def __mul__(self, other):
        new_numerator = self.a * other.a
        new_denominator = self.b * other.b
        reduced_fraction = fraction_reduction(new_numerator, new_denominator)
        if not isinstance(reduced_fraction, tuple):
            return str(reduced_fraction)
        return f'{reduced_fraction[0]}/{reduced_fraction[1]}'

    def __int__(self):
        return int(self.a / self.b)

    def __float__(self):
        return self.a / self.b


# числитель, знаменатель первой дроби/числа
# numerator and denominator the second fraction/number
a = 1.52
b = 1

# числитель, знаменатель второй дроби/числа
# numerator and denominator the second fraction/number
c = 26
d = -50

fraction_1 = Fraction(a, b)
fraction_2 = Fraction(c, d)

print(f'Дано: {fraction_1}, {fraction_2}')  # given
print(f'Сумма: {fraction_1 + fraction_2}')  # add
print(f'Разность: {fraction_1 - fraction_2}')  # subtract
print(f'Произведение: {fraction_1 * fraction_2}')  # multiply

