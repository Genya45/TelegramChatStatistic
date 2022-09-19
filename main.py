#!/usr/bin/python3
 
from bs4 import BeautifulSoup
import os
from Class_Form_Page_HTML import Form_Html_Page

RESULT_PACH_NAME = 'result'
RESULT_FILE_NAME_TXT = 'statistic.txt'
RESULT_FILE_NAME_HTML = 'statistic.html'
 
fileNameList = os.listdir()

dictMessage = {}
userName = 'NoName'
chatName = 'NoName'

for fileName in fileNameList:
    if fileName.endswith(".html"):
        with open(fileName, "r", encoding='utf-8') as f:
            
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')

            chatName = soup.find("div", attrs={ "class" : "content"}).find("div", attrs={ "class" : "text"}).text
                   

            for message in soup.find_all("div", attrs={ "class" : "default"}): 
                user = message.find("div", attrs={ "class" : "from_name"})  
                if user != None:
                    userName =  user.text.split('\n')[1] 
                    
                wordCount = 0
                textMessage = message.find("div", attrs={ "class" : "text"})
                if textMessage != None:
                    wordCount = len(textMessage.text.split('\n')[1].split(' '))
                    

                if dictMessage.get(userName) != None:
                    dictMessage[userName] = [dictMessage[userName][0] + 1, dictMessage[userName][1] + wordCount]
                else:    
                    dictMessage[userName] = [1, wordCount]

allMessageCount = 0
allMessageWords = 0
for userDict in list(dictMessage):
    if dictMessage[userDict][0] == 1 or dictMessage[userDict][1] == 0 :
        dictMessage.pop(userDict)
    else:            
        allMessageCount = allMessageCount + dictMessage[userDict][0]
        allMessageWords = allMessageWords + dictMessage[userDict][1]
    
print(dictMessage)
print(allMessageCount)
print(allMessageWords)
print('*****************')


if os.path.exists(RESULT_PACH_NAME) == False:
    os.mkdir(RESULT_PACH_NAME)

"""statisticFile = open(RESULT_PACH_NAME + '/' + RESULT_FILE_NAME_TXT, 'w', encoding='utf-8')

for userDict in list(dictMessage):
    percentMessages = round(100 * dictMessage[userDict][0] / allMessageCount, 2)
    percentWord = round(100 * dictMessage[userDict][1] / allMessageWords, 2)
    wordInMessage = round(dictMessage[userDict][1] / dictMessage[userDict][0], 2)

    statisticFile.writelines("\nСообщения от: " + userDict)
    statisticFile.writelines("\nНаписано сообщений: " + str(dictMessage[userDict][0]) + ' из ' + str(allMessageCount) + ' (' + str(percentMessages) + '%)')
    statisticFile.writelines("\nНаписано cлов: " + str(dictMessage[userDict][1]) + ' из ' + str(allMessageWords) + ' (' + str(percentWord) + '%)')
    statisticFile.writelines("\nСлов на сообщение: " + str(wordInMessage))
    statisticFile.writelines("\n ")

statisticFile.close()"""


htmlObj = Form_Html_Page(dictMessage, allMessageCount, allMessageWords, chatName)
statisticFileHTML = open(RESULT_PACH_NAME + '/' + RESULT_FILE_NAME_HTML, 'w', encoding='utf-8')
statisticFileHTML.writelines(htmlObj.getPageHTML())
statisticFileHTML.close()
