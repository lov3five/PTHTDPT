""" 
3)Viết chương trình mã hóa 2 chuỗi và cho biết kết quả sau khi mã hóa
s1="ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH"
s2='Khoa Công nghệ thông tin' 
"""
import string

s1 = "ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH"
s2 = 'Khoa Công nghệ thông tin'

#Mã hóa 
print("Mã hóa")
print(s1.encode("utf-8"))
print(s2.encode("utf-8"))
#Giải mã
print("Giải mã")
print(s1.encode("utf-8").decode("utf-8"))
print(s2.encode("utf-8").decode("utf-8"))