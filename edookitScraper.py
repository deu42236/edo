#minor changes
from bs4 import BeautifulSoup
import requests
import keys
from datetime import datetime

url = 'https://spseol.edookit.net'
cookies = keys.cookies
headers = keys.headers
response = requests.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
lessons = soup.findAll(attrs={'class':'lesson-info'})



def format_converter(input_str, time_position):
    date_time_str = input_str[3:]
    # Step 2: Split the date and time
    date_str, time_str = date_time_str.split(',')
    date_str = date_str.strip()
    time_str = time_str.split('–')[time_position].strip()
    date_time_combined_str = f"{date_str} {time_str}"
    date_time_obj = datetime.strptime(date_time_combined_str, "%d.%m.%Y %H:%M")
    output_str = date_time_obj.strftime("%Y-%m-%dT%H:%M:%S")
    return output_str

def all_lessons():
    try:
        finalList = [] #matrix of all lessons
        for j in range(len(lessons)):
            multiLineLesson = lessons[j].text.splitlines() #multiline string to list of strings
            currentLesson = []
            for i in multiLineLesson:
                i = i.replace('            ', '')
                i = i.replace('        ', '')
                i = i.replace('    ', '',)
                i = i.replace('\u2009', '')
                i = i.replace('Informace o hodině', '')
                if i != '':       #remove empty elements
                    currentLesson.append(i)
            finalList.append(currentLesson)
        finalList[0].insert(0, format_converter(finalList[0][0], 0))
        finalList[0].insert(1, format_converter(finalList[0][1], 1))
        finalList[0].pop(2)
        return(finalList)
    except response.status_code == 200:
        print('Error: ', response.status_code)
        exit()


"""
                                    [0] - začátek
                                    [1] - konec
                                    [2] - předmět
                                    [3] - Učitel
                                    [4] - Místnost
""" 


print(len(lessons))
print(len(all_lessons()))