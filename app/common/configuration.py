from decouple import config
from socket import gethostname

HOSTNAME: str = gethostname()

PASSWORD_SALT = config("PASSWORD_SECRET", "CH4NG3_M3")

FLASK_SECRET: str           = config("FLASK_SECRET", "CH4NG3_M3")
FLASK_SESSION_LIFETIME: int = int(config("FLASK_SESSION_LIFETIME", 30))
FLASK_PORT: int             = int(config("FLASK_PORT", 5000))
FLASK_DEBUG: bool           = config("FLASK_DEBUG", "true").lower() == "true"

MONGO_HOST: str = config("MONGO_HOST", "localhost")
MONGO_PORT: int = int(config("MONGO_PORT", 27017))
MONGO_USER: str = config("MONGO_USER", "root")
MONGO_PASS: str = config("MONGO_PASS", "root")
MONGO_SRV: bool = config("MONGO_SRV", "false") == "true"
MONGO_URI: str  = f"mongodb{'+srv' if MONGO_SRV else ''}://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}{(':' + str(MONGO_PORT)) if not MONGO_SRV else ''}"

REDIS_HOST: str = config("REDIS_HOST", "localhost")
REDIS_PORT: int = int(config("REDIS_PORT", 6379))
REDIS_PASS: str = config("REDIS_PASS", "root")

FVWEB_DATABASE               = config("FVWEB_DATABASE", "fvWeb")
FVWEB_COLLECTION_USERS       = config("FVWEB_USERS", "Accounts")
FVWEB_COLLECTION_ARTICLES    = config("FVWEB_ARTICLES", "Articles")
FVWEB_COLLECTION_DISCUSSIONS = config("FVWEB_DISCUSSIONS", "Discussions")
