from rich.panel import Panel
from rich.markdown import Markdown
from utils import console

def display_faq():
    faq_text = """
**Q1: Why is the server not starting?**
   A: Ensure the `server.jar` file exists and Java is installed.
   
**Q2: Why can't I connect to the server?**
   A: Make sure the IP and port are correct, and your firewall allows connections.

**Q3: Why is the server lagging?**
   A: Check system resources and consider increasing RAM allocation.
    """
    
    faq_panel = Panel(Markdown(faq_text), title="FAQ - Common Issues", border_style="green")
    console.print(faq_panel, justify="center")

def info_and_more():
    console.print("[bold cyan]Info & More Section[/bold cyan]", justify="center")
    display_faq()
    input("\nPress Enter to return to the main menu...")
