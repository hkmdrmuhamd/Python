import string as s

from random import *



while True:
	ranges = int(input("Pls do enter some digit"))
	if ranges >= 8:
		ch = s.ascii_letters + s.digits + s.punctuation
		password = "".join(choice(ch) for i in range(randint(8,(ranges+1))))
		break
	else:
		print("Min 8!")


print(password)