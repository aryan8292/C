from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "3334521"))
    API_HASH = getenv("API_HASH", "29edd7420d528140c7a04bd47486886f")
    BOT_TOKEN = getenv("BOT_TOKEN", "5559125670:AAFQBcG8z3xPm1pGr-8kTmSbMqB0JZBUXo0")
    FSUB = getenv("FSUB", "ARY_NETWORK")
    CHID = int(getenv("CHID", "-1001550619816"))
    SUDO = list(map(int, getenv("5079629749").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Aryan829235:Aryan829235@cluster0.btc4eto.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
