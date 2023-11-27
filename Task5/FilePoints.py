import os.path

class FilePoints:

    @staticmethod

    def write_to_file(string_to_write_to_file: str):

        if os.path.isfile('news_gen.txt'):  # If file exists
            with open('news_gen.txt', 'a') as file_to_write:   # Open file to add new record
                print(string_to_write_to_file, file=file_to_write)  # print to file
        else:                                                   # If file is not exist
            with open('news_gen.txt', 'w') as file_to_write:       # Create and open file to write
                print(string_to_write_to_file, file=file_to_write)  # print to file



