
import csv

favMovies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
["Training Day", "Man on Fire",	"Flight"]]

with open("movies.csv", "w", newline="") as testbob:
    w = csv.writer(testbob, delimiter=",")
    w.writerow(favMovies[0])
    w.writerow(favMovies[1])

with open("movies.csv", "r") as testbob:
    r = csv.reader(testbob, delimiter=",")
    for row in r:
        print(",".join(row))
