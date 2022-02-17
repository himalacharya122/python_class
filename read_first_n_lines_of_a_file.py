#write a python programe to read first n line of a file


file = open("read_first_n_line.txt")

number_of_line = 1

for i in range(number_of_line):
    print(file.readline())

file.close
