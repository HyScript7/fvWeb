from common.configuration import FVWEB_COLLECTION_ARTICLES, FVWEB_DATABASE

from . import Client

articles_db = Client()[FVWEB_DATABASE][FVWEB_COLLECTION_ARTICLES]
