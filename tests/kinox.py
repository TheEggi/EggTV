import re
import time
import unittest

from scrapers.kinox_scraper import KinoxScraper
from shared.constants import Language
from shared.constants import VideoType


class TestStringMethods(unittest.TestCase):
    def test_kinox_search(self):
        start_time = time.time()
        scraper = KinoxScraper();
        kinox = KinoxScraper.search(scraper, VideoType.TV, 'Game of Thrones', None, None)
        self.assertGreater(len(kinox), 1, 'no results found')
        self.assertTrue(any(x.language == Language.de and re.match(
            r'http.://kinox.tv/Stream/Game_of_Thrones-Das_Lied_von_Eis_und_Feuer.html', x.url) for x in kinox))
        self.assertLess((time.time() - start_time), 2)

    def test_kinox_get_links(self):
        scraper = KinoxScraper();
        kinox = KinoxScraper.search(scraper, VideoType.TV, 'Game of Thrones', None, None, season='1', episode='2')
        video = next(v for v in kinox if v.language == Language.de
                     and re.match(r'http.://kinox.tv/Stream/Game_of_Thrones-Das_Lied_von_Eis_und_Feuer.html', v.url))
        video = KinoxScraper.get_links(scraper, video)
        self.assertGreater(len(video.urls), 10)


