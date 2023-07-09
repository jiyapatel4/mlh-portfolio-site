#!/bin/bash

# This script searches the entire file system for a given filename

# Check if exactly one argument is passed
if [ $# -ne 1 ]
then
    echo "Incorrect usage. Please provide a filename. Usage: ./find-file.sh filename"
    exit 1
fi

# Searching the file system
results=$(find / -name "$1" 2>/dev/null)

# Count the number of matches
count=$(echo "$results" | wc -l)

if [ $count -eq 0 ]
then
    echo "Found 0 matches"
else
    echo "Found $count matches"
    echo "$results"
fi
