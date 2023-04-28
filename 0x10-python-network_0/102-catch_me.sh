#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -X PUT 0.0.0.0:5000/catch_me -H "Origin:HolbertonSchool" -d \
"user_id=98" -L -H "Referer: 0.0.0.0:5000/catch_me" -w "\n" -o /dev/null
