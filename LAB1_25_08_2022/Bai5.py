""" 
5)cho chuỗi text = "記者 鄭啟源 羅智堅" ; 
a)Kết quả mã hóa của chuỗi text
b)Cho biết kết quả của 2 lệnh sau:
print(len(text))
print(len(text.encode('utf-8')))
 """
""" text = "記者 鄭啟源 羅智堅"
 #a)Kết quả mã hóa của chuỗi text
print("Kết quả mã hóa của chuỗi text: ")
print(text.encode("utf-8")) """
"""  
b)Cho biết kết quả của 2 lệnh sau:
print(len(text))
print(len(text.encode('utf-8'))) 
"""
""" print("Kết quả của lệnh print(len(text)):")
print(len(text))

print("Kết quả của lệnh print(len(text.encode('utf-8'))):")
print(len(text.encode('utf-8'))) """

arr = list("LƯỢNG TRẦN");
arrTemp = []
for i in arr:
    arrTemp.append(ord(i))
print(arrTemp)

print(ord("Ư"))

