
#day-10   escape sequences

#   \\     backslash(\)
#   \'     single-quote(')
#   \"     double-quote(") 
#   \a     ascii bell(bel)
#   \b     ascii backspace(bs)
#   \n     ascii linefeed(lf)
#   \N{name} character named name in the unicode database 
#   \xhh   character with hex value hh
#   \ooo   character with octal value oo
#   \t     horizontal tab (tab)
   
   
tabby_cat = "\t i'm tabbed in . "
persian_cat = "i'm split \non a line ."
backslash_cat = "i'm \\ a \\ cat . "

fat_cat = """ 
i'll do a list :
\t cat food
\t fishes
\t catnip\n\t grass
"""

print (tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)



#answer
#         i'm tabbed in . 
#i'm split 
#on a line .
#i'm \ a \ cat . 
 
#i'll do a list :
#         cat food
#        fishes
#         catnip
#         grass
