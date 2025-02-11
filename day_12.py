
#run it with commandline

from sys import argv

script , user_name = argv
 
prompt = '>'

print("hi %s , i'm %s script." %(user_name , script))
print("i'd like to ask you few questions.")
print("do you like me %s ?" %user_name)

likes = input(prompt)

print("where do you live %s?" %user_name )
lives = input(prompt)

print("what kind of computer do you have %s? " %user_name )
computer = input(prompt)

print ("""
       alright, so you said %r about liking me .
       you live in %r , not sure where that is.
       and you a %r computer .nice.
       """ %(likes , lives , computer))


#answer
#python day_12.py maede
#hi maede , i'm day_12.py script.
#i'd like to ask you few questions.
#do you like me maede ?
#>yes
#where do you live maede?
#>karaj
#what kind of computer do you have maede? 
#>gaming :D

#       alright, so you said 'yes' about liking me .
#       you live in 'karaj' , not sure where that is.
#       and you a 'gaming :D' computer .nice.
       
