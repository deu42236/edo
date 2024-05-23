from bs4 import BeautifulSoup
import requests
import pprint

#open https://spseol.edookit.net/
#inspect -> network -> F5 -> right click on the first request [spseol.edookit.net] -> copy -> copy as cURL(bash)
#copy cURL(bash) and convert
#https://curlconverter.com/

url = 'https://spseol.edookit.net/timetable/static/'

cookies = {

}

headers = {

}


response = requests.get(url, cookies=cookies, headers=headers)
#print(response.status_code)
# response 200 -> OK, if not big bad

soup = BeautifulSoup(response.content, 'html.parser')
# lessonsRaw = soup.findAll(attrs={'class':'lesson-info'})
lessonRaw = soup.find(attrs={'class':'lesson-info'})

lessonExtract = []
multiLineLesson = lessonRaw.text.splitlines() #multiline string to list of strings

for i in multiLineLesson:
    i = i.replace(' ', '')
    if i != '': #remove empty elements
        lessonExtract.append(i)

print(lessonExtract)