a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
def lonnhat(a,b,c):
    x=a
        
    if x<b:
        x=b
    if x<c:
        x=c
    

    return x
def nhonhat(a,b,c):
    z=a
    if z>b:
        z=b
    if z>c:
        z=c
    return z
print("Số lớn nhất là:",lonnhat(a,b,c))
print("Số nhỏ nhất là:",nhonhat(a,b,c))

