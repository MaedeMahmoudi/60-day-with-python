
#day-14
#file methods

#close --> closes the file . like File  --> save..in your editor.
#read --> rea the contents of the file . you can assign the result to a variable . 
#readline --> read just one  line of a text file .
#truncate --> empties the file . watch out if you care about the file .
#write(stuff) --> write stuff to the file .

#write takes a  parameter of a string you want to write to the file . 

from sys import argv

script , filename = argv

print("we're going to erase %r ." %filename)
print("if you don't want that , hit CTRL-C (^c) .") 
print("if you do want that , hit RETURN .")

input("?")

print("opening the file...")
target = open(filename , 'w')

print("truncating the file . goodbye")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("i'm going to write these to file . ")
 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and we finally close it.")
target.close()

# python day_14.py file_day14.txt
# we're going to erase 'file_day14.txt' .
# if you don't want that , hit CTRL-C (^c) .
# if you do want that , hit RETURN .
# ?RETURN
# opening the file...
# truncating the file . goodbye
# now i'm going to ask you for three lines.
# line 1 : hi1
# line 2 : hii2
# line 3 : hiii3
# i'm going to write these to file . 
# and we finally close it.

