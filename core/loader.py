import os


def load_modules():

    print("\n📦 Installed Modules\n")

    path = "modules"

    if not os.path.exists(path):

        print("Modules folder not found")

        return

    items = os.listdir(path)

    if not items:

        print("No modules installed")

        return

    for item in items:

        print(f"✓ {item}")


def load_plugins():

    print("\n🔌 Installed Plugins\n")

    path = "plugins"

    if not os.path.exists(path):

        print("Plugins folder not found")

        return

    items = os.listdir(path)

    if not items:

        print("No plugins installed")

        return

    for item in items:

        print(f"✓ {item}")
