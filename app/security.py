import hashlib
import secrets
import string
import os

from rich.console import Console
from rich.panel import Panel


console = Console()


def password_generator():

    panjang = int(input("Panjang password: "))

    karakter = string.ascii_letters + string.digits + "!@#$%^&*"

    password = "".join(
        secrets.choice(karakter)
        for _ in range(panjang)
    )

    console.print(
        f"\n🔑 Password:\n{password}"
    )


def hash_generator():

    teks = input("Masukkan teks: ")

    hasil = hashlib.sha256(
        teks.encode()
    ).hexdigest()

    console.print(
        f"\n#️⃣ SHA256:\n{hasil}"
    )


def file_checksum():

    nama = input("Nama file: ")

    if os.path.isfile(nama):

        with open(nama, "rb") as f:
            data = f.read()

        hasil = hashlib.sha256(data).hexdigest()

        console.print(
            f"\n📄 SHA256 File:\n{hasil}"
        )

    else:
        console.print(
            "❌ File tidak ditemukan"
        )


def token_generator():

    token = secrets.token_hex(32)

    console.print(
        f"\n🎲 Token:\n{token}"
    )


def password_checker():

    password = input("Password: ")

    skor = 0

    if len(password) >= 8:
        skor += 1

    if any(c.isdigit() for c in password):
        skor += 1

    if any(c.isupper() for c in password):
        skor += 1

    if any(c in "!@#$%^&*" for c in password):
        skor += 1


    level = {
        0: "Sangat Lemah",
        1: "Lemah",
        2: "Sedang",
        3: "Kuat",
        4: "Sangat Kuat"
    }

    console.print(
        f"🛡 Kekuatan: {level[skor]}"
    )


def show_security():

    while True:

        console.clear()

        console.print(
            Panel(
"""
🔒 Apollo Security Tools

1. 🔑 Password Generator
2. #️⃣ Hash Generator
3. 📄 File Checksum
4. 🎲 Random Token
5. 🛡 Password Checker
0. 🔙 Kembali
""",
                title="Security Tools",
                border_style="red"
            )
        )


        pilihan = input("Pilih: ")


        if pilihan == "1":
            password_generator()

        elif pilihan == "2":
            hash_generator()

        elif pilihan == "3":
            file_checksum()

        elif pilihan == "4":
            token_generator()

        elif pilihan == "5":
            password_checker()

        elif pilihan == "0":
            break

        else:
            console.print("❌ Pilihan salah")


        input("\nEnter untuk kembali...")
