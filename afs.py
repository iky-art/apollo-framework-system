#!/usr/bin/env python3

import os

from rich.console import Console
from rich.panel import Panel

from core.loader import (
    get_modules,
    run_module
)

from core.plugin import (
    get_plugins,
    run_plugin
)

from core.package import (
    get_packages,
    search_package
)

from core.config import (
    load_config,
    save_config
)

console = Console()

AFS_VERSION = "0.5.0"

config = load_config()


def banner():

    console.print(
        Panel.fit(
f"""
🚀 Apollo Framework System

Version : {AFS_VERSION}
Status  : Online

Core Engine : Active
Modules     : {len(get_modules())}
Plugins     : {len(get_plugins())}
Theme       : {config['theme']}
""",
        title="AFS"
        )
    )


def show_modules():

    modules = get_modules()

    console.print("\n📦 Installed Modules\n")

    if not modules:

        console.print("No modules installed")

        return

    for module in modules:

        console.print(f"✓ {module}")


def show_plugins():

    plugins = get_plugins()

    console.print("\n🔌 Installed Plugins\n")

    if not plugins:

        console.print("No plugins installed")

        return

    for plugin in plugins:

        console.print(f"✓ {plugin}")


def show_packages():

    packages = get_packages()

    console.print("\n📦 Installed Packages\n")

    if not packages:

        console.print("No packages installed")

        return

    for package in packages:

        console.print(f"✓ {package}")


def show_config():

    global config

    console.print("\n⚙ AFS Configuration\n")

    for key, value in config.items():

        console.print(f"{key} : {value}")


def help_menu():

    console.print("""
AFS Commands

help
version

modules
run <module>

plugins
plugin <plugin>

packages
package search <name>
package install <name>
package remove <name>
package info <name>
package update

config
config set <key> <value>

clear
exit
""")

def terminal():

    global config

    while True:

        command = input("\nAFS > ").strip()

        if command == "":
            continue

        elif command == "help":

            help_menu()

        elif command == "version":

            console.print(f"AFS Version {AFS_VERSION}")

        elif command == "modules":

            show_modules()

        elif command.startswith("run "):

            run_module(command[4:].strip())

        elif command == "plugins":

            show_plugins()

        elif command.startswith("plugin "):

            run_plugin(command[7:].strip())

        elif command == "packages":

            show_packages()

        elif command.startswith("package search "):

            keyword = command.replace(
                "package search ",
                ""
            )

            result = search_package(keyword)

            console.print("\n🔍 Search Result\n")

            if not result:

                console.print("No package found")

            else:

                for item in result:

                    console.print(f"✓ {item}")

        elif command.startswith("package info "):

            name = command.replace(
                "package info ",
                ""
            )

            console.print(f"""
📦 Package Information

Name    : {name}
Version : 1.0.0
Status  : Installed
Author  : Apollo
""")

        elif command.startswith("package install "):

            name = command.replace(
                "package install ",
                ""
            )

            console.print(f"📥 Installing {name}...")
            console.print("✅ Package installed.")

        elif command.startswith("package remove "):

            name = command.replace(
                "package remove ",
                ""
            )

            console.print(f"🗑 Removing {name}...")
            console.print("✅ Package removed.")

        elif command == "package update":

            console.print("🔄 Checking packages...")
            console.print("✅ All packages are up to date.")

        elif command == "config":

            show_config()

        elif command.startswith("config set "):

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

            console.clear()
            banner()

        elif command == "exit":

            console.print("🔴 AFS Shutdown")
            break

        else:

            console.print("❌ Unknown command")


def main():

    banner()
    terminal()


if __name__ == "__main__":
    main()
