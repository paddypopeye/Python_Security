import Image, stepic

img = Image.open("TestSteg.jpg", "r")
img.show()
fh = open("myfile", "r")
text = fh.read()
stego = stepic.encode(img, "This is some text")
stego = stepic.encode(img, text)
stego.save("steg.jpg", "JPEG")

img2 = Image.open("steg.jpg")
img2.show()
