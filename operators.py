

class Fraction:

    @staticmethod
    def __gcd(a, b):
        while(b != 0):
            a,b = b, a%b
        return a
    
    # denominator -- знаменатель
    # numerator   -- числитель
    def __init__(self, numerator, denominator):
        if not isinstance(numerator,int) and isinstance(denominator,int):
            raise TypeError("Введенные числитель и знаменатель должны быть целыми")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        
        gcd = self.__gcd(numerator,denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
    def __repr__(self):
        return f"Fraction {self.numerator}/{self.denominator}"          
    def __str__(self): 
        return f"Fraction {self.numerator}/{self.denominator}" 
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator + 
                    self.denominator * other.numerator)
            new_denominator = (self.denominator * other.denominator)
            return Fraction(new_numerator, new_denominator)


           
'''
Питон -- язык с динамической типизацией и на один класс только один add и тд,
не как в плюсах
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

'''
q = Fraction(13,26)
z = Fraction(13,26)
print(q+z)

