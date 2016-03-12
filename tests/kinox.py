import unittest

from scrapers.kinox_scraper import KinoxScraper
from shared.constants import VideoType


class TestStringMethods(unittest.TestCase):
    def test_kinox(self):
        scraper = KinoxScraper();
        kinox = KinoxScraper.search(scraper, VideoType.TV, 'Game of thrones', 2011, 100);
