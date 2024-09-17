import subprocess
import time
import itertools
from mainmenu import main_menu
from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TimeElapsedColumn  # Missing imports added
from rich.live import Live
from utils import console, clear_console

def check_for_updates():
    """Checks for updates by running git pull from the repository."""
    try:
        # Run 'git pull' to fetch updates from GitHub
        result = subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if "Already up to date" in result.stdout:
            console.print("No updates available. Everything is up to date.", style="green")
            return False  # No update found
        else:
            console.print("Updates were downloaded and applied!", style="green")
            return True  # Update found
    except subprocess.CalledProcessError as e:
        console.print(f"Error checking for updates: {e.stderr}", style="bold red")
        return False

def loading_screen_with_spinner():
    """Displays a spinner-based loading screen and checks for updates, ensuring it runs for at least 3.4 seconds."""
    spinner_chars = ['◐', '◒', '◑', '◓']  # Spinner characters
    spinner_cycle = itertools.cycle(spinner_chars)  # Create an infinite cycle of spinner characters

    update_checked = False
    update_found = False
    min_duration = 3.4  # Minimum spinner duration in seconds
    start_time = time.time()  # Track the start time of the spinner

    with Live(console=console, refresh_per_second=10):  # Refresh 10 times per second (every 0.1 seconds)
        spinner_task = "[#9d9ce7]Checking for updates...[/#9d9ce7]"

        while time.time() - start_time < min_duration or not update_checked:
            # Get the next character in the spinner cycle
            spinner_char = next(spinner_cycle)
            
            # Display the spinner and message
            console.print(f"{spinner_task} {spinner_char}", end='\r', style="#9d9ce7")

            time.sleep(0.1)  # Wait 0.1 seconds between spins

            if not update_checked:
                update_found = check_for_updates()  # Check for updates once
                update_checked = True

        # If an update was found, you can call the update progress screen
        if update_found:
            show_update_download_screen()

def show_update_download_screen():
    """Displays a green progress bar for updating and shows download progress."""
    clear_console()
    
    # Simulate a download task for the update (we'll fake file size for this example)
    total_size = 100 * 1024 * 1024  # 100 MB for demonstration (adjust as needed)
    progress = Progress(
        TextColumn("[bold green]Updating: {task.description}"),
        BarColumn(bar_width=35, complete_style="green", finished_style="green"),
        DownloadColumn(),  # Shows file size progress
        TextColumn("[#ffffff]{task.percentage:>3.0f}%[/#ffffff]"),
        TimeElapsedColumn(),
    )

    with Live(progress, console=console):
        task = progress.add_task("Downloading update...", total=total_size)
        
        # Simulate download with progress
        downloaded = 0
        chunk_size = total_size // 100  # Simulate 100 download chunks
        for _ in range(100):  # Simulate 100% progress
            time.sleep(0.05)  # Simulate download speed
            downloaded += chunk_size
            progress.update(task, advance=chunk_size)

if __name__ == "__main__":
    loading_screen_with_spinner()  # Display loading screen and check for updates
    main_menu()  # Launch main menu after loading
