# from settings import

def applyToClassMethod(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

def debugInfo(fn):
    print("hol")
    return fn

@applyToClassMethod(debugInfo)
class C(object):
    def m1(self):
        print("fsdfsa")
    def m2(self, x): pass

if __name__ == "__main__":
    aa = C()
    # print(getattr(C, "m1"))
    # aaaa = mydecorator(aaaa)
    aa.m1()