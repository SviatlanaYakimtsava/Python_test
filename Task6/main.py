from FilePoints import FilePoints
from news import News
from horoscope import Horoscope
from private_ad import PrivateAd
from datetime import datetime
from RecordFiles import RecordsFiles
from datetime import timedelta


class NewsGeneratorMenu:

    def __init__(self):
        self.file_to_write = FilePoints()  # initialization of local variable with object of FileOperations class

    @staticmethod
    def get_input_from_console() -> str:
        menu_input = input(">>> ")  # input selected option from the console
        return menu_input.lower()  # return lowercased input text

    def initial_menu(self):
        while True:     # loop until exit
            print("Hi! I can read news from file or generate new one, what would you prefer ?:\n"
                  "\t1. Generate news menu\n"
                  "\t2. Read news from file\n"
                  "\t0. Exit")
            choice = NewsGeneratorMenu.get_input_from_console()     # get input from the console
            if choice == "generate" or choice == "1":     # if user select generate
                self.generate_news_menu()                                   # open menu for generating news
            elif choice == "read" or choice == "2":       # if user select read
                self.read_from_file_menu()                                  # open menu to read news
            elif choice == "exit" or choice == "0":       # if user select exit
                break                                                       # exit from the loop
            else:                                                           # if input was not recognized - try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'generate\', "
                      "\'read\' or \'exit\'")

    def generate_news_menu(self):
        while True:
            print("Select data type to generate: \n"  # print menu text 
                  "\t1. News\n"  # to generate news
                  "\t2. Private ad\n"  # to generate ad 
                  "\t3. Horoscope\n"  # to generate horoscope 
                  "\t0. Back")  # to exip from the loop

            choice = NewsGeneratorMenu.get_input_from_console()     # get input from the console

            if choice.find("news") != -1 or choice == "1":  # if user selected news or menu number
                # FileOperations(add_news_menu())  # write to file generated news feed
                self.news_menu()  # Call the function to get news generator menu
                # if user selected ad, private of menu number
            elif choice == "ad" or choice.find("private") != -1 or choice == "2":
                self.private_ad_menu()  # Call the function to get private ad generator menu
                    # if user selected weather or menu number
            elif choice == "horoscope" or choice == "3":
                self.horoscope_menu()  # Call the function to get weather forecast generator menu
                    # if user selected exit of menu number
            elif choice == "back" or choice == "0":
                break  # exit from the infinite loop
            else:  # else print to console that printed text was incorrect
                print("Try again to enter right values")

    def read_from_file_menu(self):
        while True:     # loop until exit
            print("Read from the default file or select another file?:\n"
                  "\t1. Default file\n"
                  "\t2. Personal file\n"
                  "\t0. Back")
            choice = NewsGeneratorMenu.get_input_from_console()            # get input from the console
            if choice.find("default") != -1 or choice == "1":     # if user select default file
                self.get_news_from_default_file()                          # open default file
            elif choice.find("personal") != -1 or choice == "2":  # if user select personal file
                self.get_news_from_personal_file()                         # open personal file
            elif choice.find("back") != -1 or choice == "0":      # if user select back
                break                                                      # go to previous menu
            else:                                                          # if input was not recognized - try again
                print("Incorrect input. Try again")

    def news_menu(self):
        news_body = input("Tell the news \n")
        if len(news_body) == 0:  # if input was empty
            news_body = "You haven't entered news"
        news_city = input("Where news happen? \n")
        if len(news_city) == 0:  # if input was empty
            news_city = "You haven't entered city"
        self.file_to_write.write_to_file(News().generate_news(news_body, news_city))  # write to file
        pass

    def private_ad_menu(self):
        ad_text = input('What you want to advertise? \n')
        if len(ad_text) == 0:  # input was empty
            ad_text = "You haven't entered advertising"  # put default value to the variable
        while True:  # infinite loop to get correct expiration date
            expdate = input("What is an expiration date? (dd/mm/yyyy) \n")
            if len(expdate) == 0:  # if input is empty
                expdate = None  # put the default value
                break
            else:  # if input is not empty
                try:  # error handler of incorrect input data
                    expdate = datetime.strptime(str(expdate), '%d/%m/%Y').date()
                    if expdate < datetime.now().date():  # if input date is less than current one
                        print("Entered expiration date is less than current one. Try again.")  # print to console
                    else:  # if input date is more than current one
                        break
                except ValueError:  # exception handler
                    print("The entered date has wrong format. Try again.")  # print to console
        self.file_to_write.write_to_file(PrivateAd().generate_private_ad(ad_text, expdate))
        pass

    def horoscope_menu(self):
        zodiacsign = input('Enter your zodiac sign \n')
        if len(zodiacsign) == 0:  # if input value is empty
            zodiacsign = "You haven't entered zodiac sign"  # put default value to the variable
        self.file_to_write.write_to_file(Horoscope().generate_horoscope(zodiacsign))
        pass
    @staticmethod
    def get_news_from_default_file():
        file_to_read = RecordsFiles()      # initialization object of the RecordsFromFilesHandler class
        file_to_read.write_new_records_to_the_file()  # write new records to the file

    @staticmethod
    def get_news_from_personal_file():
        # initialization object of the RecordsFromFilesHandler class with provided path
        file_to_read = RecordsFiles(RecordsFiles.get_file_path())
        file_to_read.write_new_records_to_the_file()  # write new records to the file

