from libs import requests
from scrapers.basescraper import BaseScraper
from shared.constants import Languages
from shared.video import Video

BASE_URL = 'https://kinox.tv/'


class KinoxScraper(BaseScraper):
    def get_name(cls):
        return 'Kinox.tv'

    def get_supported_languages(cls):
        return [Languages.GERMAN, Languages.ENGLISH]

    def search(self, video_type, titles, year, tmdb_id, season='', episode=''):
        try:
            params = {'q': titles}
            resp = requests.post(BASE_URL + 'Search.html', params)
        except Exception as e:
            asdf = e

        return Video()

    def get_sources(self, video):
        pass
