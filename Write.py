# read th file and store all the lines in the list
# reverse the list

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
print(content)
with open('test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)
