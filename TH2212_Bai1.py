a=float(input("Nhập số đo chiều dài: "))
b=float(input("Nhập số đo chiều rộng: "))
while a<=0.0 or b>=100.0 :
    print(f"Vui lòng nhập lại dữ liệu")
    a=float(input("Nhập số đo chiều dài: "))
    b=float(input("Nhập số đo chiều rộng: "))
print(f"Chu vi hình chữ nhật là:{(a+b)*2:.2f} ")
print(f"Diện tích hình chữ nhật là:{a*b:.2f} ")

