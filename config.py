# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20919286")

API_HASH = os.environ.get("API_HASH", "57b85f72104db3f08f9795b0410eb556")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6297238954:AAGLpbcNF0kgmYyHx9nam2HBaV0GKU1T-Ng") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Movies_Hub_Og") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Wen:Wen@cluster0.dopcbu3.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/815501c2fd28f7e7a7a0d.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5909932224').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
