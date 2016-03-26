"""

"""
import sys
import urllib

import xbmcgui
import xbmcplugin

from shared import log_util
from shared.urldispatcher import dispatcher_function, dispatch


class MainDispatcher(object):
    @dispatcher_function(mode='None')
    def main(self):
        log_util.log('main called')
        url = build_url({'mode': 'folder', 'foldername': 'Folder One'}, base_url=self.base_url)
        li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=url,
                                    listitem=li, isFolder=True)

        url = build_url({'mode': 'folder', 'foldername': 'Folder Two'}, base_url=self.base_url)
        li = xbmcgui.ListItem('Folder Two', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=url,
                                    listitem=li, isFolder=True)

        xbmcplugin.endOfDirectory(self.addon_handle)

    @dispatcher_function(mode='folder')
    def folder(self):
        url = build_url({'mode': 'asdf', 'foldername': 'asdf Two'}, base_url=self.base_url)
        li = xbmcgui.ListItem('foldername' + ' Video', iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=self.addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(self.addon_handle)


main_dispatcher = MainDispatcher()

def main(argv=None):
    if sys.argv:
        argv = sys.argv
    log_util.log('Args: |%s|' % (argv))
    if not hasattr(main_dispatcher, 'base_url'):
        base_url = sys.argv[0]
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'movies')
        main_dispatcher.addon_handle = addon_handle
        main_dispatcher.base_url = base_url
    dispatch(sys.argv, main_dispatcher)


def build_url(query, base_url):
    return base_url + '?' + urllib.urlencode(query)


if __name__ == '__main__':
    sys.exit(main())
