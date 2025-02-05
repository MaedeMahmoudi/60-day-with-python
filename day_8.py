
#day_8 printing, printing :)

#we use %r foe debugging
#we use %s for string
#we use %d for numbers

formatter  = "%r %r %r %r"

print (formatter %(1,2,3,4))
print (formatter %('one' , 'two' , 'three' , 'four'))
print(formatter %(True , False , False , True ))
print(formatter %(formatter , formatter , formatter , formatter))
print(formatter %(
    "i had this things.",
    "that you could type up right.",
    "but it didn't sing.",
    "so i said goodnight."
))

#answer

#1 2 3 4
#'one' 'two' 'three' 'four'
#True False False True
#'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
#'i had this things.' 'that you could type up right.' "but it didn't sing." 'so i said goodnight.'
