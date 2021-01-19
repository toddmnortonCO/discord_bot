from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

load_dotenv(find_dotenv())
env_path = Path('.')/'.env'
load_dotenv(dotenv_path = env_path)

TOKEN = os.getenv('TOKEN')