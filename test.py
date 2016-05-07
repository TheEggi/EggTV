import requests
import trakt

TRAKT_APPLICATION_ID = '9153'
TRAKT_CLIENT_ID = '81c82e6994bc365b184e930fbb4f52f026b5ac2f55a25b2bbf266e3fe4a68a67'
TRAKT_CLIENT_SECRET = '4e90365a2a63266dea7e1c99d4cb9ce96bd90ac843d3ff21c01628b36af4c598'

trakt.AUTH_METHOD = trakt.PIN_AUTH
trakt.APPLICATION_ID = TRAKT_APPLICATION_ID
trakt.core.CLIENT_ID = TRAKT_CLIENT_ID
trakt.core.CLIENT_SECRET = TRAKT_CLIENT_SECRET
trakt.core.APPLICATION_ID = TRAKT_APPLICATION_ID
trakt.core.OAUTH_TOKEN = 'dde8120329f50c0df20aac4a0e64287b0d64ac7e677548a1e276519f7faaa5e9'

token = 'dde8120329f50c0df20aac4a0e64287b0d64ac7e677548a1e276519f7faaa5e9'
trakt.core.OAUTH_TOKEN = 'dde8120329f50c0df20aac4a0e64287b0d64ac7e677548a1e276519f7faaa5e9'
requests.packages.urllib3.disable_warnings()
from trakt.movies import get_recommended_movies

movies = get_recommended_movies()

for movie in movies:
    print movie.title
    print movie.images_url['thumb']['full']
