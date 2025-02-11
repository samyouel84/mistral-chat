# Mistral AI Chat

Mistral AI Chat is a simple command-line interface for interacting with Mistral's large language models. It provides a clean interface for chatting with Mistral AI models like Mistral-7B, Mixtral-8x7B, or other Mistral-based models. The chat can be ended by typing 'exit'.

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
    git clone https://github.com/samyouel84/mistral-chat.git
    cd mistral-chat
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your configuration:
    - Copy the `config.example` file to `config.py`:
    ```sh
    cp .config.example .config.py
    ```
    - Edit the `config.py` file and add your Mistral API key:
    ```python
    MISTRAL_API_KEY = "your_api_key_here"
    MISTRAL_MODEL = "mistral-medium"  # Optional, remove this line to use default model
    API_URL = "https://api.mistral.ai/v1/chat/completions"  # Mistral API endpoint
    ```

## Usage

Run the chat application:
```sh
python main.py
```

- Type your message and press Enter to send it to the AI.
- The AI's response will be displayed in the terminal.
- Type 'exit' to end the chat.
- Type 'clear' to clear the screen.

## Configuration

The `.config.py` file should contain your Mistral API key, optional model selection, and API URL:

- `MISTRAL_API_KEY`: Your Mistral API key from [mistral.ai](https://mistral.ai/en)
- `MISTRAL_MODEL`: (Optional) The Mistral model you want to use. Available options:
  - `mistral-tiny`: Fastest, good for simple tasks
  - `mistral-small`: Balanced speed and capability
  - `mistral-medium`: Most capable model
  - If not specified, defaults to `mistral-small`
- `API_URL`: The endpoint for the Mistral API.

Example `.config.py` file:
```python
MISTRAL_API_KEY = "your_api_key_here"  # Replace with your actual API key
MISTRAL_MODEL = "mistral-small"  # Optional, remove this line to use default model
API_URL = "https://api.mistral.ai/v1/chat/completions"  # Mistral API endpoint
```

The application uses the Mistral API endpoint (https://api.mistral.ai/v1/chat/completions).

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


