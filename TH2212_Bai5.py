n=int(input("Nhập số n: "))
i=0
j=2
b=0
a=0
for i in range(n):
    i=i+1
    a=a+i
for j in range(n//2):
    j=j+2
S=a/j
print(S)