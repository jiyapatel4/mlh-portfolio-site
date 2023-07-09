#!/bin/bash

# This script runs another script until it fails

# Check if exactly one argument is passed
if [ $# -ne 1 ]
then
    echo "Incorrect usage. Please provide a file path. Usage: ./debug-script.sh filepath"
    exit 1
fi

# Filepath to the script to debug
script=$1

# Count of runs
count=0

# Temp files for stdout and stderr
stdout=$(mktemp)
stderr=$(mktemp)

# Run the script until it fails
while true; do
    # Increase the count
    count=$((count+1))
    
    # Run the script and capture stdout and stderr
    bash "$script" >"$stdout" 2>"$stderr"
    
    # If the script failed, break the loop
    if [ $? -ne 0 ]; then
        break
    fi
done

# Print the count and outputs
echo "It took $count runs to fail."
echo "Standard Output:"
cat "$stdout"
echo "Standard Error:"
cat "$stderr"

# Clean up temp files
rm "$stdout"
rm "$stderr"