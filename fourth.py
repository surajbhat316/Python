fname = input("Enter a filename")

fhand = open(fname,'r')
for lines in fhand:
    print(lines.upper())
