import urllib

import xbmcgui
import xbmcplugin
from gui.uiconstants import Modes
from shared import log_util
from shared.kodi import i18n, get_keyboard, notify
from shared.log_util import log_function
from shared.urldispatcher import dispatcher_function
from shared import kodi


class MainGui(object):
    @dispatcher_function(mode=None)
    def main(self):
        log_util.log('main called')
        log_util.log(self.base_url)

        kodi.create_item({'mode': Modes.SEARCH, 'section': 'test'}, 'Search')
        kodi.create_item({'mode': Modes.TV_SHOWS, 'section': 'test'}, 'TV Shows')
        kodi.create_item({'mode': Modes.MOVIES, 'section': 'test'}, 'Movies')

        kodi.end_of_directory()

    @dispatcher_function(mode=Modes.TV_SHOWS.value)
    def tv_shows(self):
        kodi.create_item({'mode': Modes.SEARCH, 'section': 'test'}, 'Oarsch')
        kodi.end_of_directory()

    @dispatcher_function(mode=Modes.MOVIES.value)
    def movies(self):
        url = self.build_url({'mode': Modes.MOVIES + Modes.SEARCH})
        li = xbmcgui.ListItem('foldername' + ' Video', iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(self.addon_handle)

    @dispatcher_function(mode=Modes.SEARCH.value)
    def search(self):
        log_util.log('WHAT?!')
        heading = 'SEARCH YOUR SHIT'
        search_text = get_keyboard(heading)
        notify(header='Your shit:', msg=search_text)

    @log_function
    def build_url(self, query):
        return self.base_url + '?' + urllib.urlencode(query)