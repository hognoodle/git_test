#method 1

mark_favs = {"book":"LOTR","movie":"The Good, The Bad and The Ugly","band":"Led Zeppelin","color":"red"}
#print(mark_favs)

#method 2

mark_fav = {}
#or mark_fav = tuple()
mark_fav["book"] = "LOTR"
mark_fav["movie"] = "The Good, The Bad and The Ugly"
mark_fav["band"] = "Led Zeppelin"
mark_fav["color"] = "red"

response = input("Do you want to know my favorite book, movie, band or color?: ")

if response in mark_fav:
	print("My favorite " + response + " is " + mark_fav[response] + ".")
else:
	print("That was not a correct query.")



