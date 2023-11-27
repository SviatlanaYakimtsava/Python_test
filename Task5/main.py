from FilePoints import FilePoints
from news import News
from horoscope import Horoscope
from private_ad import PrivateAd
from datetime import datetime
from datetime import timedelta


class NewsGeneratorMenu:

    def __init__(self):
        self.file = FilePoints()        # initialization of local variable with object of FileOperations class

    # function with general menu
    def general_menu(self):
        while True:
            print("Select data type to generate: \n"  # print menu text 
                  "\t1. News\n"  # to generate news
                  "\t2. Private ad\n"  # to generate ad 
                  "\t3. Horoscope\n"  # to generate horoscope forecast
                  "\t0. Exit")  # to exip from the loop

            menu_input = input("Your choice: ")  # input selected option from the console
            menu_input = menu_input.lower()  # lowercased input text

            if menu_input.find("news") != -1 or menu_input.find("1") != -1:  # if user selected news or menu number
                self.news_menu()      # Call the function to get news generator menu
            else:
                if menu_input.find("ad") != -1 or menu_input.find("private") != -1 or menu_input.find("2") != -1:
                    self.private_ad_menu()      # Call the function to get private ad generator menu
                else:
                    if menu_input.find("horoscope") != -1 or menu_input.find("3") != -1:
                        self.horoscope_forecast_menu()    # Call the function to get horoscope forecast generator menu
                    else:
                        if menu_input.find("exit") != -1 or menu_input.find("0") != -1:
                            break  # exit from the infinite loop
                        else:  # else print to console that printed text was incorrect
                            print("Incorrect data type selected. Try again to type menu number (1-3) or type \'news\', "
                                  "\'ad\' or \'horoscope\'")

    def news_menu(self):
        news_body = input("Tell the news \n")
        if len(news_body) == 0:  # if input was empty
            news_body = "You haven't entered news"
        news_city = input("Where news happen? \n")
        if len(news_city) == 0:  # if input was empty
            news_city = "You haven't entered city"
        self.file.write_to_file(News().generate_news(news_body, news_city)) # write to file
        pass

    def private_ad_menu(self):
        ad_text = input('What you want to advertise? \n')
        if len(ad_text) == 0:  # input was empty
            ad_text = "You haven't entered advertising" # put default value to the variable
        while True:  # infinite loop to get correct expiration date
            expdate = input("What is an expiration date? (dd/mm/yyyy) \n")
            if len(expdate) == 0:  # if input is empty
                expdate = None # put the default value
                break
            else:  # if input is not empty
                try:  # error handler of incorrect input data
                    expdate = datetime.strptime(str(expdate), '%d/%m/%Y').date()
                    if expdate < datetime.now().date():  # if input date is less than current one
                        print("Entered expiration date is less than current one. Try again.")  # print to console
                    else:  # if input date is more than current one
                        break  # exit from the loop
                except ValueError:  # exception handler
                    print("The entered date has wrong format. Try again.")  # print to console
        self.file.write_to_file(PrivateAd().generate_private_ad(ad_text, expdate))
        pass

    def horoscope_forecast_menu(self):
        zodiacsign = input('Enter your zodiac sign \n')
        if len(zodiacsign) == 0:  # if input value is empty
            zodiacsign = "You haven't entered zodiac sign"  # put default value to the variable
        self.file.write_to_file(Horoscope().generate_horoscope(zodiacsign))
        pass