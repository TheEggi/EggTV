import abc

from shared.constants import DEFAULT_SCRAPER_TIMEOUT

BASE_URL = ''


class abstractclassmethod(classmethod):
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super(abstractclassmethod, self).__init__(callable)


class BaseScraper(object):
    __metaclass__ = abc.ABCMeta
    base_url = BASE_URL

    def __init__(self, timeout=DEFAULT_SCRAPER_TIMEOUT):
        """
        Constructor for the scraper.
        :param timeout: Timeout for the scraper operation.
        """
        pass

    @abstractclassmethod
    def get_supported_languages(cls):
        """
        Get the supported languages
        :return: Languages
        """
        raise NotImplementedError

    @abstractclassmethod
    def get_name(cls):
        """
        Gets the name of the plugin. Normally the name of the service.
        :return: Service name
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_sources(self, video):
        """
        Evaluates the links returned from get_links and uses them to
        get links for urlresolver.
        :param video: Video item with the available information after get_links.
        :return: Dictionary
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_links(self, video):
        """
        Evaluates the links returned from search and parses the result into
        video items.
        :param video: Video item from search.
        :return: Array of Video items.
        """

    @abc.abstractmethod
    def search(self, video_type, titles, year, tmdb_id, season='', episode=''):
        """
        Try to find results by using the provided parameters.
        Should be fast in order to be skipped early.
        Throws NoResultsFoundError.

        :param video_type: VideoType enum.
        :param titles: Dictionary of titles (['language'] = title)
        :param season: Season.
        :param episode: Episode.
        :param year: Year when the title aired.
        :param tmdb_id: The movie db id.
        :return: Array of Video items.
        """
        raise NotImplementedError
