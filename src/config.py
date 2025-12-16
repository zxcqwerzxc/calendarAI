from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_HOST=os.environ.get("POSTGRES_HOSTNAME")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT")
POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASS=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_NAME=os.environ.get("POSTGRES_NAME")

POSTGRES_URL=f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
