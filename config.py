from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "20046177"))
API_HASH = environ.get("API_HASH", "83d15f2956be4b4b927acded8bdf780f")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7793156995")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1001958478348")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://Goku_God_7:Goku_God_7@cluster0.yl7choa.mongodb.net/?appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
