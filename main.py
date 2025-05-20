from bs4 import BeautifulSoup
import requests
import sys

def help():
    print('''Usage:
python main.py [link]

Example:
python main.py https://www.google.com''')

link = ''
try:
    link = sys.argv[1]
except IndexError:
    help()
    exit(1)

if link == "-h" or link=="--help":
    help()
else:
    try:
        r = requests.get(link)
    except:
        print("Arr error occured!")
        exit(1)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')

    linkText = ""
    with open("links.txt", "a") as file:
        for i in soup.find_all('a'):
            linkText += str(i) 
        file.write(linkText)

    print("Link extracted successfully to links.txt file in the current directory")
