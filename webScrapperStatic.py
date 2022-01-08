import urllib.request
FILENAME = "web"

def getWeb():
    web = open(FILENAME+'.html','wb')
    request = urllib.request.urlopen('https://lorem2.com')
    request = request.read()
    web.write(request)
    web.close()

def getTitle():
    print('TITLE: ')
    files = open(FILENAME+'.html','rb')
    start = '<title>'
    end = '</title>'
    lines = files.readlines()
    for line in lines:
        line = str(line)
        if start in line:
            x = line.find(start)
            x = x + len(start)
            y = line.find(end)
            print(line[x:y])

def getList():
    print('LIST: ')
    web = open(FILENAME+'.html','rb')
    start = '<li>'
    end = '</li>'
    specialLabel = "href"
    for line in web.readlines():
        line = str(line)
        if start in line and specialLabel not in line:
            x = line.find(start)
            x = x + len(start)
            y = line.find(end)
            print(line[x:y])
 
if __name__ == '__main__':
    getWeb()
    getTitle()
    getList()