# Homework 2: create a full calculator
print("")
print("Welcome to the calculator!")
print("")
print("Options")
print("1: sum")
print("2: subtraction")
print("3: multiplication")
print("4: division")
print("q: quit")
print("")
options = ["1","2","3","4","q"]
print("")

while True:
	choice = input("Please select the desired operation: ")
	print("")
	if choice not in options:
		print("")
		print("Please choose a valid choice")
		continue
	else:
		if choice == "1"
		





















while True:
	choice = input("Please choose the desired operation: ")
	if choice not in options:
		print("")
		print("Please choose a valid option.")
		continue
	else:
		while True:
			try:
				x = int(input("Please enter the first number: "))
			except ValueError:
				print("Your input is invalid.")
				continue
		else:
			break
		while True:
			try:
				y = int(input("Please enter the second number: "))
			except ValueError:
				print("Your input is invalid.")
				continue
			else:
				break

		if choice == "1":
			print("")
			print("The sum of", x," and ",y," is ",(x+y))
			print("")
			break
		elif choice == "2":
			print("")
			print("The subtraction of", x," and ",y," is ",(x-y))
			print("")
			break
		elif choice == "3":
			print("")
			print("The multiplication of", x," and ",y," is ",(x*y))
			print("")
			break
		elif choice == "4":
			if y != 0:
				print("")
				print("The division of", x," by ",y," is ",(x/y))
				print("")
				break
			else:
				while True:
					try:
						z = int(input("Please enter a valid non zero number: "))
						if z != 0:
							print("")
							print("The division of", x, "by", z, "is" , (x/z))
							print("")
							break
						else:
							print("NON-ZERO!!")
							continue
					except ValueError:
						print("Your input is invalid.")
						continue
					else:
						break
		elif choice == "q":
			print("")
			print("Thanks for using the calculator")
			print("")
			quit()

# while True:
# 	try:
# 		x = int(input("Please enter the first number: "))
# 	except ValueError:
# 		print("Your input is invalid.")
# 		continue
# 	else:
# 		break
# while True:
# 	try:
# 		y = int(input("Please enter the second number: "))
# 	except ValueError:
# 		print("Your input is invalid.")
# 		continue
# 	else:
# 		break
