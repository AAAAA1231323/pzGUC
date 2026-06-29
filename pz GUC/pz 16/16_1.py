#Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
#Добавьте методы для вычисления процентных начислений и снятия денег.

class B:
    def __init__(self, m, r):
        self.m = m
        self.r = r

    def p(self):
        return self.m * (self.r / 100)

    def w(self, a):
        if a <= self.m:
            self.m -= a
            return True
        return False


if __name__ == "__main__":
    x = B(100000, 12.5)
    print(x.p())
    print(x.w(30000))
    print(x.m)
    print(x.w(80000))