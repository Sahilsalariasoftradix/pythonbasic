file = open('test.txt')

# Read all the contents of the file
# read n numbers of characters by passing parameters
# print(file.read())

# Read one single line
# print(file.readline())
# print(file.readline())


# Print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()
