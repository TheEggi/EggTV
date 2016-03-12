from libs.enum import Enum, unique

DEFAULT_SCRAPER_TIMEOUT = 15


@unique
class Languages(Enum):
    GERMAN = 'de'
    ENGLISH = 'en'


@unique
class VideoType(Enum):
    Movie = 1,
    TV = 2,
    Unknown = 3
