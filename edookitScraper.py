from bs4 import BeautifulSoup
import requests
import keys
from datetime import datetime, timedelta, date

url = 'https://spseol.edookit.net'
cookies = keys.cookies
headers = keys.headers
response = requests.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
lessons = soup.findAll(attrs={'class':'lesson-info'})

today = date.today()
today = today.strftime('%d') + '.' + str(int(today.strftime('%m'))) + '.' + today.strftime('%Y') #today in edookit format
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime('%d') + '.' + str(int(yesterday.strftime('%m'))) + '.' + yesterday.strftime('%Y') #yesterday in edookit format


def format_converter(input_str, time_position): #edookit format -> google calendar format
    date_time_str = input_str[3:]
    date_str, time_str = date_time_str.split(',')
    date_str = date_str.strip()
    time_str = time_str.split('–')[time_position].strip()
    date_time_combined_str = f"{date_str} {time_str}"
    date_time_obj = datetime.strptime(date_time_combined_str, "%d.%m.%Y %H:%M")
    output_str = date_time_obj.strftime("%Y-%m-%dT%H:%M:%S")
    return output_str

# def format_check(date_str):
#     try:
#         datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
#         return True
#     except ValueError:
#         return False


def all_lessons():
    finalList = [] #matrix of all lessons
    for j in range(len(lessons)):
    #for j in range(3):
        multiLineLesson = lessons[j].text.splitlines() #multiline string to list of strings
        currentLesson = []
        for i in multiLineLesson:
            i = i.replace('            ', '')
            i = i.replace('        ', '')
            i = i.replace('    ', '',)
            i = i.replace('\u2009', '')
            i = i.replace('Informace o hodině', '')
            i = i.replace('Včera, ', f"Po {yesterday}, ")
            i = i.replace('Dnes ', f"Po {today}, ")
            i = i.replace('Dnes, ', f"Po {today}, ")

            if i != '':       #remove empty elements
                currentLesson.append(i)
            
        finalList.append(currentLesson)
    
    finalfinalList = []


    for i in range(len(lessons)):
        try:
            finalList[i].insert(0, format_converter(finalList[i][0], 0))
            finalList[i].insert(1, format_converter(finalList[i][1], 1))
            finalList[i].pop(2)
            finalfinalList.append(finalList[i])
        except:
            continue

    return(finalfinalList)
all_lessons()