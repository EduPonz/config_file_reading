"""
Library for reading configuration files.

Created by Eduardo Ponz for Seluxit. 9-nov-2017.
"""


class FileReader():
    """
    Class for reading configuration files.

    Each line is suposed to be in the form of key = value.
    """

    def __init__(self, file_path):
        """Constructor."""
        self.file = open(file_path)
        self.config_dict = self.read_config()

    def read_config(self):
        """Return the file in a dict."""
        config_dict = {}
        for lines in self.file:
            items = lines.split(' = ', 1)
            config_dict[items[0]] = eval(items[1])
        return config_dict

    def get_lines_list(self, from_line, to_line):
        """Return a list with values in lines [from_line, to_line]."""
        matrix = []
        count = 0
        for key, value in self.config_dict.items():
            if count >= from_line and count <= to_line:
                matrix.append(value)
            count += 1
        return matrix

    def get_line_value(self, line):
        """Return the value in line."""
        count = 0
        for key, value in self.config_dict.items():
            if count == line:
                val = value
            count += 1

        if val:
            return val
        else:
            return None

    def get_file_list(self):
        """Return a list with all the file values."""
        matrix = []
        for key, value in self.config_dict.items():
            matrix.append(value)
        return matrix

    def get_file_dict(self):
        """Retunrn the file in a dict."""
        return self.config_dict

    def get_lines_dict(self, from_line, to_line):
        """Return a dict with the values in lines [from_line, to_line]."""
        lines_dict = {}
        count = 0
        for key, value in self.config_dict.items():
            if count >= from_line and count <= to_line:
                lines_dict[key] = value
            count += 1
        return lines_dict
