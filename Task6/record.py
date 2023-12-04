from config import separator


# general class for all records
class Record:
    # class constructor, get title and text
    def __init__(self, title, text):
        self.title = title  # initialize self.title
        self.text = text    # initialize self.text

    def convert_to_string(self):
        parsed_string = ''  # initializing empty string
        for key, value in self.__dict__.items():    # for all parameters
            parsed_string += value + '\n'   # add parameter to the string
        parsed_string += separator  # add separator
        return parsed_string        # return the string