

def Decorator(F):
    def Rasst(U,U1,t):
        a=F(U,U1,t)
        S=U*t+(a*(t*t))/2

        print(S,'Расстояние')
    return Rasst

@Decorator
def Fizika(U,U1,t):
    a=(U1-U)/t
    print(a,'Ускорение')
    return a


try:
    print('Скорость начальная')
    U=int(input())
    print('Скорость конечная')
    U1=int(input())
    print('Время')
    t=int(input())
    Fizika(U,U1,t)

except ZeroDivisionError:
    print('Дурачек?На ноль не делят...Попробуй заново.')
except TypeError:
    print('Ты по моему перепутал(тип),попробуй заново ВВЕСТИ ЧИСЛА...')
except ValueError:
    print('Ты по моему перепутал(валюта),попробуй заново ВВЕСТИ ЧИСЛА...')

