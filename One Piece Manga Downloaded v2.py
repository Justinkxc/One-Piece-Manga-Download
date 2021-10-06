# HOW ASSIGN W TO LINE 15 BUT ALSO MAKE W CHANGE WITH THE WHILE LOOP SO THAT THE VALUE OF W WILL INCREASE FOR LINE 15

w = 1
import requests
import re

x = input("Manga Chapter: ")
y = ("https://mangapill.com/chapters/2-1%s000/one-piece-chapter" % (x))
z = ("https://cdn.readdetectiveconan.com/file/mangap/2/1%s000/%d\.png" % (x, w))

while w <= 20:
    r = requests.get(y)  # make a request from the webpage y
    print(r.status_code)  # this tell us the outcome of the request
    images = re.findall(z, r.text)
    w = w + 1

    for image in images:
        r1 = requests.get(image)
        outfile = open("Page %d.jpg" % w, "wb")  # wb the b means binary. images open in binary
        outfile.write(r1.content)
        outfile.close()
