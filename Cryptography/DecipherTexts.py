import sys, itertools, operator

freq_eng = {}
freq_eng = dict(freq_eng, **{' ':15, ':':2,';':2})
charset = ''.join(freq_eng.keys())


def strxor(a, b):
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)],b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(b[:len(a)],a)])

def combine_charset(charset):
	comb = {}

	for ch1, ch2 in list(itertools.combinations(charset, 2)):
		comb.setdefault(ord(ch1)^ord(ch2), set()).add(ch1)
		comb.setdefault(ord(ch1)^ord(ch2), set()).add(ch2)
	return comb


def keystream_from_manytime_pad(ct_list, charset):
	ks = [{} for i in range(len(sorted(ct_list, key=len, reverse=True)[0]))]
	comb = combine_charset(charset)

	for ct1, ct2 in list(itertools.combinations(ct_list, 2)):
		for i in range(min(len(ct1),len(ct2))):
			mix = ord(ct1[i]) ^ ord(ct2[i])
			if comb.has_key(mix):
				for ch in comb[mix]:
					mix_1 = chr(ord(ct1[i]) ^ ord(ch))
					mix_2 = chr(ord(ct2[i]) ^ ord(ch))
					ks[i].setdefault(mix_1,0)
					ks[i].setdefault(mix_2,0)
					ks[i][mix_1] += freq_eng[ch]
					ks[i][mix_2] += freq_eng[ch]
	ks[25]['\x7f'] = 1000
	ks_str = ''
	for k in ks:
		if(len(k) > 0):
			ks_str += sorted(k.items(), key=operator.itemgetter(1), reverse=True)[0][0]
		else:
			ks_str += "\x00"
	return ks_str


def main(argv):
	with open('cipherTexts.txt') as f:
		ct_samples = [line.rstrip().decode('hex') for line in f]
	ks = keystream_from_manytime_pad(ct_samples, charset)
	print strxor(ct_samples[-1],ks)

if __name__ == "__main__":
	main(sys.argv)

