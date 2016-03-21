registry = []

def url_dispatch_class(cls):
   for name, method in cls.__dict__.iteritems():
        if hasattr(method, 'mode'):
            mode = getattr(method, 'mode')
            registry[mode] = method
   return cls

def dispatch(mode='MAIN'):
    def decorator(func):
        # mark the method as something that requires view's class
        func.mode = mode
        return func
    return decorator
