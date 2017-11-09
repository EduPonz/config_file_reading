import os
from lib.config_file_read import FileReader

file_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(file_path, os.pardir))
file_path = os.path.abspath(os.path.join(file_path, "config"))
file_path = os.path.abspath(os.path.join(file_path, "config_file.config"))
print(file_path)
reader = FileReader(file_path)

list_1 = reader.get_lines_list(0,3)
value_1 = reader.get_line_value(4)
list_2 = reader.get_lines_list(5,8)
value_2 = reader.get_line_value(9)
myList = reader.get_file_list()
print('value 1 = {}'.format(value_1))
for i in range(len(list_1)):
	print(list_1[i])
print('value 2 = {}'.format(value_2))
for i in range(len(list_2)):
	print(list_2[i])
print(myList)

dict_1 = reader.get_lines_dict(0,3)
dict_2 = reader.get_lines_dict(5,8)
myDict = reader.get_file_dict()
print(dict_1)
print(dict_2)
print(myDict)


first_dict = {}
dict_list = [first_dict]
dict_list[0] = reader.get_file_dict()
print(dict_list)
print(first_dict)
first_dict = dict_list[0]
print(first_dict)
print(first_dict['led 1 pin'])
count = 1
for key, value in first_dict.items():
	if count == 3:
		print(value)
	count += 1