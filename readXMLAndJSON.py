import urllib.request
import xml.etree.ElementTree as xml
import json

def readXML():
    print("XML: ")
    url="https://www.w3schools.com/xml/simple.xml"
    info=urllib.request.urlopen(url).read()
    archive = xml.fromstring(info.decode())

    query = archive.findall("food")
    print("Foods: ",len(query),"\n")

    for line in query:
        print("Name: ",line.find("name").text)
        print("Price: ",line.find("price").text)
        print("Description: ",line.find("description").text)
        print("Calories: ",line.find("calories").text)
        print("")

def readJson():
    print("JSON: ")
    file = open("example.json","r")
    fileJson = json.loads(file.read())

    menuItems = fileJson["menu"]["popup"]["menuItem"]
    print(f"Have {len(menuItems)} menuItems")
    
    for data in menuItems:
        print("value: " + data["value"])
        print("onclick: " + data["onclick"])
        print("")

if __name__ == '__main__':
    readXML()
    readJson()