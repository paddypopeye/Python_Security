import re

def main():
	ReplaceWord()
	DemarcationLine()
	MatchAndReplaceWord()

def ReplaceWord():
	try:
		files = open('./TestFile.txt')
		for line in files:
			print(re.sub('lenor|more', '#####', line),end='')

	except FileNotFound as e:
		print('File not found...', e)

def MatchAndReplaceWord():
	try:
		files = open('./TestFile.txt')
		for line in files:
			match = re.search('(len|neverm)ore', line)

			if match:
				print(line.replace(match.group(),"######"), end='')

	except FileNotFound as e:
		print('File not found...', e)

def DemarcationLine():
	print ('###################')


if __name__ == '__main__':
	main()