import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7912602315:AAFGONkeZ2CRAmvjOnJjDPRGmezMVC5uITw")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21855175"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "693d541b34acfe8fa0c86278b0c31705")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7973269652"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ashishyadav987654rao:HcY9XybOLAnu5ch6@cluster0.yo17vac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
