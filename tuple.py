fruits = ("apple","banana","cherry")
print(fruits[0])

fruits = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])
#เพิ่มค่า
x = ("apple","banana","cherry")
y = list(x) #แปลงเป็น list แล้วเก้บค่าเข้า y
y[1] = "kiwi"
x = tuple(y)
 #แปลง list เป็น tuple แล้วเก็บค่ากลับ x
print(x)

#ลบค่าใน tuple
x = ("apple","banana","cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

#join
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 =tuple1 + tuple2
print(tuple3)

#range
x = range(3,6)
for n in x :
    print(n)

x = range(3, 20, 2)
for n in x:
    print("rangeแบบstep2" ,n)
#นาย วรพล วิถีธรรม ม.6/14 เลขที่ 23