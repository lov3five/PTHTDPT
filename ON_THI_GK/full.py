import string

# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
s = "What's wrong with ASCII?!?!?+++++++++"
"""s.rstrip(string.punctuation)"""
# print(s.rstrip(string.punctuation))
# Result: 'What's wrong with ASCII'

# Hàm xóa kí tự các kí tự "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" ở cuối chuỗi
def removeLastCharacter(str):
    return str.rstrip(string.punctuation)
# print(removeLastCharacter(s))

# Hàm chuyển đổi unicode sang binary ASCII
def convertUnicodeToBinary(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)
# print("A = ", convertUnicodeToBinary("A"))

#Tinh 2^nbits
def n_possible_values(nbits: int) -> int:
    return 2 ** nbits
# print(n_possible_values(3))


from math import ceil, log
#Tinh so bit yeu cau
def n_bits_required(nvalues: int) -> int:
    return ceil(log(nvalues) / log(2))
# print(n_bits_required(124)) # Result = 7


s1 = "ĐẠI HỌC CÔNG NGHIỆP TP HỒ CHÍ MINH"
s2 = 'Khoa Công nghệ thông tin'
# Mã hóa
def encode(str):
    return str.encode("utf-8")
# print(encode(s1))

# Giải mã
def decode(str):
    return str.decode("utf-8")
""" tmp = encode(s1)
print(decode(tmp)) """

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