""" 
MSSV: 19525521
Họ và tên: Trần Thanh Lượng
"""
# Câu 1
# Chuỗi gốc
str_original = "Đại học Công Nghiệp TP HCM"
# Mã hoá UTF-8
bytes_encoded = str_original.encode(encoding="utf-8") 
# In ra màn hình type của biến bytes_encoded
print(type(bytes_encoded))
# Giải mã UTF-8
str_decoded=bytes_encoded.decode()
# In ra màn hình type của biến str_decoded
print(type(str_decoded))
# In ra màn hình chuỗi đã mã hóa
print('Encoded bytes = ', bytes_encoded)
# In ra màn hình chuỗi đã giải mã từ chuỗi mã hóa
print('Decoded String = ', str_decoded)
# So sánh chuỗi -> True or False
print('str_original equals str_decoded = ', str_original == str_decoded)