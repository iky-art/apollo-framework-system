import json
import os

INSTALLED_FILE = "packages/installed.json"
REPOSITORY_FILE = "packages/repository.json"


def _load_json(path, default):
    if not os.path.exists(path):
        return default

    with open(path, "r") as f:
        return json.load(f)


def get_packages():
    data = _load_json(INSTALLED_FILE, {"packages": []})
    return data["packages"]


def search_package(keyword):
    data = _load_json(REPOSITORY_FILE, {"packages": []})

    result = []

    for pkg in data["packages"]:
        if keyword.lower() in pkg["name"].lower():
            result.append(pkg["name"])

    return result


def install_package(name):
    data = _load_json(INSTALLED_FILE, {"packages": []})

    if name not in data["packages"]:
        data["packages"].append(name)

        with open(INSTALLED_FILE, "w") as f:
            json.dump(data, f, indent=4)

        return True

    return False


def remove_package(name):
    data = _load_json(INSTALLED_FILE, {"packages": []})

    if name in data["packages"]:
        data["packages"].remove(name)

        with open(INSTALLED_FILE, "w") as f:
            json.dump(data, f, indent=4)

        return True

    return False
