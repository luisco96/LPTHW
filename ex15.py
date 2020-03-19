from sys import argv
# gets file name
script, filename = argv
txt = open(filename)

print(f"Here's your file {filename}:")
# reads and prints the whole file
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()