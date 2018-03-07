response = input("Who is your favorite Johnson?: ")

testbob = open("favJohnson.txt", "w")
testbob.write(response)
testbob.close()