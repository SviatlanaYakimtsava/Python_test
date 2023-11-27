from datetime import datetime

class News:

    def __init__(self):
        self.news_in_string = 'News -------------------------\n'    # initialization of the local variable

    def generate_news(self, news_body, news_city):
        timestamp = datetime.now().strftime("%Y/%m/%d %H.%M")  #  current timestamp with formar
        self.news_in_string += str(news_body + '\n' + news_city + ', ' + str(
            timestamp) + '\n------------------------------\n\n')
        return self.news_in_string