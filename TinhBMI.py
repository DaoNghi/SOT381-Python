print ("Nhập chiều cao theo Cm: ")
a=int(input())
a=a/100
print ("Nhập cân nặng theo Kg: ")
b=int(input())
c=b/(a*a)
if c<18.5:
  print("Bạn hơi gầy")
elif c>=18.5 and c<=24.9:
  print("Cơ thể bạn bình thường")
elif c>=25 and c<=29.9:
  print("Cơ thể bạn hơi béo")
elif c>=30 and c<=34.9:
  print("Bạn đang béo phì cấp độ 1")
elif c>=35 and c<=39.9:
  print("Bạn đang béo phì cấp độ 2")
elif c>=40:
  print("Bạn đang béo phì cấp độ 3")


