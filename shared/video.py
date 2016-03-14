from shared.constants import Language


class Video(object):
    def __init__(self, title, season='', episode='', url='', quality=0, views=0, rating=0, output='test', tmdb_id=0,
                 language=Language.en, *additional):
        self.url = url
        self.link_urls = []
        self.hoster_urls = []
        self.quality = quality
        self.views = views
        self.rating = rating
        self.additional = additional
        self.output = output
        self.tmdb_id = tmdb_id
        self.language = language
        self.episode = episode
        self.season = season
        self.title = title