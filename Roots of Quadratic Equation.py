import math
print ('General form of a quadratic equation is ax²+bx+c')
a=int(input('Enter coefficient of x²:'))
b=int(input('Enter coefficient of x:'))
c=int(input('Enter constant:'))
D=(b*b)-(4*a*c)
if D==0:
    x=-b/(2*a)
    print (x)
    print ('Roots are equal')
    
elif D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print ('x1=',x1,'& x2=',x2)
    print ('Roots are real')
else:
    print ('Roots are imaginary')

