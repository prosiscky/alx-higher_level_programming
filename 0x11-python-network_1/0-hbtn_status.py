#!/usr/bin/python3


"""Python script that fetches https://alx-intranet.hbtn.io/status
REQUIREMENTS:
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as resp:
        content = resp.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(utf8_content.decode('utf-8')))

