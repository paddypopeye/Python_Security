import Image, stepic, binascii
from Crypto.Cipher import AES

cryptObj = AES.new("This is my key16", AES.MODE_CBC, "16 character vec")
plainText = "This is some text that will be encrypted        "
cipherText = cryptObj.encrypt(plainText)
binval = binascii.b2a_base64(cipherText)
img = Image.open("/home/eugene/Downloads/20171027_162037.jpg")
print("ASCII: ", binval)

steg = stepic.encode(img, binval)
steg.save("stegEncrypt.bmp","BMP")	
newImg = Image.open("stegEncrypt.bmp")
data = stepic.decode(newImg).rstrip('\n')
print("The extracted data: ", data)

encrypted = binascii.a2b_base64(data)
newCryptObj = AES.new("This is my key16", AES.MODE_CBC, "16 character vec")
result = newCryptObj.decrypt(encrypted)
print(result)




















print(cipherText)

newCryptObj = AES.new("This imy key16", AES.MODE_CBC, "16 character vec")
result = newCryptObj.decrypt(cipherText)

print(result)