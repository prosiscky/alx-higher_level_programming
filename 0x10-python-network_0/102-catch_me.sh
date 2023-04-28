#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -H "Origin: HolbertonSchool" -H "Referer: 0.0.0.0:5000/catch_me" -d "user_id=98" 0.0.0.0:5000/catch_me -o /dev/null
