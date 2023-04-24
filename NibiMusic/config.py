import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "23854524"))
API_HASH = getenv("API_HASH", "e765ba734e8c485b1b1f72dff94127de")
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
OWNER_USERNAME = getenv("OWNER_USERNAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1952625698").split()))
aiohttpsession = aiohttp.ClientSession()
