from libs.enum import Enum, unique


@unique
class Modes(Enum):
    MAIN = None
    TV_SHOWS = 'TVShows'
    MOVIES = 'Movies'
    SEARCH = 'Search'
    SEARCH_RESULT = 'SeachResult'
