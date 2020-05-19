# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count= count + 1
    pos = line.find(':')

    a = float(line[pos+1:])
    add = add +a
    avg = add/count

print('Average spam confidence:',avg)
