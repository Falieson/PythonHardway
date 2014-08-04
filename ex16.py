from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "cancel by pressing ctrl+c"
print "press enter to continue."

raw_input  ("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 lines:"
line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I'm going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "and close the file...."

target.close()
