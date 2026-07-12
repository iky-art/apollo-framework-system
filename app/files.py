import os
from rich.console import Console
from rich.panel import Panel

console = Console()


def show_files():

    while True:

        console.clear()

        lokasi = os.getcwd()

        console.print(
            Panel(
                f"""
📁 Apollo File Manager

Lokasi:
{lokasi}

1. Lihat isi folder
2. Masuk folder
3. Kembali folder
4. Buat folder
5. Buat file
6. Hapus file
0. Kembali
""",
                title="File Manager",
                border_style="green"
            )
        )

        pilihan = input("Pilih: ")


        if pilihan == "1":

            console.print("\n📂 Isi folder:")

            for item in os.listdir(lokasi):
                console.print(" - " + item)

            input("\nEnter kembali...")


        elif pilihan == "2":

            nama = input("Folder: ")

            if os.path.isdir(nama):
                os.chdir(nama)

            else:
                console.print("❌ Folder tidak ditemukan")
                input("Enter...")


        elif pilihan == "3":

            os.chdir("..")


        elif pilihan == "4":

            nama = input("Nama folder: ")

            os.mkdir(nama)

            console.print("✅ Folder dibuat")
            input("Enter...")


        elif pilihan == "5":

            nama = input("Nama file: ")

            open(nama, "w").close()

            console.print("✅ File dibuat")
            input("Enter...")


        elif pilihan == "6":

            nama = input("Nama file: ")

            if os.path.isfile(nama):
                os.remove(nama)
                console.print("✅ File dihapus")

            else:
                console.print("❌ File tidak ditemukan")

            input("Enter...")


        elif pilihan == "0":

            break
