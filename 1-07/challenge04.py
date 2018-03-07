winning_nums = [3,13,17,23,33,43]
wins = 0


while True:
	match = False
	a = input("Enter a number from 1 to 49 ('q' to quit): ")
	if a == "q":
		break
	for num in winning_nums:
		if int(a) == num:
			print("That's a winner.")
			match = True
			break
	if not match:
		print("That's not a winner")



