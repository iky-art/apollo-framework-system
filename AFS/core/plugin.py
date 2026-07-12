import os
import importlib


def get_plugins():

    plugins = []

    path = "plugins"

    if not os.path.exists(path):
        return plugins

    for item in os.listdir(path):

        folder = os.path.join(path, item)

        if os.path.isdir(folder) and item != "__pycache__":
            plugins.append(item)

    return plugins


def run_plugin(name):

    try:

        plugin = importlib.import_module(
            f"plugins.{name}.main"
        )

        plugin.run()

    except Exception as e:

        print(f"❌ Plugin error: {e}")
