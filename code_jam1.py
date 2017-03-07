# Problem

# You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items.
 #From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers 
 #indicating the positions of the items in your list (smaller number first).

# Input

# The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

# One line containing the value C, the amount of credit you have at the store.
# One line containing the value I, the number of items in the store.
# One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
# Each test case will have exactly one solution.
# Output

# For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. 
#The lower index should be output first.
case = int(raw_input("Enter the number of cases :: "))

for i in range(0,case):
	store_credit = int(raw_input("Enter the amount of store credit :: "))
	items = int(raw_input("Enter the number of items :: "))
	price = list()
	solu = list()
	for x in range(0,items):
		p = int(raw_input("Enter the price of item %d:: "%(x+1)))
		price.insert(x,p)
	print price
	f=0
	for j in range(0,items):
		for k in range(1,items):
			if (price[j]+price[k]) == store_credit:
				f=1
				solu.insert(0,(j+1))
				solu.insert(1,(k+1))
		if f == 1:
			break

	print solu