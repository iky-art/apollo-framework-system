import json
import os

CONFIG_FILE = "data/config.json"

DEFAULT_CONFIG = {
    "name": "Apollo Framework System",
    "version": "0.5.0",
    "theme": "dark",
    "language": "id",
    "workspace": "workspace",
    "auto_update": True,
    "plugins": True
}


def load_config():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CONFIG_FILE):

        save_config(DEFAULT_CONFIG)

    with open(CONFIG_FILE, "r") as f:

        return json.load(f)


def save_config(config):

    with open(CONFIG_FILE, "w") as f:

        json.dump(config, f, indent=4)
