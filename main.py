from bs4 import BeautifulSoup
import requests
import sys

# Display help 
def help():
    print('''Usage:
python main.py [link]

Example:
python main.py https://www.google.com''')

if __name__ == "__main__":
# Extract link fromm command link argument
    link = ''
    try:
        link = sys.argv[1]
    except IndexError:
        help()
        exit(1)

    if link == "-h" or link=="--help":
        help()
    else:
        # Request the code and extract links from the html page
        try:
            r = requests.get(link)
        except:
            print("Arr error occured!")
            exit(1)
        soup = BeautifulSoup(r.content.decode(), 'lxml')

        linkText = ""

        # Find all the links
        for i in soup.find_all('a'):
            linkText += str(i.get('href')) 
        # Write links to links.txt file in current directory
        with open("links.txt", "a") as file:
            file.write(linkText)

        print("Link extracted successfully to links.txt file in the current directory")

