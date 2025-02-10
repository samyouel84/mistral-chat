# Mistral AI Chat

Mistral AI Chat is a simple command-line interface for interacting with an AI model. It allows users to type messages and receive responses from the AI. The chat can be ended by typing 'exit'.

## Author

Samuel Morrison

## Features

- **Colourful Output**: Uses `colorama` to provide coloured output for better readability.
- **Text Wrapping**: Automatically wraps long responses to fit the terminal width.
- **Customisable**: Easily configurable with API key, model, and API URL.
- **Typewriter Effect**: Adds a typewriter effect to the welcome message.
- **Version**: v1.0.0

## Requirements

- Python 3.6+
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/mistral-ai-chat.git
    cd mistral-ai-chat
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your configuration:
    - Create a `config.py` file in the project root.
    - Add your API key, model, and API URL to the `config.py` file:
    ```python
    API_KEY = 'your_api_key_here'
    MODEL = 'your_model_here'
    API_URL = 'your_api_url_here'
    ```

## Usage

Run the chat application:
```sh
python main.py
```

- Type your message and press Enter to send it to the AI.
- The AI's response will be displayed in the terminal.
- Type 'exit' to end the chat.

## Configuration

The `config.py` file should contain the following variables:

- `API_KEY`: Your API key for the AI service.
- `MODEL`: The AI model you want to use.
- `API_URL`: The URL of the AI service API.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 Samuel Morrison

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


