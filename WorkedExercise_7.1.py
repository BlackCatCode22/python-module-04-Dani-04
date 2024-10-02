fh = open ('mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print (ly.upper())

#Note to self: Ensure you are in Module04 directory on CMD in order for program to run