# Class for reading configuration files. Each line is suposed to be in the form of key = value.
# Eduardo Ponz for Seluxit. 9-Nov-2017
class FileReader():

	def __init__(self, file_path):
		self.file = open(file_path)
		self.config_dict = self.read_config()

	# Returns the file in a dict
	def read_config(self):	
		config_dict = {}
		for lines in self.file:
			items = lines.split(' = ', 1)
			config_dict[items[0]] = eval(items[1])
		return config_dict

	# Returns a list with the values in lines (from_line, to_line), both included
	def get_lines_list(self, from_line, to_line):
		matrix = []
		count = 0
		for key, value in self.config_dict.items():
			if count >= from_line and count <= to_line:
				matrix.append(value)
			count += 1
		return matrix

	# Returns the value in line
	def get_line_value(self, line):
		count = 0
		for key, value in self.config_dict.items():
			if count == line:
				val = value
			count += 1

		if val:
			return val
		else:
			return None

	# Returns a list with all the file values
	def get_file_list(self):
		matrix = []
		for key, value in self.config_dict.items():
			matrix.append(value)
		return matrix

	# Retunrns the file in a dict
	def get_file_dict(self):
		return self.config_dict

	# Returns a dict with the values in lines (from_line, to_line), both included
	def get_lines_dict(self, from_line, to_line):
		lines_dict = {}
		count = 0
		for key, value in self.config_dict.items():
			if count >= from_line and count <= to_line:
				lines_dict[key] = value
			count += 1
		return lines_dict