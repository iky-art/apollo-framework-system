import os
import importlib


def get_modules():

    modules = []

    path = "modules"

    if not os.path.exists(path):
        return modules


    for item in os.listdir(path):

        if os.path.isdir(
            os.path.join(path, item)
        ):
            modules.append(item)


    return modules



def run_module(name):

    try:

        module = importlib.import_module(
            f"modules.{name}.info"
        )

        module.run()


    except Exception as e:

        print(
            f"❌ Module error: {e}"
        )
