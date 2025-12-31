n=int(input("Nhap n: "))
ds=[]
i=1
s=0
j=0
while i<=n:
    a=int(input(f"Nhap phan tu thu {i}: "))
    i=i+1
    ds.append(a)
for j in range(n):
    Ds=ds[j]
    if Ds%2==0 or Ds%3==0:
        s=s+Ds
print(f"Tong cac so chia het cho 2 va 3 trong danh sach la: {s}")
