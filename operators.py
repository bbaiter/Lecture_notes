

class Fraction:

    @staticmethod
    def __gcd(a, b):
        a, b = abs(a), abs(b)
        while(b != 0):
            a,b = b, a%b
        return a
    
    # denominator -- знаменатель
    # numerator   -- числитель
    # пока без float
    # constructor
    def __init__(self, numerator, denominator = 1):
        if not (isinstance(numerator,int) and isinstance(denominator,int)):
            raise TypeError("Введенные числитель и знаменатель должны быть целыми")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        
        gcd = self.__gcd(numerator,denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        if denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        return f"Fraction {self.numerator}/{self.denominator}"  
    
    # print(Frac)     
    def __str__(self): 
        if self.numerator == 0:
            return '0'
        return f"Fraction {self.numerator}/{self.denominator}" 
    
    # a/b -> b/a
    @property
    def reverse(self):
        return Fraction(self.denominator,self.numerator)
    # Frac + other
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator + 
                    self.denominator * other.numerator)
            new_denominator = (self.denominator * other.denominator)
            return Fraction(new_numerator, new_denominator)
        if isinstance(other, int):
            new_numerator = (self.numerator + 
                    self.denominator * other)
            new_denominator = self.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented
    # other + Frac
    # комутативная операция
    def __radd__(self, other):
        return self + other
    
    # Frac * other
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        return NotImplemented
    # other * Frac
    def __rmul__(self, other):
        return self * other
        
    # Frac - other
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return self + Fraction(-other.numerator, other.denominator)
        
        if isinstance(other, int):
            return self + Fraction(-other, 1)
        return NotImplemented
    # other - Frac
    def __rsub__(self,other):
        if isinstance(other, int):
            return Fraction(other) - self
        return NotImplemented

    # Frac / other
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self * other.reverse
        
        if isinstance(other, int):
            return self * Fraction(1, other)
        return NotImplemented
    
    # other / Frac
    def __rtruediv__(self, other):
        return other * self.reverse

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return ((self.denominator == other.denominator) and \
                (self.numerator == other.numerator))
        if isinstance(other, int):
            return ((self.denominator == 1) and \
                        (self.numerator == other))
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, (Fraction, int)):
            q = self - other
            return q.numerator < 0
        return NotImplemented
        
    def __le__(self, other):
        if isinstance(other, (Fraction, int)):
            return ((self < other) or (self == other))
        return NotImplemented
    def __gt__(self,other):
        if isinstance(other, (Fraction, int)):
            return not((self < other) or (self == other))
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, (Fraction, int)):
            return not (self < other)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, (Fraction, int)):
            return not (self == other)
        return NotImplemented


           
'''
Питон -- язык с динамической типизацией и на один класс только один add и тд,
не как в плюсах

Нельзя создать несколько инит. Только если парсить *args в одной функции
def __add__(self, other):    frac+frac
def __mul__(self, other):    frac*frac
def __eq__(self, other):     ==
определять для того, чтобы разрешить кэшировать объекты класса
(например для ключей словаря)
при перегрузке == хэширование пропадает -- надо определять самому
def __hash__ (self)                     
def __ne__(self, other):     !=
def __lt__(self, other):     < 
def __le__(self, other):    <=
def __gt__(self, other):    >
def __ge__(self, other):    >=
def __bool__(self):         bool(Fraction)
def __str__(self):          info for users
def __repr__(self)          info for devs
def __len__(self)           ???
def __call__(self, *args, **kwargs)

'''
q = Fraction(10,3)
z = Fraction(1,3)
print(Fraction(1, 1) > 1)

