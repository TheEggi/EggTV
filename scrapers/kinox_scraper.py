import re
from urlparse import urljoin

import requests
from bs4 import BeautifulSoup

from scrapers.basescraper import BaseScraper
from shared.constants import Language, VideoType
from shared.noresultsfounderror import NoResultsFoundError
from shared.urlwithparam import UrlWithParam
from shared.video import Video

BASE_URL = 'https://kinox.tv/'


class KinoxScraper(BaseScraper):
    _search_pattern = re.compile(r'/gr/sys/lng/([0-9]+).png')
    _find_seasonselect = re.compile(r'.*Addr=(.+)&amp;.*?SeriesID=([0-9]+)', flags=re.DOTALL)
    _find_episodes = re.compile(r'.*?rel="(.+?)&amp;Hoster=([0-9]+)&amp;.*?class="Named">(.*?)</div>.*?class="Data">.+?[0-9]+/([0-9]+?)<br/>', flags=re.DOTALL)

    def get_name(cls):
        return 'Kinox.tv'

    def get_supported_languages(cls):
        return [Language.de, Language.en]

    def search(self, video_type, titles, year, tmdb_id, season='', episode=''):
        query_parameters = {'q': titles}
        resp = requests.post(BASE_URL + 'Search.html', params=query_parameters)
        bs = BeautifulSoup(resp.content, 'html.parser')
        table = bs.find('table', id='RsltTableStatic')
        body = table.find('tbody')
        rows = body.find_all('tr')
        results = []
        for row in rows:
            img = row.find('img', alt='language')
            language = self._search_pattern.match(img['src']).group(1)
            language = int(language)
            language = self._map_flag_to_language(language)
            type = row.find('img', alt='type')['title']
            linkrow = row.find('td', class_='Title')
            alinkrow = linkrow.find('a')
            spanrow = linkrow.find('span')
            title = alinkrow.text
            url = urljoin(BASE_URL, alinkrow['href'])
            year = spanrow.text
            rating = row.find('td', class_='Rating').text
            results.append(
                Video(title=title, season=season, episode=episode, url=url, rating=rating, language=language))
        if not results:
            raise NoResultsFoundError
        return results

    def get_links(self, video):
        resp = requests.get(video.url)
        matches = self._find_seasonselect.match(resp.content)
        addr, series_id = matches.groups()
        params = {
            'Addr': addr,
            'SeriesID': series_id,
            'Season': video.season,
            'Episode': video.episode
        }
        resp = requests.get(BASE_URL + 'aGET/MirrorByEpisode/', params=params)

        fix = resp.content
        iterate = self._find_episodes.findall(resp.content)
        video.urls = []
        for match in iterate:
            series, hoster_id, hoster_name, maxEpisode = match

            params = {
                'Hoster': hoster_id,
                'Season': video.season,
                'Episode': video.episode
            }
            for mirror in range(1, int(maxEpisode) + 1):
                params['Mirror'] = mirror
                urlwithparam = UrlWithParam(BASE_URL + 'aGET/Mirror/' + series, params)
                video.urls.append(urlwithparam)

        return video

    def get_sources(self, video):
        pass

    def _map_type(self, title):
        if title == 'series':
            return VideoType.TV
        elif title == 'movie':
            return VideoType.Movie

    def _map_flag_to_language(self, flag_number):
        if flag_number == 1:
            return Language.de
        elif flag_number == 2:
            return Language.en
        elif flag_number == 4:
            return Language.ch
        elif flag_number == 5:
            return Language.es
        elif flag_number == 6:
            return Language.fr
        elif flag_number == 7:
            return Language.tr
        elif flag_number == 8:
            return Language.ja
        elif flag_number == 9:
            return Language.sy
        elif flag_number == 11:
            return Language.it
        elif flag_number == 12:
            return Language.hr
        elif flag_number == 13:
            return Language.yu
        elif flag_number == 14:
            return Language.ba
        return None;
