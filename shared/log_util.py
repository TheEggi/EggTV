import functools
import time

import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
name = addon.getAddonInfo('name')

LOGDEBUG = xbmc.LOGDEBUG
LOGERROR = xbmc.LOGERROR
LOGFATAL = xbmc.LOGFATAL
LOGINFO = xbmc.LOGINFO
LOGNONE = xbmc.LOGNONE
LOGNOTICE = xbmc.LOGNOTICE
LOGSEVERE = xbmc.LOGSEVERE
LOGWARNING = xbmc.LOGWARNING


def log(msg, level=LOGNOTICE):
    # override message level to force logging when addon logging turned on
    if addon.getSetting('addon_debug') == 'true' and level == LOGDEBUG:
        level = LOGNOTICE

    try:
        if isinstance(msg, unicode):
            msg = '%s (ENCODED)' % (msg.encode('utf-8'))

        xbmc.log('%s: %s' % (name, msg), level)
    except Exception as e:
        try:
            xbmc.log('Logging Failure: %s' % (e), level)
        except:
            raise


def log_function(func):
    @functools.wraps(func)
    def log_wrap(*args, **kwargs):
        start = time.time()
        log('>> Enter {func} with *args: {args}, **kwargs: {kwargs}'.format(**{'func': func.__name__,
                                                                               'args': args,
                                                                               'kwargs': kwargs}))
        func(*args, **kwargs)
        log('<< Exit {func} after {time}'.format(**{'func': func.__name__,
                                                    'time': start - time.time()}))

    return log_wrap
