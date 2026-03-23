from main import sha1

with open("File-1.pdf", "rb") as f:
    data1 = f.read()
    print("SHA-1:", sha1(data1))

with open("File-2.pdf", "rb") as f:
    data2 = f.read()
    print("SHA-1:", sha1(data2))

print("match:", sha1(data1) == sha1(data2))
