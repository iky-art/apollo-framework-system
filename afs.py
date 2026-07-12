#!/usr/bin/env python3

import os
from rich.console import Console
from rich.panel import Panel

from core.config import load_config, save_config
from core.loader import (
    load_modules,
    load_plugins
)
from core.package import (
    show_packages,
    search_package
)

console = Console()


VERSION = "0.5.0"


def banner():
    console.print(
        Panel.fit(
            f"""
[cyan]
    █████╗ ███████╗███████╗
   ██╔══██╗██╔════╝██╔════╝
   ███████║█████╗  ███████╗
   ██╔══██║██╔══╝  ╚════██║
   ██║  ██║██║     ███████║

Apollo Framework System
Version : {VERSION}
[/cyan]
"""
        )
    )


def show_help():
    console.print("""

Available Commands

help
info
version
clear
exit

modules
plugins
packages

package search <name>

config
config set <key> <value>

""")


def show_info():

    console.print(f"""

Apollo Framework System

Version : {VERSION}
Python  : 3.x

""")


def terminal():

    while True:

        command = input("AFS > ").strip()

        if command == "":
            continue

        elif command == "help":

            show_help()

        elif command == "info":

            show_info()

        elif command == "version":

            console.print(VERSION)

        elif command == "modules":

            load_modules()

        elif command == "plugins":

            load_plugins()

        elif command == "packages":

            show_packages()

        elif command.startswith("package search "):

            keyword = command.replace(
                "package search ",
                ""
            )

            result = search_package(keyword)

            console.print("\nSearch Result\n")

            if not result:
                console.print("No package found")

            else:

                for item in result:

                    console.print(f"✓ {item}")

                elif command == "config":

            config = load_config()

            console.print(f"""

AFS Configuration

name         : {config.get("name")}
version      : {config.get("version")}
theme        : {config.get("theme")}
language     : {config.get("language")}
workspace    : {config.get("workspace")}
auto_update  : {config.get("auto_update")}
plugins      : {config.get("plugins")}

""")

        elif command.startswith("config set "):

            config = load_config()

            args = command.split()

            if len(args) >= 4:

                key = args[2]
                value = " ".join(args[3:])

                if value.lower() == "true":
                    value = True

                elif value.lower() == "false":
                    value = False

                config[key] = value

                save_config(config)

                console.print("✅ Configuration Updated")

            else:

                console.print(
                    "Usage: config set <key> <value>"
                )

        elif command == "clear":

            os.system("clear")

            banner()

        elif command == "exit":

            console.print("👋 Goodbye.")

            break

        else:

            console.print("❌ Unknown command")


def main():

    banner()

    terminal()


if __name__ == "__main__":

    main()
