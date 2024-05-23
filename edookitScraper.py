from bs4 import BeautifulSoup
import requests


#open https://spseol.edookit.net/
#inspect -> network -> right click on the first request [spseol.edookit.net] -> copy -> copy as cURL(bash)
#copy cURL(bash) and convert
#https://curlconverter.com/




url = 'https://spseol.edookit.net/timetable/?familyTimetable-value=7&do=familyTimetable-changeFilter'

cookies = {

}

headers = {
    
}




response = requests.get(url, cookies=cookies, headers=headers)
#print(response.status_code)
# response 200 -> OK, if not big bad

soup = BeautifulSoup(response.content, 'html.parser')
lessons = soup.findAll(attrs={'class':'lesson-info'})
lessonRaw = soup.find(attrs={'class':'lesson-info'})


# print(lessons[0].text.splitlines())
finalList = [] #matrix of all lessons

for j in range(5):
    multiLineLesson = lessons[j].text.splitlines() #multiline string to list of strings
    currentLesson = []
    for i in multiLineLesson:
        i = i.replace(' ', '')
        # i = i.replace('\u2006', ' ')
        if i != '': #remove empty elements
            currentLesson.append(i)
    finalList.append(currentLesson)
print(finalList) #matrix of all lessons