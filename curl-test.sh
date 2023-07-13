#!/bin/bash
	
POST=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=TEST&email=jiya.patel@mlh.io&content=Just added a database to my portfolio site!')
GET=$(curl -s http://127.0.0.1:5000/api/timeline_post | jq '.timeline_posts[0]')

if  diff -w <(echo $POST) <(echo $GET)
then
	echo "Post was successful."
else
	echo "Post was unsuccessful."
fi
