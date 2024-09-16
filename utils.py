import os
from rich.console import Console

# Initialize Rich console
console = Console()

# ASCII Art and Author Credit
ascii_art = """┏┓┏┓┏┓┏┳┓┓┏┏┓┳┓┓ ┏┏┓┳┏┓┓┏┏┳┓   ┏┓┏┓┳┓┳┓┏┓┏┓┏┳┓
┣ ┣ ┣┫ ┃ ┣┫┣ ┣┫┃┃┃┣ ┃┃┓┣┫ ┃    ┃ ┃┃┃┃┃┃┣ ┃  ┃ 
┻ ┗┛┛┗ ┻ ┛┗┗┛┛┗┗┻┛┗┛┻┗┛┛┗ ┻    ┗┛┗┛┛┗┛┗┗┛┗┛ ┻ """

author_credit = "━━━━━━━━━━━━ nikolojo ━━━━━━━━━━━━"

def set_working_directory():
    """Set the current working directory to the script's location."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

def clear_console():
    """Clear the console screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display the ASCII art and author credit."""
    clear_console()
    console.print("\n\n" + ascii_art, style="#9d9ce7", justify="center")
    console.print(author_credit + "\n", style="#ffffff", justify="center")
