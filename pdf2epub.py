import os
from time import sleep
import sys
import argparse
parser = argparse.ArgumentParser(description = "Convert PDF/HTML to EPUB/MOBI")  

parser.add_argument("-d", "--directory", help="input directory")
parser.add_argument("-o", "--output", help="output directory")
parser.add_argument("-t", "--ext", help="input extension, default: PDF")
parser.add_argument("-f", "--format", help="output format, default: EPUB")

args = parser.parse_args()

path = os.getcwd()
print(path)

if args.directory:
	path = str(args.directory)

output = path
if args.output:
	output = str(args.output)

ext = "PDF"
if args.ext:
	ext = args.ext

ext = ext.upper()

fformat = "EPUB"
if args.format:
	fformat = args.format

fformat = fformat.upper()

files = os.listdir(path)

#remove espacos e insere _
#for file in files:
#	os.rename(os.path.join(path, file), os.path.join(path, file.replace(' ', '_')))

for file in files:
	if file.upper().endswith('.'+ext):
		f = file.split('.')
		fx = ""
		i = 0
		while i < len(f)-1:
			if i < len(f) - 2:
				fx += f[i]+"_"
			else:
				fx += f[i]
			i += 1

		os.system('ebook-convert {} {}'.format(path+"\\"+file, output+"\\"+fx+"."+fformat))
sleep(10)
print ('Completed.')