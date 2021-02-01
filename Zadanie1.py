

def Decorator(F):
    def Rasst(U,U1,t):
        a=F(U,U1,t)
        c=U*t
        b=(a*(t*t))/2
        S=c+b

        print(S,'Расстояние')
    return Rasst

@Decorator
def Fizika(U,U1,t):
    a=(U1-U)/t
    print(a,'Ускорение')
    return Fizika


try:
    print('Скорость начальная')
    U=float(input())
    print('Скорость конечная')
    U1=float(input())
    print('Время')
    t=float(input())
    Fizika(U,U1,t)

except ZeroDivisionError:
    print('Дурачек?На ноль не делят...Попробуй заново.')
except TypeError:
    print('Ты по моему перепутал(тип),попробуй заново ВВЕСТИ ЧИСЛА...')
except ValueError:
    print('Ты по моему перепутал(валюта),попробуй заново ВВЕСТИ ЧИСЛА...')

