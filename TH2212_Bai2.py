a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
x=a
z=a
if x<b:
    x=b
if x<c:
    x=c
if z>b:
    z=b
if z>c:
    z=c
print(f"Số lớn nhất là:{x}")
print(f"Số lớn nhất là:{z}")
