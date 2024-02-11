import json
import sys

def generate_html(conversations, output_file):
    # HTML template with inline CSS for basic styling
    html_template = """<!DOCTYPE html>
<html>
<head>
    <title>Conversations Overview</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .title {{ color: green; }}
        .url {{ color: dodgerblue; }}
    </style>
</head>
<body>
    <h1>Conversations Overview</h1>
    <ul>
        {items}
    </ul>
</body>
</html>"""
 
    # Generate list items for each conversation
    items = '\n'.join([
        f'<li><span class="title">{conversation["title"]}</span>: <a class="url" href="https://chat.openai.com/c/{conversation["conversation_id"]}" target="_blank">Link</a></li>'
        for conversation in conversations
    ])
    
    # Write the formatted HTML content to the specified output file
    with open(output_file, 'w') as file:
        file.write(html_template.format(items=items))
    
    print(f"HTML file generated: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_json_file> <output_html_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    output_html_path = sys.argv[2]

    # Load JSON data
    try:
        with open(json_file_path, 'r') as json_file:
            conversations = json.load(json_file)
    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(2)

    # Validate JSON data structure
    if not isinstance(conversations, list) or not all("title" in conv and "conversation_id" in conv for conv in conversations):
        print("Invalid JSON structure. Ensure it is a list of objects with 'title' and 'conversation_id'.")
        sys.exit(3)

    # Generate HTML file
    generate_html(conversations, output_html_path)

