# Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. 
#A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

# Input

# The first line of input gives the number of cases, N.
# N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words.
# Spaces will not appear at the start or end of a line.

# Output

# For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.
n = int(raw_input("Number of Cases ::"))
s = list()
def getr(data):
	d = data.split(" ")
	st = ""
	l = len(d)
	while l >0:
		st+=d[l-1]
		l-=1
		if l>0:
			st+=" "
	return st
for i in range(0,n):
 	data = str(raw_input("Enter your String :: "))
 	a=getr(data)
 	s.insert(i,a)
	
for n in s:
	print n
