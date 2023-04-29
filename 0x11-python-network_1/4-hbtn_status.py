#!/usr/bin/python3

"""
Write a Python script that fetches
     https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the
 example (tabulation before -)
"""

import requests

def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    status = fetch_status()
    print("- type: {}\n- content: {}".format(type(status), status))
