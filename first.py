#!/usr/bin/env python
import requests
import re
import subprocess
import optparse


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-l", "--link", dest="link",
                      help="intface to change its mac add ")

    return parser.parse_args()


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


url = ["https://www.facebook.com/"]
# x = url[0].split("//")
# z = x[1].split(".com")
# y = z[0].split(".edu")
# e = y[0].split(".")

# print("////////////////////////////////////////////////////////////////////////////////////////////")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

r = requests.get(url[0], headers=headers)

# print(r.text)

with open("ez.text", 'wb') as f:
    f.write(r.content)


arr = []

with open('ez.text', 'r') as in_file:
    for line in in_file:
        if 'http' in line:
            result = re.search('https:.*.\.js', line)
            if result:
                arr.append(result.group(0))

# for i in range(0, len(arr)):
   # print(arr[i])

Arr_2 = []

# Iterating values in Arr_1
for item in arr:
    # split the values in each item using "," separator.
    for i in item.split(","):
        # append each value in after splitiing into Arr_2
        Arr_2.append(i)

# printing arrays


# for i in range(0, len(Arr_2)):
   # print(Arr_2[i])

print("////////////////////////////////////////////////////////////////////////////////////////////")
with open("dom.text", "w") as txt_file:
    for line in Arr_2:
        txt_file.write("".join(line) + "\n")

ee = []
with open('dom.text', 'r') as in_file:
    for line in in_file:
        if 'http' in line:
            result = re.search('https:.*.\.js', line)
            if result:
                ee.append(result.group(0))

for i in range(0, len(ee)):
    print(ee[i])

s = "Hello\n"

# for k in range(0, len(ee)):
#  try:

#  r1 = requests.get(ee[k], headers=headers)
#    with open("f.text", 'wb') as g:
#       g.write(r1.content)
#    g.close()
# print(r1.status_code)
# if r1.status_code == 404:
#       print("this url dosn't exist")
#  except Exception as error:
#   print(error, "مش شغال")

java = []
for k in range(0, len(ee)):
    try:

        r1 = requests.get(ee[k], headers=headers)
        sc = r1.content
        java.insert(k, sc)
        print(r1.status_code)
        if r1.status_code == 404:
            print("this url dosn't exist")
    except Exception as error:
        print(error, "not working")

# print("////////////////////////////////////////////////////////////////////////////////////////////")
# for o in range(0, len(java)):
  #  print(java[o], len(java))


print("////////////////////////////////////////////////////////////////////////////////////////////")
with open("f.text", "w") as txet_file:
    txet_file.write("\n  ".join(str(v) for v in java))


values = ["Document.write()", "Document.writeln()", "Document.domain()", "Location.href()",
          "Element.innerhtml", "Element.outerHTML", "Element.insertadjancentHTML"]
values1 = ["location.host", "location.hostname", "location.href", "location.pathname",
           "location.search", "location.protocol", "location.assign()", "location.replace()"]
values2 = ["Window.location.search",
           "Window.location.hash", "Document.referrer"]
values2 = ["targetWindow.postMessage", "window.addEventListener"]
# Open the text file


def my_function(path, values, type):
    with open(path, 'r') as file:
       # Loop through the array
        for line in file:
            # Loop through each line of the file
            for value in values:
                # Check if the value is in the line
                result = re.search(value, line)

        if result:
            print("ther is a possibility website infaction", type)
        else:
            print("the website clear", type)


# Close the file

my_function("f.text", values, "on DOM XSS")
my_function("f.text", values1, "on open-redirection vulnerabilities")
my_function("f.text", values2, "on ProtoType Pollution")
my_function("f.text", values2, "on Cross Window Message Attack")
