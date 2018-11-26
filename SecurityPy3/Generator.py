#!/usr/bin/python3

class InclusiveRange:
	"""docstring for InclusiceRange"""
	def __init__(self, *args):
		numberOfArgs =len(args)

		if numberOfArgs < 1:
			raise TypeError('At least one arg is required')

		elif numberOfArgs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1

		elif numberOfArgs == 2:
			(self.start, stop) = args

		elif numberOfArgs == 3:
			(self.start,self.stop,self.step) = args

		else:
			raise TypeError("!!Maximum of three args.{}"\
				.format(numberOfArgs))

	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i
			i += self.step

def main():
	ranges = InclusiveRange(5,210,10)

	for x in ranges:
		print('\n',x, end='')
	print('\n')


if __name__ == '__main__':
	main()
		
