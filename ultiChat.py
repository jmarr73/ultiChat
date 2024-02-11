#!/usr/bin/env python3

import json
import sys
from datetime import datetime
import os

def format_timestamp(unix_timestamp):
    """Convert UNIX timestamp to 'Year-Month-Day' format."""
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%b-%d')

def generate_html(conversations, output_file):
    if not output_file.endswith('.html'):
        print("Output file must have a .html extension.")
        sys.exit(1)

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Conversations Overview</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Conversations Overview</h1>
        <table>
            <tr>
                <th>Title</th>
                <th>Date</th>
                <th>Link</th>
            </tr>
    """

    for conversation in conversations:
        title = conversation.get('title', 'No Title')
        date = format_timestamp(conversation.get('create_time', 0))
        conversation_id = conversation.get('conversation_id', 'No ID')
        link = f"https://chat.openai.com/c/{conversation_id}"

        html_content += f"""
            <tr>
                <td>{title}</td>
                <td>{date}</td>
                <td><a href="{link}" target="_blank">{link}</a></td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"HTML file generated successfully: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ultiChat.py <input_json_file> [output_html_file]")
        sys.exit(1)

    input_json_file = sys.argv[1]
    output_html_file = 'ultiChat.html' if len(sys.argv) == 2 else sys.argv[2]

    # Ensure the output file has a .html extension
    if not output_html_file.endswith('.html'):
        output_html_file += '.html'

    # Ensure the output file is written to the current working directory
    output_html_file = os.path.join(os.getcwd(), output_html_file)

    try:
        with open(input_json_file, 'r') as json_file:
            conversations = json.load(json_file)
        generate_html(conversations, output_html_file)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
