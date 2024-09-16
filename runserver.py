import os
import subprocess
from utils import set_working_directory, display_header, console

def display_network_info():
    """Display server address and port information."""
    # Example of how to fetch IP/Port info (replace this with actual code)
    PublicIP = "127.0.0.1"
    Port = "25565"
    
    server_address = f"{PublicIP}:{Port}"
    console.print(f"Server running at {server_address}", style="bold green", justify="center")

def run_minecraft_server():
    set_working_directory()
    display_header()  # Display header

    jar = "server.jar"
    minram = "1G"
    maxram = "2G"

    if not os.path.exists(jar):
        console.print(f"Error: Unable to access jarfile {jar}", style="bold red")
        input("Press Enter to return to the menu...")
        return

    java_command = f"java -Xms{minram} -Xmx{maxram} --add-modules=jdk.incubator.vector " \
                   f"-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 " \
                   f"-XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch " \
                   f"-XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 " \
                   f"-XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 " \
                   f"-XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 " \
                   f"-XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 " \
                   f"-Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true " \
                   f"-XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 " \
                   f"-XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar \"{jar}\" --nogui"

    try:
        # Execute the Java command to run the Minecraft server
        subprocess.run(java_command, shell=True)
    except Exception as e:
        console.print(f"Error running the server: {str(e)}", style="bold red")
        input("Press Enter to return to the menu...")
