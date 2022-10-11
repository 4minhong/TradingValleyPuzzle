from functools import wraps

def singleton(orig_cls):
    orig_new = orig_cls.__new__
    instance = None

    @wraps(orig_cls.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **kwargs)
        return instance
    orig_cls.__new__ = __new__
    return orig_cls

@singleton
class SayHello(object):
    def sayHello(self, name, message):
      print("Hi, %s. Your message: %s" % (name, message))

if __name__ == '__main__':
    user1 = SayHello()
    user2 = SayHello()

    assert user1 is user2
    user1.sayHello('min','hi')

