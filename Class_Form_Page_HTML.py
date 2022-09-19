
#from msilib.schema import Class


FIRST_PART_TEXT = '''

    <!DOCTYPE html>
    <html lang="ru">

    <head>
        <title>Statistic</title>
        <meta charset="utf-8">
        <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            html{
                background: linear-gradient(90deg,  rgba(9, 255, 0, 0.705), rgba(251, 255, 2, 0.849), rgba(255, 0, 0, 0.589));
            }
            body { 
                color: rgb(0, 0, 0);
                text-align: center; 
                font-family: "Trebuchet MS", Arial; 
                margin-left:auto; 
                margin-right:auto;
                height: 100%;
                min-height:100vh        
            }
            small{        
                color: rgba(34, 0, 0, 0.377);
            }
            p{
                font-size: 1em;
                margin: 0.2em;
            }
            h1{        
                font-size: 3em;
            }
            span{
                color: rgb(0, 0, 0);                
                font-weight: bold;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }

            footer{
                left: 0;
                bottom: 0;
                width: 100%;
                height: 80px;
            }
        </style>
        <!--
        <script type="text/javascript">  
            setTimeout("window.location.reload()",1000)         
        </script>
        -->    

    </head>

        <body>

            <header>
                <h1>Статистика</h1>
            </header>

            <div class="content">
            '''

LAST_PART_TEXT = '''
            </div>

            <footer>
                <small>&copy; arhiopteryx </small>
                </br>
                <a href="https://t.me/arhiopteryx">Telegram</a>
                </br>
                <a href="http://arhiopteryx.myftp.org">My Website</a>
            </footer>

        </body>

    </html>
'''

class Form_Html_Page:

    def __init__(self, dictMessage, allMessageCount, allMessageWords, chatName):
        self.allText = ''
        self.dictMessage = dictMessage
        self.allMessageCount = allMessageCount
        self.allMessageWords = allMessageWords
        self.chatName = chatName
        
    
    def formPage(self):
        self.allText = self.allText + FIRST_PART_TEXT
        self.allText = self.allText + '\n            <p><span>' + self.chatName + '</span></p></br></br>'
        
        for userDict in list(self.dictMessage):
            percentMessages = round(100 * self.dictMessage[userDict][0] / self.allMessageCount, 2)
            percentWord = round(100 * self.dictMessage[userDict][1] / self.allMessageWords, 2)
            wordInMessage = round(self.dictMessage[userDict][1] / self.dictMessage[userDict][0], 2)
            self.allText = self.allText + '\n            <p>Сообщения от: <span>' + userDict + '</span></p>'
            self.allText = self.allText + '\n            <p>Написано сообщений: <span>' + str(self.dictMessage[userDict][0]) + ' из ' + str(self.allMessageCount) + ' (' + str(percentMessages) + '%)' + '</span></p>'
            self.allText = self.allText + '\n            <p>Написано cлов: <span>' + str(self.dictMessage[userDict][1]) + ' из ' + str(self.allMessageWords) + ' (' + str(percentWord) + '%)' + '</span></p>'
            self.allText = self.allText + '\n            <p>Слов на сообщение: <span>' + str(wordInMessage) + '</span></p>'
            self.allText = self.allText + '\n            </br>'

        self.allText = self.allText + LAST_PART_TEXT
    
    def getPageHTML(self):
        self.formPage()
        return self.allText