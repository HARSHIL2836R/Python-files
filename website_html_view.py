# This will import urlopen
# class from urllib module
from urllib.request import urlopen

link = input("Paste the link to view its details:- ")
page = urlopen(link)

content = page.read()
print(content)


input('press Enter to exit')
