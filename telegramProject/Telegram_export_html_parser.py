import pandas as pd 
import os
import dateutil
import re 
import urllib3
from bs4 import BeautifulSoup
import codecs
# Inputs
# Number of messages.html export files from Telegram Export
exportMessageCount = 427

def parse_telegram_export(html_str, tz_name=None):
    ''' Parses a Telegram html export.
    Params:
      - html_str (str): The html string containing the Telegram export.
      - tz_name (str|None): The name of the timezone where the export was made (eg. "Italy/Rome").
        If None, no time zone will be set for the resulting datetime.
    Returns (generator<(str, datetime.datetime, str, list<str>)>): A generator object
        that yields a (from_name, date, text, links) tuple for each messages in the export,
        where from_name is the sender name, date and text are the date and text of the message
        and links is a list of the links eventually found in the message.
    '''
    soup = BeautifulSoup(html_str, 'html.parser')
    tz = dateutil.tz.gettz(tz_name) if tz_name else None
    for div in soup.select("div.message.default"):
        body = div.find('div', class_='body')
        from_name_ = body.find('div', class_='from_name')
        if from_name_ is not None:
            from_name = from_name_.string
            if from_name is None:
                from_name = from_name
            else:
                from_name = from_name.strip()

        text = body.find('div', class_='text')
        if text is not None:
            text = text.get_text().strip()

        raw_date = body.find('div', class_='date')['title']
        naiv_date = dateutil.parser.parse(raw_date)
        date = naiv_date.astimezone(tz) if tz else naiv_date
        yield (from_name, date, text)

# Open html file
raw = open("messages.html", encoding='utf8')    


data = parse_telegram_export(raw, tz_name=None)

# Data in tuple format
df1 = pd.DataFrame(list(data), columns = ['from_name','date','text'])

# Open html file
for i in range(2,exportMessageCount+1):
      filename = "messages" + str(i) + ".html"
      raw = open(filename, encoding='utf8')
      data = parse_telegram_export(raw, tz_name=None)
      df2 = pd.DataFrame(list(data), columns = ['from_name','date','text'])
      df1 = df1.append(df2).reset_index(drop = True)

      completion = round(float(i)/float(exportMessageCount) * 100)
      print(str(completion) + "%" + " completed.")

      if( i == int(exportMessageCount)):
          print('Completed')
    
# Export
df1.to_csv('Chat_Data v1.0.csv')