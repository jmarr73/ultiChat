#!/bin/bash

# Usage function to display help
usage() {
    echo "Usage: $0 -f <path_to_json_file> -o <output_file.md>"
    echo "  -f  Specifies the path to the JSON file."
    echo "  -o  Specifies the path to the output markdown file (must end with .md)."
}

# ANSI color codes for coloring output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
WHITE='\033[0;37m'
NC='\033[0m' # No Color

# Initialize variables for command-line arguments
JSON_FILE=""
OUTPUT_FILE=""

# Parse command-line arguments
while getopts "f:o:" opt; do
  case ${opt} in
    f )
      JSON_FILE=$OPTARG
      ;;
    o )
      OUTPUT_FILE=$OPTARG
      ;;
    \? )
      usage
      exit 1
      ;;
  esac
done

# Validate JSON file path was provided
if [ -z "$JSON_FILE" ]; then
    echo -e "${YELLOW}Error: JSON file path is required.${NC}"
    usage
    exit 1
fi

# Validate output file has .md extension
if [[ ! $OUTPUT_FILE =~ \.md$ ]]; then
    echo -e "${RED}Error: Output file must have a .md extension.${NC}"
    exit 1
fi

# Base URL to prepend to conversation IDs
BASE_URL="https://chat.openai.com/c/"

# Generate markdown table and display with symmetry
generate_markdown_display() {
    echo "# Conversations Table" | tee "$OUTPUT_FILE"
    echo "" | tee -a "$OUTPUT_FILE"
    echo "| Title | URL |" | tee -a "$OUTPUT_FILE"
    echo "|-------|-----|" | tee -a "$OUTPUT_FILE"
    jq -r '.[] | "\(.title)|\(.conversation_id)"' "$JSON_FILE" | while read -r line; do
        conversation_id=$(echo "$line" | awk -F'|' '{print $2}')
        title=$(echo "$line" | awk -F'|' '{print $1}')
        printf "| %-50s | [Link](%s) |\n" "$title" "${BASE_URL}${conversation_id}" | tee -a "$OUTPUT_FILE"
    done
}

# Execute function to generate markdown and display output
generate_markdown_display

