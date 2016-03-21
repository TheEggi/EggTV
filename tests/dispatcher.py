import unittest


def class_decorator(cls):
   for name, method in cls.__dict__.iteritems():
        if hasattr(method, "use_class"):
            attr = getattr(method, 'use_class')
            # do something with the method and class
            print name, cls, attr
        else:
            print 'not decorated %s' % name
   return cls

def method_decorator_args(mode='asdf'):
    def method_decorator(func):
        # mark the method as something that requires view's class
        func.use_class = mode
        print 'method decorator excuted for %s' % func.__name__
        return func
    return method_decorator

@class_decorator
class ModelA(object):
    @method_decorator_args(mode='aaaa')
    def a_method(self):
        # do some stuff
        pass

    def b_method(self):
        pass


class TestDispatch(unittest.TestCase):
    def class_decorator_test(self):
        pass
        #model = ModelA()
