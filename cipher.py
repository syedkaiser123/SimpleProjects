
from cryptography.fernet import Fernet

def genratePassKey():
	key = Fernet.generate_key()
	# print(key)
	# print(type(key))
	abc = open("PasswordKey.key",'wb')
	abc.write(key)
	abc.close()
	return key



def getMyKey():
	abc = open("PasswordKey.key",'rb')
	return abc.read()

def getContentFromUser():
	return input("Enter your message: ")

def encryptMssg(content):

	key = getMyKey()
	k = Fernet(key)
	cipher = k.encrypt(content)
	return cipher

def decryptMssg(D_key,cipher):

	key = getMyKey()
	k = Fernet(key)
	# print(type(D_key),'\n')
	U_key = input("enter the Decryption key :")
	print(U_key,'\n')


	if str(D_key) == U_key:
		decrypted_Mssg = k.decrypt(cipher)
		return decrypted_Mssg
	else:
		return "wrong key entered"


D_key = genratePassKey()
print(D_key,'\n')
# pin = getMyKey()
content = bytes(getContentFromUser(),"utf-8")
cipherText = encryptMssg(content)
print('\n',cipherText)
Decipher = decryptMssg(D_key,cipherText)
print('\n')
print(Decipher)



