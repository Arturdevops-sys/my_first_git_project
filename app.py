import os
from dotenv import load_dotenv
import requests

load_dotenv()

db = os.getenv("DATABASE")
port = os.getenv("PORT")

print("Database:", db)
print("Port:", port)

response = requests.get("https://api.github.com")
print("Status:", response.status_code)
