# Mã hó chuỗi "UTF-8 PYTHON PROGRAMMING ENCODING AND DECODING" sau đó giải mã, giải thích code

# Chuỗi gốc
str = "UTF-8 PYTHON PROGRAMMING ENCODING AND DECODING"

# Mã hóa chuỗi utf-8
str1 = str.encode("utf-8")

# In ra chuỗi sau khi mã hoá của biến str1
print("Chuỗi sau khi mã hóa là: ",str1)

# Giải mã chuỗi utf-8 và in ra chuỗi sau khi giải mã
print("Giải mã chuỗi đã mã hóa",str1.decode("utf-8"))

# Giải mã chuỗi utf-16 và in ra chuỗi sau khi giải mã
print("Giải mã chuỗi đã mã hóa",str1.decode("utf-16"))
