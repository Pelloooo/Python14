fruits = ["apple","banana","charry","watermelon","blueberry"]
print(fruits[0])

#เปลี่ยนค่าใน list
fruits[0] = "blackcurrant"
print(fruits[0])

#เปลี่ยนค่าใน list หลสายค่า
fruits[1:3] =["kiwi","mango","pineapple"]
print(fruits)

#เพิ่มค่าใน list
fruits.append("orange")
print(fruits)

#แทรกค่าใน list
fruits.insert(3, "grape")
print(fruits)
tropical = ["mango" ,"pineapple","papaya"]
fruits.extend(tropical)
print(fruits)

#ลบค่าใน list
fruits.remove("watermelon")
print(fruits)

fruits.pop(5)
print(fruits)

#del alphabet
#print(alphabet)

#เรียง list ใหม่
fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

#นาย วรพล วิถีธรรม ม.6/14 เลขที่ 23