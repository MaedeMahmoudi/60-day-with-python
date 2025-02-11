
#day_13 reading files

from sys import argv

script,file_name = argv

txt = open(file_name)

print("here's your file %r : " %file_name )
print(txt.read())
print("type the file name again : ")

file_again = input('>')
txt_again = open(file_again)

print(txt_again.read())

#answer
#first you should open commandline , then make a file for example in arch linux that i have
#I write : touch myfile.txt  and then for writing in a file : nano myfile.txt and after that you can write some stuff in it :)

#result:

#python day_13.py myfile.txt
#here's your file 'myfile.txt' : 
#this is stuff i typed into a file
#it is really cool stuff
#lots and lots of fun to have in here
#:)



#type the file name again : 
#>myfile.txt
#this is stuff i typed into a file
#it is really cool stuff
#lots and lots of fun to have in here
#:)
