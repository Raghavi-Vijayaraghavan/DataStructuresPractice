# An example of tail recursive function


def prints(n):

	if (n < 0):
		return
	print(str(n), end=' ')

	# The last executed statement is recursive call
	prints(n-1)

	# This code is contributed by Pratham76
	# improved by ashish2021
