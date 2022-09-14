# From lib/python3.7/string.py

'''whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
'''
import string

s = "What's wrong with ASCII?!?!?"
"""s.rstrip(string.punctuation)"""
print(s.rstrip(string.punctuation))
# Result: 'What's wrong with ASCII'


def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)
""" Phía bên trái của dấu hai chấm, , là đối tượng thực tế có giá trị sẽ được định dạng và chèn vào đầu ra. 
Sử dụng hàm Python cung cấp cho bạn điểm mã base-10 cho một ký tự duy nhất .ord(i)ord()str 
Phía bên tay phải của dấu hai chấm là mã xác định định dạng. có nghĩa là chiều rộng 8, 0 đệm và các hàm như 
một dấu hiệu để xuất số kết quả trong cơ số 2 (nhị phân).08b"""

print("bits: " + make_bitseq("bits"))
print("CAPS: " + make_bitseq("CAPS"))
print("$25.43: " + make_bitseq("$25.43"))
print("~5: " + make_bitseq("~5"))

#Tinh 2^nbits
def n_possible_values(nbits: int) -> int:
    return 2 ** nbits

print(n_possible_values(8)) # Result: 4

#Tinh x khi 2^x = nvalues
from math import ceil, log

def n_bits_required(nvalues: int) -> int:
    return ceil(log(nvalues) / log(2))

print(n_bits_required(256)) # Result: 8
print(n_bits_required(129)) # Result: 7