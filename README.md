Utility to create family structure files for the Optimal Birth Intervals model (see optimal-birth-intervals repository)
==========================

This python code will create two files:
- families.txt contains all possible combinations of the ages of children in a family
- fam.in contains a list of integers representing the binary strings for each family (especially useful in the old FORTRAN code)

You will manually need to remove all occurrences of `[`, `,` and `]` from `families.txt` before using the file.

Finally, import `families.txt` into the Optimal Birth Intervals Visual Studio project to use in the model.

The code, as is, will create all possible combinations of child ages for kids up to 14 years old with a birth interval of 2 years. To change the uppermost child ages, change the value of K in the code before running.
