from shared.constants import Language


class Video(object):
    def __init__(self, host='', url='', quality=0, views=0, rating=0, output='test', tmdb_id=0,
                 language=Language.en, *additional):
        self.host = host
        self.url = url
        self.quality = quality
        self.views = views
        self.rating = rating
        self.additional = additional
        self.output = output
        self.tmdb_id = tmdb_id
        self.language = language
