a=int(input("enter nomber a:"))
b=int(input("enter nomber b:"))
c=int(input("enter nomber c:"))
D=b**2-4*a*c
if D<0:
    print("the equation is no solution")
elif D==0:
    x=(-b)/(2*a)
    print("the equation solution is",x)
else:
    x1=(-b-D**0.5)/2*a
    x2=(-b+D**0.5)/2*a
    print("the equations solution is",x1,"and",x2)
    