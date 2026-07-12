from rich.console import Console
from rich.panel import Panel


console = Console()


def show_menu():

    console.clear()

    console.print(
        Panel(
"""
🚀 Apollo CLI v1.6

1. 📊 Dashboard Real-Time
2. 💻 System Monitor
3. 📁 File Manager
4. 🤖 AI Assistant
5. 🌐 Network Tools
6. 🔒 Security Tools
7. ☁ GitHub Manager
8. ▲ Vercel Manager

0. 🚪 Exit
""",
            title="Apollo CLI",
            border_style="cyan"
        )
    )


    return input("Pilih fitur: ")
