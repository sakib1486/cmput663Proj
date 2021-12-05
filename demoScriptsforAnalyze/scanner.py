import numpy as np
import pathlib
import os
import re


#collecting the declared methods from a java file and no. of arguments
def collect_method(linelist):
	regex_method = "(public|protected|private|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])"
	methods = []
	arguments = []


	for line in linelist:
		if re.search(regex_method, line):
			m = line.split("(")[0].strip().split()
			meth = m[len(m)-1]
			arg = line.split("(")[1].split(")")[0].split(",")
			methods.append(meth)
			arguments.append(arg)

	return methods, arguments			
			
#collecting the bugs because of unequal arguments in method calls
def find_bugs(linelist, methods, arguments):

	bugs = []
	for i in range(len(linelist)):
		for r in range(len(methods)):
			if re.search(methods[r], linelist[i]):
				if len(linelist[i].split("(")) > 1:
					m = linelist[i].split("(")[0].strip().split()
					meth = m[len(m)-1]
					arg = linelist[i].split("(")[1].split(")")[0].split(",")
					if len(arg) != len(arguments[r]):
						bug_info = "Expected "+str(len(arguments[r]))+" but found "+str(len(arg))+" at line "+str(i+1)+"."
						bugs.append((linelist[i], bug_info))

	return bugs


#runs when a directory is provided
def main():
	#regex pattern for finding method declaration
	f = open("MSort.java", "r")
	linelist = f.readlines()
	methods, arguments = collect_method(linelist)
	bugs = find_bugs(linelist,methods, arguments)
	print(bugs)

main()