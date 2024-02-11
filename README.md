# ultiChat

UltiChat is a Python-based tool designed to convert your ChatGPT JSON-formatted conversation histories into searchable, neatly formatted HTML files. It enables users to quickly navigate through their chat history with OpenAI's ChatGPT, providing easy access to past conversations and insights.

## Features

- **Convert JSON to HTML**: Transform your conversation history JSON file into an easily navigable HTML document.
- **Searchable Conversations**: Utilize browser search capabilities (Ctrl+F) to find specific conversations or topics within the HTML output.
- **Symmetrical Layout**: Enjoy a clean, table-formatted layout ensuring symmetry and alignment of conversation titles, dates, and links.
- **Direct Links**: Access conversations directly via hyperlinks to the ChatGPT platform.
- **Custom Output Filename**: Specify the output HTML file name or use the default ultiChat.html.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jmarr73/ultiChat.git
    cd ultiChat
    ```

2. Ensure you have Python installed. UltiChat was developed with Python 3.11+, but it should work with any Python 3+ version.

3. No additional libraries are required beyond the Python Standard Library.

## Usage

To generate an HTML file from your JSON-formatted conversation history, run:

1. Download your personal export data from ChatGPT.  
    - (Click on username bottom left, Settings & Beta, Data Controls, Export Data.)

2. Unzip your personal export data.

3. Run the following command

```bash
python ultiChat.py path/to/conversations.json [optional_output_filename.html]
```

- **path/to/conversations.json**: Replace this with the path to your JSON file containing the ChatGPT conversation history.
- **[optional_output_filename.html]**: Optionally, specify the name of the output HTML file. If omitted, the output will default to ultiChat.html in the current working directory.

## General Information

The `./scripts` directory in this project contains a few items that started off as the direction intended. Ultimately settled on the current option. They were useful and thought why not keep them around.  

The python code has zero dependencies on the `./scripts` directory.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

## License

UltiChat is released under the MIT License.

## Contact

For questions or feedback, please open an issue in the GitHub repository.
