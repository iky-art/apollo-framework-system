import os
import socket
import urllib.request
from rich.console import Console
from rich.panel import Panel


console = Console()


def show_network():

    while True:

        console.clear()

        console.print(
            Panel(
"""
🌐 Apollo Network Tools

1. 📡 Cek IP Address
2. 🌍 Cek Internet
3. 📶 Ping Server
4. 🔎 DNS Lookup
5. 🔗 Cek Website
0. 🔙 Kembali
""",
                title="Network Tools",
                border_style="blue"
            )
        )


        pilihan = input("Pilih: ")


        if pilihan == "1":

            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)

            console.print(
                f"📡 IP Address: {ip}"
            )

            input("\nEnter...")


        elif pilihan == "2":

            try:
                urllib.request.urlopen(
                    "https://google.com",
                    timeout=5
                )

                console.print(
                    "🟢 Internet aktif"
                )

            except:
                console.print(
                    "🔴 Tidak ada internet"
                )

            input("\nEnter...")


        elif pilihan == "3":

            host = input("Server: ")

            os.system(
                f"ping -c 4 {host}"
            )

            input("\nEnter...")


        elif pilihan == "4":

            domain = input("Domain: ")

            try:
                ip = socket.gethostbyname(domain)

                console.print(
                    f"🔎 {domain} -> {ip}"
                )

            except:
                console.print(
                    "❌ DNS gagal"
                )

            input("\nEnter...")


        elif pilihan == "5":

            url = input("Website: ")

            try:
                urllib.request.urlopen(
                    url,
                    timeout=5
                )

                console.print(
                    "🟢 Website Online"
                )

            except:
                console.print(
                    "🔴 Website Offline"
                )

            input("\nEnter...")


        elif pilihan == "0":
            break
