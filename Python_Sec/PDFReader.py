import pyPdf
from pyPdf import PdfFileReader
import optparse

def printMeta(fileName):
	
	pdfFile = PdfFileReader(file(fileName, 'rb'))
	docInfo = pdfFile.getDocumentInfo()
	print '[*]PDF Metadata for: ' + str(fileName)

	for metaItem in docInfo:
		print '[*] ' + metaItem + ":" + docInfo[metaItem]

def main():
	parser = optparse.OptionParser('Usage%prog' + '-F <PDF filename>')
	parser.add_option('-F', dest='fileName', type='string', help='specify the PDF file')
	(options, args) = parser.parse_args()
	fileName = options.fileName
	if fileName == None:
		print parser.usage
		exit(0)
	else:
		printMeta(fileName)

if __name__ == '__main__':
	main()