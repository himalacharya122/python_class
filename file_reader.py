# To read files

file_content = open("test.txt")
print(file_content.read())

# To write files

'''file = open("test.txt", "w")
file.write("This is new content")
file.close()'''

file = open("test.txt", "a")
file.write("\t")
file.write( "This is new content")
file.close()