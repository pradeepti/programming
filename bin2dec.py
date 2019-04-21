
def bintodec(binary):
	dec = 0
	i = 0
	n = 0
	binary = int(binary)
	#binary = int(binary)
	print ("binary:", binary)
	while (binary != 0):
		rem = binary % 10
		dec = dec + rem * pow (2, i)
		binary = int(binary / 10)
		i = i + 1
	print (dec)


if __name__ == '__main__':
	#f = True
	while True:
		user_option = input("Do you want to give a binary number?(Y/N):")
		if user_option == "Y" or user_option == "y":
			bin_number = input("Enter the binary number:")
			#print (bin_number)
			bintodec(bin_number)
		else:
			print ("Exiting the program")
			break





