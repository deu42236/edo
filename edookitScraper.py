#minor changes
from bs4 import BeautifulSoup
import requests
import keys



url = 'https://spseol.edookit.net/timetable/static'

cookies = keys.cookies
headers = keys.headers

response = requests.get(url, cookies=cookies, headers=headers)
#print(response.status_code)
# response 200 -> OK, if not big bad

soup = BeautifulSoup(response.content, 'html.parser')
lessons = soup.findAll(attrs={'class':'lesson-info'})
# lessonRaw = soup.find(attrs={'class':'lesson-info'})

# print(lessons[0].text.splitlines())
finalList = [] #matrix of all lessons

for j in range(10):
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

"""
[0] - čas
[1] - předmět
[2] - Učitel
[3] - Místnost
"""

print(finalList) #matrix of all lessons