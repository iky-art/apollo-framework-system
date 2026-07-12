import json
import os

CONFIG_FILE = "data/config.json"

DEFAULT_CONFIG = {
    "name": "Apollo Framework System",
    "version": "0.4.0",
    "theme": "dark",
    "language": "id",
    "workspace": "workspace",
    "auto_update": True,
    "plugins": True
}


def load_config():

    if not os.path.exists(CONFIG_FILE):

        os.makedirs("data", exist_ok=True)

        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
