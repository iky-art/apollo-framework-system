import os
import webbrowser

from rich.console import Console
from rich.panel import Panel


console = Console()


def show_github():

    while True:

        console.clear()

        console.print(
            Panel(
"""
☁ Apollo GitHub Manager

1. 📂 Git Status
2. 📥 Clone Repository
3. 📝 Commit Perubahan
4. 📤 Push Repository
5. 🌐 Buka GitHub
6. 🔗 Cek Remote Repository
0. 🔙 Kembali
""",
                title="GitHub Manager",
                border_style="magenta"
            )
        )

        pilihan = input("Pilih: ")


        if pilihan == "1":

            os.system("git status")

            input("\nTekan Enter...")


        elif pilihan == "2":

            url = input("URL Repository: ")

            os.system(
                f"git clone {url}"
            )

            input("\nTekan Enter...")


        elif pilihan == "3":

            pesan = input("Pesan commit: ")

            os.system("git add .")

            os.system(
                f'git commit -m "{pesan}"'
            )

            input("\nTekan Enter...")


        elif pilihan == "4":

            os.system("git push")

            input("\nTekan Enter...")


        elif pilihan == "5":

            webbrowser.open(
                "https://github.com"
            )


        elif pilihan == "6":

            os.system(
                "git remote -v"
            )

            input("\nTekan Enter...")


        elif pilihan == "0":

            break


        else:

            console.print(
                "❌ Pilihan tidak tersedia"
            )

            input("\nTekan Enter...")
