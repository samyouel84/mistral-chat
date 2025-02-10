import os
import requests
from colorama import Fore, Style, init
from config import API_KEY, MODEL, API_URL
import textwrap
import shutil
import time
import sys
import re

# Initialize colorama with different settings
init(autoreset=True, strip=True, convert=True)

def wrap_text_with_indent(text, width=None, subsequent_indent='    '):
    """Wrap text with proper indentation for subsequent lines."""
    if width is None:
        # Get terminal width, default to 80 if cannot determine
        width = shutil.get_terminal_size().columns - 2

    # Split into paragraphs
    paragraphs = text.split('\n\n')
    wrapped_paragraphs = []
    
    for paragraph in paragraphs:
        lines = paragraph.strip().split('\n')
        wrapped_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Match any number followed by a period
            number_match = re.match(r'(\d+\.)', line)
            
            if number_match:
                # Get the full number prefix including the period
                prefix = number_match.group(1) + ' '
                rest = line[len(prefix):].strip()
                
                # Calculate proper indentation based on number width
                indent = ' ' * len(prefix)
                
                if '**' in rest:
                    # Don't wrap lines with bold markers
                    wrapped_lines.append(Fore.CYAN + line + Style.RESET_ALL)
                else:
                    # Wrap the content after the number
                    wrapped = textwrap.fill(
                        rest,
                        width=width - len(indent),
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
                if '**' in line:
                    wrapped_lines.append(Fore.CYAN + line + Style.RESET_ALL)
                else:
                    wrapped = textwrap.fill(
                        line,
                        width=width,
                        initial_indent='',
                        subsequent_indent=subsequent_indent,
                        break_long_words=True,
                        break_on_hyphens=True,
                        expand_tabs=True,
                        replace_whitespace=True
                    )
                    wrapped_lines.append(wrapped)
                    
        wrapped_paragraphs.append('\n'.join(wrapped_lines))
    
    return '\n\n'.join(wrapped_paragraphs)

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
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)
        user_input_lower = user_input.lower()
        
        if user_input_lower in ['exit', 'quit']:
            print(Fore.RED + "Chat ended. Goodbye!" + Style.RESET_ALL)
            break
        elif user_input_lower == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # Print "Mistral AI:" in cyan
        print(Fore.CYAN + "Mistral AI: " + Style.RESET_ALL)
        response = get_chat_response(user_input)
        wrapped_response = wrap_text_with_indent(response)
        
        # Print the wrapped response in default color
        print(wrapped_response)

if __name__ == "__main__":
    main() 