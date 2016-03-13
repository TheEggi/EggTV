from libs.enum import Enum, unique

DEFAULT_SCRAPER_TIMEOUT = 15


@unique
class Language(Enum):
    de = 'de'
    en = 'en'
    ch = 'ch'
    es = 'es'
    fr = 'fr'
    tr = 'tr'
    ja = 'ja'
    sy = 'sy'
    it = 'it'
    hr = 'hr'
    yu = 'yu'
    ba = 'ba'



@unique
class VideoType(Enum):
    Movie = 1,
    TV = 2,
    Unknown = 3
