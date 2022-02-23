file = open("change_file1.txt")
f = file.readlines()
f.pop()
f.append("four")

file.close()


file1 = open("change_file1.txt", "w")

for i in f:
    file1.write(i)

file.close()