import sys

MSGS = ( --- 11 secret messages ---)

def strxor(a, b):
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)],b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(b[:len(a)],a)])

def random(size=16):
	return open("/dev/urandom").read(size)

def encrypt(key ,msg):
	c = strxor(key, msg)
	print()
	print(c.encode('hex'))
	return c

def main():
	key = random(1024)
	cipherTexts = [encrypt(key,msg) for msg in MSGS]

if __name__ == "__main__":
	main()