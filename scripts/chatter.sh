#!/bin/bash

# Check if a path argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_json_file>"
    exit 1
fi

# Assign the first argument as the JSON file path
JSON_FILE="$1"

# Base URL to prepend to conversation IDs
BASE_URL="https://chat.openai.com/c/"

# Extract conversation titles and IDs, and generate structured output
jq -r '.[] | "\(.title): \(.conversation_id)"' "$JSON_FILE" | while read -r line; do
    conversation_id=$(echo "$line" | sed -E 's/.*: (.*)/\1/')
    title=$(echo "$line" | sed -E 's/(.*): .*/\1/')
    echo "Title: $title" "URL: ${BASE_URL}${conversation_id}"
#    echo "" # Add a newline for better readability
done

