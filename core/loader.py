import os
import importlib


MODULES_DIR = "modules"


def get_modules():

    if not os.path.exists(MODULES_DIR):
        return []

    return [
        item
        for item in os.listdir(MODULES_DIR)
        if os.path.isdir(os.path.join(MODULES_DIR, item))
        and not item.startswith("__")
    ]


def run_module(name):

    try:

        module = importlib.import_module(
            f"modules.{name}"
        )

        if hasattr(module, "run"):
            module.run()

        else:
            print(f"Module '{name}' has no run()")

    except Exception as e:

        print(e)
