#!/bin/bash
# send a request to an URL with curl, displays size of body of the response
curl - s "$1" | wc - c
