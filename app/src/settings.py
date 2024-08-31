import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./config/prod.env')
load_dotenv(dotenv_path=dotenv_path)

MONGO_URI = os.getenv("MONGO_URI")
DATABASE = os.getenv("DATABASE")
