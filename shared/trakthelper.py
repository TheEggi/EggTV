import requests.packages.urllib3
import trakt

from shared import kodi
from shared import log_util


class TraktHelper:
    TRAKT_APPLICATION_ID = '9153'
    TRAKT_CLIENT_ID = '81c82e6994bc365b184e930fbb4f52f026b5ac2f55a25b2bbf266e3fe4a68a67'
    TRAKT_CLIENT_SECRET = '4e90365a2a63266dea7e1c99d4cb9ce96bd90ac843d3ff21c01628b36af4c598'
    trakt.core.CONFIG_PATH = kodi.get_path()
    log_util.log(trakt.core.CONFIG_PATH)

    trakt.AUTH_METHOD = trakt.PIN_AUTH
    trakt.APPLICATION_ID = TRAKT_APPLICATION_ID

    @classmethod
    def getmovies(cls):
        requests.packages.urllib3.disable_warnings()
        trakt.init(pin='34F07DF0', client_id=cls.TRAKT_CLIENT_ID,
                   client_secret=cls.TRAKT_CLIENT_SECRET)
        trakt.core.OAUTH_TOKEN = 'dde8120329f50c0df20aac4a0e64287b0d64ac7e677548a1e276519f7faaa5e9'
        from trakt.movies import get_recommended_movies
        log_util.log('login called %s, %s' % (trakt.core.CLIENT_SECRET, trakt.core.CLIENT_ID))

        movies = get_recommended_movies()

        return movies
