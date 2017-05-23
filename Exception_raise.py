class Rational:
    def __init__(self,x,y):
        number=x
        if y==0:
            raise ZeroDivisionError()
        else:
            denom=y
try:
    rat1 = Rational(1,2)
    rat2 = Rational(2,0)
except:
    print("Cannot have rational no with 0")
