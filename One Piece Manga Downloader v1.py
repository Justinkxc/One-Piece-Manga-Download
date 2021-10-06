import requests
import re

x=input("Manga Chapter: ")
y=("https://mangapill.com/chapters/2-1%s000/one-piece-chapter" % (x))
z=("https://cdn.readdetectiveconan.com/file/mangap/2/1%s000/.+\.png" % (x))

for i in range (1, 20, 1):
    print(i)
    r = requests.get(y)     #make a request from the webpage y
    print(r.status_code)	#this tell us the outcome of the request
    images = re.findall(z, r.text)
    print(images)

    for image in images:
        r1 = requests.get(image)
        outfile = open("Page %d.jpg" % i, "wb") #wb the b means binary. images open in binary
        outfile.write(r1.content)
        outfile.close()