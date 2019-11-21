f=open('',"r")
average = 0
for line in f:
    average += int(line.strip('\n'))
print average