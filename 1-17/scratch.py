import re

l = "Beautiful hams are beautiful"

matches = re.findall("beautiful", l)
#matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)