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

today = str(datetime.today())



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
                i = i.replace('Včera ', 'Po ')
                i = i.replace('Dnes, ', 'Po ')
                if i != '':       #remove empty elements
                    currentLesson.append(i)
            finalList.append(currentLesson)
        # finalList[0].insert(0, format_converter(finalList[0][0], 0))
        # finalList[0].insert(1, format_converter(finalList[0][1], 1))
        # finalList[0].pop(2)

        # finalList[1].insert(0, format_converter(finalList[0][0], 0))
        # finalList[1].insert(1, format_converter(finalList[0][1], 1))
        # finalList[1].pop(2)
        return(finalList)
    


    except response.status_code == 200:
        print('Error: ', response.status_code)
        print('Check your internet connection or update keys.py file.')
        exit()



# print(len(lessons))
# print(len(all_lessons()))
# print(all_lessons()[0])
# print(type(all_lessons()[1]))


# print(format_converter(all_lessons()[0][0], 0))
# print(format_converter(all_lessons()[1][0], 0))
# print(format_converter(all_lessons()[3][0], 1))
# print(format_converter(all_lessons()[4][0], 0))
# print(format_converter(all_lessons()[5][0], 1))
# print(format_converter(all_lessons()[6][0], 0))
# print(format_converter(all_lessons()[7][0], 1))
# print(format_converter(all_lessons()[8][0], 0))
# print(format_converter(all_lessons()[9][0], 1))
# print(format_converter(all_lessons()[10][0], 0))



finalList = all_lessons()
for i in range(3):
    finalList[i].insert(0, format_converter(finalList[i][0], 0))
    finalList[i].insert(1, format_converter(finalList[i][1], 1))
    finalList[i].pop(2)

print(finalList)
