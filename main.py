import os
import requests
from colorama import Fore, Style, init
from config import MISTRAL_API_KEY as API_KEY, MISTRAL_MODEL as MODEL, API_URL
import textwrap
import shutil
import time
import sys
import re

# Initialize colorama with different settings
init(autoreset=True, strip=True, convert=True)

def wrap_text_with_indent(text, width, subsequent_indent='    '):
    """Wrap text with proper indentation for subsequent lines."""
    lines = text.strip().split('\n')
    wrapped_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            wrapped_lines.append('')  # Preserve empty lines
            continue
                
        # Match numbered list items (e.g., "1.", "1)", "1-")
        number_match = re.match(r'^(\s*\d+(?:\.|\)|\-)?\s*)', line)
        
        if number_match:
            # Get the full number prefix including the period and any spaces
            prefix = number_match.group(1).rstrip() + ' '  # Ensure single space after prefix
            rest = line[len(prefix):].strip()
            
            # Calculate proper indentation based on number width
            indent = ' ' * len(prefix)
            
            if line.startswith(prefix + '**'):
                # Don't wrap lines that start with bold markers
                wrapped_lines.append(Fore.CYAN + line + Style.RESET_ALL)
                if rest.endswith(':'):
                    # Insert a blank line after headings
                    wrapped_lines.append('')
            else:
                # Wrap the content after the number
                wrapped = textwrap.fill(
                    rest,
                    width=width,
                    initial_indent=prefix,
                    subsequent_indent=indent,
                    break_long_words=True,
                    break_on_hyphens=True,
                    expand_tabs=True,
                    replace_whitespace=True
                )
                wrapped_lines.append(wrapped)
        else:
            # Handle non-numbered lines
            if line.startswith('**') and line.endswith('**'):
                # Preserve bold formatting for entire lines
                wrapped_lines.append(Fore.CYAN + line + Style.RESET_ALL)
            else:
                # Wrap regular lines
                wrapped = textwrap.fill(
                    line,
                    width=width,
                    break_long_words=True,
                    break_on_hyphens=True,
                    expand_tabs=True,
                    replace_whitespace=True
                )
                wrapped_lines.append(wrapped)
                
    return '\n'.join(wrapped_lines)

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_chat_response(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content']

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal first
    
    # Welcome messages with typewriter effect
    welcome_message = "Welcome to the Mistral AI Chat!"
    typewriter_effect(Fore.CYAN + Style.BRIGHT + welcome_message + Style.RESET_ALL)
    
    exit_message = "Type 'exit' or 'quit' to end the chat, 'clear' to clear the screen."
    typewriter_effect(Fore.YELLOW + exit_message + Style.RESET_ALL)
    
    version_message = "v1.0.0"
    typewriter_effect(Fore.YELLOW + version_message + Style.RESET_ALL)
    
    print()  # Add a blank line for better spacing

    while True:
        # Get terminal width at the start of each loop
        terminal_width = shutil.get_terminal_size().columns - 2
        
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)
        user_input_lower = user_input.lower()
        
        print()
        
        if user_input_lower in ['exit', 'quit']:
            print(Fore.RED + "Chat ended. Goodbye!" + Style.RESET_ALL)
            break
        elif user_input_lower == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # Print "Mistral AI:" in cyan
        print(Fore.CYAN + "Mistral AI: " + Style.RESET_ALL)
        response = get_chat_response(user_input)
        
        # Ensure the response is wrapped according to the terminal width
        wrapped_response = wrap_text_with_indent(response, terminal_width)
        
        # Print the wrapped response in default color
        print(wrapped_response)
        print()  # Add extra line break before next user input

if __name__ == "__main__":
    main() 