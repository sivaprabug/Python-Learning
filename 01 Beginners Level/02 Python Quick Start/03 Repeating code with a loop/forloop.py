#!/usr/bin/python3

print '\n'
# read the lines from the file
fh = open('sourceFile.txt')
for line in fh.readlines():
   print  (line),
print '\n'

# Split the word to letter
myjob= 'hacker'
for c in myjob:
	print (c),
print '\n'

# Split the word to letter direct for in loop
for letter in 'Python':
   print 'Current Letter :', letter
print '\n'
