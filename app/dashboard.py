import os
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel


console = Console()


def get_cpu():
    cores = 0

    with open("/proc/cpuinfo") as f:
        for line in f:
            if line.startswith("processor"):
                cores += 1

    return f"{cores} Core ARM64"


def get_ram():
    total = 0
    available = 0

    with open("/proc/meminfo") as f:
        for line in f:
            if "MemTotal" in line:
                total = int(line.split()[1]) // 1024

            if "MemAvailable" in line:
                available = int(line.split()[1]) // 1024

    used = total - available

    return f"{used}MB / {total}MB"


def get_storage():
    result = os.popen("df -h / | tail -1").read()
    data = result.split()

    return f"{data[2]} / {data[1]}"


def show_dashboard():

    while True:
        console.clear()

        dashboard = f"""
🚀 Apollo CLI v1.2

🕒 Time      : {datetime.now().strftime("%H:%M:%S")}

💻 CPU       : {get_cpu()}
🧠 RAM       : {get_ram()}
💾 Storage   : {get_storage()}

🤖 AI        : Offline
☁ GitHub     : Not Connected
▲ Vercel     : Not Connected

🟢 Status    : System Online
"""

        console.print(
            Panel(
                dashboard,
                title="Apollo Dashboard",
                border_style="cyan"
            )
        )

        time.sleep(2)
