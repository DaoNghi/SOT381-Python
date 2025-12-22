n=int(input("Nhập số n: "))
a=0
b=1
c=0
s=0
for i in range(n):
    a=b
    b=c
    c=a+b
    s+=b
    print(b,end=' ')

print(f"\nTổng bằng:{s}")