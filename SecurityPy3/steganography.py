import Image, stepic, binascii
from Crypto.Cipher import AES

cryptObj = AES.new("This is my key16", AES.MODE_CBC, "16 character vec")
plainText = "This is some text that will be encrypted        "#padded to match key size
cipherText = cryptObj.encrypt(plainText)
binvalue = binascii.b2a_base64(cipherText)
img = Image.open("/home/eugene/Downloads/TestSteg.jpg")
print("ASCII: ", binvalue)

stego = stepic.encode(img, binvalue)
steg.save("stepInjected.bmp","BMP")	
img2 = Image.open("stepInjected.bmp")
data = stepic.decode(newImg).rstrip('\n')
print("Extracted data ", data)

encrypted = binascii.a2b_base64(data)
newCryptObj = AES.new("This is my key16", AES.MODE_CBC, "16character Ivec")
result = newCryptObj.decrypt(encrypted)
print(result)




















print(cipherText)

newCryptObj = AES.new("This imy key16", AES.MODE_CBC, "16 character vec")
result = newCryptObj.decrypt(cipherText)

print(result)