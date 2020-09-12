Line1=input()
Value_int=[int(X) for X in Line1.split(" ")]
A=Value_int[0]
B=Value_int[1]
C=Value_int[2]
D=Value_int[3]
Value=B>C
Value=Value and D>A
Value=Value  and C+D>A+B
Value=Value and C>0 and D>0
Value=Value and  A%2==0
if(Value) :
    print("Valores aceitos")
else :
    print("Valores nao aceitos")