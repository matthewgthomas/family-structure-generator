import itertools
import re

# create list of all possible binary strings of length k
k=14
families_bin = map(''.join, itertools.product('01', repeat=k))

# cut out those with adjacent 1s (i.e. births interval is one year)
families_bin = [s for s in families_bin if s.find("11")==-1]

# convert to list of ints
families_dec = [int(s, 2) for s in families_bin]

# write to file
fam_file = open("fam.in", "w")
for family in families_dec:
	fam_file.write("%i\n" % family)

fam_file.close()

# convert families into ages and wite to file
fam_file_bin = open("families.txt", "w")
for family in families_bin:
	# search all binary strings for "1". Reverse the string (so LSB is at beginning) then count indices (+1 because zero-based)
	fam_file_bin.write("%s\n" % [m.start() + 1 for m in re.finditer("(?=1)", family[::-1])])
	
fam_file_bin.close()
