from questionary import select
from utils import display_header
from info import info_and_more
from runserver import run_minecraft_server
from prompt_toolkit.styles import Style

custom_style = Style([
    ('separator', 'fg:#6C6C6C'),
    ('question', 'bold fg:#A0A0A0'),
    ('selected', 'fg:#ffffff bg:#444444 bold'),
    ('pointer', 'fg:#ffffff'),
    ('instruction', 'fg:#6C6C6C'),
    ('questionmark', 'fg:#000000'),
])

def main_menu():
    while True:
        display_header()  # Display the header at the top of the menu
        menu_selection = select(
            "Main Menu (Use Arrow Keys)\n",
            choices=[
                "Run Server",
                "Info & More",
                "Exit"
            ],
            style=custom_style,
            pointer="  ▶",
            instruction=" ",
            qmark=" "
        ).ask()

        if menu_selection == "Run Server":
            run_minecraft_server()
        elif menu_selection == "Info & More":
            info_and_more()
        elif menu_selection == "Exit":
            break  # Exit the loop and end the program
