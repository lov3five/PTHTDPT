""" 
4)Cho s1=b'Vi\xe1\xbb\x87t Nam m\xe1\xba\xbfn y\xc3\xaau' ; 
s2= b'ng\xc6\xb0\xe1\xbb\x9di Vi\xe1\xbb\x87t d\xc3\xb9ng h\xc3\xa0ng Vi\xe1\xbb\x87t'
a)Viết lệnh giải mã chuỗi s1 và s2 và cho biết kết quả.
b)Cho biết kích thước của chuỗi s1 và s2
c)Cho biết kết quả của lệnh print(list(s1)) và print(list(s2)) 
"""

from pickle import PicklingError


s1 = b'Vi\xe1\xbb\x87t Nam m\xe1\xba\xbfn y\xc3\xaau'
s2 = b'ng\xc6\xb0\xe1\xbb\x9di Vi\xe1\xbb\x87t d\xc3\xb9ng h\xc3\xa0ng Vi\xe1\xbb\x87t'

# a)Viết lệnh giải mã chuỗi s1 và s2 và cho biết kết quả.
print("Kết quả giải mã chuỗi s1: ")
print(s1.decode("utf-8"))

print("Kết quả giải mã chuỗi s2: ")
print(s2.decode("utf-8"))

#b)Cho biết kích thước của chuỗi s1 và s2
print("Kích thước của chuỗi s1 chưa giải mã: ")
print(len(s1))

print("Kích thước của chuỗi s2 chưa giải mã: ")
print(len(s2))

print("Kích thước của chuỗi s1 sau khi giải mã: ")
print(len(s1.decode("utf-8")))

print("Kích thước của chuỗi s2 sau khi giải mã: ")
print(len(s2.decode("utf-8")))

#c)Cho biết kết quả của lệnh print(list(s1)) và print(list(s2)) 
print("kết quả của lệnh print(list(s1)) và print(list(s2))")
print(list(s1))
print(list(s2))