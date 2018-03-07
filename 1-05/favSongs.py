fav_songs = {"Buckethead":"Listen for the Whisper",
			 "Led Zeppelin":"Achilles Last Stand",
			 "Rush":"La Villa Strangiato",
			 "Pink Floyd":"Shine On You Crazy Diamond",
			 "Genesis":"Supper's Ready",
			 "Elton John":"Funeral For a Friend"}

band = input("Enter one of my favorite bands and I'll tell you my favorite song by them: ")

if band in fav_songs:
	print("My favorite " + band + " song is " + fav_songs[band] + ".")
else:
	print("That is not one of my favorite bands.")