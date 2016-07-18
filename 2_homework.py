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
		print("Please choose a valid choice")
		print("")
		continue
	elif choice == "q":
			print("Thanks for using the calculator!")
			print("")
			quit()
	elif choice == "1":
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
		print("")
		print("The sum of ", x, "and", y, "is", (x+y))
		print("")
		quit()
	elif choice == "2":
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
		print("")
		print("The quocient of ", x, "and", y, "is", (x-y))
		print("")
		quit()
	elif choice == "3":
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
		print("")
		print("The product of ", x, "and", y, "is", (x*y))
		print("")		
		quit()
	elif choice == "4":
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
				y = int(input("Please enter a number different from zero: "))
				if y == 0:
					print("")
					print("NON-ZERO!!")
					print("")
					continue
				else:
					break	
			except ValueError:
				print("Your input is invalid.")
				continue
			else:
				break
		print("")
		print("The division of ", x, "and", y, "is", (x/y))
		print("")
		break
