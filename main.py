import subprocess
from mainmenu import main_menu
from rich.progress import Progress, BarColumn, TextColumn
from rich.live import Live
from rich.align import Align
from rich.padding import Padding
import time
import random
from utils import console

def check_for_updates():
    """Checks for updates by running git pull from the repository."""
    try:
        # Run 'git pull' to fetch updates from GitHub
        result = subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "Already up to date" in result.stdout:
            console.print("No updates available. Everything is up to date.", style="green")
        else:
            console.print("Updates were downloaded and applied!", style="green")
    except subprocess.CalledProcessError as e:
        console.print(f"Error checking for updates: {e.stderr}", style="bold red")

def loading_screen_with_updates():
    """Displays a loading screen and checks for updates from GitHub."""
    total_duration = random.choice([0.05, 0.15, 0.2, 0.23])
    update_interval = 0.0005
    total_updates = int(total_duration / update_interval)

    progress = Progress(
        TextColumn("Checking for updates and loading..."),
        BarColumn(bar_width=35, complete_style="#9d9ce7", finished_style="#9d9ce7"),
        TextColumn("[#ffffff][progress.percentage]{task.percentage:>3.0f}%[/#ffffff]"),
    )

    terminal_height = console.size.height
    padding_top = (terminal_height // 2) - 1

    with Live(console=console, refresh_per_second=50) as live:
        task = progress.add_task("", total=total_updates)
        
        # Check for updates in a background process
        update_checked = False

        for _ in range(total_updates):
            if not update_checked:
                check_for_updates()  # Check for updates only once
                update_checked = True
            
            time.sleep(update_interval)
            centered_progress = Align.center(progress)
            padded_progress = Padding(centered_progress, (padding_top, 0))
            live.update(padded_progress)
            progress.advance(task)

if __name__ == "__main__":
    loading_screen_with_updates()  # Display loading screen and check for updates
    main_menu()  # Launch main menu after loading
