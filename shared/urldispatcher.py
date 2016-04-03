import urlparse

from shared import log_util

registry = {}


def dispatcher_class(cls):
   for name, method in cls.__dict__.iteritems():
        if hasattr(method, 'mode'):
            mode = getattr(method, 'mode')

   return cls


def dispatcher_function(mode=None):
    def decorator(func):
        # mark the method as something that requires view's class
        func.mode = mode or 'None'
        log_util.log('function %s added with mode %s' % (func.__name__, func.mode))
        registry[func.mode] = func
        return func
    return decorator


def dispatch(argv, instance):
    args = urlparse.parse_qs(argv[2][1:])
    mode = args.get('mode')
    if mode:
        mode = mode[0]
    else:
        mode = 'None'
    log_util.log('Dispatch mode %s' % mode)
    registry[mode](instance)
