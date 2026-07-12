from app.menu import show_menu

from app.dashboard import show_dashboard
from app.system import info
from app.files import show_files
from app.network import show_network
from app.security import show_security
from app.github import show_github


def pause():
    input("\nTekan Enter untuk kembali...")


def main():

    while True:

        pilihan = show_menu()


        if pilihan == "1":
            show_dashboard()


        elif pilihan == "2":
            info()
            pause()


        elif pilihan == "3":
            show_files()


        elif pilihan == "4":
            print("🤖 Apollo AI belum aktif")
            pause()


        elif pilihan == "5":
            show_network()


        elif pilihan == "6":
            show_security()


        elif pilihan == "7":
            show_github()


        elif pilihan == "8":
            print("▲ Vercel Manager belum aktif")
            pause()


        elif pilihan == "0":
            print("🚀 Apollo CLI ditutup")
            break


        else:
            print("❌ Pilihan tidak tersedia")
            pause()


if __name__ == "__main__":
    main()
