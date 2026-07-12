import os

PACKAGE_DIR = "packages"


def get_packages():

    if not os.path.exists(PACKAGE_DIR):
        return []

    packages = []

    for item in os.listdir(PACKAGE_DIR):

        folder = os.path.join(PACKAGE_DIR, item)

        if os.path.isdir(folder) and item != "__pycache__":
            packages.append(item)

    return sorted(packages)


def search_package(keyword):

    keyword = keyword.lower()

    return [
        pkg for pkg in get_packages()
        if keyword in pkg.lower()
    ]
