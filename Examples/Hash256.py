import hashlib

str = 'NGY0NzMzODNjYTUxMjE0NTljZDQ2ZWNmNDJjOWZjZGU6MTY3MzAzOTEzOA=='

# Encode() converts the string into bytes to be accepted by the hash function.
result = hashlib.sha256(str.encode())

# Hexidigest() returns the encoded data in hexadecimal format
print('the hexadecimal equivalent of sha256 is : ', result.hexdigest())

# Python program to find SHA256 hash string of a file
filename = 'DocToScan\\IoTArticle1.pdf'
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())