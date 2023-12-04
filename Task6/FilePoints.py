import os.path
from config import all_news_file_path, default_file_to_read_news, separator

class FilePoints:

    @staticmethod
    def write_to_file(string_to_write_to_file):
        if os.path.isfile('news_gen.txt'):  # If file exists
            with open('news_gen.txt', 'a') as file_to_write:   # Open file to add new record
                print(string_to_write_to_file, file=file_to_write)  # print to file
        else:                                                   # If file is not exist
            with open('news_gen.txt', 'w') as file_to_write:       # Create and open file to write
                print(string_to_write_to_file, file=file_to_write)  # print to file

    @staticmethod
    def read_from_file(file_path=all_news_file_path) -> list:
        records = []      # initialization of the empty list to hold records
        if os.path.exists(file_path):   # if file exists
            with open(file_path, 'r') as file_to_read:  # open file to read
                text = file_to_read.read()              # read all the file
            records_list = text.split(separator)        # split the string by separator
            for record in records_list:                 # loop threw all records
                if record != '':                        # if record is not empty
                    record = FilePoints.text_normalizing(record)    # normalize the string
                    records.append(record.lstrip('\n'))   # append record to the list with removing '\n' from the left side
        return records                    # return created list

    @staticmethod
    def delete_file(file_path) -> bool:
        if os.path.isfile(file_path):       # if file by path exists
            os.remove(file_path)            # remove file
            return True
        else:
            return False

    @staticmethod
    def text_normalizing(stringnorm) -> str:
        stringnorm = stringnorm.lower().capitalize()  # get string, normalize and capitalize it
        flag_to_change_case = False                                     # initialize flag with false as default
        for x in range(len(stringnorm) - 2):                   # loop threw the string
            if flag_to_change_case and stringnorm[x].isalpha(): # check flag and that current element is a char
                stringnorm = stringnorm[:x] + stringnorm[x].swapcase() + stringnorm[x + 1:]
                flag_to_change_case = False  # changing back flag value
            if stringnorm[x] in ['!', '?', '\n', '\t'] or \
                    (stringnorm[x] == '.' and not stringnorm[x + 1].isalpha()):
                flag_to_change_case = True  # changing flag value
        return stringnorm      # return normalized string