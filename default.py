"""

"""
import sys

import xbmcplugin
from gui.maingui import MainGui
from shared import kodi
from shared import log_util
from shared.urldispatcher import dispatch

main_ui = MainGui()

def main(argv=None):
    if sys.argv: argv = sys.argv
    queries = kodi.parse_query(sys.argv[2])

    log_util.log('Version: |%s| Queries: |%s|' % (kodi.get_version(), queries))
    log_util.log('Args: |%s|' % (argv))
    if not hasattr(main_ui, 'base_url'):
        base_url = sys.argv[0]
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'movies')
        main_ui.addon_handle = addon_handle
        main_ui.base_url = base_url
    dispatch(sys.argv, main_ui)

if __name__ == '__main__':
    sys.exit(main())
