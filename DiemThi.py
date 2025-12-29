a=int(input("Nhập điểm thi môn Toán : "))
b=int(input("Nhập điểm thi môn Lý : "))
c=int(input("Nhập điểm thi môn Hóa : "))
if a+b+c>=15 and a>=4 and b>=4 and c>=4:
    print("Đậu")
    if a>5 and b>5 and c>5:
        print("Học đều các môn")
    else:
        print("Học chưa đều các môn")
else:
    print("Thi hỏng")