import requests, time, json

with open("config.json") as f:
    config = json.load(f)

urlBase = config['urlBase']
botKey = config['botKey']
url = urlBase + botKey
sourceRoom = config['sourceRoom']
targetRoom =  config['targetRoom']
msgCount = config['msgCount']
user_id = 0

def getMe():
    req = requests.get(url+'/getMe')
    print(req.text)

def getUpdates():
    req = requests.get(url+'/getUpdates')
    print(req.text)

def getChat(room):
    req = requests.get(url+'/getChat?chat_id={}'.format(room))
    print(req.text)

def getChatAdministrators(room):
    req = requests.get(url+'/getChatAdministrators?chat_id={}'.format(room))
    print(req.text)

def getChatMember(room, user):
    req = requests.get(url+'/getChatAdministrators?chat_id={}&user_id={}'.format(room, user))
    print(req.text)

def getWebhook():
    req = requests.get(url+'/getWebhookInfo')
    print(req.text)

def deleteWebhook():
    req = requests.get(url+'/deleteWebhook')
    print(req.text)

def getFile(fileId):
    req = requests.get(url+'/getFile?file_id={}'.format(fileId))
    data = json.loads(req.text)
    filePath = data['result']['file_path']
    req = requests.get('https://api.telegram.org/file/'+botKey+'/'+filePath)
    data = req.content
    with open('tmpFile.dat', 'wb') as f:
        f.write(data)


def forwardAll(sourceRoom, targetRoom):
    for i in range(1,msgCount):
        try:
            req = requests.get(url+'/copyMessage?chat_id={}&from_chat_id={}&message_id={}'.format(targetRoom,sourceRoom, i))
            print(req.text)
        except:
            continue
        time.sleep(3)


getMe()
getUpdates()
getWebhook()
getChat(sourceRoom)
getChatAdministrators(sourceRoom)
#forwardAll(sourceRoom, targetRoom)
#deleteWebhook()
#getFile('')
