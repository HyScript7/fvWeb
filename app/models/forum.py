from common.configuration import FVWEB_COLLECTION_DISCUSSIONS, FVWEB_DATABASE

from . import Client

discussions_db = Client()[FVWEB_DATABASE][FVWEB_COLLECTION_DISCUSSIONS]
