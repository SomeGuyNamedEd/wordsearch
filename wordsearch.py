#!/usr/bin/python
#
# Usage:
# python2 wordsearch.py --input --wordlist
#
# Pre-requisites:
# python 2.7+
# Wordlist format: one line/search string, case insensitive, no trailing carriage return at end of file

import sys
import re
import os.path
import getopt
import argparse

#Read command line args
parser = argparse.ArgumentParser(description='This reads a word list and will find lines containing the words.')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-w','--wordlist',help='Wordlist file name', required=True)
args = parser.parse_args()

#Return word in context
def search(searchLine, searchText, n):
	searchLine=searchLine.lower().strip('\n')
	startWord=(searchLine.find(searchText.lower()))
	startPos=startWord-n
	endWord=(searchLine.find(searchText.lower()))+len( searchText )
	endPos=endWord+n
	if startPos-n <= 0:
		startPos=0
	if endPos >= len(searchLine):
		endPos=len(searchLine)
	return ( searchLine[startPos:startWord]+"\033[91m\033[1m"+searchLine[startWord:endWord]+"\033[0m"+searchLine[endWord:endPos] )

def main():
	inputfile=args.input
	wordlist=args.wordlist

	#check if file exists
	if os.path.isfile(inputfile):
		print ("[+] Searching input file: %s" % inputfile )
	else:
		print ("[x] Input file not found: %s" % inputfile ) 
		sys.exit()

	if os.path.isfile(wordlist):
	        print ("[+] Wordlist file: %s" % wordlist )
	else:
	        print ("[x] File not found: %s" % wordlist )
	        sys.exit()


	#read wordlist
	wordlist = [line.rstrip('\n') for line in open(wordlist)]
	print ( "[+] Length of wordlist: \033[1m%d\033[0m " % len(wordlist) )

	#do search
	with open(inputfile) as inputFile:
		for linenumber, line in enumerate(inputFile, 1):
			for word in wordlist:
				if word.lower() in line.lower():
					print ( "[+] Line #: \033[1m%d\033[0m Word: \033[91m\033[1m%s\033[0m String: %s" % (linenumber, word, search(line, word, 10)) )
		print ("[+] Lines processed: \033[1m%d\033[0m" % linenumber)

if __name__ == '__main__':
	main()