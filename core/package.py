PACKAGES = [
    "requests",
    "rich",
    "colorama",
    "numpy",
    "pandas",
    "flask",
    "fastapi"
]


def show_packages():

    print("\n📦 Installed Packages\n")

    if not PACKAGES:

        print("No package installed")

        return

    for pkg in PACKAGES:

        print(f"✓ {pkg}")


def search_package(keyword):

    return [
        pkg
        for pkg in PACKAGES
        if keyword.lower() in pkg.lower()
    ]
