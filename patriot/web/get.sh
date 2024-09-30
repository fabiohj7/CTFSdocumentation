!#/bin/bash

curl --verbose --header "X-Forwarded-For: 127.0.0.5" -X GET http://chal.competitivecyber.club:8081/
