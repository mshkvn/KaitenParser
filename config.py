from dotenv import load_dotenv
import os
import yaml

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

with open("params.yaml", "r") as f:
    yaml_config = yaml.safe_load(f)

CARD_ID = yaml_config.get("CARD_ID")