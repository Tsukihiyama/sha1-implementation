from main import sha1
import hashlib

message = input("Enter a message: ").encode()

a = sha1(message)
b = hashlib.sha1(message).hexdigest() 
print("Custom SHA-1:", a)
print("Hashlib SHA-1:", b)  
print("match:", a == b)