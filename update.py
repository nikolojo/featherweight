import subprocess
from utils import display_header

def check_for_updates():
    display_header()  # Display the header before checking for updates
    try:
        subprocess.run(["git", "pull"], check=True)
        print("Successfully checked for updates!")
    except subprocess.CalledProcessError as e:
        print(f"Error checking for updates: {e}")
