#Chạy đoạn code sau và giải thích từng dòng code
str_original = "UTF-8 PYTHON PROGRAMMING ENCODING AND DECODING"
# Mã hoá UTF-8
bytes_encoded = str_original.encode(encoding="utf-8") 
# In ra màn hình type của biến bytes_encoded
print(type(bytes_encoded))
# Giải mã UTF-8
str_decoded=bytes_encoded.decode()
# In ra màn hình type của biến str_decoded
print(type(str_decoded))

# So sánh kết quả của 2 giá trị => return True or False
print(bytes_encoded==str_decoded) # False

