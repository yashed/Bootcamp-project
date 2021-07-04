import hashlib
data = input("Input Your Data =")

hash_data = hashlib.md5(data.encode("utf-8"))
md5_hash_data = hash_data.hexdigest()

print("MD5 Data = ", md5_hash_data)
