def stringCheck(s,lg):
	counter = 1
	words = ""
	for i in s:
		if counter <= lg:
			words += i
			counter += 1
		else:
			words += "\n"
			words += i
			counter = 2

	return words

string = input("Pls enter the string:")

length = int(input("Pls enter the length:"))

print(stringCheck(string,length))

