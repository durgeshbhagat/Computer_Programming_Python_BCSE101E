file_object = open('sample.txt', 'r')
line_list = file_object.readlines()
print(line_list)
# for line in line_list:
#     print(line)
file_object.close()