

#day-11   argv --> this variable holds the arguments you pass to your python script when you run it
#you should run this file by commandline


from sys import argv

if len(argv != 4):
    print("please enter exact 3 argument ") #i write 3 argument --> arg[0] = script --> name of script file,
                                             #arg[1] = first ,  arg[3] = second ,  arg[4] = third
    exit(1)


script , first , second , third = argv

print("the script is called : ",script)
print("your first variable is : ",first)
print("your second variable is : ",second)
print("your third variable is : ", third)

#answer

#python day_11.py hello hi hi3
#the script is called :  day_11.py
#your first variable is :  hello
#your second variable is :  hi
#your third variable is :  hi3




