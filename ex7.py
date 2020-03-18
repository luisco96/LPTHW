print("Mary had a little lamb.")
# format is like printf but you just out {} where you want to add the variable value
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# Multiply a string to print it an amount of times 
print("." * 10) # what'd that do?

# A bunch of character variables
# but I think python just accepts strings 
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# whatch that comma at the end, try removing it to see what happens
# apparently the first statment before the command just concatenates all the variables
# but to make a new variable and assign it, you have to make a separated statement
# with the comma, but you can do it inside the function call
# and end is just in the scope of that function call
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)