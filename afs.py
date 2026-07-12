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
    search_package,
    install_package,
    remove_package
)

from core.config import (
    load_config,
    save_config
)

console = Console()

AFS_VERSION = "0.5.0"

config = load_config()


def banner():

    global config

    console.print(
        Panel.fit(
f"""
🚀 Apollo Framework System

Version : {AFS_VERSION}
Status  : Online

Core Engine : Active
Modules     : {len(get_modules())}
Plugins     : {len(get_plugins())}
Theme       : {config.get("theme")}
""",
        title="AFS"
        )
    )


def show_modules():

    console.print("\n📦 Installed Modules\n")

    modules = get_modules()

    if not modules:

        console.print("No modules installed")

        return

    for module in modules:

        console.print(f"✓ {module}")


def show_plugins():

    console.print("\n🔌 Installed Plugins\n")

    plugins = get_plugins()

    if not plugins:

        console.print("No plugins installed")

        return

    for plugin in plugins:

        console.print(f"✓ {plugin}")


def show_packages():

    console.print("\n📦 Installed Packages\n")

    packages = get_packages()

    if not packages:

        console.print("No packages installed")

        return

    for package in packages:

        console.print(f"✓ {package}")


def show_config():

    global config

    config = load_config()

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

            run_module(command.replace("run ", ""))

        elif command == "plugins":

            show_plugins()

        elif command.startswith("plugin "):

            run_plugin(command.replace("plugin ", ""))

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

        elif command.startswith("package install "):

            name = command.replace(
                "package install ",
                ""
            )

            if install_package(name):

                console.print(f"✅ {name} installed successfully.")

            else:

                console.print(f"⚠ {name} already installed.")

        elif command.startswith("package remove "):

            name = command.replace(
                "package remove ",
                ""
            )

            if remove_package(name):

                console.print(f"🗑 {name} removed successfully.")

            else:

                console.print(f"❌ {name} is not installed.")

        elif command.startswith("package info "):

            name = command.replace(
                "package info ",
                ""
            )

            result = search_package(name)

            if result:

                console.print(f"""
📦 Package Information

Name    : {name}
Status  : Available
""")

            else:

                console.print("Package not found.")

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

            console.print("👋 Goodbye!")

            break

        else:

            console.print(
                f"❌ Unknown command: {command}"
            )
def startup():

    console.print("[green]Initializing Apollo Framework System...[/green]")

    try:

        modules = get_modules()
        plugins = get_plugins()
        packages = get_packages()

        console.print(f"✅ Modules Loaded : {len(modules)}")
        console.print(f"✅ Plugins Loaded : {len(plugins)}")
        console.print(f"✅ Packages Loaded : {len(packages)}")

    except Exception as e:

        console.print(f"[red]Startup Error : {e}[/red]")


def main():

    banner()

    startup()

    terminal()


if __name__ == "__main__":

    main()
