# This will import urlopen
# class from urllib module
from urllib.request import urlopen

link = input("Paste the link to view its details:- ")
page = urlopen(link)
print(page.headers)


input('press Enter to exit')
