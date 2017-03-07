import sys
num = int(raw_input("Enter any Number :: "))


k=num
for i in range(0,num):
	for k in range(0,num-i):
		sys.stdout.write("  ")
	for j in range(0,i):
		sys.stdout.write("$ ")
	print "\n"

print ("\n\n")

for i in range(1,num):
	for j in range(1,i+1):
		sys.stdout.write("* ")
	print "\n"


s=num
for i in range(0,num):
	for k in range(0,s):
		sys.stdout.write(" ")
	s-=1
	for j in range(0,i+1):
		sys.stdout.write("$ ")
	print "\n"