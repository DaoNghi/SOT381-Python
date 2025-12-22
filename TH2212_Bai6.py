n=int(input("Nhập số lượng bài hát: "))
i=0
nhac=[]
while i<n:
    a=str(input(f"Nhập tên bài hát thứ {i+1}: "))
    i=i+1
    nhac.append(a)
for i in range(n):
    Nhac=nhac[i]
    NHAC=Nhac.upper()
    print(f"Bài {i+1} : {NHAC}")
for i in range(n):
    Nhac=nhac[i]
    if Nhac.find("yêu")!=-1:
        print(f"Bài {i+1} : {Nhac}")
   
tendai=nhac[0]
tudai=len(tendai.split())
vitri=0
for i in range(n):
    hac=nhac[i]
    tu=len(hac.split())
    if tu>tudai:
        vitri=i
        tendai=hac
        tudai=tu
   
print(f"Bài: {tendai} có tên dài nhất")
    
    