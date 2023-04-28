#!/usr/bin/python3


"""Python script that fetches https://alx-intranet.hbtn.io/status
REQUIREMENTS:
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement"""


import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as resp:
    content = resp.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8_content}")

