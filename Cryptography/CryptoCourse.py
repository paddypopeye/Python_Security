#! /usr/bin/python2.7

import sys

def main():
	text1 = "attacl at dawn"
	encode1 = "6c73d5240a948c86981bc294814d".decode("hex")
	key = xor_strings(text1, encode1)

	text2 = "attack at dusk"
	encode2 = xor_strings(text2, key)
	print encode2.encode("hex")

def xor_strings(strA, strB):
	return "".join(chr(ord(chrA) ^ ord(chrB)) for (chrA,chrB) in zip(strA,strB))

main()