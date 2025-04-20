from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7810709783:AAGs2TQyXtHVQyL6U-LBYHEB466mdROBDRs", "")
BOT_USERNAME = getenv("@MeiMei_MusicBot", "")
admins = {}
API_ID = int(getenv("13953815"))
API_HASH = getenv("7fa7ed73c482696decfdea7345b4cadf", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
