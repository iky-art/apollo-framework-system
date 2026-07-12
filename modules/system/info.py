import platform
import os


def run():

    print("""
🖥 AFS System Module

System  : {}
Machine : {}
Python  : {}
CPU     : {}

""".format(
        platform.system(),
        platform.machine(),
        platform.python_version(),
        os.cpu_count()
    ))
