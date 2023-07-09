#!/bin/bash

# This script says hello to the provided argument

# Check if at least one argument is passed
if [ $# -eq 0 ]
then
    echo "No arguments provided. Usage: ./say-hello-to.sh [Your String]"
    exit 1
fi

# Concatenate all arguments
message="$*"

# Output the hello message
echo "Hello, $message!"
