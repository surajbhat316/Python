fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for lines in fh:
    if not lines.startswith('From:'):
        continue
    else:
        count = count+1
        a =lines.split()
        print(a[1])


print("There were", count, "lines in the file with From as the first word")
