"""

"""
import sys
import urllib
import urlparse

import xbmcgui
import xbmcplugin

from shared import log_util


def main(argv=None):
    if sys.argv: argv = sys.argv
    # queries = kodi.parse_query(sys.argv[2])
    log_util.log('Args: |%s|' % (argv))

    base_url = sys.argv[0]
    addon_handle = int(sys.argv[1])
    args = urlparse.parse_qs(sys.argv[2][1:])

    xbmcplugin.setContent(addon_handle, 'movies')

    mode = args.get('mode', None)

    if mode is None:
        url = build_url({'mode': 'folder', 'foldername': 'Folder One'}, base_url=base_url)
        li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

        url = build_url({'mode': 'folder', 'foldername': 'Folder Two'}, base_url=base_url)
        li = xbmcgui.ListItem('Folder Two', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

        xbmcplugin.endOfDirectory(addon_handle)

    elif mode[0] == 'folder':
        foldername = args['foldername'][0]
        url = 'http://localhost/some_video.mkv'
        li = xbmcgui.ListItem(foldername + ' Video', iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)


def build_url(query, base_url):
    return base_url + '?' + urllib.urlencode(query)

    # don't process params that don't match our url exactly. (e.g. plugin://plugin.video.1channel/extrafanart)
    """
    plugin_url = 'plugin://%s/' % (kodi.get_id())
    if argv[0] != plugin_url:
        return

    try:
        global db_connection
        db_connection = DB_Connection()
        mode = queries.get('mode', None)
        url_dispatcher.dispatch(mode, queries)
    except (TransientTraktError, TraktError) as e:
        log_utils.log(str(e), xbmc.LOGERROR)
        kodi.notify(msg=str(e), duration=5000)
    except DatabaseRecoveryError as e:
        log_utils.log('Attempting DB recovery due to Database Error: %s' % (e), log_utils.LOGWARNING)
        db_connection.attempt_db_recovery()

    """


if __name__ == '__main__':
    sys.exit(main())
